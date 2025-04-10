from django import forms

from core.utils import BaseModelSelect2WidgetMixin
from counterparty.models import Manufacturer

from .models import Os, Software


class ManufacturerWidget(BaseModelSelect2WidgetMixin):
    empty_label = "--выбрать--"
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    search_fields = [
        "name__icontains",
        "country__icontains",
        "production__icontains",
    ]


class SoftwareForm(forms.ModelForm):  # type: ignore[type-arg]
    class Meta:
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
    class Meta:
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
