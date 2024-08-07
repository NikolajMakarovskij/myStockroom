from django import forms

from core.utils import BaseModelSelect2WidgetMixin
from counterparty.models import Manufacturer

from .models import AccCat, Accessories, Categories, Consumables


class ManufacturerWidget(BaseModelSelect2WidgetMixin):
    empty_label = "--выбрать--"
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    search_fields = [
        "name__icontains",
        "country__icontains",
        "production__icontains",
    ]


class CategoryWidget(BaseModelSelect2WidgetMixin):
    empty_label = "--выбрать--"
    model = Categories
    queryset = Categories.objects.all().order_by("name")
    search_fields = ["name__icontains"]


class AccCatWidget(BaseModelSelect2WidgetMixin):
    empty_label = "--выбрать--"
    model = AccCat
    queryset = AccCat.objects.all().order_by("name")
    search_fields = ["name__icontains"]


class ConsumablesForm(forms.ModelForm):
    class Meta:
        model = Consumables
        fields = [
            "name",
            "categories",
            "manufacturer",
            "serial",
            "serialImg",
            "invent",
            "inventImg",
            "description",
            "note",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "categories": CategoryWidget,
            "description": forms.Textarea(
                attrs={
                    "class": "form-control form-control-lg",
                }
            ),
            "note": forms.Textarea(
                attrs={
                    "class": "form-control form-control-lg",
                }
            ),
            "manufacturer": ManufacturerWidget,
            "serial": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "serialImg": forms.FileInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "invent": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "inventImg": forms.FileInput(
                attrs={"class": "form-control form-control-lg"}
            ),
        }


class AccessoriesForm(forms.ModelForm):
    class Meta:
        model = Accessories
        fields = [
            "name",
            "categories",
            "manufacturer",
            "serial",
            "serialImg",
            "invent",
            "inventImg",
            "description",
            "note",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "categories": AccCatWidget,
            "description": forms.Textarea(
                attrs={
                    "class": "form-control form-control-lg",
                }
            ),
            "note": forms.Textarea(
                attrs={
                    "class": "form-control form-control-lg",
                }
            ),
            "manufacturer": ManufacturerWidget,
            "serial": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "serialImg": forms.FileInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "invent": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "inventImg": forms.FileInput(
                attrs={"class": "form-control form-control-lg"}
            ),
        }
