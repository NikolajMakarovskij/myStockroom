from django.contrib import admin
from import_export.admin import ImportExportModelAdmin  # type: ignore[import-untyped]

from .models import Os, Software


@admin.register(Software)
class SoftwareAdmin(ImportExportModelAdmin):
    """_SoftwareAdmin_
    Add model to admin panel
    """

    list_display = [
        "name",
        "manufacturer",
        "version",
        "bitDepth",
        "licenseKeyText",
        "licenseKeyImg",
        "licenseKeyFile",
    ]
    list_filter = [
        "manufacturer",
        "bitDepth",
    ]
    search_fields = [
        "name",
        "manufacturer",
        "version",
        "bitDepth",
        "licenseKeyText",
        "licenseKeyImg",
        "licenseKeyFile",
    ]


@admin.register(Os)
class OsAdmin(ImportExportModelAdmin):
    """_OsAdmin_
    Add model to admin panel
    """

    list_display = [
        "name",
        "manufacturer",
        "version",
        "bitDepth",
        "licenseKeyText",
        "licenseKeyImg",
        "licenseKeyFile",
    ]
    list_filter = [
        "manufacturer",
        "bitDepth",
    ]
    search_fields = [
        "name",
        "manufacturer",
        "version",
        "bitDepth",
        "licenseKeyText",
        "licenseKeyImg",
        "licenseKeyFile",
    ]
