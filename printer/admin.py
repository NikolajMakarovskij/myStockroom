from django.contrib import admin
from .models import Printer, Printer_cat
from catalog.utils import ExportAdmin

class PrinterAdmin(ExportAdmin, admin.ModelAdmin):
    model = Printer
    list_display = ['name','categories','manufacturer','workplace','consumable','score','note']
    list_filter = ['manufacturer', 'workplace__room__floor', 'workplace__room__building' ]
    search_fields = ['name','modelPrinter','manufacturer','serial','serialImg','inventImg','invent','usbPort','lanPort',
        'tray1','tray2','tray3','traySide','workplace','consumable','score','note']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Printer, PrinterAdmin)

class Printer_catAdmin(ExportAdmin, admin.ModelAdmin):
    model = Printer_cat
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name", )}
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Printer_cat, Printer_catAdmin)