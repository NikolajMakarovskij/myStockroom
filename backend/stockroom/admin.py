from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from core.utils import ExportAdmin
from stockroom.models.accessories import CategoryAcc, HistoryAcc, StockAcc
from stockroom.models.consumables import StockCat, History, Stockroom
from stockroom.models.devices import CategoryDev, HistoryDev, StockDev


# Consumables

@admin.register(Stockroom)
class StockAdmin(ImportExportModelAdmin):
    list_display = ['stock_model', 'dateAddToStock', 'dateInstall', 'rack', 'shelf']
    list_filter = ['categories']
    search_fields = ['stock_model__name', 'stock_model__device__name', 'dateAddToStock', 'dateInstall', 'rack', 'shelf']


@admin.register(History)
class HistoryAdmin(ImportExportModelAdmin):
    list_display = ['stock_model', 'stock_model_id', 'device', 'categories', 'quantity', 'dateInstall', 'user']
    list_filter = ['categories']
    search_fields = ['stock_model', 'categories__name', 'quantity', 'dateInstall', ]


@admin.register(StockCat)
class StockCatAdmin(ImportExportModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}


# Accessories
@admin.register(StockAcc)
class StockAccAdmin(ImportExportModelAdmin):
    list_display = ['stock_model', 'dateAddToStock', 'dateInstall', 'rack', 'shelf']
    list_filter = ['categories']
    search_fields = ['stock_model__name', 'stock_model__device__name', 'dateAddToStock', 'dateInstall', 'rack', 'shelf']


@admin.register(HistoryAcc)
class HistoryAccAdmin(ImportExportModelAdmin):
    list_display = ['stock_model', 'stock_model_id', 'device', 'categories', 'quantity', 'dateInstall', 'user']
    list_filter = ['categories']
    search_fields = ['stock_model', 'categories__name', 'quantity', 'dateInstall']


@admin.register(CategoryAcc)
class CategoryAccAdmin(ImportExportModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}


# Devices
@admin.register(StockDev)
class StockDevAdmin(ImportExportModelAdmin):
    list_display = ['stock_model', 'dateAddToStock', 'dateInstall', 'rack', 'shelf']
    list_filter = ['categories']
    search_fields = ['stock_model__name', 'stock_model__invent', 'categories__name']


@admin.register(HistoryDev)
class HistoryDevAdmin(ImportExportModelAdmin):
    list_display = ['stock_model', 'stock_model_id', 'categories', 'quantity', 'dateInstall', 'user']
    list_filter = ['categories']
    search_fields = ['stock_model', 'stock_model_id', 'categories__name', 'quantity', 'dateInstall']


@admin.register(CategoryDev)
class CategoryDevAdmin(ImportExportModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}
