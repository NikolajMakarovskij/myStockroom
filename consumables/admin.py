from django.contrib import admin
from .models import Consumables, Categories
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

