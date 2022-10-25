from django import forms
from .utils import WidgetCanAdd
from django.utils.translation import gettext_lazy as _
from .models.models import *

#Рабочее место
class workplaceForm(forms.ModelForm):  
    class Meta:
        model = Workplace
        fields = ['name', 'Room']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'Room': WidgetCanAdd(Room, related_url="new-room", attrs={'class': 'input-group form-select form-select-lg'}),
        } 

class roomForm(forms.ModelForm):  
    class Meta:
        model = Room
        fields = ['name', 'Floor', 'Building']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'Floor': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'Building': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        }

#Сотрудники
class employeeForm(forms.ModelForm):  
    class Meta:
        model = Employee
        fields = ['name', 'sername','family','Workplace','post','employeeEmail']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'sername': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'family': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'Workplace': WidgetCanAdd(Workplace, related_url="new-workplace", attrs={'class': 'input-group form-select form-select-lg'}),
            'post': WidgetCanAdd(Workplace, related_url="new-post", attrs={'class': 'input-group form-select form-select-lg'}),
            'employeeEmail': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
        } 
        error_messages = {
            'employeeEmail': {
                'unique': ("Такой адрес почты уже существует"),
            },
        }

class postForm(forms.ModelForm):  
    class Meta:
        model = post
        fields = ['name', 'departament',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'departament': WidgetCanAdd(departament, related_url="new-departament", attrs={'class': 'input-group form-select form-select-lg'}),
        } 

class departamentForm(forms.ModelForm):  
    class Meta:
        model = departament
        fields = ['name', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        } 

class softwareForm(forms.ModelForm):  
    class Meta:
        model = software
        fields = ['name', 'manufacturer', 'version', 'bitDepth', 'licenseKeyText', 'licenseKeyImg', 'licenseKeyFile', 'workstation']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
            'version': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'bitDepth': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'licenseKeyText': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'licenseKeyImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'licenseKeyFile': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'workstation': WidgetCanAdd(workstation, related_url="", attrs={'class': 'input-group form-select form-select-lg'}),
        } 

class manufacturerForm(forms.ModelForm):  
    class Meta:
        model = manufacturer
        fields = ['name', 'country', 'production' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'country': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'production': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        }     