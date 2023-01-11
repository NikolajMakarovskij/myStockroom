from django.contrib import admin
from .models import room, workplace
import csv
import datetime
from django.http import HttpResponse


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'экспорт CSV'

class RoomAdmin(admin.ModelAdmin):
    model = room
    list_display = ['name','floor','building',]
    list_filter = ['floor', 'building']
    search_fields = ['name', 'floor', 'building']
    actions = [export_to_csv]
    
admin.site.register(room, RoomAdmin)


class WorkplaceAdmin(admin.ModelAdmin):
    model = workplace
    list_display = ['name','room']
    list_filter = ['room', 'room__floor', 'room__building']
    search_fields = ['name', 'room']
    actions = [export_to_csv]

admin.site.register(workplace, WorkplaceAdmin)

