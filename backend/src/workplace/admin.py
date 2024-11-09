from django.contrib import admin
from import_export.admin import ImportExportModelAdmin  # type: ignore[import-untyped]

from .models import Room, Workplace


@admin.register(Room)
class RoomAdmin(ImportExportModelAdmin):
    """_RoomAdmin_
    Add model to admin panel
    """

    list_display = [
        "name",
        "floor",
        "building",
    ]
    list_filter = ["floor", "building"]
    search_fields = ["name", "floor", "building"]


@admin.register(Workplace)
class WorkplaceAdmin(ImportExportModelAdmin):
    """_WorkplaceAdmin_
    Add model to admin panel
    """

    list_display = ["name", "room"]
    list_filter = ["room", "room__floor", "room__building"]
    search_fields = ["name", "room"]
