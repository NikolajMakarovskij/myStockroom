from django.db import models
from django.urls import reverse
from counterparty.models import Manufacturer
from employee.models import Employee
from catalog.utils import ModelMixin
import uuid 
from django.template.defaultfilters import slugify

#Расходники
class Categories(ModelMixin, models.Model):
    """
    Модель группы для расходников
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
        return reverse('consumables:category',kwargs={'category_slug': self.slug})


    class Meta:
        verbose_name = 'Группа расходников'
        verbose_name_plural = 'Группы расходников'
        ordering = ['name']

class Consumables (ModelMixin, models.Model):
    """
    Модель расходников
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
    categories = models.ForeignKey(
        'Categories',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите группу",
        verbose_name="группа"
        )
    serial = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите серийный номер",
        verbose_name="Серийный номер"
        )
    serialImg = models.ImageField(
        upload_to='сonsumables/serial/',
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
        upload_to='сonsumables/invent/',
        blank=True, null=True,
        help_text="Прикрепите файл",
        verbose_name="Фото инвентарного номера"
        )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите производителя",
        verbose_name="Производитель"
        )
    buhCode = models.CharField(
        max_length=50,
        help_text="Введите код по бухгалтерии",
        verbose_name="Код в бухгалтерии"
        )
    score = models.IntegerField(
        blank=True, default=0,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе",
        )
    description = models.TextField(
        max_length=1000,
        blank=True, null=True,
        help_text="Введите описание",
        verbose_name="Описание"
        )
    note = models.TextField(
        max_length=1000,
        blank=True, null=True,
        help_text="Введите примечание",
        verbose_name="Примечание"
        )
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('consumables:consumables-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Расходник'
        verbose_name_plural = 'Расходники'
        ordering = ['name', 'categories']


#Картридж
class Cartridge (ModelMixin, models.Model):
    """
    Модель картриджей
    """
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
    buhCode = models.CharField(
        max_length=50,
        help_text="Введите код по бухгалтерии",
        verbose_name="Код в бухгалтерии"
        )
    score = models.IntegerField(
        blank=True, default=0,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе",
        )
    rack = models.IntegerField(
        blank=True, default=0,
        help_text="Укажите стеллаж",
        verbose_name="№ стеллажа",
        )
    shelf = models.IntegerField(
        blank=True, default=0,
        help_text="Укажите полку",
        verbose_name="№ полки",
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('consumables:cartridge-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Картридж'
        verbose_name_plural = 'Картриджы'
        ordering = ['name']
        

#Фотовал
class Fotoval (ModelMixin, models.Model):
    """
    Модель фотовалов
    """
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
    buhCode = models.CharField(
        max_length=50,
        help_text="Введите код по бухгалтерии",
        verbose_name="Код в бухгалтерии"
        )
    mileage = models.IntegerField(
        blank=True, null=True,
        help_text="Введите пробег",
        verbose_name="Пробег"
        )
    score = models.IntegerField(
        blank=True, default=0,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе"
        )
    rack = models.IntegerField(
        blank=True, default=0,
        help_text="Укажите стеллаж",
        verbose_name="№ стеллажа",
        )
    shelf = models.IntegerField(
        blank=True, default=0,
        help_text="Укажите полку",
        verbose_name="№ полки",
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('consumables:fotoval-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Фотовал'
        verbose_name_plural = 'Фотовалы'
        ordering = ['name']

#Тонер
class Toner (ModelMixin, models.Model):
    """
    Модель тонеров
    """
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
    buhCode = models.CharField(
        max_length=50,
        help_text="Введите код по бухгалтерии",
        verbose_name="Код в бухгалтерии"
        )
    score = models.IntegerField(
        blank=True, default=0,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе"
        )
    rack = models.IntegerField(
        blank=True, default=0,
        help_text="Укажите стеллаж",
        verbose_name="№ стеллажа",
        )
    shelf = models.IntegerField(
        blank=True, default=0,
        help_text="Укажите полку",
        verbose_name="№ полки",
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('consumables:toner-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Тонер'
        verbose_name_plural = 'Тонеры'
        ordering = ['name']

#Аккумулятор
class Accumulator (ModelMixin, models.Model):
    """
    Модель аккумуляторов
    """
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
    power = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите мощность",
        verbose_name="Мощность"
        )
    voltage = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите напряжение",
        verbose_name="Напряжение"
        )
    current = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите ток",
        verbose_name="Ток"
        )
    score = models.IntegerField(
        blank=True, default=0,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе"
        )
    rack = models.IntegerField(
        blank=True, default=0,
        help_text="Укажите стеллаж",
        verbose_name="№ стеллажа",
        )
    shelf = models.IntegerField(
        blank=True, default=0,
        help_text="Укажите полку",
        verbose_name="№ полки",
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('consumables:accumulator-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Аккумулятор'
        verbose_name_plural = 'Аккумуляторы'
        ordering = ['name']   

#Накопитель
class Storage(ModelMixin, models.Model):
    """
    Модель накопителей
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
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите производителя",
        verbose_name="Производитель"
        )
    modelStorage = models.CharField(
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
        upload_to='storage/serial/',
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
        upload_to='storage/invent/',
        blank=True, null=True,
        help_text="Прикрепите файл",
        verbose_name="Фото инвентарного номера"
        )
    plug = models.TextField(
        max_length=20,
        blank=True, null=True,
        help_text="Укажите тип подключения",
        verbose_name="Тип подключения"
        )
    typeMemory = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Укажите тип памяти",
        verbose_name="Тип памяти"
        )
    volumeMemory = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Укажите объем памяти",
        verbose_name="Объем памяти"
        )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите сотрудника",
        verbose_name="Сотрудник"
        )
    score = models.IntegerField(
        blank=True, default=0,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе"
        )
    rack = models.IntegerField(
        blank=True, default=0,
        help_text="Укажите стеллаж",
        verbose_name="№ стеллажа",
        )
    shelf = models.IntegerField(
        blank=True, default=0,
        help_text="Укажите полку",
        verbose_name="№ полки",
        )
    
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('consumables:storage-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Накопитель'
        verbose_name_plural = 'Накопители'
        ordering = ["employee", "name", ]