from django import forms

from consumables.models import Accessories, Consumables
from core.utils import BaseModelSelect2WidgetMixin, BaseSelect2MultipleWidgetMixin
from counterparty.models import Manufacturer

from .models import Device, DeviceCat


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
        model (DeviceCat):
        querysets (DeviceCat): _returns querysets of model in form_
        search_fields (list[str]): _fields of the model to search for are specified_
    """

    empty_label = "--выбрать--"
    model = DeviceCat
    queryset = DeviceCat.objects.all().order_by("name")
    search_fields = [
        "name__icontains",
    ]


class ConWidget(BaseSelect2MultipleWidgetMixin):
    """_ConWidget_
    Autocomplete plugin for the consumables selection field

    Returns:
        empty_label (str): _value of empty_label_
        model (Consumables):
        querysets (Consumables): _returns querysets of model in form_
        search_fields (list[str]): _fields of the model to search for are specified_
    """

    empty_label = "--выбрать--"
    model = Consumables
    queryset = Consumables.objects.all().order_by("name")
    search_fields = [
        "name__icontains",
        "categories__name__icontains",
        "description__icontains",
        "note__icontains",
        "manufacturer__name__icontains",
        "manufacturer__country__icontains",
        "manufacturer__production__icontains",
    ]


class AccWidget(BaseSelect2MultipleWidgetMixin):
    """_AccWidget_
    Autocomplete plugin for the consumables selection field

    Returns:
        empty_label (str): _value of empty_label_
        model (Accessories):
        querysets (Accessories): _returns querysets of model in form_
        search_fields (list[str]): _fields of the model to search for are specified_
    """

    empty_label = "--выбрать--"
    model = Accessories
    queryset = Accessories.objects.all().order_by("name")
    search_fields = [
        "name__icontains",
        "categories__name__icontains",
        "description__icontains",
        "note__icontains",
        "manufacturer__name__icontains",
        "manufacturer__country__icontains",
        "manufacturer__production__icontains",
    ]


class DeviceForm(forms.ModelForm):
    """_DeviceForm_"""

    class Meta:
        """_Class returns form of Device model_

        Returns:
            model (Device):
            fields (list[str]): _returns fields of model in form_
            widgets (dict[str,str]): _returns widgets of model in form_
        """

        model = Device
        fields = [
            "name",
            "categories",
            "serial",
            "serialImg",
            "invent",
            "inventImg",
            "hostname",
            "ip_address",
            "login",
            "pwd",
            "accessories",
            "consumable",
            "manufacturer",
            "description",
            "note",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "categories": CategoryWidget,
            "manufacturer": ManufacturerWidget,
            "hostname": forms.TextInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "ip_address": forms.TextInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "login": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "pwd": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "serial": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "serialImg": forms.FileInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "invent": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "inventImg": forms.FileInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control form-control-lg"}
            ),
            "consumable": ConWidget,
            "accessories": AccWidget,
            "note": forms.Textarea(attrs={"class": "form-control form-control-lg"}),
        }
