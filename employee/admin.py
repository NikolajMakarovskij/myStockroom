from django.contrib import admin
from .models import employee, post, departament
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

class EmployeeAdmin(admin.ModelAdmin):
    model = employee
    list_display = ['name', 'sername','family','workplace','post',]
    list_filter = ['workplace__room__building', 'workplace__room__floor', 'post__departament' ]
    search_fields = ['name', 'sername','family','workplace','post','employeeEmail']
    actions = [export_to_csv]
    
admin.site.register(employee, EmployeeAdmin)

class PostAdmin(admin.ModelAdmin):
    model = post
    list_display = ['name', 'departament',]
    list_filter = ['departament', ]
    search_fields = ['name', 'departament',]
    actions = [export_to_csv]
    
admin.site.register(post, PostAdmin)

class DepartamentAdmin(admin.ModelAdmin):
    model = departament
    list_display = ['name']
    search_fields = ['name']
    actions = [export_to_csv]
    
admin.site.register(departament, DepartamentAdmin)


