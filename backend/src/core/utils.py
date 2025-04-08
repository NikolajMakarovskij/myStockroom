from django.contrib import messages
from django.core.cache import cache
from django_select2.forms import (  # type: ignore[import-untyped]
    ModelSelect2MultipleWidget,
    ModelSelect2Widget,
)

menu = [
    {"title": "Главная страница", "url_name": "core:index"},
    {"title": "Раб. места", "url_name": "workplace:workplace_index"},
    {"title": "Устройства", "url_name": "device:device_list"},
    {"title": "Сотрудники", "url_name": "employee:employee_index"},
    {"title": "Софт", "url_name": "software:software_index"},
    {"title": "ЭЦП", "url_name": "signature:signature_list"},
    {"title": "Склад", "url_name": "stockroom:stock_index"},
    {"title": "Расходники", "url_name": "consumables:consumables_list"},
    {"title": "Комплектующие", "url_name": "consumables:accessories_list"},
    {"title": "Контрагенты", "url_name": "counterparty:counterparty"},
    {"title": "Баланс", "url_name": "accounting:accounting_index"},
]


class DataMixin:
    """_DataMixin_: Mixin add pagination and menu in views

    Returns:
        paginate (int): _pagination const_
    """

    paginate: int = 20

    def get_user_context(self, **kwargs):
        """_get_user_context_: returns context for views

        Returns:
            menu (dict[str, str]): _Navigation side menu_
            query (str): _q_ returns query for search in views
            obj_list_count (int): _count_ queryset count
        """
        side_menu = cache.get("side_menu")
        if not side_menu:
            side_menu = menu
            cache.set("side_menu", side_menu, 3000)
        context = kwargs
        context["menu"] = side_menu
        context["query"] = self.request.GET.get("q")  # type: ignore[attr-defined]
        context["obj_list_count"] = self.get_queryset().count()  # type: ignore[attr-defined]
        return context


class BaseModelSelect2WidgetMixin(ModelSelect2Widget):
    """_BaseModelSelect2WidgetMixin_ Adds plugin Select2 in views"""

    def __init__(self, **kwargs):
        """_add js and css styles_

        Returns:
            class (str): _js-example-placeholder-single js-states form-control form-control-lg_
            style (str): "width:100%"
        """
        super().__init__(kwargs)
        self.attrs = {
            "class": "js-example-placeholder-single js-states form-control form-control-lg",
            "style": "width:100%",
        }

    def build_attrs(self, base_attrs, extra_attrs=None):
        """_build_attrs_

        Args:
            base_attrs (_type_): _description_
            extra_attrs (_type_, optional): _description_

        Returns:
            _base_attrs (_type_): _update attrs_
        """
        base_attrs = super().build_attrs(base_attrs, extra_attrs)
        base_attrs.update(
            {
                "data-minimum-input-length": 0,
                "data-placeholder": self.empty_label,
            }
        )
        return base_attrs


class BaseSelect2MultipleWidgetMixin(ModelSelect2MultipleWidget):
    """_BaseSelect2MultipleWidgetMixin_ Adds plugin Select2 in views for multiple select"""

    def __init__(self, **kwargs):
        """_add js and css styles_

        Returns:
            class (str): _js-example-placeholder-single js-states form-control form-control-lg_
            style (str): "width:100%"
        """
        super().__init__(kwargs)
        self.attrs = {
            "class": "js-example-placeholder-single js-states form-control form-control-lg",
            "style": "width:100%",
        }

    def build_attrs(self, base_attrs, extra_attrs=None):
        """_build_attrs_

        Args:
            base_attrs (_type_): _description_
            extra_attrs (_type_, optional): _description_

        Returns:
            _base_attrs (_type_): _update attrs_
        """
        base_attrs = super().build_attrs(base_attrs, extra_attrs)
        base_attrs.update(
            {
                "data-minimum-input-length": 0,
                "data-placeholder": self.empty_label,
            }
        )
        return base_attrs


class ModelMixin:
    """_ModelMixin_ Mixin with methods from models"""

    def get_all_fields(self):
        """_get_all_fields_: returns all fields from model

        Returns:
            fields (dict[str, str]): dict from the list of fields and their values for the model, except those excluded fields
            expose_fields (list[str]): excluded fields
        """

        fields = []
        expose_fields = ["id", "slug"]
        for f in self._meta.fields:  # type: ignore[attr-defined]
            fname = f.name
            # added selectable lists with get_xyz_display()
            get_choice = "get_" + fname + "_display"
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
                        "label": f.verbose_name,
                        "name": f.name,
                        "value": value,
                    }
                )
        return fields


class FormMessageMixin:
    """_FormMessageMixin_ Add messages in forms

    Returns:
        success_message (str): _description_
        debug_message (str): _description_
        info_message (str): _description_
        warning_message (str): _description_
        error_message (str): _description_
    """

    success_message: str = ""
    debug_message: str = ""
    info_message: str = ""
    warning_message: str = ""
    error_message: str = ""

    def form_valid(self, form):
        """_form_valid_ Validation forms

        Args:
            form (_type_): _description_

        Returns:
            response (bool | str): _Returns server response or error message_
        """
        response = super().form_valid(form)  # type: ignore[misc]
        success_message = self.get_success_message(form.cleaned_data)
        debug_message = self.get_debug_message(form.cleaned_data)
        info_message = self.get_info_message(form.cleaned_data)
        warning_message = self.get_warning_message(form.cleaned_data)
        error_message = self.get_error_message(form.cleaned_data)
        if not response:
            if error_message:
                messages.error(self.request, error_message)  # type: ignore[attr-defined]
        else:
            if debug_message:
                messages.debug(self.request, debug_message)  # type: ignore[attr-defined]
            if info_message:
                messages.info(self.request, info_message)  # type: ignore[attr-defined]
            if success_message:
                messages.success(self.request, success_message)  # type: ignore[attr-defined]
            if warning_message:
                messages.warning(self.request, warning_message)  # type: ignore[attr-defined]
        return response

    def get_success_message(self, cleaned_data):
        """_get_success_message_

        Args:
            cleaned_data (_type_): _clean form data_

        Returns:
            message (str): _return message_
        """
        return self.success_message % cleaned_data

    def get_debug_message(self, cleaned_data):
        """_get_debug_message_

        Args:
            cleaned_data (_type_): _clean form data_

        Returns:
            message (str): _return message_
        """
        return self.debug_message % cleaned_data

    def get_info_message(self, cleaned_data):
        """_get_info_message_

        Args:
            cleaned_data (_type_): _clean form data_

        Returns:
            message (str): _return message_
        """
        return self.info_message % cleaned_data

    def get_warning_message(self, cleaned_data):
        """_get_warning_message_

        Args:
            cleaned_data (_type_): _clean form data_

        Returns:
            message (str): _return message_
        """
        return self.warning_message % cleaned_data

    def get_error_message(self, cleaned_data):
        """_get_error_message_

        Args:
            cleaned_data (_type_): _clean form data_

        Returns:
            message (str): _return message_
        """
        return self.error_message % cleaned_data
