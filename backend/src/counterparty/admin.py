from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Manufacturer


@admin.register(Manufacturer)
class ManufacturerAdmin(ImportExportModelAdmin):
    list_display = ['name', 'country', 'production']
    list_filter = ['country', 'production']
    search_fields = ['name', 'country', 'production']
