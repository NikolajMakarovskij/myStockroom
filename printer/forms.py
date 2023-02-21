from django import forms
from catalog.utils import WidgetCanAdd
from consumables.models import Categories, Consumables
from django.utils.translation import gettext_lazy as _
from counterparty.models import Manufacturer
from .models import *
CARTRIDGE_FILTER = Consumables.objects.filter(categories__name__contains='Картриджы')
TONER_FILTER = Consumables.objects.filter(categories__name__contains='Тонер')
FOTOVAL_FILTER = Consumables.objects.filter(categories__name__contains='Фотовал')
FOTODRUMM_FILTER = Consumables.objects.filter(categories__name__contains='Фотобарабан')

class printerForm(forms.ModelForm):
    cartridge =  forms.ModelChoiceField(queryset=CARTRIDGE_FILTER, widget=forms.Select(attrs={'class':'form-select form-select-lg btn-outline-dark'}))
    fotoval =  forms.ModelChoiceField(queryset=FOTOVAL_FILTER, widget=forms.Select(attrs={'class':'form-select form-select-lg btn-outline-dark'}))
    toner =  forms.ModelChoiceField(queryset=TONER_FILTER, widget=forms.Select(attrs={'class':'form-select form-select-lg btn-outline-dark'}))
    fotodrumm =  forms.ModelChoiceField(queryset=FOTODRUMM_FILTER, widget=forms.Select(attrs={'class':'form-select form-select-lg btn-outline-dark'}))
    class Meta:
        model = Printer
        fields = ['name','categories','manufacturer','serial','serialImg','inventImg','invent','usbPort','lanPort',
        'tray1','tray2','tray3','traySide','workplace','cartridge','fotoval','toner','fotodrumm','score','note'
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
            'categories': WidgetCanAdd(Categories, attrs={'class': 'form-select form-select-lg'}),
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
            'cartridge': forms.Select(attrs={'class':'form-select form-select-lg '}),
            'fotoval': forms.Select(attrs={'class':'form-select form-select-lg '}),
            'toner':  forms.Select(attrs={'class':'form-select form-select-lg '}),
            'fotodrumm':  forms.Select(attrs={'class':'form-select form-select-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'note': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
        } 