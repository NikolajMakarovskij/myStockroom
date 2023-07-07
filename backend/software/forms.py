from django import forms
from catalog.utils import WidgetCanAdd
from counterparty.models import Manufacturer
from .models import Software, Os


class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ['name', 'manufacturer', 'version', 'bitDepth', 'licenseKeyText', 'licenseKeyImg', 'licenseKeyFile', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(Manufacturer, related_url="counterparty:new-manufacturer",
                                         attrs={'class': 'input-group form-select form-select-lg'}),
            'version': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'bitDepth': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'licenseKeyText': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'licenseKeyImg': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'licenseKeyFile': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
        }


class OSForm(forms.ModelForm):
    class Meta:
        model = Os
        fields = ['name', 'manufacturer', 'version', 'bitDepth', 'licenseKeyText', 'licenseKeyImg', 'licenseKeyFile', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(Manufacturer, related_url="counterparty:new-manufacturer",
                                         attrs={'class': 'input-group form-select form-select-lg'}),
            'version': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'bitDepth': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'licenseKeyText': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'licenseKeyImg': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'licenseKeyFile': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
        }
