from django import forms
from catalog.utils import WidgetCanAdd
from django.utils.translation import gettext_lazy as _
from catalog.models import manufacturer
from .models import software, os

class softwareForm(forms.ModelForm):  
    class Meta:
        model = software
        fields = ['name', 'manufacturer', 'version', 'bitDepth', 'licenseKeyText', 'licenseKeyImg', 'licenseKeyFile',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
            'version': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'bitDepth': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'licenseKeyText': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'licenseKeyImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'licenseKeyFile': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
        } 

class OSForm(forms.ModelForm):  
    class Meta:
        model = os
        fields = ['name', 'manufacturer', 'version', 'bitDepth', 'licenseKeyText', 'licenseKeyImg', 'licenseKeyFile',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
            'version': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'bitDepth': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'licenseKeyText': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'licenseKeyImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'licenseKeyFile': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
        }  