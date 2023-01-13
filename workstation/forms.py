from django import forms
from catalog.utils import WidgetCanAdd
from django.utils.translation import gettext_lazy as _
from .models import *

class workstationForm(forms.ModelForm):  
    class Meta:
        model = workstation
        fields = ['name','manufacturer','modelComputer','serial','serialImg','inventImg','invent','motherboard',
            'monitor','cpu','gpu','ram','ssd','hdd','dcpower','keyBoard','mouse','ups','workplace','employee', 'software', 'os'
            ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="counterparty:new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
            'modelComputer': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'motherboard': WidgetCanAdd(motherboard, related_url="workstation:new-motherboard", attrs={'class': 'input-group form-select form-select-lg'}),
            'monitor': WidgetCanAdd(monitor, related_url="workstation:new-monitor", attrs={'class': 'input-group form-select form-select-lg'}),
            'cpu': WidgetCanAdd(cpu, related_url="workstation:new-cpu", attrs={'class': 'input-group form-select form-select-lg'}),
            'gpu': WidgetCanAdd(gpu, related_url="workstation:new-gpu", attrs={'class': 'input-group form-select form-select-lg'}),
            'ram': WidgetCanAdd(ram, related_url="workstation:new-ram", attrs={'class': 'input-group form-select form-select-lg'}),
            'ssd': WidgetCanAdd(ssd, related_url="workstation:new-ssd", attrs={'class': 'input-group form-select form-select-lg'}),
            'hdd':  WidgetCanAdd(hdd, related_url="workstation:new-hdd", attrs={'class': 'input-group form-select form-select-lg'}),
            'dcpower': WidgetCanAdd(dcpower, related_url="workstation:new-dcpower", attrs={'class': 'input-group form-select form-select-lg'}),
            'keyBoard': WidgetCanAdd(keyBoard, related_url="workstation:new-keyBoard", attrs={'class': 'input-group form-select form-select-lg'}),
            'mouse': WidgetCanAdd(mouse, related_url="workstation:new-mouse", attrs={'class': 'input-group form-select form-select-lg'}),
            'ups': WidgetCanAdd(ups, related_url="ups:new-ups", attrs={'class': 'input-group form-select form-select-lg'}),
            'workplace': WidgetCanAdd(workplace, related_url="workplace:new-workplace", attrs={'class': 'input-group form-select form-select-lg'}),
            'employee': WidgetCanAdd(employee, related_url="employee:new-employee", attrs={'class': 'input-group form-select form-select-lg'}),
            'software': WidgetCanAdd(software, related_url="software:new-software", attrs={'class': 'input-group form-select form-select-lg'}),
            'os': WidgetCanAdd(os, related_url="software:new-OS", attrs={'class': 'input-group form-select form-select-lg'}),
        } 
  
class monitorForm(forms.ModelForm):  
    class Meta:
        model = monitor
        fields = ['name','manufacturer','serial','serialImg','inventImg','invent','resolution','frequency','typeDisplay',
        'dpi','usbPort','hdmi','vga','dvi','displayPort',
            ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'manufacturer': WidgetCanAdd(manufacturer, related_url="counterparty:new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
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
            'manufacturer': WidgetCanAdd(manufacturer, related_url="counterparty:new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
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
            'manufacturer': WidgetCanAdd(manufacturer, related_url="counterparty:new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
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
            'manufacturer': WidgetCanAdd(manufacturer, related_url="counterparty:new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
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
            'manufacturer': WidgetCanAdd(manufacturer, related_url="counterparty:new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
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
            'manufacturer': WidgetCanAdd(manufacturer, related_url="counterparty:new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
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
            'manufacturer': WidgetCanAdd(manufacturer, related_url="counterparty:new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
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
            'manufacturer': WidgetCanAdd(manufacturer, related_url="counterparty:new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
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
            'manufacturer': WidgetCanAdd(manufacturer, related_url="counterparty:new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
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
            'manufacturer': WidgetCanAdd(manufacturer, related_url="counterparty:new-manufacturer", attrs={'class': 'input-group form-select form-select-lg'}),
            'serial': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'serialImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'invent': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'inventImg': forms.FileInput( attrs={'class': 'form-control form-control-lg'}),
            'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        } 
