from django import forms
from catalog.utils import WidgetCanAdd
from django.utils.translation import gettext_lazy as _
from .models import *

class signatureForm(forms.ModelForm):  
    class Meta:
        model = signature
        fields = ['name','licenseKeyFileOpen','licenseKeyFileClose','periodOpen','periodClose','employeeRegister','employeeStorage','workstation','storage']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'licenseKeyFileOpen': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'licenseKeyFileClose': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'periodOpen': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'datepicker form-control form-control-lg  ', 'type': 'date' }),
            'periodClose': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'datepicker form-control form-control-lg  ', 'type': 'date' }),
            'employeeRegister': WidgetCanAdd(employee, related_url="employee:new-employee", attrs={'class': 'form-select form-select-lg'}),
            'employeeStorage': WidgetCanAdd(employee, related_url="employee:new-employee", attrs={'class': 'form-select form-select-lg'}),
            'workstation': WidgetCanAdd(workstation, related_url="workstation:new-workstation", attrs={'class': 'form-select form-select-lg'}),
            'storage': WidgetCanAdd(storage, related_url="new-storage", attrs={'class': 'form-select form-select-lg'}),
            #'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        } 