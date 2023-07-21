import uuid
from django.db import models
from django.urls import reverse
from device.models import Device
from consumables.models import Consumables, Accessories
from core.utils import ModelMixin


# Consumables
class Stockroom (ModelMixin, models.Model):
    """
    Expansion of the consumables model for the warehouse.
    The nomenclature of the consumables of the warehouse and the directory may differ,
    however, the quantity of each consumable must match
    """
    consumables = models.OneToOneField(
        Consumables,
        on_delete=models.CASCADE,
        primary_key=True,
        db_index=True,
        help_text="Введите название расходника",
        verbose_name="Расходники"
        )
    categories = models.ForeignKey(
        'StockCat',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите группу",
        verbose_name="группа"
        )
    dateAddToStock = models.DateField(
        null=True, blank=True,
        verbose_name="Дата поступления на склад"
        )
    dateInstall = models.DateField(
        null=True, blank=True,
        verbose_name="Дата установки"
        )
    rack = models.IntegerField(
        blank=True, null=True,
        help_text="Введите номер стеллажа",
        verbose_name="Стеллаж"
        )
    shelf = models.IntegerField(
        blank=True, null=True,
        help_text="Введите номер полки",
        verbose_name="Полка"
        )

    class Meta:
        verbose_name = 'Склад Расходников'
        verbose_name_plural = 'Склад Расходников'
        ordering = ['consumables']


class StockCat(ModelMixin, models.Model):
    """
    Group model for consumables
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
        help_text="Введите URL (для работы навигации)",
        verbose_name="URL"
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'stockroom:category',
            kwargs={'category_slug': self.slug}
            )

    class Meta:
        verbose_name = 'Группа расходников'
        verbose_name_plural = 'Группы расходников'
        ordering = ['name']


class History(models.Model):
    """
    Model for storing the history of the use of consumables
    """
    id = models.UUIDField(
        primary_key=True, db_index=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    consumable = models.CharField(
        blank=True, default=0,
        max_length=50,
        verbose_name="Расходники"
        )
    consumableId = models.CharField(
        blank=True, default=0,
        max_length=50,
        verbose_name="ID Расходникa"
        )
    device = models.CharField(
        blank=True, null=True,
        max_length=50,
        verbose_name="Устройства"
        )
    deviceId = models.CharField(
        blank=True, null=True,
        max_length=50,
        verbose_name="ID Устройства"
        )
    categories = models.ForeignKey(
        'StockCat',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите группу",
        verbose_name="группа"
        )
    score = models.IntegerField(
        blank=True, default=0,
        verbose_name="Количество",
        )
    dateInstall = models.DateField(
        null=True, blank=True,
        verbose_name="Дата установки"
        )
    user = models.CharField(
        blank=True, default=0,
        max_length=50,
        help_text="Укажите пользователя",
        verbose_name="Пользователь"
        )
    STATUS_CHOICES = [
        ('Приход', 'Приход'),
        ('Расход', 'Расход'),
        ('Удаление', 'Удаление'),
        ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Расход',
        )

    class Meta:
        verbose_name = 'История расходников'
        verbose_name_plural = 'История расходников'
        ordering = ['-dateInstall', 'consumable']


# Accessories
class StockAcc (ModelMixin, models.Model):
    """
    Expansion of the model of components for the warehouse.
    The nomenclature of components of the warehouse and the directory may differ,
    however, the quantity of each component must match
    """
    accessories = models.OneToOneField(
        Accessories,
        on_delete=models.CASCADE,
        primary_key=True,
        db_index=True,
        help_text="Введите название комплектующего",
        verbose_name="Комплектующие"
        )
    categories = models.ForeignKey(
        'CategoryAcc',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите группу",
        verbose_name="группа"
        )
    dateAddToStock = models.DateField(
        null=True, blank=True,
        verbose_name="Дата поступления на склад"
        )
    dateInstall = models.DateField(
        null=True, blank=True,
        verbose_name="Дата установки"
        )
    rack = models.IntegerField(
        blank=True, null=True,
        help_text="Введите номер стеллажа",
        verbose_name="Стеллаж"
        )
    shelf = models.IntegerField(
        blank=True, null=True,
        help_text="Введите номер полки",
        verbose_name="Полка"
        )

    class Meta:
        verbose_name = 'Склад комплектующих'
        verbose_name_plural = 'Склад комплектующих'
        ordering = ['accessories']


class CategoryAcc(ModelMixin, models.Model):
    """
    Group model for components
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
        help_text="Введите URL (для работы навигации)",
        verbose_name="URL"
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'stockroom:accessories_category',
            kwargs={'category_slug': self.slug}
            )

    class Meta:
        verbose_name = 'Группа комплектующих'
        verbose_name_plural = 'Группы комплектующих'
        ordering = ['name']


class HistoryAcc(models.Model):
    """
    Model for storing the history of the use of components
    """
    id = models.UUIDField(
        primary_key=True, db_index=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    accessories = models.CharField(
        blank=True, default=0,
        max_length=50,
        verbose_name="Комплектующие"
        )
    accessoriesId = models.CharField(
        blank=True, default=0,
        max_length=50,
        verbose_name="ID комплектующего"
        )
    device = models.CharField(
        blank=True, null=True,
        max_length=50,
        verbose_name="Устройства"
        )
    deviceId = models.CharField(
        blank=True, null=True,
        max_length=50,
        verbose_name="ID Устройства"
        )
    categories = models.ForeignKey(
        'CategoryAcc',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите группу",
        verbose_name="группа"
        )
    score = models.IntegerField(
        blank=True, default=0,
        verbose_name="Количество",
        )
    dateInstall = models.DateField(
        null=True, blank=True,
        verbose_name="Дата установки"
        )
    user = models.CharField(
        blank=True, default=0,
        max_length=50,
        help_text="Укажите пользователя",
        verbose_name="Пользователь"
        )
    STATUS_CHOICES = [
        ('Приход', 'Приход'),
        ('Расход', 'Расход'),
        ('Удаление', 'Удаление'),
        ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Расход',
    )

    class Meta:
        verbose_name = 'История комплектующих'
        verbose_name_plural = 'История комплектующих'
        ordering = ['-dateInstall', 'accessories']


# Devices
class StockDev (ModelMixin, models.Model):
    """
    Extension of the device model for the warehouse.
    The nomenclature of warehouse and directory devices may differ,
    however, the number and placement of each device must match
    """
    devices = models.OneToOneField(
        Device,
        on_delete=models.CASCADE,
        primary_key=True,
        db_index=True,
        help_text="Введите название устройства",
        verbose_name="Устройство"
        )
    categories = models.ForeignKey(
        'CategoryDev',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите группу",
        verbose_name="группа"
        )
    dateAddToStock = models.DateField(
        null=True, blank=True,
        verbose_name="Дата поступления на склад"
        )
    dateInstall = models.DateField(
        null=True, blank=True,
        verbose_name="Дата установки"
        )
    rack = models.IntegerField(
        blank=True, null=True,
        help_text="Введите номер стеллажа",
        verbose_name="Стеллаж"
        )
    shelf = models.IntegerField(
        blank=True, null=True,
        help_text="Введите номер полки",
        verbose_name="Полка"
        )

    class Meta:
        verbose_name = 'Склад устройств'
        verbose_name_plural = 'Склад устройств'
        ordering = ['devices']


class CategoryDev(ModelMixin, models.Model):
    """
    Group model for devices
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
        help_text="Введите URL (для работы навигации)",
        verbose_name="URL"
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'stockroom:devices_category',
            kwargs={'category_slug': self.slug}
            )

    class Meta:
        verbose_name = 'Группа устройств'
        verbose_name_plural = 'Группы устройств'
        ordering = ['name']


class HistoryDev(models.Model):
    """
    Model for storing device usage history
    """
    id = models.UUIDField(
        primary_key=True, db_index=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    devices = models.CharField(
        blank=True, default=0,
        max_length=50,
        verbose_name="Устройства"
        )
    devicesId = models.CharField(
        blank=True, default=0,
        max_length=50,
        verbose_name="ID устройства"
        )
    categories = models.ForeignKey(
        'CategoryDev',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите группу",
        verbose_name="группа"
        )
    score = models.IntegerField(
        blank=True, default=0,
        verbose_name="Количество",
        )
    dateInstall = models.DateField(
        null=True, blank=True,
        verbose_name="Дата установки"
        )
    user = models.CharField(
        blank=True, default=0,
        max_length=50,
        help_text="Укажите пользователя",
        verbose_name="Пользователь"
        )
    status = models.CharField(
        blank=True, default=0,
        max_length=50,
        verbose_name="Статус"
    )

    class Meta:
        verbose_name = 'История устройств'
        verbose_name_plural = 'История устройств'
        ordering = ['-dateInstall', 'devices']
