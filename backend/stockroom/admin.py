from django.contrib import admin

from core.utils import ExportAdmin
from stockroom.models.accessories import CategoryAcc, HistoryAcc, StockAcc
from stockroom.models.consumables import StockCat, History, Stockroom
from stockroom.models.devices import CategoryDev, HistoryDev, StockDev


# Consumables
class StockAdmin(ExportAdmin, admin.ModelAdmin):
    model = Stockroom
    list_display = ['stock_model']
    list_filter = ['categories']
    search_fields = ['stock_model__name']
    actions = [ExportAdmin.export_to_csv]


admin.site.register(Stockroom, StockAdmin)


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
        'categories__name',
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
class StockAccAdmin(ExportAdmin, admin.ModelAdmin):
    model = StockAcc
    list_display = ['stock_model']
    list_filter = ['categories']
    search_fields = ['stock_model__name']
    actions = [ExportAdmin.export_to_csv]


admin.site.register(StockAcc, StockAccAdmin)


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
        'categories__name',
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
class StockDevAdmin(ExportAdmin, admin.ModelAdmin):
    model = StockDev
    list_display = ['stock_model']
    list_filter = ['categories']
    search_fields = ['stock_model__name']
    actions = [ExportAdmin.export_to_csv]


admin.site.register(StockDev, StockDevAdmin)


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
        'stock_model_id',
        'categories__name',
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
