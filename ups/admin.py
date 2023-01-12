from django.contrib import admin
from .models import ups, cassette
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

class UpsAdmin(admin.ModelAdmin):
    model = ups
    list_display = ['name','manufacturer','power','voltage','current','score']
    list_filter = ['manufacturer' ]
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','power','voltage','current',
                    'accumulator1','accumulator2','accumulator3','accumulator4','cassette1','cassette2','cassette3','cassette4','score']
    actions = [export_to_csv]
    
admin.site.register(ups, UpsAdmin)

class CassetteAdmin(admin.ModelAdmin):
    model = cassette
    list_display = ['name','manufacturer','power','voltage','current','score']
    list_filter = ['manufacturer',]
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','power','voltage','current',
                    'accumulator1','accumulator2','accumulator3','accumulator4','accumulator5','accumulator6','accumulator7','accumulator8','accumulator9','accumulator10','score']
    actions = [export_to_csv]
    
admin.site.register(cassette, CassetteAdmin)