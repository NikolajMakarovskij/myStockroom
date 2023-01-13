from django.contrib import admin
from .models import software, os
from catalog.utils import ExportAdmin

class SoftwareAdmin(ExportAdmin, admin.ModelAdmin):
    model = software
    list_display = ['name', 'manufacturer', 'version', 'bitDepth', 'licenseKeyText', 'licenseKeyImg', 'licenseKeyFile',]
    list_filter = ['manufacturer', 'bitDepth', ]
    search_fields = ['name', 'manufacturer', 'version', 'bitDepth', 'licenseKeyText', 'licenseKeyImg', 'licenseKeyFile', ]
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(software, SoftwareAdmin)

class OsAdmin(ExportAdmin, admin.ModelAdmin):
    model = os
    list_display = ['name', 'manufacturer', 'version', 'bitDepth', 'licenseKeyText', 'licenseKeyImg', 'licenseKeyFile',]
    list_filter = ['manufacturer', 'bitDepth', ]
    search_fields = ['name', 'manufacturer', 'version', 'bitDepth', 'licenseKeyText', 'licenseKeyImg', 'licenseKeyFile',]
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(os, OsAdmin)
