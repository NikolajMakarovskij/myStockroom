from django.contrib import admin

from core.utils import ExportAdmin
from .models import Consumables, Categories, AccCat, Accessories


class ConsumablesAdmin(ExportAdmin, admin.ModelAdmin):
    model = Consumables
    list_display = ['name', 'categories', 'manufacturer', 'quantity', 'serial', 'invent', 'description', 'note']
    list_filter = ['categories']
    search_fields = ['name', 'categories__name', 'manufacturer__name', 'quantity', 'serial', 'invent', 'description',
                     'note']
    actions = [ExportAdmin.export_to_csv]


admin.site.register(Consumables, ConsumablesAdmin)


class CategoriesAdmin(ExportAdmin, admin.ModelAdmin):
    model = Categories
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}
    actions = [ExportAdmin.export_to_csv]


admin.site.register(Categories, CategoriesAdmin)


class AccessoriesAdmin(ExportAdmin, admin.ModelAdmin):
    model = Accessories
    list_display = ['name', 'categories', 'manufacturer', 'quantity', 'serial', 'invent', 'description', 'note']
    list_filter = ['categories']
    search_fields = ['name', 'categories__name', 'manufacturer__name', 'quantity', 'serial', 'invent', 'description',
                     'note']
    actions = [ExportAdmin.export_to_csv]


admin.site.register(Accessories, AccessoriesAdmin)


class AccCatAdmin(ExportAdmin, admin.ModelAdmin):
    model = AccCat
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}
    actions = [ExportAdmin.export_to_csv]


admin.site.register(AccCat, AccCatAdmin)
