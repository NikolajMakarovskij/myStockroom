from django.contrib import admin
from .models import printer
from catalog.utils import ExportAdmin

class PrinterAdmin(ExportAdmin, admin.ModelAdmin):
    model = printer
    list_display = ['name','modelPrinter','manufacturer','workplace','cartridge','fotoval','toner','score']
    list_filter = ['manufacturer', 'workplace__room__floor', 'workplace__room__building' ]
    search_fields = ['name','modelPrinter','manufacturer','serial','serialImg','inventImg','invent','usbPort','lanPort',
        'tray1','tray2','tray3','traySide','workplace','cartridge','fotoval','toner','score' ]
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(printer, PrinterAdmin)
