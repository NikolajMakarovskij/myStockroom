from django.contrib import admin
from .models import Stock_cat, History, HistoryAcc, CategoryAcc, HistoryDev, CategoryDev
from catalog.utils import ExportAdmin


#Расходники
class HistoryAdmin(ExportAdmin, admin.ModelAdmin):
    model = History
    list_display = ['consumable','consumableId','device','categories','score','dateInstall', 'user']
    list_filter = ['categories']
    search_fields = ['consumable','categories','score','dateInstall','room']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(History, HistoryAdmin)

class Stock_catAdmin(ExportAdmin, admin.ModelAdmin):
    model = Stock_cat
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name", )}
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Stock_cat, Stock_catAdmin)


#Комплектующие
class HistoryAccAdmin(ExportAdmin, admin.ModelAdmin):
    model = HistoryAcc
    list_display = ['accessories','accessoriesId','device','categories','score','dateInstall', 'user']
    list_filter = ['categories']
    search_fields = ['accessories','categories','score','dateInstall']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(HistoryAcc, HistoryAccAdmin)

class CategoryAccAdmin(ExportAdmin, admin.ModelAdmin):
    model = CategoryAcc
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name", )}
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(CategoryAcc, CategoryAccAdmin)

#Устройства
class HistoryDevAdmin(ExportAdmin, admin.ModelAdmin):
    model = HistoryDev
    list_display = ['devicies','deviciesId','categories','score','dateInstall', 'user']
    list_filter = ['categories']
    search_fields = ['devicies','categories','score','dateInstall']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(HistoryDev, HistoryDevAdmin)

class CategoryDevAdmin(ExportAdmin, admin.ModelAdmin):
    model = CategoryDev
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name", )}
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(CategoryDev, CategoryDevAdmin)