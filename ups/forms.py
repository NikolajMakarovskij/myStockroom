from django import forms
from catalog.utils import WidgetCanAdd
from django.utils.translation import gettext_lazy as _
from consumables.models import accumulator
from .models import *

class upsForm(forms.ModelForm):   
    class Meta:
        model = ups
        fields = ['name','manufacturer','serial','serialImg','inventImg','invent','power','voltage','current',
                    'accumulator1','accumulator2','accumulator3','accumulator4','cassette1','cassette2','cassette3','cassette4','score']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="counterparty:new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'power': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'voltage': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'current': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'accumulator1': WidgetCanAdd(accumulator, related_url="consumables:new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator2': WidgetCanAdd(accumulator, related_url="consumables:new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator3': WidgetCanAdd(accumulator, related_url="consumables:new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator4': WidgetCanAdd(accumulator, related_url="consumables:new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'cassette1': WidgetCanAdd(cassette, related_url="ups:new-cassette", attrs={'class': 'input-group form-select form-select-lg'}),
            'cassette2': WidgetCanAdd(cassette, related_url="ups:new-cassette", attrs={'class': 'input-group form-select form-select-lg'}),
            'cassette3': WidgetCanAdd(cassette, related_url="ups:new-cassette", attrs={'class': 'input-group form-select form-select-lg'}),
            'cassette4': WidgetCanAdd(cassette, related_url="ups:new-cassette", attrs={'class': 'input-group form-select form-select-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        }  

class cassetteForm(forms.ModelForm):   
    class Meta:
        model = cassette
        fields = ['name','manufacturer','serial','serialImg','inventImg','invent','power','voltage','current',
                    'accumulator1','accumulator2','accumulator3','accumulator4','accumulator5','accumulator6','accumulator7','accumulator8','accumulator9','accumulator10','score']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="counterparty:new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'power': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'voltage': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'current': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'accumulator1': WidgetCanAdd(accumulator, related_url="consumables:new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator2': WidgetCanAdd(accumulator, related_url="consumables:new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator3': WidgetCanAdd(accumulator, related_url="consumables:new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator4': WidgetCanAdd(accumulator, related_url="consumables:new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator5': WidgetCanAdd(accumulator, related_url="consumables:new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator6': WidgetCanAdd(accumulator, related_url="consumables:new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator7': WidgetCanAdd(accumulator, related_url="consumables:new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator8': WidgetCanAdd(accumulator, related_url="consumables:new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator9': WidgetCanAdd(accumulator, related_url="consumables:new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator10': WidgetCanAdd(accumulator, related_url="consumables:new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        } 