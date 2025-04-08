from django import forms

from core.utils import BaseModelSelect2WidgetMixin
from counterparty.models import Manufacturer

from .models import Os, Software


class ManufacturerWidget(BaseModelSelect2WidgetMixin):
    """_CManufacturerWidget_
    Autocomplete plugin for the manufacturer selection field

    Returns:
        empty_label (str): _value of empty_label_
        model (Manufacturer):
        querysets (Manufacturer): _returns querysets of model in form_
        search_fields (list[str]): _fields of the model to search for are specified_
    """

    empty_label = "--выбрать--"
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    search_fields = [
        "name__icontains",
        "country__icontains",
        "production__icontains",
    ]


class SoftwareForm(forms.ModelForm):  # type: ignore[type-arg]
    """_SoftwareForm_"""

    class Meta:
        """_Class returns form of Software model_

        Returns:
            model (Software):
            fields (list[str]): _returns fields of model in form_
            widgets (dict[str,str]): _returns widgets of model in form_
            error_messages (str): _returns error messages of model field in form_
        """

        model = Software
        fields = [
            "name",
            "manufacturer",
            "version",
            "bitDepth",
            "licenseKeyText",
            "licenseKeyImg",
            "licenseKeyFile",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "manufacturer": ManufacturerWidget,
            "version": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "bitDepth": forms.TextInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "licenseKeyText": forms.TextInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "licenseKeyImg": forms.FileInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "licenseKeyFile": forms.FileInput(
                attrs={"class": "form-control form-control-lg"}
            ),
        }


class OSForm(forms.ModelForm):  # type: ignore[type-arg]
    """_OSForm_"""

    class Meta:
        """_Class returns form of OS model_

        Returns:
            model (OS):
            fields (list[str]): _returns fields of model in form_
            widgets (dict[str,str]): _returns widgets of model in form_
            error_messages (str): _returns error messages of model field in form_
        """

        model = Os
        fields = [
            "name",
            "manufacturer",
            "version",
            "bitDepth",
            "licenseKeyText",
            "licenseKeyImg",
            "licenseKeyFile",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "manufacturer": ManufacturerWidget,
            "version": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "bitDepth": forms.TextInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "licenseKeyText": forms.TextInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "licenseKeyImg": forms.FileInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "licenseKeyFile": forms.FileInput(
                attrs={"class": "form-control form-control-lg"}
            ),
        }
