from django.db import models
from counterparty.models import Manufacturer
from django.urls import reverse
import uuid 
from .models import *
from workplace.models import Workplace
from employee.models import Employee
from software.models import Software, Os
from ups.models import Ups
from catalog.utils import ModelMixin


class Workstation_cat(ModelMixin, models.Model):
    """
    Модель группы для принтеров
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите название",
        verbose_name="Название"
        )
    slug = models.SlugField(
        max_length=50, unique=True, db_index=True,
        help_text="Введите URL (для работы навигациии в расходниках)",
        verbose_name="URL"
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('workstation:category',kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Группа рабочих станций'
        verbose_name_plural = 'Группы рабочих станций'
        ordering = ['name']

class Workstation(ModelMixin, models.Model):
    """
    Модель компьютерной техники
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        db_index=True,
        help_text="ID"
    )
    name = models.CharField(
        max_length=50,
        help_text="Введите номер станции",
        verbose_name="Рабочая станция"
        )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите производителя",
        verbose_name="Производитель"
        )
    categories = models.ForeignKey(
        'Workstation_cat',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите группу",
        verbose_name="Группа"
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
    motherboard = models.CharField(
        max_length=150,
        blank=True, null=True,
        help_text="Укажите материнскую плату",
        verbose_name="Материнская плата"
        )
    monitor = models.ForeignKey(
        'Monitor',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите монитор",
        verbose_name="Монитор"
        )
    cpu = models.CharField(
        max_length=150,
        blank=True, null=True,
        help_text="Укажите CPU",
        verbose_name="CPU"
        )
    gpu = models.CharField(
        max_length=150,
        blank=True, null=True,
        help_text="Укажите GPU",
        verbose_name="GPU"
        )
    ram = models.ForeignKey(
        'Ram',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите RAM",
        verbose_name="RAM"
        )
    ssd = models.ForeignKey(
        'Ssd',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите SSD",
        verbose_name="SSD"
        )
    hdd = models.ForeignKey(
        'Hdd',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите HDD",
        verbose_name="HDD"
        )
    dcpower = models.CharField(
        max_length=150,
        blank=True, null=True,
        help_text="Укажите блок питания",
        verbose_name="Блок питания"
        )
    keyBoard = models.ForeignKey(
        'KeyBoard',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите клавиатуру",
        verbose_name="Клавиатура"
        )
    mouse = models.ForeignKey(
        'Mouse',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите мышь",
        verbose_name="Мышь"
        )
    ups = models.ForeignKey(
        Ups,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите блок бесперебойного питания",
        verbose_name="Блок бесперебойного питания"
        )
    workplace = models.ForeignKey(
        Workplace,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите рабочее место",
        verbose_name="Рабочее место"
        )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите сотрудника",
        verbose_name="Сотрудник"
        )
    software = models.ForeignKey(
        Software,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите програмное обеспечение",
        verbose_name="Програмное обеспечение"
        )
    os = models.ForeignKey(
        Os,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите операционную систему",
        verbose_name="Операционная система"
        )
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('workstation:workstation-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Рабочая станция'
        verbose_name_plural = 'Рабочие станции'
        ordering = ["employee", "name", "workplace"]

class Monitor (ModelMixin, models.Model):
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
        Manufacturer,
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
        return reverse('workstation:monitor-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Монитор'
        verbose_name_plural = 'Мониторы'
        ordering = ['name']

class Ram (ModelMixin, models.Model):
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
        Manufacturer,
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
        upload_to='ram/serial/',
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
        upload_to='ram/invent/',
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
        return reverse('workstation:ram-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'RAM'
        verbose_name_plural = 'RAMs'
        ordering = ['name']

class Ssd (ModelMixin, models.Model):
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
        Manufacturer,
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
        upload_to='ssd/serial/',
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
        upload_to='ssd/invent/',
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
        return reverse('workstation:ssd-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'SSD'
        verbose_name_plural = 'SSDs'
        ordering = ['name']

class Hdd (ModelMixin, models.Model):
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
        Manufacturer,
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
        upload_to='hdd/serial/',
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
        upload_to='hdd/invent/',
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
        return reverse('workstation:hdd-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'HDD'
        verbose_name_plural = 'HDDs'
        ordering = ['name']

class KeyBoard (ModelMixin, models.Model):
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
        Manufacturer,
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
        upload_to='keyBoard/serial/',
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
        upload_to='keyBoard/invent/',
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
        return reverse('workstation:keyBoard-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Клавиатура'
        verbose_name_plural = 'Клавиатуры'
        ordering = ['name']

class Mouse (ModelMixin, models.Model):
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
        Manufacturer,
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
        upload_to='mouse/serial/',
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
        upload_to='mouse/invent/',
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
        return reverse('workstation:mouse-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Мышь'
        verbose_name_plural = 'Мышки'
        ordering = ['name']
