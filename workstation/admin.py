from django.contrib import admin
from .models import *
import csv
import datetime
from django.http import HttpResponse


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'экспорт CSV'

class WorkstationAdmin(admin.ModelAdmin):
    model = workstation
    list_display = ['name','manufacturer','modelComputer','workplace','employee', 'software', 'os']
    list_filter = ['workplace__room__floor', 'workplace__room__building','manufacturer', 'os']
    search_fields = ['name','manufacturer','modelComputer','serial','serialImg','inventImg','invent','motherboard',
            'monitor','cpu','gpu','ram','ssd','hdd','dcpower','keyBoard','mouse','ups','workplace','employee', 'software', 'os']
    actions = [export_to_csv]
    
admin.site.register(workstation ,WorkstationAdmin)

class MonitorAdmin(admin.ModelAdmin):
    model = monitor
    list_display = ['name','manufacturer','resolution','frequency','typeDisplay','hdmi','vga','dvi','displayPort']
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','resolution','frequency','typeDisplay',
        'dpi','usbPort','hdmi','vga','dvi','displayPort']
    actions = [export_to_csv]
    
admin.site.register(monitor, MonitorAdmin)

class MotherboardAdmin(admin.ModelAdmin):
    model = motherboard
    list_display = ['name','manufacturer','cpuSoket','ramSlot','pcie_x1','pcie_x16', 'vga','hdmi','dvi','dispayPort' ]
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','cpuSoket','ramSlot',
                    'usb_2','usb_3','usb_3_1','usb_3_2','usb_4_0','comPort','pcie_x1','pcie_x16', 
                    'pci','sata','m2','vga','hdmi','dvi','dispayPort','powerSupply','powerSupplyCPU' ]
    actions = [export_to_csv]
    
admin.site.register(motherboard, MotherboardAdmin)

class CpuAdmin(admin.ModelAdmin):
    model = cpu
    list_display = ['name','manufacturer','socket','frequency','core','thread','score' ]
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','socket','frequency',
                    'l1','l2','l3','core','thread','memory','memoryCapacity','channelsCapacity','tdp','supply','score']
    actions = [export_to_csv]
    
admin.site.register(cpu, CpuAdmin)

class GpuAdmin(admin.ModelAdmin):
    model = gpu
    list_display = ['name','manufacturer','type','gram','score']
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','type','serial','serialImg','inventImg','invent','gram','gramType','pcie','supply','score']
    actions = [export_to_csv]
    
admin.site.register(gpu, GpuAdmin)

class RamAdmin(admin.ModelAdmin):
    model = ram
    list_display = ['name','manufacturer','type','ramCapacity','rang','score']
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','type','serial','serialImg','inventImg','invent','ramCapacity','rang','score']
    actions = [export_to_csv]
    
admin.site.register(ram, RamAdmin )

class SsdAdmin(admin.ModelAdmin):
    model = ssd
    list_display = ['name','manufacturer','type','capacity','plug','score']
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','type','serial','serialImg','inventImg','invent','capacity','plug','speedRead','speadWrite','resourse','score']
    actions = [export_to_csv]
    
admin.site.register(ssd, SsdAdmin )

class HddAdmin(admin.ModelAdmin):
    model = hdd
    list_display = ['name','manufacturer','capacity','plug','score']
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','capacity','plug','speedRead','speadWrite','rpm','score']
    actions = [export_to_csv]
    
admin.site.register(hdd, HddAdmin )

class DcpowerAdmin(admin.ModelAdmin):
    model = dcpower
    list_display = ['name','manufacturer','serial','power','score']
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','power','motherboard','cpu','gpu','sata','molex','score']
    actions = [export_to_csv]
    
admin.site.register(dcpower, DcpowerAdmin )

class KeyBoardAdmin(admin.ModelAdmin):
    model = keyBoard
    list_display = ['name','manufacturer','score']
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','score']
    actions = [export_to_csv]
    
admin.site.register(keyBoard, KeyBoardAdmin )

class MouseAdmin(admin.ModelAdmin):
    model = mouse
    list_display = ['name','manufacturer','score']
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','score']
    actions = [export_to_csv]
    
admin.site.register(mouse, MouseAdmin )
