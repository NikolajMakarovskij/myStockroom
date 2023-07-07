from django import forms
from catalog.utils import WidgetCanAdd
from .models import *


class ConsumablesForm(forms.ModelForm):
    class Meta:
        model = Consumables
        fields = ['name', 'buhCode', 'categories', 'manufacturer', 'serial', 'serialImg', 'invent', 'inventImg',
                  'description', 'note', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'categories': WidgetCanAdd(Categories, attrs={'class': 'form-select form-select-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg', }),
            'note': forms.Textarea(attrs={'class': 'form-control form-control-lg', }),
            'manufacturer': WidgetCanAdd(Manufacturer, related_url="counterparty:new-manufacturer",
                                         attrs={'class': 'form-select form-select-lg'}),
            'buhCode': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
        }


class AccessoriesForm(forms.ModelForm):
    class Meta:
        model = Accessories
        fields = ['name', 'buhCode', 'categories', 'manufacturer', 'serial', 'serialImg', 'invent', 'inventImg',
                  'description', 'note', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'categories': WidgetCanAdd(AccCat, attrs={'class': 'form-select form-select-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg', }),
            'note': forms.Textarea(attrs={'class': 'form-control form-control-lg', }),
            'manufacturer': WidgetCanAdd(Manufacturer, related_url="counterparty:new-manufacturer",
                                         attrs={'class': 'form-select form-select-lg'}),
            'buhCode': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
        }
