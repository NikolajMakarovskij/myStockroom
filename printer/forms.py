from django import forms
from catalog.utils import WidgetCanAdd
from consumables.models import Consumables
from django.utils.translation import gettext_lazy as _
from counterparty.models import Manufacturer
from .models import *


class printerForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = ['name','categories','manufacturer','serial','serialImg','inventImg','invent','usbPort','lanPort',
        'tray1','tray2','tray3','traySide','workplace','consumable','score','note'
            ]
        FORMAT = (
            ('A4', 'A4'),
            ('A3', 'A3'),
            ('A2', 'A2'),
            ('A1', 'A1'),
            ('A0', 'A0'),
            ('A5', 'A5'),
            ('Конверт', 'Конверт'),
            ('Отсутствует', 'Отсутствует'),
            )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'categories': WidgetCanAdd(Printer_cat, attrs={'class': 'form-select form-select-lg'}),
            'manufacturer': WidgetCanAdd(Manufacturer, related_url="counterparty:new-manufacturer", attrs={'class': 'form-select form-select-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'usbPort': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'lanPort': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'tray1': forms.Select(choices=FORMAT, attrs={'class': 'form-select form-select-lg'}),
            'tray2': forms.Select(choices=FORMAT, attrs={'class': 'form-select form-select-lg'}),
            'tray3': forms.Select(choices=FORMAT, attrs={'class': 'form-select form-select-lg'}),
            'traySide': forms.Select(choices=FORMAT, attrs={'class': 'form-select form-select-lg'}),
            'workplace': WidgetCanAdd(Workplace, related_url="workplace:new-workplace", attrs={'class': 'form-select form-select-lg'}),
            'consumable': WidgetCanAdd(Consumables, related_url="consumables:new-consumables", attrs={'class': 'form-select form-select-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'note': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
        } 