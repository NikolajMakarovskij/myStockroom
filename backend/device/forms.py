from django import forms
from core.utils import BaseModelSelect2WidgetMixin
from consumables.models import Consumables, Accessories
from counterparty.models import Manufacturer
from .models import Device, DeviceCat


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
    model = DeviceCat
    queryset = DeviceCat.objects.all().order_by("name")
    search_fields = [
        "name__icontains",
    ]


class ConWidget(BaseModelSelect2WidgetMixin):
    empty_label = "--выбрать--"
    model = Consumables
    queryset = Consumables.objects.all().order_by("name")
    search_fields = [
        "name__icontains",
        "categories__name__icontains",
        "description__icontains",
        "note__icontains",
        "buhCode__icontains",
        "manufacturer__name__icontains",
        "manufacturer__country__icontains",
        "manufacturer__production__icontains",
    ]


class AccWidget(BaseModelSelect2WidgetMixin):
    empty_label = "--выбрать--"
    model = Accessories
    queryset = Accessories.objects.all().order_by("name")
    search_fields = [
        "name__icontains",
        "categories__name__icontains",
        "description__icontains",
        "note__icontains",
        "buhCode__icontains",
        "manufacturer__name__icontains",
        "manufacturer__country__icontains",
        "manufacturer__production__icontains",
    ]


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'categories', 'manufacturer', 'serial', 'serialImg', 'invent', 'inventImg', 'description',
                  'note', 'accessories', 'consumable']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'categories': CategoryWidget,
            'manufacturer': ManufacturerWidget,
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'consumable': ConWidget,
            'accessories': AccWidget,
            'note': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),

        }
