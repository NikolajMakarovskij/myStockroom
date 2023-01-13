from django.contrib import admin
from .models import *
from catalog.utils import ExportAdmin

class WorkstationAdmin(ExportAdmin, admin.ModelAdmin):
    model = workstation
    list_display = ['name','manufacturer','modelComputer','workplace','employee', 'software', 'os']
    list_filter = ['workplace__room__floor', 'workplace__room__building','manufacturer', 'os']
    search_fields = ['name','manufacturer','modelComputer','serial','serialImg','inventImg','invent','motherboard',
            'monitor','cpu','gpu','ram','ssd','hdd','dcpower','keyBoard','mouse','ups','workplace','employee', 'software', 'os']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(workstation ,WorkstationAdmin)

class MonitorAdmin(ExportAdmin, admin.ModelAdmin):
    model = monitor
    list_display = ['name','manufacturer','resolution','frequency','typeDisplay','hdmi','vga','dvi','displayPort']
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','resolution','frequency','typeDisplay',
        'dpi','usbPort','hdmi','vga','dvi','displayPort']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(monitor, MonitorAdmin)

class MotherboardAdmin(ExportAdmin, admin.ModelAdmin):
    model = motherboard
    list_display = ['name','manufacturer','cpuSoket','ramSlot','pcie_x1','pcie_x16', 'vga','hdmi','dvi','dispayPort' ]
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','cpuSoket','ramSlot',
                    'usb_2','usb_3','usb_3_1','usb_3_2','usb_4_0','comPort','pcie_x1','pcie_x16', 
                    'pci','sata','m2','vga','hdmi','dvi','dispayPort','powerSupply','powerSupplyCPU' ]
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(motherboard, MotherboardAdmin)

class CpuAdmin(ExportAdmin, admin.ModelAdmin):
    model = cpu
    list_display = ['name','manufacturer','socket','frequency','core','thread','score' ]
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','socket','frequency',
                    'l1','l2','l3','core','thread','memory','memoryCapacity','channelsCapacity','tdp','supply','score']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(cpu, CpuAdmin)

class GpuAdmin(ExportAdmin, admin.ModelAdmin):
    model = gpu
    list_display = ['name','manufacturer','type','gram','score']
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','type','serial','serialImg','inventImg','invent','gram','gramType','pcie','supply','score']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(gpu, GpuAdmin)

class RamAdmin(ExportAdmin, admin.ModelAdmin):
    model = ram
    list_display = ['name','manufacturer','type','ramCapacity','rang','score']
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','type','serial','serialImg','inventImg','invent','ramCapacity','rang','score']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(ram, RamAdmin )

class SsdAdmin(ExportAdmin, admin.ModelAdmin):
    model = ssd
    list_display = ['name','manufacturer','type','capacity','plug','score']
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','type','serial','serialImg','inventImg','invent','capacity','plug','speedRead','speadWrite','resourse','score']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(ssd, SsdAdmin )

class HddAdmin(ExportAdmin, admin.ModelAdmin):
    model = hdd
    list_display = ['name','manufacturer','capacity','plug','score']
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','capacity','plug','speedRead','speadWrite','rpm','score']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(hdd, HddAdmin )

class DcpowerAdmin(ExportAdmin, admin.ModelAdmin):
    model = dcpower
    list_display = ['name','manufacturer','serial','power','score']
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','power','motherboard','cpu','gpu','sata','molex','score']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(dcpower, DcpowerAdmin )

class KeyBoardAdmin(ExportAdmin, admin.ModelAdmin):
    model = keyBoard
    list_display = ['name','manufacturer','score']
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','score']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(keyBoard, KeyBoardAdmin )

class MouseAdmin(ExportAdmin, admin.ModelAdmin):
    model = mouse
    list_display = ['name','manufacturer','score']
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','score']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(mouse, MouseAdmin )
