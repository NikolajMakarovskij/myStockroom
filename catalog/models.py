from datetime import date
import datetime
from django.db import models
from .models import *
from django.urls import reverse
import uuid 
from django.forms.models import model_to_dict

class Building(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        'Building',
        max_length=200
        )

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
    class Meta:
        verbose_name_plural = 'Здание'

class Floor(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=15,
        help_text="Введите номер этажа"
        )
    Building = models.ForeignKey(
        'Building',
        on_delete=models.SET_NULL,
        blank=True, null=True
        )

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Этаж'


class Room(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=15,
        help_text="Введите номер кабинета"
        )
    Building = models.ForeignKey(
        'Building',
        on_delete=models.SET_NULL,
        blank=True, null=True
        )
    Floor = models.ForeignKey(
        'Floor',
        on_delete=models.SET_NULL,
        blank=True, null=True
        )

    def __str__(self):
        return self.name
    def get_all_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for f in self._meta.fields:

            fname = f.name        
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+fname+'_display'
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, fname)
                except AttributeError:
                    value = None

            # only display fields with values and skip some fields entirely
            if f.editable and value and f.name not in ('id', 'status', 'workshop', 'user', 'complete') :

                fields.append(
                    {
                    'label':f.verbose_name, 
                    'name':f.name, 
                    'value':value,
                    }
                )
        return fields
    class Meta:
        verbose_name_plural = 'Рабочее место'
        ordering = ["name","Room"]
    class Meta:
        verbose_name_plural = 'Кабинет'
        ordering = ["Building", "Floor", "name"]

class Employee(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите ФИО сотрудника",
        verbose_name="ФИО сотрудника")
    Workplace = models.ForeignKey(
        'Workplace',
        on_delete=models.SET_NULL,
        blank=True, null=True
        )
    post = models.ForeignKey(
        'Post',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Должность"
        )
    departament= models.ForeignKey(
        'Departament',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Отдел"
        )

    def __str__(self):
        return self.name
    def get_all_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for f in self._meta.fields:

            fname = f.name        
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+fname+'_display'
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, fname)
                except AttributeError:
                    value = None

            # only display fields with values and skip some fields entirely
            if f.editable and value and f.name not in ('id', 'Workplace') :

                fields.append(
                    {
                    'label':f.verbose_name, 
                    'name':f.name, 
                    'value':value,
                    }
                )
        return fields
    class Meta:
        verbose_name_plural = 'Сотрудник'
        ordering = ["name", "-Workplace"]

class Workplace(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите номер рабочего места",
        verbose_name="Рабочее место"
        )
    Room = models.ForeignKey(
        'Room',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Номер кабинета"
        )
    Floor = models.ForeignKey(
        'Floor',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Этаж"
        )
    Building = models.ForeignKey(
        'Building',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Здание"    
    )
    

    def __str__(self):
        return self.name
    def get_all_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for f in self._meta.fields:

            fname = f.name        
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+fname+'_display'
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, fname)
                except AttributeError:
                    value = None

            # only display fields with values and skip some fields entirely
            if f.editable and value and f.name not in ('id') :

                fields.append(
                    {
                    'label':f.verbose_name, 
                    'name':f.name, 
                    'value':value,
                    }
                )
        return fields
    class Meta:
        verbose_name_plural = 'Рабочее место'
        ordering = ["-Building", "-Floor", "Room", ]

class departament(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="Введите название отдела"
        )

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Отдел'

class post(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите должность"
        )
    departament = models.ForeignKey(
        'departament',
        on_delete=models.SET_NULL,
        blank=True, null=True
        )

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Должность'

class software (models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="ВВедите название ПО"
        )
    Employee = models.ForeignKey(
        'Employee',
        on_delete=models.SET_NULL,
        blank=True, null=True
        )
    manufacturer = models.CharField(
        max_length=200,
        blank=True, null=True,
        help_text="Описание производителя")
    licenseKeyText = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите лицензтонный ключ")
    licenseKeyImg = models.ImageField(
        upload_to='soft/',
        blank=True, null=True,
        help_text="прикрепите файл")
    licenseKeyFile = models.FileField(
        upload_to='soft/',
        blank=True, null=True,
        help_text="прикрепите файл")
    workstation = models.ForeignKey(
        'workstation',
        on_delete=models.SET_NULL,
        blank=True, null=True
        )


    def __str__(self):
        return self.name
    def get_all_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for f in self._meta.fields:

            fname = f.name        
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+fname+'_display'
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, fname)
                except AttributeError:
                    value = None

            # only display fields with values and skip some fields entirely
            if f.editable and value and f.name not in ('id', 'licenseKeyImg', 'licenseKeyFile', 'licenseKeyText') :

                fields.append(
                    {
                    'label':f.verbose_name, 
                    'name':f.name, 
                    'value':value,
                    }
                )
        return fields
    class Meta:
        verbose_name_plural = 'ПО'
        ordering = [ "Employee", "name"]

class OS (models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите Название ОС",
        verbose_name="Название"
        )
    manufacturer = models.CharField(
        max_length=200,
        blank=True, null=True,
        help_text="Описание производителя",
        verbose_name="Производитель"
        )    
    licenseKeyText = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите лицензтонный ключ",
        )
    licenseKeyImg = models.ImageField(
        upload_to='OS/',
        blank=True, null=True,
        help_text="прикрепите файл"
        )
    licenseKeyFile = models.FileField(
        upload_to='soft/',
        blank=True, null=True,
        help_text="прикрепите файл"
        )

    def __str__(self):
        return self.name
    def get_all_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for f in self._meta.fields:

            fname = f.name        
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+fname+'_display'
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, fname)
                except AttributeError:
                    value = None

            # only display fields with values and skip some fields entirely
            if f.editable and value and f.name not in ('id', 'licenseKeyImg', 'licenseKeyFile', 'licenseKeyText') :

                fields.append(
                    {
                    'label':f.verbose_name, 
                    'name':f.name, 
                    'value':value,
                    }
                )
        return fields
    class Meta:
        verbose_name_plural = 'ОС'

class workstation(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
    )
    name = models.CharField(
        max_length=50,
        help_text="Введите номер станции",
        verbose_name="Рабочая станция"
        )
    manufacturer = models.CharField(
        max_length=200,
        blank=True, null=True,
        help_text="Описание производителя",
        verbose_name="Производитель"
        )
    modelComputer = models.CharField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите название модели",
        verbose_name="модель"
        )
    serial = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите серийный номер"
        )
    serialImg = models.ImageField(
        upload_to='workstation/serial/',
        blank=True, null=True,
        help_text="прикрепите файл"
        )
    invent = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите инвентаризационный номер"
        )
    inventImg = models.ImageField(
        upload_to='workstation/invent/',
        blank=True, null=True,
        help_text="прикрепите файл")
    OS = models.ForeignKey(
        'OS',
        on_delete=models.SET_NULL,
        blank=True, null=True
        )
    motherboard = models.ForeignKey(
        'motherboard',
        on_delete=models.SET_NULL,
        blank=True, null=True
        )
    monitor = models.ForeignKey(
        'monitor',
        on_delete=models.SET_NULL,
        blank=True, null=True
        )
    CPU = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Описание CPU")
    GPU = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Описание GPU"
        )
    RAM = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Описание RAM"
        )
    SSD = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Описание SSD"
        )
    HDD = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Описание HDD"
        )
    DCPower = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Описание блока питания",
        verbose_name="Блок питания"
        )
    keyBoard = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Описание клавиатуры",
        verbose_name="Клавиатура"
        )
    mouse = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Описание мыши",
        verbose_name="Мышь"
        )
    Workplace = models.ForeignKey(
        'Workplace',
        on_delete=models.SET_NULL,
        blank=True, null=True
        )
    Employee = models.ForeignKey(
        'Employee',
        on_delete=models.SET_NULL,
        blank=True, null=True
        )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('workstation-detail', args=[str(self.id)])
    def get_all_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for f in self._meta.fields:

            fname = f.name        
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+fname+'_display'
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, fname)
                except AttributeError:
                    value = None

            # only display fields with values and skip some fields entirely
            if f.editable and value and f.name not in (
                'id', 'serialImg', 'inventImg', 'serial',
                'invent', 'OS', 'monitor', 'motherboard',
                'name', 'Workplace', 'Employee',
                ) :

                fields.append(
                    {
                    'label':f.verbose_name, 
                    'name':f.name, 
                    'value':value,
                    }
                )
        return fields
    class Meta:
        verbose_name_plural = 'Рабочая станция'
        ordering = ["Employee", "name", "Workplace"]

class monitor (models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID")
    name = models.CharField(
        max_length=50,
        help_text="Введите Название модели",
        verbose_name="Модель"
        )
    manufacturer = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите Название производителя",
        verbose_name="Производитель"
        ) 
    serial = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите серийный номер"
        )
    serialImg = models.ImageField(
        upload_to='monitor/serial/',
        blank=True, null=True,
        help_text="прикрепите файл")
    invent = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите инвентаризационный номер")
    inventImg = models.ImageField(
        upload_to='monitor/invent/',
        blank=True, null=True,
        help_text="прикрепите файл"
        )

    def __str__(self):
        return self.name
    def get_all_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for f in self._meta.fields:

            fname = f.name        
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+fname+'_display'
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, fname)
                except AttributeError:
                    value = None

            # only display fields with values and skip some fields entirely
            if f.editable and value and f.name not in (
                'id', 'name', 'serialImg', 'inventImg', 'serial', 'invent') :

                fields.append(
                    {
                    'label':f.verbose_name, 
                    'name':f.name, 
                    'value':value,
                    }
                )
        return fields
    class Meta:
        verbose_name_plural = 'Монитор'

class motherboard (models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите Название модели"
        )
    manufacturer = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите Название производителя",
        verbose_name="Производитель"        
        )
    serial = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите серийный номер")
    serialImg = models.ImageField(
        upload_to='motherboard/',
        blank=True, null=True,
        help_text="прикрепите файл")
    invent = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите серийный номер")
    inventImg = models.ImageField(
        upload_to='motherboard/',
        blank=True, null=True,
        help_text="прикрепите файл")
    CPUSoket = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Описание сокета",
        verbose_name="CPU Soket"
        )
    RAMSlot = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Описание RAM",
        verbose_name="RAM Slot"
        )
    USBPort = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество и тип",
        verbose_name="USB Port"
        )
    COMPort = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество",
        verbose_name="COM Port"
        )
    PCI_E = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество",
        verbose_name="PCI Express"
        )
    PCI = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество и тип",
        verbose_name="PCI"
        )
    VGA = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество"
        
        )
    SATA = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество"
        )
    HDMI = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество"
        )
    DispayPort = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество"
        )
    powerSupply = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите конфигурацию",
        verbose_name="Питание материнской платы"
        )
    powerSupplyCPU = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите конфигурацию",
        verbose_name="Питание CPU"
        )

    def __str__(self):
        return self.name
    def get_all_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for f in self._meta.fields:

            fname = f.name        
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+fname+'_display'
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, fname)
                except AttributeError:
                    value = None

            # only display fields with values and skip some fields entirely
            if f.editable and value and f.name not in ('id', 'name', 'serialImg', 'inventImg', 'serial', 'invent' ) :

                fields.append(
                    {
                    'label':f.verbose_name, 
                    'name':f.name, 
                    'value':value,
                    }
                )
        return fields
    class Meta:
        verbose_name_plural = 'Материнская плата'

class printer (models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите название модели",
        verbose_name="Модель"
        )
    manufactured = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите название производителя",
        verbose_name="Производитель"
        )
    serial = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите серийный номер",
        verbose_name="Серийный номер"
        )
    serialImg = models.ImageField(
        upload_to='motherboard/soft/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Серийный номер"
        )
    invent = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите инвентаризационный номер",
        verbose_name="Инвентарный номер"
        )
    inventImg = models.ImageField(
        upload_to='workstation/invent/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Инвентарный номер"
        )
    cartridge = models.ForeignKey(
        'cartridge',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Картридж"
        )
    paper = models.ForeignKey(
        'paper',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Бумага"
        )
    USBPort = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество и тип",
        verbose_name="USB"
        )
    LANPort = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество",
        verbose_name="LAN"
        )
    Workplace = models.ForeignKey(
        'Workplace',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Рабочее место"
        )
    Employee = models.ForeignKey(
        'Employee',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Сотрудник"
        )
    workstation = models.ForeignKey(
        'workstation',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Рабочая станция"
        )

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('printer-detail', args=[str(self.id)])
    def get_all_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for f in self._meta.fields:

            fname = f.name        
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+fname+'_display'
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, fname)
                except AttributeError:
                    value = None

            # only display fields with values and skip some fields entirely
            if f.editable and value and f.name not in ('id', 'Employee',  'workstation',  'Workplace') :

                fields.append(
                    {
                    'label':f.verbose_name, 
                    'name':f.name, 
                    'value':value,
                    }
                )
        return fields
    class Meta:
        verbose_name_plural = 'Принтер'
        ordering = [ "Employee", "name"]

class cartridge (models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите название модели",
        verbose_name="Модель"
        )
    manufactured = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите название производителя",
        verbose_name="Производитель"
        )
    serial = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите серийный номер",
        verbose_name="Серийный номер"
        )
    serialImg = models.ImageField(
        upload_to='printer/cartridge/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Серийный номер")
    buhCode = models.CharField(
        max_length=50,
        help_text="Введите код по бухгалтерии",
        verbose_name="Код в бухгалтерии"
        )
    score = models.IntegerField(
        blank=True, null=True,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе"
        )

    def __str__(self):
        return self.name
    def get_all_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for f in self._meta.fields:

            fname = f.name        
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+fname+'_display'
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, fname)
                except AttributeError:
                    value = None

            # only display fields with values and skip some fields entirely
            if f.editable and value and f.name not in ('id', ) :

                fields.append(
                    {
                    'label':f.verbose_name, 
                    'name':f.name, 
                    'value':value,
                    }
                )
        return fields
    class Meta:
        verbose_name_plural = 'картридж'

class paper (models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите название модели",
        verbose_name="Название",

        )
    manufactured = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите название производителя",
        verbose_name="Производитель"
        )
    FORMAT = (
        ('A4', 'A4'),
        ('A3', 'A3'),
        ('A2', 'A2'),
        ('A1', 'A1'),
        ('A0', 'A0'),
        ('A5', 'A5'),
        )
    paperFormat = models.CharField(
        max_length=5,
        choices=FORMAT,
        default='A4',
        help_text="Укажите формат",
        verbose_name="Формат"
        )
    score = models.IntegerField(
        blank=True, null=True,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе"
        )

    def __str__(self):
        return self.name
    def get_all_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for f in self._meta.fields:

            fname = f.name        
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+fname+'_display'
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, fname)
                except AttributeError:
                    value = None

            # only display fields with values and skip some fields entirely
            if f.editable and value and f.name not in ('id', ) :

                fields.append(
                    {
                    'label':f.verbose_name, 
                    'name':f.name, 
                    'value':value,
                    }
                )
        return fields
    class Meta:
        verbose_name_plural = 'Бумага'

class digitalSignature (models.Model): #electronic digital signature
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите номер ключа",
        verbose_name="Ключ"
        )
    licenseKeyText = models.CharField(
        blank=True, null=True,
        max_length=50,
        help_text="Введите лицензионный ключ",
        )
    licenseKeyImg = models.ImageField(
        upload_to='OS/',
        blank=True, null=True,
        help_text="прикрепите файл"
        )
    licenseKeyFile = models.FileField(
        upload_to='soft/',
        blank=True, null=True,
        help_text="прикрепите файл"
        )
    Workplace = models.ForeignKey(
        'Workplace',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Рабочее место"
        )
    Employee = models.ForeignKey(
        'Employee',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Сотрудник"
        )
    workstation = models.ForeignKey(
        'workstation',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Рабочая станция"
        )
    validityPeriod = models.DateField(
        null=True, blank=True
        )
    employeeEmail = models.EmailField(
        null=True, blank=True
        )


    def __str__(self):
        return self.name
    
    def validateP(self):
        return self.validateP

    def get_absolute_url(self):
        return reverse('digitalsignature-detail', args=[str(self.id)])
    
    def danger_date(self):
        return self.danger_date and  (date.today())
    
    def warningOneWeek(self):
        return self.warningOneWeek and (datetime.date.today() + datetime.timedelta(weeks=1))

    def warningTwoWeeks(self):
        return self.warningTwoWeeks and (datetime.date.today() + datetime.timedelta(weeks=2))

    def warningThreeWeeks(self):
        return self.warningThreeWeeks and (datetime.date.today() + datetime.timedelta(weeks=3))

    def warningOneMounth(self):
        return self.warningOneMounth and (datetime.date.today() + datetime.timedelta(weeks=4))
    
    def warningTwoMounth(self):
        return self.warningTwoMounth and (datetime.date.today() + datetime.timedelta(weeks=8))
        
    def get_all_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for f in self._meta.fields:

            fname = f.name        
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+fname+'_display'
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, fname)
                except AttributeError:
                    value = None

            # only display fields with values and skip some fields entirely
            if f.editable and value and f.name not in ('id', 'licenseKeyText', 'licenseKeyImg', 'licenseKeyFile', ) :

                fields.append(
                    {
                    'label':f.verbose_name, 
                    'name':f.name, 
                    'value':value,
                    }
                )
        return fields

    class Meta:
        verbose_name_plural = 'ЭЦП'
        ordering = [ "validityPeriod",]


        