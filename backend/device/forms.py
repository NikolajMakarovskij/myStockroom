from django import forms
from catalog.utils import WidgetCanAdd, BaseModelSelect2WidgetMixin
from consumables.models import Consumables, Accessories
from counterparty.models import Manufacturer
from workplace.models import Workplace
from .models import Device, DeviceCat


class WorkplaceWidget(BaseModelSelect2WidgetMixin):
    empty_label = "--выбрать--"
    model = Workplace
    queryset = Workplace.objects.all().order_by("name")
    search_fields = [
        "name__icontains",
    ]


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'categories', 'manufacturer', 'serial', 'serialImg', 'invent', 'inventImg', 'description',
                  'note', 'accessories', 'consumable', 'workplace']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'categories': WidgetCanAdd(DeviceCat, attrs={'class': 'form-select form-select-lg'}),
            'manufacturer': WidgetCanAdd(Manufacturer, related_url="counterparty:new-manufacturer",
                                         attrs={'class': 'form-select form-select-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'consumable': WidgetCanAdd(Consumables, related_url="consumables:new-consumables",
                                       attrs={'class': 'form-select form-select-lg'}),
            'accessories': WidgetCanAdd(Accessories, related_url="consumables:new-accessories",
                                        attrs={'class': 'form-select form-select-lg'}),
            'note': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),

        }
