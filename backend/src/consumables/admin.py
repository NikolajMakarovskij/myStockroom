from django.contrib import admin
from import_export.admin import ImportExportModelAdmin  # type: ignore[import-untyped]

from .models import AccCat, Accessories, Categories, Consumables


@admin.register(Consumables)
class ConsumablesAdmin(ImportExportModelAdmin):
    """_ConsumablesAdmin_
    Add model to admin panel
    """

    list_display = [
        "name",
        "categories",
        "manufacturer",
        "quantity",
        "serial",
        "invent",
        "description",
        "note",
    ]
    list_filter = ["categories"]
    search_fields = [
        "name",
        "categories__name",
        "manufacturer__name",
        "quantity",
        "serial",
        "invent",
        "description",
        "note",
    ]


@admin.register(Categories)
class CategoriesAdmin(ImportExportModelAdmin):
    """_CategoriesAdmin_
    Add categories model to admin panel
    """

    list_display = ["name", "slug"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Accessories)
class AccessoriesAdmin(ImportExportModelAdmin):
    """_AccessoriesAdmin_
    Add model to admin panel
    """

    list_display = [
        "name",
        "categories",
        "manufacturer",
        "quantity",
        "serial",
        "invent",
        "description",
        "note",
    ]
    list_filter = ["categories"]
    search_fields = [
        "name",
        "categories__name",
        "manufacturer__name",
        "quantity",
        "serial",
        "invent",
        "description",
        "note",
    ]


@admin.register(AccCat)
class AccCatAdmin(ImportExportModelAdmin):
    """_AccCatAdmin_
    Add categories model to admin panel
    """

    list_display = ["name", "slug"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}
