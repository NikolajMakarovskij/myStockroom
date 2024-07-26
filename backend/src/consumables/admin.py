from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import AccCat, Accessories, Categories, Consumables


@admin.register(Consumables)
class ConsumablesAdmin(ImportExportModelAdmin):
    list_display = ['name', 'categories', 'manufacturer', 'quantity', 'serial', 'invent', 'description', 'note']
    list_filter = ['categories']
    search_fields = ['name', 'categories__name', 'manufacturer__name', 'quantity', 'serial', 'invent', 'description',
                     'note']


@admin.register(Categories)
class CategoriesAdmin(ImportExportModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Accessories)
class AccessoriesAdmin(ImportExportModelAdmin):
    list_display = ['name', 'categories', 'manufacturer', 'quantity', 'serial', 'invent', 'description', 'note']
    list_filter = ['categories']
    search_fields = ['name', 'categories__name', 'manufacturer__name', 'quantity', 'serial', 'invent', 'description',
                     'note']


@admin.register(AccCat)
class AccCatAdmin(ImportExportModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}
