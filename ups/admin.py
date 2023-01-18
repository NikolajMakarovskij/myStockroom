from django.contrib import admin
from .models import Ups, Cassette
from catalog.utils import ExportAdmin

class UpsAdmin(ExportAdmin, admin.ModelAdmin):
    model = Ups
    list_display = ['name','manufacturer','power','voltage','current','score']
    list_filter = ['manufacturer' ]
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','power','voltage','current',
                    'accumulator1','accumulator2','accumulator3','accumulator4','cassette1','cassette2','cassette3','cassette4','score']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Ups, UpsAdmin)

class CassetteAdmin(ExportAdmin, admin.ModelAdmin):
    model = Cassette
    list_display = ['name','manufacturer','power','voltage','current','score']
    list_filter = ['manufacturer',]
    search_fields = ['name','manufacturer','serial','serialImg','inventImg','invent','power','voltage','current',
                    'accumulator1','accumulator2','accumulator3','accumulator4','accumulator5','accumulator6','accumulator7','accumulator8','accumulator9','accumulator10','score']
    actions = [ExportAdmin.export_to_csv]
    
admin.site.register(Cassette, CassetteAdmin)