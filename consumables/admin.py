from django.contrib import admin
from .models import cartridge, fotoval, toner, accumulator
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

class CartridgeAdmin(admin.ModelAdmin):
    model = cartridge
    list_display = ['name','manufacturer','buhCode','score' ]
    list_filter = ['manufacturer', ]
    search_fields = ['name','manufacturer','buhCode','score' ]
    actions = [export_to_csv]
    
admin.site.register(cartridge, CartridgeAdmin)

class TonerAdmin(admin.ModelAdmin):
    model = toner
    list_display = ['name','manufacturer','buhCode','score' ]
    list_filter = ['manufacturer', ]
    search_fields = ['name','manufacturer','buhCode','score' ]
    actions = [export_to_csv]
    
admin.site.register(toner, TonerAdmin)

class FotovalAdmin(admin.ModelAdmin):
    model = fotoval
    list_display = ['name','manufacturer','mileage','buhCode','score']
    list_filter = ['manufacturer', ]
    search_fields = ['name','manufacturer','mileage','buhCode','score']
    actions = [export_to_csv]
    
admin.site.register(fotoval, FotovalAdmin)

class AccumulatorAdmin(admin.ModelAdmin):
    model = accumulator
    list_display = ['name','manufacturer','power','voltage','current','score' ]
    list_filter = ['manufacturer', ]
    search_fields = ['name','manufacturer','power','voltage','current','score']
    actions = [export_to_csv]
    
admin.site.register(accumulator, AccumulatorAdmin)


