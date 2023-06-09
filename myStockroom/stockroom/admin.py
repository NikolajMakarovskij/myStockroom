from django.contrib import admin
from .models import Stock_cat, History
from catalog.utils import ExportAdmin

class HistoryAdmin(ExportAdmin, admin.ModelAdmin):
    model = History
    list_display = ['consumable','consumableId','device','categories','score','dateInstall', 'user']
    list_filter = ['categories']
    search_fields = ['consumable','categories','score','dateInstall']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(History, HistoryAdmin)

class Stock_catAdmin(ExportAdmin, admin.ModelAdmin):
    model = Stock_cat
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name", )}
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Stock_cat, Stock_catAdmin)
