from django import forms
from .utils import WidgetCanAdd
from django.utils.translation import gettext_lazy as _
from workplace.models import workplace
from employee.models import employee
from workstation.models import workstation
from .models.models import *
from .models.printer_model import *
from .models.signature_model import *
from .models.ups_model import *



class manufacturerForm(forms.ModelForm):  
    class Meta:
        model = manufacturer
        fields = ['name', 'country', 'production' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'country': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'production': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        }

    

class upsForm(forms.ModelForm):   
    class Meta:
        model = ups
        fields = ['name','manufacturer','serial','serialImg','inventImg','invent','power','voltage','current',
                    'accumulator1','accumulator2','accumulator3','accumulator4','cassette1','cassette2','cassette3','cassette4','score']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'power': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'voltage': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'current': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'accumulator1': WidgetCanAdd(accumulator, related_url="new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator2': WidgetCanAdd(accumulator, related_url="new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator3': WidgetCanAdd(accumulator, related_url="new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator4': WidgetCanAdd(accumulator, related_url="new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'cassette1': WidgetCanAdd(cassette, related_url="new-cassette", attrs={'class': 'input-group form-select form-select-lg'}),
            'cassette2': WidgetCanAdd(cassette, related_url="new-cassette", attrs={'class': 'input-group form-select form-select-lg'}),
            'cassette3': WidgetCanAdd(cassette, related_url="new-cassette", attrs={'class': 'input-group form-select form-select-lg'}),
            'cassette4': WidgetCanAdd(cassette, related_url="new-cassette", attrs={'class': 'input-group form-select form-select-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        }  

class cassetteForm(forms.ModelForm):   
    class Meta:
        model = cassette
        fields = ['name','manufacturer','serial','serialImg','inventImg','invent','power','voltage','current',
                    'accumulator1','accumulator2','accumulator3','accumulator4','accumulator5','accumulator6','accumulator7','accumulator8','accumulator9','accumulator10','score']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'power': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'voltage': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'current': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'accumulator1': WidgetCanAdd(accumulator, related_url="new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator2': WidgetCanAdd(accumulator, related_url="new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator3': WidgetCanAdd(accumulator, related_url="new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator4': WidgetCanAdd(accumulator, related_url="new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator5': WidgetCanAdd(accumulator, related_url="new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator6': WidgetCanAdd(accumulator, related_url="new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator7': WidgetCanAdd(accumulator, related_url="new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator8': WidgetCanAdd(accumulator, related_url="new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator9': WidgetCanAdd(accumulator, related_url="new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'accumulator10': WidgetCanAdd(accumulator, related_url="new-accumulator", attrs={'class': 'input-group form-select form-select-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        } 

class accumulatorForm(forms.ModelForm):   
    class Meta:
        model = accumulator
        fields = ['name','manufacturer','serial','serialImg','inventImg','invent','power','voltage','current','score']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'power': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'voltage': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'current': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        } 

class printerForm(forms.ModelForm):  
    class Meta:
        model = printer
        fields = ['name','modelPrinter','manufacturer','serial','serialImg','inventImg','invent','usbPort','lanPort',
        'tray1','tray2','tray3','traySide','workplace','cartridge','fotoval','toner','score'
            ]
        FORMAT = (
            ('A4', 'A4'),
            ('A3', 'A3'),
            ('A2', 'A2'),
            ('A1', 'A1'),
            ('A0', 'A0'),
            ('A5', 'A5'),
            ('Конверт', 'Конверт'),
            ('Отсутствует', 'Отсутствует'),
            )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'modelPrinter': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'form-select form-select-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'usbPort': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'lanPort': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'tray1': forms.Select(choices=FORMAT, attrs={'class': 'form-select form-select-lg'}),
            'tray2': forms.Select(choices=FORMAT, attrs={'class': 'form-select form-select-lg'}),
            'tray3': forms.Select(choices=FORMAT, attrs={'class': 'form-select form-select-lg'}),
            'traySide': forms.Select(choices=FORMAT, attrs={'class': 'form-select form-select-lg'}),
            'workplace': WidgetCanAdd(workplace, related_url="new-workplace", attrs={'class': 'form-select form-select-lg'}),
            'cartridge': WidgetCanAdd(cartridge, related_url="new-cartridge", attrs={'class': 'form-select form-select-lg'}),
            'fotoval': WidgetCanAdd(fotoval, related_url="new-fotoval", attrs={'class': 'form-select form-select-lg'}),
            'toner': WidgetCanAdd(toner, related_url="new-toner", attrs={'class': 'form-select form-select-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        } 

class cartridgeForm(forms.ModelForm):  
    class Meta:
        model = cartridge
        fields = ['name','manufacturer','buhCode','score' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'form-select form-select-lg'}),
            'buhCode': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        } 

class fotovalForm(forms.ModelForm):  
    class Meta:
        model = fotoval
        fields = ['name','manufacturer','mileage','buhCode','score' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'form-select form-select-lg'}),
            'mileage': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'buhCode': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        } 

class tonerForm(forms.ModelForm):  
    class Meta:
        model = toner
        fields = ['name','manufacturer','buhCode','score' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'form-select form-select-lg'}),
            'buhCode': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        } 

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
            'employeeRegister': WidgetCanAdd(employee, related_url="new-employee", attrs={'class': 'form-select form-select-lg'}),
            'employeeStorage': WidgetCanAdd(employee, related_url="new-employee", attrs={'class': 'form-select form-select-lg'}),
            'workstation': WidgetCanAdd(workstation, related_url="new-workstation", attrs={'class': 'form-select form-select-lg'}),
            'storage': WidgetCanAdd(storage, related_url="new-storage", attrs={'class': 'form-select form-select-lg'}),
            #'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        } 

class storageForm(forms.ModelForm):  
    class Meta:
        model = storage
        fields = ['name','modelStorage','manufacturer','serial','serialImg','inventImg','invent','plug','typeMemory','volumeMemory','employee']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'modelStorage': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'form-select form-select-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'plug': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'typeMemory': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'volumeMemory': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'employee': WidgetCanAdd(employee, related_url="new-employee", attrs={'class': 'form-select form-select-lg'}),
        } 