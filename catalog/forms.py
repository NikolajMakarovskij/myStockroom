from django import forms
from .utils import WidgetCanAdd
from django.utils.translation import gettext_lazy as _
from .models.models import *
from .models.workstation_model import *
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
            'workstation': WidgetCanAdd(workstation, related_url="new-workstation", attrs={'class': 'input-group form-select form-select-lg'}),
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
            'cpu': WidgetCanAdd(cpu, related_url="new-cpu", attrs={'class': 'input-group form-select form-select-lg'}),
            'gpu': WidgetCanAdd(gpu, related_url="new-gpu", attrs={'class': 'input-group form-select form-select-lg'}),
            'ram': WidgetCanAdd(ram, related_url="new-ram", attrs={'class': 'input-group form-select form-select-lg'}),
            'ssd': WidgetCanAdd(ssd, related_url="new-ssd", attrs={'class': 'input-group form-select form-select-lg'}),
            'hdd':  WidgetCanAdd(hdd, related_url="new-hdd", attrs={'class': 'input-group form-select form-select-lg'}),
            'os': WidgetCanAdd(os, related_url="new-OS", attrs={'class': 'input-group form-select form-select-lg'}),
            'dcpower': WidgetCanAdd(dcpower, related_url="new-dcpower", attrs={'class': 'input-group form-select form-select-lg'}),
            'keyBoard': WidgetCanAdd(keyBoard, related_url="new-keyBoard", attrs={'class': 'input-group form-select form-select-lg'}),
            'mouse': WidgetCanAdd(mouse, related_url="new-mouse", attrs={'class': 'input-group form-select form-select-lg'}),
            'ups': WidgetCanAdd(ups, related_url="new-ups", attrs={'class': 'input-group form-select form-select-lg'}),
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

class cpuForm(forms.ModelForm):  
    class Meta:
        model = cpu
        fields = ['name','manufacturer','serial','serialImg','inventImg','invent','socket','frequency',
                    'l1','l2','l3','core','thread','memory','memoryCapacity','channelsCapacity','tdp','supply','score'
            ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'socket': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'frequency': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'l1': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'l2': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'l3': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'core': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'thread': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'memory': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'memoryCapacity': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'channelsCapacity': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'tdp': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'supply': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        } 

class gpuForm(forms.ModelForm):  
    class Meta:
        model = gpu
        fields = ['name','manufacturer','type','serial','serialImg','inventImg','invent','gram','gramType','pcie','supply','score']
        plug = (
            ('Интегрированная','Интегрированная'),
            ('Дискретная','Дискретная')
            )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
            'type': forms.Select(choices=plug, attrs={'class': 'form-select form-select-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'gram': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'gramType': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'pcie': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'supply': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        }

class ramForm(forms.ModelForm):  
    class Meta:
        model = ram
        fields = ['name','manufacturer','type','serial','serialImg','inventImg','invent','ramCapacity','rang','score']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
            'type': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'ramCapacity': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'rang': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        }    

class ssdForm(forms.ModelForm):  
    class Meta:
        model = ssd
        fields = ['name','manufacturer','type','serial','serialImg','inventImg','invent','capacity','plug','speedRead','speadWrite','resourse','score']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
            'type': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'capacity': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'plug': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'speedRead': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'speadWrite': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'resourse': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        }

class hddForm(forms.ModelForm):   
    class Meta:
        model = hdd
        fields = ['name','manufacturer','serial','serialImg','inventImg','invent','capacity','plug','speedRead','speadWrite','rpm','score']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'capacity': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'plug': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'speedRead': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'speadWrite': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'rpm': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        }

class dcpowerForm(forms.ModelForm):   
    class Meta:
        model = dcpower
        fields = ['name','manufacturer','serial','serialImg','inventImg','invent','power','motherboard','cpu','gpu','sata','molex','score']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'power': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'motherboard': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'cpu': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'gpu': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'sata': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'molex': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        }      

class keyBoardForm(forms.ModelForm):   
    class Meta:
        model = keyBoard
        fields = ['name','manufacturer','serial','serialImg','inventImg','invent','score']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        }   

class mouseForm(forms.ModelForm):   
    class Meta:
        model = mouse
        fields = ['name','manufacturer','serial','serialImg','inventImg','invent','score']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
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