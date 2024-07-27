from django.contrib import admin
from import_export.admin import ImportExportModelAdmin  # type: ignore[import-untyped]

from decommission.models import CategoryDec, CategoryDis, Decommission, Disposal


# Decommission
@admin.register(CategoryDec)
class CategoryDecAdmin(ImportExportModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name", )}


@admin.register(Decommission)
class DecommissionAdmin(ImportExportModelAdmin):
    list_display = ['stock_model', 'categories', 'date']
    list_filter = ['categories']
    search_fields = ['stock_model__name']


# Disposal
@admin.register(CategoryDis)
class CategoryDisAdmin(ImportExportModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name", )}


@admin.register(Disposal)
class DisposalAdmin(ImportExportModelAdmin):
    list_display = ['stock_model', 'categories', 'date']
    list_filter = ['categories']
    search_fields = ['stock_model__name']