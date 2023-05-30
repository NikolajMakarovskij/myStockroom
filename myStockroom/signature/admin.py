from django.contrib import admin
from .models import Signature
from catalog.utils import ExportAdmin

class SignatureAdmin(ExportAdmin, admin.ModelAdmin):
    model = Signature
    list_display = ['name','periodOpen','periodClose','employeeRegister','employeeStorage','workstation','storage']
    list_filter = [ 'workstation__workplace__room__floor', 'workstation__workplace__room__building' ]
    search_fields = ['name','licenseKeyFileOpen','licenseKeyFileClose','periodOpen','periodClose','employeeRegister','employeeStorage','workstation','storage' ]
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Signature, SignatureAdmin)