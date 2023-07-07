from django.contrib import admin
from .models import Software, Os
from catalog.utils import ExportAdmin


class SoftwareAdmin(ExportAdmin, admin.ModelAdmin):
    model = Software
    list_display = ['name', 'manufacturer', 'version', 'bitDepth', 'licenseKeyText', 'licenseKeyImg',
                    'licenseKeyFile', ]
    list_filter = ['manufacturer', 'bitDepth', ]
    search_fields = ['name', 'manufacturer', 'version', 'bitDepth', 'licenseKeyText', 'licenseKeyImg',
                     'licenseKeyFile', ]
    actions = [ExportAdmin.export_to_csv]


admin.site.register(Software, SoftwareAdmin)


class OsAdmin(ExportAdmin, admin.ModelAdmin):
    model = Os
    list_display = ['name', 'manufacturer', 'version', 'bitDepth', 'licenseKeyText', 'licenseKeyImg',
                    'licenseKeyFile', ]
    list_filter = ['manufacturer', 'bitDepth', ]
    search_fields = ['name', 'manufacturer', 'version', 'bitDepth', 'licenseKeyText', 'licenseKeyImg',
                     'licenseKeyFile', ]
    actions = [ExportAdmin.export_to_csv]


admin.site.register(Os, OsAdmin)
