from django.contrib import admin
from import_export.admin import ImportExportModelAdmin  # type: ignore[import-untyped]

from .models import Departament, Employee, Post


@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    """_EmployeeAdmin_ 
    Add model to admin panel
    """
    list_display = [
        "name",
        "surname",
        "last_name",
        "workplace",
        "post",
    ]
    list_filter = [
        "workplace__room__building",
        "workplace__room__floor",
        "post__departament",
    ]
    search_fields = [
        "name",
        "surname",
        "last_name",
        "workplace",
        "post",
        "employeeEmail",
    ]


@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    """_PostAdmin_ 
    Add model to admin panel
    """
    list_display = [
        "name",
        "departament",
    ]
    list_filter = [
        "departament",
    ]
    search_fields = [
        "name",
        "departament",
    ]


@admin.register(Departament)
class DepartamentAdmin(ImportExportModelAdmin):
    """_DepartamentAdmin_ 
    Add model to admin panel
    """
    list_display = ["name"]
    search_fields = ["name"]
