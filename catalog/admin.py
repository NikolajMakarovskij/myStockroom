from django.contrib import admin
from .models.workstation_model import *
from .models.models import  *

@admin.register(room)
class Room(admin.ModelAdmin):
    model = room
    exclude = ['id']

@admin.register(employee)
class Employee(admin.ModelAdmin):
    model = employee
    exclude = ['id']

@admin.register(workplace)
class Workplace(admin.ModelAdmin):
    model = workplace
    exclude = ['id']

@admin.register(departament)
class departament(admin.ModelAdmin):
    model = departament
    exclude = ['id']

@admin.register(post)
class post(admin.ModelAdmin):
    model = post
    exclude = ['id']

@admin.register(workstation)
class workstation(admin.ModelAdmin):
    model = workstation
    exclude = ['id']

@admin.register(software)
class software(admin.ModelAdmin):
    model = software
    exclude = ['id']

@admin.register(manufacturer)
class manufacturer(admin.ModelAdmin):
    model = manufacturer
    exclude = ['id']

@admin.register(os)
class OS(admin.ModelAdmin):
    model = os
    exclude = ['id']

@admin.register(monitor)
class monitor(admin.ModelAdmin):
    model = monitor
    exclude = ['id']

@admin.register(motherboard)
class motherboard(admin.ModelAdmin):
    model = motherboard
    exclude = ['id']

@admin.register(cpu)
class cpu(admin.ModelAdmin):
    model = cpu
    exclude = ['id']

@admin.register(gpu)
class gpu(admin.ModelAdmin):
    model = gpu
    exclude = ['id']

@admin.register(printer)
class printer(admin.ModelAdmin):
    model = printer
    exclude = ['id']

@admin.register(cartridge)
class cartridge(admin.ModelAdmin):
    model = cartridge
    exclude = ['id']

@admin.register(fotoval)
class fotoval(admin.ModelAdmin):
    model = fotoval
    exclude = ['id']

@admin.register(toner)
class toner(admin.ModelAdmin):
    model = toner
    exclude = ['id']

@admin.register(signature)
class signature(admin.ModelAdmin):
    model = signature
    exclude = ['id']

@admin.register(storage)
class storage(admin.ModelAdmin):
    model = storage
    exclude = ['id']


