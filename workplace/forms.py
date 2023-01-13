from django import forms
from catalog.utils import WidgetCanAdd
from django.utils.translation import gettext_lazy as _
from .models import *

class workplaceForm(forms.ModelForm):  
    class Meta:
        model = workplace
        fields = ['name', 'room',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'room': WidgetCanAdd(room, related_url="workplace:new-room", attrs={'class': 'input-group form-select form-select-lg'}),
        } 

class roomForm(forms.ModelForm):  
    class Meta:
        model = room
        fields = ['name', 'floor', 'building',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'floor': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'building': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        }