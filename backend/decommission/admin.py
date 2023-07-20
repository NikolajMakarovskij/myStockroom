from django.contrib import admin
from decommission.models import CategoryDec, CategoryDis
from core.utils import ExportAdmin


# Decommission
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
