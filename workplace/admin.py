from django.contrib import admin
from .models import Room, Workplace
from catalog.utils import ExportAdmin

class RoomAdmin(ExportAdmin, admin.ModelAdmin):
    model = Room
    list_display = ['name','floor','building',]
    list_filter = ['floor', 'building']
    search_fields = ['name', 'floor', 'building']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Room, RoomAdmin)


class WorkplaceAdmin(ExportAdmin, admin.ModelAdmin):
    model = Workplace
    list_display = ['name','room']
    list_filter = ['room', 'room__floor', 'room__building']
    search_fields = ['name', 'room']
    actions = [ExportAdmin.export_to_csv]

admin.site.register(Workplace, WorkplaceAdmin)

