from django.contrib import admin
from import_export.admin import ImportExportModelAdmin  # type: ignore[import-untyped]

from .models import Accounting, Categories


@admin.register(Accounting)
class AccountingAdmin(ImportExportModelAdmin):
    """_AccountingAdmin_ Add model to admin panel"""

    list_display = [
        "name",
        "categories",
        "account",
        "consumable",
        "accessories",
        "code",
        "quantity",
        "cost",
        "note",
    ]
    list_filter = ["categories"]
    search_fields = [
        "name",
        "categories",
        "account",
        "consumable",
        "accessories",
        "code",
        "quantity",
        "cost",
        "note",
    ]


@admin.register(Categories)
class CategoriesAdmin(ImportExportModelAdmin):
    """_CategoriesAdmin_ Add model to admin panel"""

    list_display = ["name", "slug"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}
