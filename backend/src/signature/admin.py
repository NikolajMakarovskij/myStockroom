from django.contrib import admin
from import_export.admin import ImportExportModelAdmin  # type: ignore[import-untyped]

from .models import Signature


@admin.register(Signature)
class SignatureAdmin(ImportExportModelAdmin):
    """_SignatureAdmin_
    Add model to admin panel
    """

    list_display = [
        "name",
        "periodOpen",
        "periodClose",
        "employeeRegister",
        "employeeStorage",
        "workstation",
        "storage",
    ]
    list_filter = [
        "workstation__workplace__room__floor",
        "workstation__workplace__room__building",
    ]
    search_fields = [
        "name",
        "licenseKeyFileOpen",
        "licenseKeyFileClose",
        "periodOpen",
        "periodClose",
        "employeeRegister",
        "employeeStorage",
        "workstation",
        "storage",
    ]
