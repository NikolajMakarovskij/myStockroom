from django.contrib import admin
from .models import Ups, Cassette
from catalog.utils import ExportAdmin

class UpsAdmin(ExportAdmin, admin.ModelAdmin):
    model = Ups
    list_display = ['name','manufacturer','power','voltage','current','score']
    list_filter = ['manufacturer' ]
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','power','voltage','current',
                    'accumulator','cassette','score']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Ups, UpsAdmin)

class CassetteAdmin(ExportAdmin, admin.ModelAdmin):
    model = Cassette
    list_display = ['name','manufacturer','power','voltage','current','score']
    list_filter = ['manufacturer',]
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','power','voltage','current',
                    'accumulator','score']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Cassette, CassetteAdmin)