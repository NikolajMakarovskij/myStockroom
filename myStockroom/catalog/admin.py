from django.contrib import admin
from .models import References
from .utils import ExportAdmin

admin.site.site_header = 'Панель администратора базы техники компании'
admin.site.site_title = 'Панель администратора'
admin.site.index_title = 'Администрирование базы'


class ReferencesAdmin(ExportAdmin, admin.ModelAdmin):
    model = References
    list_display = ['name', 'linkname', ]
    search_fields = ['name', 'linkname', ]
    actions = [ExportAdmin.export_to_csv]


admin.site.register(References, ReferencesAdmin)
