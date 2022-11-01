from django.db import models
from .models import *
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
    cpu = models.ForeignKey(
        'cpu',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите CPU",
        verbose_name="CPU"
        )
    gpu = models.ForeignKey(
        'gpu',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите GPU",
        verbose_name="GPU"
        )
    ram = models.ForeignKey(
        'ram',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите RAM",
        verbose_name="RAM"
        )
    ssd = models.ForeignKey(
        'ssd',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите SSD",
        verbose_name="SSD"
        )
    hdd = models.ForeignKey(
        'hdd',
        on_delete=models.SET_NULL,
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
    dcpower = models.ForeignKey(
        'dcpower',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите блок питания",
        verbose_name="Блок питания"
        )
    keyBoard = models.ForeignKey(
        'keyBoard',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите клавиатуру",
        verbose_name="Клавиатура"
        )
    mouse = models.ForeignKey(
        'mouse',
        on_delete=models.SET_NULL,
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
        help_text="Укажите плотность пикселей",
        verbose_name="Плотность пикселей"
        )
    usbPort = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите количество USB",
        verbose_name="Количество USB"
        )
    hdmi = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите количество HDMI",
        verbose_name="Количество HDMI"
        )
    vga = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите количество VGA",
        verbose_name="Количество VGA"
        )
    dvi = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите количество DVI",
        verbose_name="Количество DVI"
    )
    displayPort = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите количество DisplayPort",
        verbose_name="Количество DisplayPort"
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

class cpu (models.Model):
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
        upload_to='cpu/serial/',
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
        upload_to='cpu/invent/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Фото инвентарного номера"
        )
    socket = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите сокет",
        verbose_name="Сокет"
        )
    frequency = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите частоту",
        verbose_name="Частота"
        )
    l1 = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите размер L1 cache",
        verbose_name="L1 cache"
        )
    l2 = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите размер L2 cache",
        verbose_name="L2 cache"
        )
    l3 = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите размер L3 cache",
        verbose_name="L3 cache"
        )
    core = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите количество ядер",
        verbose_name="Количество ядер"
        )
    thread = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите количество потоков",
        verbose_name="Количество потоков"
        )
    memory = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите тип RAM",
        verbose_name="Тип RAM"
        )
    memoryCapacity = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите поддерживаемый обЪем памяти",
        verbose_name="Поддерживаемый обЪем памяти"
        )
    channelsCapacity = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите количество каналов памяти",
        verbose_name="Количество каналов памяти"
    )
    tdp = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите TDP",
        verbose_name="TDP"
        )
    supply = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите тип питания",
        verbose_name="Питание"
        )
    score = models.IntegerField(
        blank=True, null=True,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе"
        )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('cpu-detail', args=[str(self.id)])
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
        verbose_name_plural = 'CPU'

class gpu (models.Model):
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
    plug = (
        ('Интегрированная','Интегрированная'),
        ('Дискретная','Дискретная')
    )
    type = models.CharField(
        max_length=50,
        choices=plug,
        help_text="Укажите тип подключения",
        verbose_name="Тип подключения"
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
        upload_to='gpu/serial/',
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
        upload_to='gpu/invent/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Фото инвентарного номера"
        )
    gram = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите объем памяти",
        verbose_name="Объем памяти"
        )
    gramType = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите тип памяти",
        verbose_name="Тип памяти"
        )
    pcie = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите версию PCI Express",
        verbose_name="Версия PCI Express"
        )
    supply = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите тип питания",
        verbose_name="Питание"
        )
    score = models.IntegerField(
        blank=True, null=True,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе"
        )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('gpu-detail', args=[str(self.id)])
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
        verbose_name_plural = 'GPU'

class ram (models.Model):
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
    type = models.CharField(
        max_length=50,
        help_text="Введите тип памяти",
        verbose_name="Тип памяти"
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
        upload_to='gpu/serial/',
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
        upload_to='gpu/invent/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Фото инвентарного номера"
        )
    ramCapacity = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите объем памяти",
        verbose_name="Объем памяти"
        )
    rang = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите ранг памяти",
        verbose_name="Ранг памяти"
        )
    score = models.IntegerField(
        blank=True, null=True,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе"
        )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ram-detail', args=[str(self.id)])
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
        verbose_name_plural = 'RAM'

class ssd (models.Model):
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
    type = models.CharField(
        max_length=50,
        help_text="Введите тип памяти",
        verbose_name="Тип памяти"
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
        upload_to='gpu/serial/',
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
        upload_to='gpu/invent/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Фото инвентарного номера"
        )
    capacity = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите объем памяти",
        verbose_name="Объем памяти"
        )
    plug = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите тип подключения",
        verbose_name="Тип подключения"
        )
    speedRead = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите скорость чтения",
        verbose_name="Скорость чтения"
        )
    speadWrite = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите скорость записи",
        verbose_name="Скорость записи"
        )
    resourse = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите ресурс",
        verbose_name="Ресурс"
        )
    score = models.IntegerField(
        blank=True, null=True,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе"
        )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ssd-detail', args=[str(self.id)])
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
        verbose_name_plural = 'ssd'

class hdd (models.Model):
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
        upload_to='gpu/serial/',
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
        upload_to='gpu/invent/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Фото инвентарного номера"
        )
    capacity = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите объем памяти",
        verbose_name="Объем памяти"
        )
    plug = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите тип подключения",
        verbose_name="Тип подключения"
        )
    speedRead = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите скорость чтения",
        verbose_name="Скорость чтения"
        )
    speadWrite = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите скорость записи",
        verbose_name="Скорость записи"
        )
    rpm = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите RPM",
        verbose_name="RPM"
        )
    score = models.IntegerField(
        blank=True, null=True,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе"
        )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('hdd-detail', args=[str(self.id)])
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
        verbose_name_plural = 'hdd'

class dcpower (models.Model):
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
        upload_to='gpu/serial/',
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
        upload_to='gpu/invent/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Фото инвентарного номера"
        )
    power = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите мощность",
        verbose_name="Мощность"
        )
    motherboard = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите питание материнской платы",
        verbose_name="Питание материнской платы"
        )
    cpu = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите питание CPU",
        verbose_name="Питание CPU"
        )
    gpu = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите питание GPU",
        verbose_name="Питание GPU"
        )
    sata = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите питание SATA",
        verbose_name="Питание SATA"
        )
    molex = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите питание molex",
        verbose_name="Питание molex"
        )
    score = models.IntegerField(
        blank=True, null=True,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе"
        )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('dcpower-detail', args=[str(self.id)])
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
        verbose_name_plural = 'dcpower'

class keyBoard (models.Model):
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
        upload_to='gpu/serial/',
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
        upload_to='gpu/invent/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Фото инвентарного номера"
        )
    score = models.IntegerField(
        blank=True, null=True,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе"
        )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('keyBoard-detail', args=[str(self.id)])
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
        verbose_name_plural = 'keyBoard'

class mouse (models.Model):
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
        upload_to='gpu/serial/',
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
        upload_to='gpu/invent/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Фото инвентарного номера"
        )
    score = models.IntegerField(
        blank=True, null=True,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе"
        )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('mouse-detail', args=[str(self.id)])
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
        verbose_name_plural = 'mouse'