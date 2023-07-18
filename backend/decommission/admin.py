from django.contrib import admin
from decommission.models import CategoryDec, HistoryDec, Disposal, CategoryDis, HistoryDis
from core.utils import ExportAdmin


# Decommission
class HistoryDecAdmin(ExportAdmin, admin.ModelAdmin):
    model = HistoryDec
    list_display = [
        'devices',
        'devicesId',
        'categories',
        'date',
        'user'
        ]
    list_filter = ['categories']
    search_fields = [
        'devices',
        'categories',
        'date'
        ]
    actions = [ExportAdmin.export_to_csv]


admin.site.register(HistoryDec, HistoryDecAdmin)


class CategoryDecAdmin(ExportAdmin, admin.ModelAdmin):
    model = CategoryDec
    list_display = [
        'name',
        'slug'
        ]
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name", )}
    actions = [ExportAdmin.export_to_csv]


admin.site.register(CategoryDec, CategoryDecAdmin)


# Disposal
class HistoryDisAdmin(ExportAdmin, admin.ModelAdmin):
    model = HistoryDis
    list_display = [
        'devices',
        'devicesId',
        'categories',
        'date',
        'user'
        ]
    list_filter = ['categories']
    search_fields = [
        'devices',
        'categories',
        'date'
        ]
    actions = [ExportAdmin.export_to_csv]


admin.site.register(HistoryDis, HistoryDisAdmin)


class CategoryDisAdmin(ExportAdmin, admin.ModelAdmin):
    model = CategoryDis
    list_display = [
        'name',
        'slug'
        ]
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name", )}
    actions = [ExportAdmin.export_to_csv]


admin.site.register(CategoryDis, CategoryDisAdmin)
