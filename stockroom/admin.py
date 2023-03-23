from django.contrib import admin
from .models import Categories, History
from catalog.utils import ExportAdmin

class HistoryAdmin(ExportAdmin, admin.ModelAdmin):
    model = History
    list_display = ['consumable','consumableId','categories','score','dateInstall', 'user']
    list_filter = ['categories']
    search_fields = ['consumable','categories','score','dateInstall']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(History, HistoryAdmin)

class CategoriesAdmin(ExportAdmin, admin.ModelAdmin):
    model = Categories
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name", )}
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Categories, CategoriesAdmin)
