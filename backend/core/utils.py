import csv
import datetime

from django.contrib import messages
from django.core.cache import cache
from rest_framework import permissions
from django_select2.forms import ModelSelect2Widget, ModelSelect2MultipleWidget

menu = [
    {'title': "Главная страница", 'url_name': 'core:index'},
    {'title': "Устройства", 'url_name': 'device:device_list'},
    {'title': "Софт", 'url_name': 'software:software_index'},
    {'title': "ЭЦП", 'url_name': 'signature:signature_list'},
    {'title': "Склад", 'url_name': 'stockroom:stock_index'},
    {'title': "Баланс", 'url_name': 'accounting:accounting_index'},
]


class DataMixin:
    """
    Mixin add pagination and menu in views
    """
    paginate_by = 20

    def get_user_context(self, **kwargs):
        side_menu = cache.get('side_menu')
        if not side_menu:
            side_menu = menu
            cache.set('side_menu', side_menu, 30000)
        context = kwargs
        context['menu'] = menu
        context['query'] = self.request.GET.get('q')
        context['obj_list_count'] = self.get_queryset().count()
        return context


class BaseModelSelect2WidgetMixin(ModelSelect2Widget):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.attrs = {'class': 'js-example-placeholder-single js-states form-control form-control-lg',
                      'style': 'width:100%'}

    def build_attrs(self, base_attrs, extra_attrs=None):
        base_attrs = super().build_attrs(base_attrs, extra_attrs)
        base_attrs.update(
            {"data-minimum-input-length": 0,
             "data-placeholder": self.empty_label,

             }
        )
        return base_attrs


class BaseSelect2MultipleWidgetMixin(ModelSelect2MultipleWidget):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.attrs = {'class': 'js-example-placeholder-single js-states form-control form-control-lg',
                      'style': 'width:100%'}

    def build_attrs(self, base_attrs, extra_attrs=None):
        base_attrs = super().build_attrs(base_attrs, extra_attrs)
        base_attrs.update(
            {"data-minimum-input-length": 0,
             "data-placeholder": self.empty_label,

             }
        )
        return base_attrs


class ModelMixin:
    """
    Mixin with methods from models
    """

    def get_all_fields(self):
        """
        Returned list all fields from model. Used in DetailView
        """
        fields = []
        expose_fields = ['id', 'slug']
        for f in self._meta.fields:

            fname = f.name
            # added selectable lists with get_xyz_display()
            get_choice = 'get_' + fname + '_display'
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, fname)
                except AttributeError:
                    value = None

            # Views all fields
            if f.editable and value and f.name not in expose_fields:
                fields.append(
                    {
                        'label': f.verbose_name,
                        'name': f.name,
                        'value': value,
                    }
                )
        return fields


class FormMessageMixin:
    """
    added messages in form
    """
    success_message = ''
    debug_message = ''
    info_message = ''
    warning_message = ''
    error_message = ''
    success_url = ''

    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        debug_message = self.get_debug_message(form.cleaned_data)
        info_message = self.get_info_message(form.cleaned_data)
        warning_message = self.get_warning_message(form.cleaned_data)
        error_message = self.get_error_message(form.cleaned_data)
        if not response:
            if error_message:
                messages.error(self.request, error_message)
        else:
            if success_message:
                messages.debug(self.request, debug_message)
            if info_message:
                messages.info(self.request, info_message)
            if success_message:
                messages.success(self.request, success_message)
            if warning_message:
                messages.warning(self.request, warning_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data

    def get_debug_message(self, cleaned_data):
        return self.debug_message % cleaned_data

    def get_info_message(self, cleaned_data):
        return self.info_message % cleaned_data

    def get_warning_message(self, cleaned_data):
        return self.warning_message % cleaned_data

    def get_error_message(self, cleaned_data):
        return self.error_message % cleaned_data