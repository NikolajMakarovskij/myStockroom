from django import forms
from .utils import WidgetCanAdd
from django.utils.translation import gettext_lazy as _
from .models.models import *

#Рабочее место
class workplaceForm(forms.ModelForm):  
    class Meta:
        model = workplace
        fields = ['name', 'room']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'room': WidgetCanAdd(room, related_url="new-room", attrs={'class': 'input-group form-select form-select-lg'}),
        } 

class roomForm(forms.ModelForm):  
    class Meta:
        model = room
        fields = ['name', 'floor', 'building']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'floor': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'building': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        }

#Сотрудники
class employeeForm(forms.ModelForm):  
    class Meta:
        model = employee
        fields = ['name', 'sername','family','workplace','post','employeeEmail']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'sername': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'family': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'workplace': WidgetCanAdd(workplace, related_url="new-workplace", attrs={'class': 'input-group form-select form-select-lg'}),
            'post': WidgetCanAdd(post, related_url="new-post", attrs={'class': 'input-group form-select form-select-lg'}),
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

class manufacturerForm(forms.ModelForm):  
    class Meta:
        model = manufacturer
        fields = ['name', 'country', 'production' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'country': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'production': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
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

class workstationForm(forms.ModelForm):  
    class Meta:
        model = workstation
        fields = ['name','manufacturer','modelComputer','serial','serialImg','inventImg','invent','motherboard',
            'monitor','cpu','gpu','ram','ssd','hdd','os','dcpower','keyBoard','mouse','ups','workplace','employee',
            ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
            'modelComputer': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'motherboard': WidgetCanAdd(motherboard, related_url="new-motherboard", attrs={'class': 'input-group form-select form-select-lg'}),
            'monitor': WidgetCanAdd(monitor, related_url="new-monitor", attrs={'class': 'input-group form-select form-select-lg'}),
            'cpu': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'gpu': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'ram': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'ssd': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'hdd': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'os': WidgetCanAdd(os, related_url="new-OS", attrs={'class': 'input-group form-select form-select-lg'}),
            'dcpower': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'keyBoard': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'mouse': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'ups': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'workplace': WidgetCanAdd(workplace, related_url="new-workplace", attrs={'class': 'input-group form-select form-select-lg'}),
            'employee': WidgetCanAdd(employee, related_url="new-employee", attrs={'class': 'input-group form-select form-select-lg'}),
        } 
  
class monitorForm(forms.ModelForm):  
    class Meta:
        model = monitor
        fields = ['name','manufacturer','serial','serialImg','inventImg','invent','resolution','frequency','typeDisplay',
        'dpi','usbPort','hdmi','vga','dvi','displayPort',
            ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'resolution': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'frequency': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'typeDisplay': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'dpi': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'usbPort': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'hdmi': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'vga': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'dvi': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'displayPort': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        } 

class motherboardForm(forms.ModelForm):  
    class Meta:
        model = motherboard
        fields = ['name','manufacturer','serial','serialImg','inventImg','invent','cpuSoket','ramSlot',
                    'usb_2','usb_3','usb_3_1','usb_3_2','usb_4_0','comPort','pcie_x1','pcie_x16', 
                    'pci','sata','m2','vga','hdmi','dvi','dispayPort','powerSupply','powerSupplyCPU' 
            ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'cpuSoket': forms.TextInput(attrs={'class': 'form-control form-control-lg'}), 
            'ramSlot': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'usb_2': forms.TextInput(attrs={'class': 'form-control form-control-lg'}), 
            'usb_3': forms.TextInput(attrs={'class': 'form-control form-control-lg'}), 
            'usb_3_1': forms.TextInput(attrs={'class': 'form-control form-control-lg'}), 
            'usb_3_2': forms.TextInput(attrs={'class': 'form-control form-control-lg'}), 
            'usb_4_0': forms.TextInput(attrs={'class': 'form-control form-control-lg'}), 
            'comPort': forms.TextInput(attrs={'class': 'form-control form-control-lg'}), 
            'pcie_x1': forms.TextInput(attrs={'class': 'form-control form-control-lg'}), 
            'pcie_x16': forms.TextInput(attrs={'class': 'form-control form-control-lg'}), 
            'pci': forms.TextInput(attrs={'class': 'form-control form-control-lg'}), 
            'sata': forms.TextInput(attrs={'class': 'form-control form-control-lg'}), 
            'm2': forms.TextInput(attrs={'class': 'form-control form-control-lg'}), 
            'vga': forms.TextInput(attrs={'class': 'form-control form-control-lg'}), 
            'hdmi': forms.TextInput(attrs={'class': 'form-control form-control-lg'}), 
            'dvi': forms.TextInput(attrs={'class': 'form-control form-control-lg'}), 
            'dispayPort': forms.TextInput(attrs={'class': 'form-control form-control-lg'}), 
            'powerSupply': forms.TextInput(attrs={'class': 'form-control form-control-lg'}), 
            'powerSupplyCPU': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),           
        } 


