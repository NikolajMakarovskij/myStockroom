import csv
import datetime
from django.contrib import messages
from django.core.cache import cache
from django.http import HttpResponse
from django_select2.forms import ModelSelect2Widget

menu = [
    {'title': "Главная страница", 'url_name': 'core:index'},
    {'title': "Раб. места", 'url_name': 'workplace:workplace_index'},
    {'title': "Устройства", 'url_name': 'device:device_list'},
    {'title': "Сотрудники", 'url_name': 'employee:employee_index'},
    {'title': "Софт", 'url_name': 'software:software_index'},
    {'title': "ЭЦП", 'url_name': 'signature:signature_list'},
    {'title': "Склад", 'url_name': 'stockroom:stock_index'},
    {'title': "Расходники", 'url_name': 'consumables:consumables_list'},
    {'title': "Комплектующие", 'url_name': 'consumables:accessories_list'},
    {'title': "Контрагенты", 'url_name': 'counterparty:counterparty'},
    {'title': "Баланс", 'url_name': 'accounting:accounting_index'},
]

deviceMenu = [
    {'title': "Информация об устройстве", 'anchor': '#deviceInfo'},
    {'title': "Информация о расходнике", 'anchor': '#consumableInfo'},
    {'title': "Информация о комплектующем", 'anchor': '#accessorieseInfo'},
    {'title': "Местоположение", 'anchor': '#workplaceInfo'},
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
            cache.set('side_menu', side_menu, 3000)
        context = kwargs
        context['menu'] = side_menu
        context['query'] = self.request.GET.get('q')
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


class ExportAdmin:
    """
    Mixin to export data in admin panel
    """

    def export_to_csv(modeladmin, request, queryset):
        opts = modeladmin.model._meta
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
        writer = csv.writer(response)
        fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
        # Write a first row with header information
        writer.writerow([field.verbose_name for field in fields])
        # Write data rows
        for obj in queryset:
            data_row = []
            for field in fields:
                value = getattr(obj, field.name)
                if isinstance(value, datetime.datetime):
                    value = value.strftime('%d/%m/%Y')
                data_row.append(value)
            writer.writerow(data_row)
        return response

    export_to_csv.short_description = 'экспорт CSV'

    class Meta:
        verbose_name = 'экспорт CSV'
        verbose_name_plural = 'экспорт CSV'


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
