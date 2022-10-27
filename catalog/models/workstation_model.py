import datetime
from tabnanny import verbose
from django.db import models
from .models import *
from .employee_model import *
from .workplace_model import *
from .software_model import *
from django.urls import reverse
import uuid 

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
    manufacturer = models.ForeignKey(
        'manufacturer',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите производителя",
        verbose_name="Производитель"
        )
    modelComputer = models.CharField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите название модели",
        verbose_name="Модель"
        )
    serial = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите серийный номер",
        verbose_name="Серийный номер"
        )
    serialImg = models.ImageField(
        upload_to='workstation/serial/',
        blank=True, null=True,
        help_text="Прикрепите файл",
        verbose_name="Фото серийного номера"
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
        help_text="Прикрепите файл",
        verbose_name="Фото инвентарного номера"
        )
    motherboard = models.ForeignKey(
        'motherboard',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите материнскую плату",
        verbose_name="Материнская плата"
        )
    monitor = models.ForeignKey(
        'monitor',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите монитор",
        verbose_name="Монитор"
        )
    cpu = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Укажите CPU",
        verbose_name="CPU"
        )
    gpu = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Укажите GPU",
        verbose_name="GPU"
        )
    ram = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Укажите RAM",
        verbose_name="RAM"
        )
    ssd = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Укажите SSD",
        verbose_name="SSD"
        )
    hdd = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Укажите HDD",
        verbose_name="HDD"
        )
    os = models.ForeignKey(
        'os',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите ОС",
        verbose_name="Операционная система"
        )
    dcpower = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Укажите блок питания",
        verbose_name="Блок питания"
        )
    keyBoard = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Укажите клавиатуру",
        verbose_name="Клавиатура"
        )
    mouse = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Укажите мышь",
        verbose_name="Мышь"
        )
    ups = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Укажите блок бесперебойного питания",
        verbose_name="Блок бесперебойного питания"
        )
    workplace = models.ForeignKey(
        'workplace',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите рабочее место",
        verbose_name="Рабочее место"
        )
    employee = models.ForeignKey(
        'employee',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите сотрудника",
        verbose_name="Сотрудник"
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
        verbose_name_plural = 'Рабочая станция'
        ordering = ["employee", "name", "workplace"]

class monitor (models.Model):
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
    manufacturer = models.ForeignKey(
        'manufacturer',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите производителя",
        verbose_name="Производитель"
        )
    serial = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите серийный номер",
        verbose_name="Серийный номер"
        )
    serialImg = models.ImageField(
        upload_to='monitor/serial/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Фото серийного номера"
        )
    invent = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите инвентарный номер",
        verbose_name="Инвентарный номер"
        )
    inventImg = models.ImageField(
        upload_to='monitor/invent/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Фото инвентарного номера"
        )
    resolution = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите разрешение",
        verbose_name="Разрешение"
        )
    frequency = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите частоту",
        verbose_name="Частота"
        )
    typeDisplay = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите тип матрицы",
        verbose_name="Тип матрицы"
        )
    dpi = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажит плотность пикселей",
        verbose_name="Плотность пикселей"
        )
    usbPort = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите количество USB",
        verbose_name="количество USB"
        )
    hdmi = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите количество HDMI",
        verbose_name="количество HDMI"
        )
    vga = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите количество VGA",
        verbose_name="количество VGA"
        )
    dvi = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите количество DVI",
        verbose_name="количество DVI"
    )
    displayPort = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите количество DisplayPort",
        verbose_name="количество DisplayPort"
        )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('monitor-detail', args=[str(self.id)])
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
        verbose_name_plural = 'Монитор'

class motherboard (models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите Название модели",
        verbose_name="Название модели",
        )
    manufacturer = models.ForeignKey(
        'manufacturer',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите производителя",
        verbose_name="Производитель"
        )
    serial = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите серийный номер",
        verbose_name="Серийный номер"
        )
    serialImg = models.ImageField(
        upload_to='motherboard/serial/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Фото серийного номера"
        )
    invent = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите инвентарный номер",
        verbose_name="Инвентарный номер"
        )
    inventImg = models.ImageField(
        upload_to='motherboard/invent/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Фото инвентарного номера"
        )
    cpuSoket = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Описание сокета",
        verbose_name="CPU Soket"
        )
    ramSlot = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Описание RAM",
        verbose_name="RAM Slot"
        )
    usb_2 = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество",
        verbose_name="USB 2.0"
        )
    usb_3 = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество",
        verbose_name="USB 3.0"
        )
    usb_3_1 = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество",
        verbose_name="USB 3.1"
        )
    usb_3_2 = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество",
        verbose_name="USB 3.2"
        )
    usb_4_0 = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество",
        verbose_name="USB 4.0"
        )
    comPort = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество",
        verbose_name="COM Port"
        )
    pcie_x1 = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество",
        verbose_name="PCIExpress X1"
        )
    pcie_x16 = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество",
        verbose_name="PCI Express X16"
        )
    pci = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество и тип",
        verbose_name="PCI"
        )
    sata = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество",
        verbose_name="SATA"
        )
    m2 = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество",
        verbose_name="M2"
        )
    vga = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество",
        verbose_name="VGA"
        )
    hdmi = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество",
        verbose_name="HDMI"
        )
    dvi = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество",
        verbose_name="DVI"
        )
    dispayPort = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество",
        verbose_name="DisplayPort"
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
    def get_absolute_url(self):
        return reverse('motherboard-detail', args=[str(self.id)])
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
            if f.editable and value and f.name not in ('id',  ) :

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