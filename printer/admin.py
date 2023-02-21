from django.contrib import admin
from .models import Printer, Categories
from catalog.utils import ExportAdmin

class PrinterAdmin(ExportAdmin, admin.ModelAdmin):
    model = Printer
    list_display = ['name','categories','manufacturer','workplace','cartridge','fotoval','toner','fotodrumm','score','note']
    list_filter = ['manufacturer', 'workplace__room__floor', 'workplace__room__building' ]
    search_fields = ['name','modelPrinter','manufacturer','serial','serialImg','inventImg','invent','usbPort','lanPort',
        'tray1','tray2','tray3','traySide','workplace','cartridge','fotoval','toner','fotodrumm','score','note']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Printer, PrinterAdmin)

class CategoriesAdmin(ExportAdmin, admin.ModelAdmin):
    model = Categories
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name", )}
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Categories, CategoriesAdmin)