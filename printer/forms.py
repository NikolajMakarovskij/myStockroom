from django import forms
from catalog.utils import WidgetCanAdd
from django.utils.translation import gettext_lazy as _
from workplace.models import workplace
from consumables.models import *
from catalog.models import *
from .models import printer


class printerForm(forms.ModelForm):  
    class Meta:
        model = printer
        fields = ['name','modelPrinter','manufacturer','serial','serialImg','inventImg','invent','usbPort','lanPort',
        'tray1','tray2','tray3','traySide','workplace','cartridge','fotoval','toner','score'
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
            'modelPrinter': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'form-select form-select-lg'}),
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
            'workplace': WidgetCanAdd(workplace, related_url="workplace:new-workplace", attrs={'class': 'form-select form-select-lg'}),
            'cartridge': WidgetCanAdd(cartridge, related_url="consumables:new-cartridge", attrs={'class': 'form-select form-select-lg'}),
            'fotoval': WidgetCanAdd(fotoval, related_url="consumables:new-fotoval", attrs={'class': 'form-select form-select-lg'}),
            'toner': WidgetCanAdd(toner, related_url="consumables:new-toner", attrs={'class': 'form-select form-select-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        } 