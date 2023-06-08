from django import forms
from catalog.utils import WidgetCanAdd
from consumables.models import Consumables
from django.utils.translation import gettext_lazy as _
from counterparty.models import Manufacturer
from .models import *


class deviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name','categories','consumable','manufacturer','serial','serialImg','invent','inventImg','description','note', 'workplace']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'categories': WidgetCanAdd(Device_cat, attrs={'class': 'form-select form-select-lg'}),
            'manufacturer': WidgetCanAdd(Manufacturer, related_url="counterparty:new-manufacturer", attrs={'class': 'form-select form-select-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'workplace': WidgetCanAdd(Workplace, related_url="workplace:new-workplace", attrs={'class': 'form-select form-select-lg'}),
            'consumable': WidgetCanAdd(Consumables, related_url="consumables:new-consumables", attrs={'class': 'form-select form-select-lg'}),
            'note': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
        } 