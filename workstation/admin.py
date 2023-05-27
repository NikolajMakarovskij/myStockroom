from django.contrib import admin
from .models import *
from catalog.utils import ExportAdmin

class WorkstationAdmin(ExportAdmin, admin.ModelAdmin):
    model = Workstation
    list_display = ['name','manufacturer','categories','workplace','employee', 'software', 'os']
    list_filter = ['workplace__room__floor', 'workplace__room__building','manufacturer', 'os']
    search_fields = ['name','manufacturer','modelComputer','serial','serialImg','inventImg','invent','motherboard',
            'monitor','cpu','gpu','ram','ssd','hdd','dcpower','keyBoard','mouse','ups','workplace','employee', 'software', 'os']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Workstation ,WorkstationAdmin)

class Workstation_catAdmin(ExportAdmin, admin.ModelAdmin):
    model = Workstation_cat
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name", )}
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Workstation_cat, Workstation_catAdmin)

class MonitorAdmin(ExportAdmin, admin.ModelAdmin):
    model = Monitor
    list_display = ['name','manufacturer','resolution','frequency','typeDisplay','hdmi','vga','dvi','displayPort']
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','resolution','frequency','typeDisplay',
        'dpi','usbPort','hdmi','vga','dvi','displayPort']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Monitor, MonitorAdmin)


class RamAdmin(ExportAdmin, admin.ModelAdmin):
    model = Ram
    list_display = ['name','manufacturer','type','ramCapacity','rang','score']
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','type','serial','serialImg','inventImg','invent','ramCapacity','rang','score']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Ram, RamAdmin )

class SsdAdmin(ExportAdmin, admin.ModelAdmin):
    model = Ssd
    list_display = ['name','manufacturer','type','capacity','plug','score']
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','type','serial','serialImg','inventImg','invent','capacity','plug','speedRead','speadWrite','resourse','score']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Ssd, SsdAdmin )

class HddAdmin(ExportAdmin, admin.ModelAdmin):
    model = Hdd
    list_display = ['name','manufacturer','capacity','plug','score']
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','capacity','plug','speedRead','speadWrite','rpm','score']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Hdd, HddAdmin )

class KeyBoardAdmin(ExportAdmin, admin.ModelAdmin):
    model = KeyBoard
    list_display = ['name','manufacturer','score']
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','score']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(KeyBoard, KeyBoardAdmin )

class MouseAdmin(ExportAdmin, admin.ModelAdmin):
    model = Mouse
    list_display = ['name','manufacturer','score']
    list_filter = ['manufacturer']
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','score']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Mouse, MouseAdmin )
