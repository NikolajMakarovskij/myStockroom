from django.contrib import admin
from .models import manufacturer
from catalog.utils import ExportAdmin


class ManufacturerAdmin(ExportAdmin, admin.ModelAdmin):
    model = manufacturer
    list_display = ['name', 'country', 'production']
    list_filter = [ 'country', 'production']
    search_fields = ['name', 'country', 'production']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(manufacturer, ManufacturerAdmin)
