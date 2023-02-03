from django.contrib import admin
from .models import Cartridge, Fotoval, Toner, Accumulator, Storage, Consumables, Categories
from catalog.utils import ExportAdmin

class ConsumablesAdmin(ExportAdmin, admin.ModelAdmin):
    model = Consumables
    list_display = ['name','categories','manufacturer','buhCode','score','serial','invent', 'description', 'note']
    list_filter = ['categories']
    search_fields = ['name','categories','manufacturer','buhCode','score', 'serial', 'invent', 'description', 'note']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Consumables, ConsumablesAdmin)

class CategoriesAdmin(ExportAdmin, admin.ModelAdmin):
    model = Categories
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name", )}
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Categories, CategoriesAdmin)

class CartridgeAdmin(ExportAdmin, admin.ModelAdmin):
    model = Cartridge
    list_display = ['name','manufacturer','buhCode','score', 'rack', 'shelf' ]
    list_filter = ['manufacturer', 'rack', 'shelf']
    search_fields = ['name','manufacturer','buhCode','score','rack', 'shelf' ]
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Cartridge, CartridgeAdmin)

class TonerAdmin(ExportAdmin, admin.ModelAdmin):
    model = Toner
    list_display = ['name','manufacturer','buhCode','score','rack', 'shelf' ]
    list_filter = ['manufacturer', 'rack', 'shelf']
    search_fields = ['name','manufacturer','buhCode','score','rack', 'shelf' ]
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Toner, TonerAdmin)

class FotovalAdmin(ExportAdmin, admin.ModelAdmin):
    model = Fotoval
    list_display = ['name','manufacturer','mileage','buhCode','score','rack', 'shelf']
    list_filter = ['manufacturer', 'rack', 'shelf']
    search_fields = ['name','manufacturer','mileage','buhCode','score','rack', 'shelf']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Fotoval, FotovalAdmin)

class AccumulatorAdmin(ExportAdmin, admin.ModelAdmin):
    model = Accumulator
    list_display = ['name','manufacturer','power','voltage','current','score','rack', 'shelf' ]
    list_filter = ['manufacturer', 'rack', 'shelf']
    search_fields = ['name','manufacturer','power','voltage','current','score','rack', 'shelf']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Accumulator, AccumulatorAdmin)

class StorageAdmin(ExportAdmin, admin.ModelAdmin):
    model = Storage
    list_display = ['name','modelStorage','manufacturer','plug','typeMemory','volumeMemory','employee' ]
    list_filter = ['manufacturer', ]
    search_fields = ['name','modelStorage','manufacturer','serial','serialImg','inventImg','invent','plug','typeMemory','volumeMemory','employee']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Storage, StorageAdmin)


