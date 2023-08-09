from django.contrib import admin
from .models import Accounting, Categories
from core.utils import ExportAdmin


class AccountingAdmin(ExportAdmin, admin.ModelAdmin):
    model = Accounting
    list_display = ['name', 'categories', 'account', 'consumable', 'accessories',
                    'code', 'quantity', 'cost', 'note']
    list_filter = ['categories']
    search_fields = ['name', 'categories', 'account', 'consumable', 'accessories',
                     'code', 'quantity', 'cost', 'note']
    actions = [ExportAdmin.export_to_csv]


admin.site.register(Accounting, AccountingAdmin)


class CategoriesAdmin(ExportAdmin, admin.ModelAdmin):
    model = Categories
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}
    actions = [ExportAdmin.export_to_csv]


admin.site.register(Categories, CategoriesAdmin)
