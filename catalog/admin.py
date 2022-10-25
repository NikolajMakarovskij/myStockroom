from django.contrib import admin
from .models.models import  *

@admin.register(Room)
class Room(admin.ModelAdmin):
    model = Room
    fields = [
        ('name', 'Floor', 'Building')
    ]

@admin.register(Employee)
class Employee(admin.ModelAdmin):
    model = Employee
    fields = [        
        ('name', 'sername', 'family'),
        ('post','Workplace','employeeEmail')
    ]

@admin.register(Workplace)
class Workplace(admin.ModelAdmin):
    model = Workplace
    fields = [
        'name',
        ('Room', )
    ]

@admin.register(departament)
class departament(admin.ModelAdmin):
    model = departament
    fields = [
        ('name')
    ]

@admin.register(post)
class post(admin.ModelAdmin):
    model = post
    fields = [
        ('name', 'departament')
    ]



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

@admin.register(OS)
class OS(admin.ModelAdmin):
    model = OS
    fields = [
        ('name', 'manufacturer'),
        ('licenseKeyText', 'licenseKeyImg', 'licenseKeyFile' )
    ]

@admin.register(monitor)
class monitor(admin.ModelAdmin):
    model = monitor
    fields = [
        ('name','manufacturer'),
        ('serial','serialImg'),
        ('invent','inventImg'),

    ]

@admin.register(motherboard)
class motherboard(admin.ModelAdmin):
    model = motherboard
    fields = [
        ('name','manufacturer'),
        ('serial','serialImg'),
        'CPUSoket', 'RAMSlot', 'USBPort',
        'COMPort', 'PCI_E', 'PCI', 'VGA',
        'SATA', 'HDMI', 'DispayPort',
        'powerSupply', 'powerSupplyCPU',
    ]

@admin.register(printer)
class printer(admin.ModelAdmin):
    model = printer
    fields = [
        ('name','manufactured'),
        ('serial','serialImg'),
        ('invent', 'inventImg'),
        ('cartridge', 'paper'),
        'USBPort', 'LANPort',
        'Employee', 'Workplace', 'workstation',
    ]

@admin.register(cartridge)
class cartridge(admin.ModelAdmin):
    model = cartridge
    fields = [
        ('name','manufactured'),
        ('serial','serialImg'),
        ('buhCode', 'score'),
    ]

@admin.register(paper)
class paper(admin.ModelAdmin):
    model = paper
    fields = [
        ('name','manufactured'),
        ('paperFormat','score'),
    ]

@admin.register(digitalSignature)
class digitalSignature(admin.ModelAdmin):
    model = digitalSignature
    fields = [
        ('name','validityPeriod'),
        ('licenseKeyText','licenseKeyImg', 'licenseKeyFile'),
        ('Employee', 'Workplace', 'workstation'),
    ]


