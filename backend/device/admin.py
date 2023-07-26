from django.contrib import admin
from .models import Device, DeviceCat
from core.utils import ExportAdmin


class DeviceAdmin(ExportAdmin, admin.ModelAdmin):
    model = Device
    list_display = ['name', 'description', 'categories', 'manufacturer',
                    'workplace', 'consumable', 'accessories', 'quantity', 'note']
    list_filter = ['manufacturer', 'workplace__room__floor', 'workplace__room__building']
    search_fields = ['name', 'description', 'manufacturer', 'serial', 'invent',
                     'workplace', 'consumable', 'accessories', 'quantity', 'note']
    actions = [ExportAdmin.export_to_csv]


admin.site.register(Device, DeviceAdmin)


class DeviceCatAdmin(ExportAdmin, admin.ModelAdmin):
    model = DeviceCat
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}
    actions = [ExportAdmin.export_to_csv]


admin.site.register(DeviceCat, DeviceCatAdmin)
