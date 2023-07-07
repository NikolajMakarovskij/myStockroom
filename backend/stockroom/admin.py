from django.contrib import admin
from .models import (
    StockCat, History, HistoryAcc, CategoryAcc, HistoryDev, CategoryDev
    )
from catalog.utils import ExportAdmin


# Расходники
class HistoryAdmin(ExportAdmin, admin.ModelAdmin):
    model = History
    list_display = [
        'consumable',
        'consumableId',
        'device',
        'categories',
        'score',
        'dateInstall',
        'user'
        ]
    list_filter = ['categories']
    search_fields = [
        'consumable',
        'categories',
        'score',
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


# Комплектующие
class HistoryAccAdmin(ExportAdmin, admin.ModelAdmin):
    model = HistoryAcc
    list_display = [
        'accessories',
        'accessoriesId',
        'device',
        'categories',
        'score',
        'dateInstall',
        'user'
        ]
    list_filter = ['categories']
    search_fields = [
        'accessories',
        'categories',
        'score',
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


# Устройства
class HistoryDevAdmin(ExportAdmin, admin.ModelAdmin):
    model = HistoryDev
    list_display = [
        'devices',
        'devicesId',
        'categories',
        'score',
        'dateInstall',
        'user'
        ]
    list_filter = ['categories']
    search_fields = [
        'devices',
        'categories',
        'score',
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
