from django.contrib import admin
from .models import Cartridge, Fotoval, Toner, Accumulator, Storage
from catalog.utils import ExportAdmin

class CartridgeAdmin(ExportAdmin, admin.ModelAdmin):
    model = Cartridge
    list_display = ['name','manufacturer','buhCode','score' ]
    list_filter = ['manufacturer', ]
    search_fields = ['name','manufacturer','buhCode','score' ]
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Cartridge, CartridgeAdmin)

class TonerAdmin(ExportAdmin, admin.ModelAdmin):
    model = Toner
    list_display = ['name','manufacturer','buhCode','score' ]
    list_filter = ['manufacturer', ]
    search_fields = ['name','manufacturer','buhCode','score' ]
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Toner, TonerAdmin)

class FotovalAdmin(ExportAdmin, admin.ModelAdmin):
    model = Fotoval
    list_display = ['name','manufacturer','mileage','buhCode','score']
    list_filter = ['manufacturer', ]
    search_fields = ['name','manufacturer','mileage','buhCode','score']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Fotoval, FotovalAdmin)

class AccumulatorAdmin(ExportAdmin, admin.ModelAdmin):
    model = Accumulator
    list_display = ['name','manufacturer','power','voltage','current','score' ]
    list_filter = ['manufacturer', ]
    search_fields = ['name','manufacturer','power','voltage','current','score']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Accumulator, AccumulatorAdmin)

class StorageAdmin(ExportAdmin, admin.ModelAdmin):
    model = Storage
    list_display = ['name','modelStorage','manufacturer','plug','typeMemory','volumeMemory','employee' ]
    list_filter = ['manufacturer', ]
    search_fields = ['name','modelStorage','manufacturer','serial','serialImg','inventImg','invent','plug','typeMemory','volumeMemory','employee']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Storage, StorageAdmin)


