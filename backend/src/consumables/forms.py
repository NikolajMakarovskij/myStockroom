from django import forms

from core.utils import BaseModelSelect2WidgetMixin
from counterparty.models import Manufacturer

from .models import AccCat, Accessories, Categories, Consumables


class ManufacturerWidget(BaseModelSelect2WidgetMixin):
    """_ManufacturerWidget_
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


class CategoryWidget(BaseModelSelect2WidgetMixin):
    """_CategoryWidget_
    Autocomplete plugin for the category selection field

    Returns:
        empty_label (str): _value of empty_label_
        model (Categories):
        querysets (Categories): _returns querysets of model in form_
        search_fields (list[str]): _fields of the model to search for are specified_
    """

    empty_label = "--выбрать--"
    model = Categories
    queryset = Categories.objects.all().order_by("name")
    search_fields = ["name__icontains"]


class AccCatWidget(BaseModelSelect2WidgetMixin):
    """_AccCatWidget_
    Autocomplete plugin for the category selection field

    Returns:
        empty_label (str): _value of empty_label_
        model (AccCat):
        querysets (AccCat): _returns querysets of model in form_
        search_fields (list[str]): _fields of the model to search for are specified_
    """

    empty_label = "--выбрать--"
    model = AccCat
    queryset = AccCat.objects.all().order_by("name")
    search_fields = ["name__icontains"]


class ConsumablesForm(forms.ModelForm):  # type: ignore[type-arg]
    """_ConsumablesForm_"""

    class Meta:
        """_Class returns form of Consumables model_

        Returns:
            model (Consumables):
            fields (list[str]): _returns fields of model in form_
            widgets (dict[str,str]): _returns widgets of model in form_
        """

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


class AccessoriesForm(forms.ModelForm):  # type: ignore[type-arg]
    """_AccessoriesForm_"""

    class Meta:
        """_Class returns form of Accessories model_

        Returns:
            model (Accessories):
            fields (list[str]): _returns fields of model in form_
            widgets (dict[str,str]): _returns widgets of model in form_
        """

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
