from django.contrib import admin
from .models import cartridge, fotoval, toner, accumulator, storage
from catalog.utils import ExportAdmin

class CartridgeAdmin(ExportAdmin, admin.ModelAdmin):
    model = cartridge
    list_display = ['name','manufacturer','buhCode','score' ]
    list_filter = ['manufacturer', ]
    search_fields = ['name','manufacturer','buhCode','score' ]
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(cartridge, CartridgeAdmin)

class TonerAdmin(ExportAdmin, admin.ModelAdmin):
    model = toner
    list_display = ['name','manufacturer','buhCode','score' ]
    list_filter = ['manufacturer', ]
    search_fields = ['name','manufacturer','buhCode','score' ]
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(toner, TonerAdmin)

class FotovalAdmin(ExportAdmin, admin.ModelAdmin):
    model = fotoval
    list_display = ['name','manufacturer','mileage','buhCode','score']
    list_filter = ['manufacturer', ]
    search_fields = ['name','manufacturer','mileage','buhCode','score']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(fotoval, FotovalAdmin)

class AccumulatorAdmin(ExportAdmin, admin.ModelAdmin):
    model = accumulator
    list_display = ['name','manufacturer','power','voltage','current','score' ]
    list_filter = ['manufacturer', ]
    search_fields = ['name','manufacturer','power','voltage','current','score']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(accumulator, AccumulatorAdmin)

class StorageAdmin(ExportAdmin, admin.ModelAdmin):
    model = storage
    list_display = ['name','modelStorage','manufacturer','plug','typeMemory','volumeMemory','employee' ]
    list_filter = ['manufacturer', ]
    search_fields = ['name','modelStorage','manufacturer','serial','serialImg','inventImg','invent','plug','typeMemory','volumeMemory','employee']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(storage, StorageAdmin)


