from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Os, Software


@admin.register(Software)
class SoftwareAdmin(ImportExportModelAdmin):
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
