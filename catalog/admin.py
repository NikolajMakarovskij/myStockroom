from django.contrib import admin
from .models import references
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

admin.site.site_header = 'Панель администратора базы техники компании'
admin.site.site_title = 'Панель администратора'
admin.site.index_title = 'Администрирование базы'

class ReferencesAdmin(admin.ModelAdmin):
    model = references
    list_display = ['name', 'linkname', ]
    search_fields = ['name', 'linkname', ]
    actions = [export_to_csv]
    
admin.site.register(references, ReferencesAdmin)