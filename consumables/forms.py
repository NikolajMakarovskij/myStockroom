from django import forms
from catalog.utils import WidgetCanAdd
from django.utils.translation import gettext_lazy as _
from .models import *


class cartridgeForm(forms.ModelForm):  
    class Meta:
        model = Cartridge
        fields = ['name','manufacturer','buhCode','score','rack','shelf' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(Manufacturer, related_url="counterparty:new-manufacturer", attrs={'class': 'form-select form-select-lg'}),
            'buhCode': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'rack': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'shelf': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        } 

class fotovalForm(forms.ModelForm):  
    class Meta:
        model = Fotoval
        fields = ['name','manufacturer','mileage','buhCode','score','rack','shelf' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(Manufacturer, related_url="counterparty:new-manufacturer", attrs={'class': 'form-select form-select-lg'}),
            'mileage': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'buhCode': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'rack': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'shelf': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        } 

class tonerForm(forms.ModelForm):  
    class Meta:
        model = Toner
        fields = ['name','manufacturer','buhCode','score','rack','shelf' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(Manufacturer, related_url="counterparty:new-manufacturer", attrs={'class': 'form-select form-select-lg'}),
            'buhCode': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'rack': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'shelf': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        } 

class accumulatorForm(forms.ModelForm):   
    class Meta:
        model = Accumulator
        fields = ['name','manufacturer','power','voltage','current','score','rack','shelf' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(Manufacturer, related_url="counterparty:new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
            'power': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'voltage': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'current': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'rack': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'shelf': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        } 

class storageForm(forms.ModelForm):  
    class Meta:
        model = Storage
        fields = ['name','modelStorage','manufacturer','serial','serialImg','inventImg','invent','plug','typeMemory','volumeMemory','employee']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'modelStorage': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(Manufacturer, related_url="counterparty:new-manufacturer", attrs={'class': 'form-select form-select-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'plug': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'typeMemory': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'volumeMemory': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'employee': WidgetCanAdd(Employee, related_url="employee:new-employee", attrs={'class': 'form-select form-select-lg'}),
        } 