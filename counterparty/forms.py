from django import forms
from django.utils.translation import gettext_lazy as _
from .models import  Manufacturer

class manufacturerForm(forms.ModelForm):  
    class Meta:
        model = Manufacturer
        fields = ['name', 'country', 'production' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'country': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'production': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        }