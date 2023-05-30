from django import forms
from catalog.utils import WidgetCanAdd
from django.utils.translation import gettext_lazy as _
from .models import *
from django.core.exceptions import ValidationError
from django.contrib import messages


class consumablesForm(forms.ModelForm):  
    class Meta:
        model = Consumables
        fields = ['name','categories','manufacturer','buhCode','description', 'note','score', 'serial', 'serialImg','invent', 'inventImg']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'categories': WidgetCanAdd(Categories, attrs={'class': 'form-select form-select-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg',}),
            'note': forms.Textarea(attrs={'class': 'form-control form-control-lg',}),
            'manufacturer': WidgetCanAdd(Manufacturer, related_url="counterparty:new-manufacturer", attrs={'class': 'form-select form-select-lg'}),
            'buhCode': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
        } 



