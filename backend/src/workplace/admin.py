from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Room, Workplace


@admin.register(Room)
class RoomAdmin(ImportExportModelAdmin):
    list_display = [
        "name",
        "floor",
        "building",
    ]
    list_filter = ["floor", "building"]
    search_fields = ["name", "floor", "building"]


@admin.register(Workplace)
class WorkplaceAdmin(ImportExportModelAdmin):
    list_display = ["name", "room"]
    list_filter = ["room", "room__floor", "room__building"]
    search_fields = ["name", "room"]
