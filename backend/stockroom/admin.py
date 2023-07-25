from django.contrib import admin
from .models import (
    StockCat, History, HistoryAcc, CategoryAcc, HistoryDev, CategoryDev
    )
from core.utils import ExportAdmin


# Consumables
class HistoryAdmin(ExportAdmin, admin.ModelAdmin):
    model = History
    list_display = [
        'stock_model',
        'stock_model_id',
        'device',
        'categories',
        'quantity',
        'dateInstall',
        'user'
        ]
    list_filter = ['categories']
    search_fields = [
        'stock_model',
        'categories',
        'quantity',
        'dateInstall',
        'room'
        ]
    actions = [ExportAdmin.export_to_csv]


admin.site.register(History, HistoryAdmin)


class StockCatAdmin(ExportAdmin, admin.ModelAdmin):
    model = StockCat
    list_display = [
        'name',
        'slug'
        ]
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name", )}
    actions = [ExportAdmin.export_to_csv]


admin.site.register(StockCat, StockCatAdmin)


# Accessories
class HistoryAccAdmin(ExportAdmin, admin.ModelAdmin):
    model = HistoryAcc
    list_display = [
        'stock_model',
        'stock_model_id',
        'device',
        'categories',
        'quantity',
        'dateInstall',
        'user'
        ]
    list_filter = ['categories']
    search_fields = [
        'stock_model',
        'categories',
        'quantity',
        'dateInstall'
        ]
    actions = [ExportAdmin.export_to_csv]


admin.site.register(HistoryAcc, HistoryAccAdmin)


class CategoryAccAdmin(ExportAdmin, admin.ModelAdmin):
    model = CategoryAcc
    list_display = [
        'name',
        'slug'
        ]
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name", )}
    actions = [ExportAdmin.export_to_csv]


admin.site.register(CategoryAcc, CategoryAccAdmin)


# Devices
class HistoryDevAdmin(ExportAdmin, admin.ModelAdmin):
    model = HistoryDev
    list_display = [
        'stock_model',
        'stock_model_id',
        'categories',
        'quantity',
        'dateInstall',
        'user'
        ]
    list_filter = ['categories']
    search_fields = [
        'stock_model',
        'categories',
        'quantity',
        'dateInstall'
        ]
    actions = [ExportAdmin.export_to_csv]


admin.site.register(HistoryDev, HistoryDevAdmin)


class CategoryDevAdmin(ExportAdmin, admin.ModelAdmin):
    model = CategoryDev
    list_display = [
        'name',
        'slug'
        ]
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name", )}
    actions = [ExportAdmin.export_to_csv]


admin.site.register(CategoryDev, CategoryDevAdmin)
