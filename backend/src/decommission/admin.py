from django.contrib import admin
from import_export.admin import ImportExportModelAdmin  # type: ignore[import-untyped]

from decommission.models import CategoryDec, CategoryDis, Decommission, Disposal


# Decommission
@admin.register(CategoryDec)
class CategoryDecAdmin(ImportExportModelAdmin):
    """_CategoryDecAdmin_
    Add categories model to admin panel
    """

    list_display = ["name", "slug"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Decommission)
class DecommissionAdmin(ImportExportModelAdmin):
    """_DecommissionAdmin_
    Add model to admin panel
    """

    list_display = ["stock_model", "categories", "date"]
    list_filter = ["categories"]
    search_fields = ["stock_model__name"]


# Disposal
@admin.register(CategoryDis)
class CategoryDisAdmin(ImportExportModelAdmin):
    """_CategoryDisAdmin_
    Add categories model to admin panel
    """

    list_display = ["name", "slug"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Disposal)
class DisposalAdmin(ImportExportModelAdmin):
    """_DisposalAdmin_
    Add model to admin panel
    """

    list_display = ["stock_model", "categories", "date"]
    list_filter = ["categories"]
    search_fields = ["stock_model__name"]
