from django.contrib import admin
from .models import employee, post, departament
from catalog.utils import ExportAdmin

class EmployeeAdmin(ExportAdmin, admin.ModelAdmin):
    model = employee
    list_display = ['name', 'sername','family','workplace','post',]
    list_filter = ['workplace__room__building', 'workplace__room__floor', 'post__departament' ]
    search_fields = ['name', 'sername','family','workplace','post','employeeEmail']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(employee, EmployeeAdmin)

class PostAdmin(ExportAdmin, admin.ModelAdmin):
    model = post
    list_display = ['name', 'departament',]
    list_filter = ['departament', ]
    search_fields = ['name', 'departament',]
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(post, PostAdmin)

class DepartamentAdmin(ExportAdmin, admin.ModelAdmin):
    model = departament
    list_display = ['name']
    search_fields = ['name']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(departament, DepartamentAdmin)


