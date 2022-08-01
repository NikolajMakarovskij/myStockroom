from cProfile import label
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime 
from django.forms import ModelForm
from .models import Building

class RenewBuildingModelForm(ModelForm):
    class Meta:
        model = Building
        fields = ['name']
        label = {'text':'name'}