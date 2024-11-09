from django.contrib import admin
from import_export.admin import ImportExportModelAdmin  # type: ignore[import-untyped]

from .models import Manufacturer


@admin.register(Manufacturer)
class ManufacturerAdmin(ImportExportModelAdmin):
    """_ManufacturerAdmin_ Add model to admin panel"""

    list_display = ["name", "country", "production"]
    list_filter = ["country", "production"]
    search_fields = ["name", "country", "production"]
