from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Device, DeviceCat
from .resources import DeviceResource


@admin.register(Device)
class DeviceAdmin(ImportExportModelAdmin):
    resource_classes = [DeviceResource]
    list_display = ['name', 'description', 'categories', 'manufacturer',
              'workplace', 'quantity', 'note']
    list_filter = ['categories']
    search_fields = ['name', 'description', 'manufacturer__name', 'serial', 'invent',
                     'workplace__name', 'consumable__name', 'accessories__name', 'quantity', 'note']


@admin.register(DeviceCat)
class DeviceCatAdmin(ImportExportModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}
