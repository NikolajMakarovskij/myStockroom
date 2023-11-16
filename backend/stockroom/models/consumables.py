import uuid

from django.db import models
from django.urls import reverse

from consumables.models import Consumables
from core.utils import ModelMixin


# Consumables
class Stockroom (ModelMixin, models.Model):
    """
    Expansion of the stock_model model for the warehouse.
    The nomenclature of the stock_model of the warehouse and the directory may differ,
    however, the quantity of each stock_model must match
    """
    stock_model = models.OneToOneField(
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
        ordering = ['rack', 'shelf']
        permissions = [
            ('remove_consumables_from_stock', 'Удалить co склада'),
            ('add_consumables_to_stock', 'Добавить на склада'),
            ('add_consumables_to_device', 'Установить в устройство'),
            ('can_export_device', 'Экспорт'),
        ]


class StockCat(ModelMixin, models.Model):
    """
    Group model for stock_model
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
    Model for storing the history of the use of stock_model
    """
    id = models.UUIDField(
        primary_key=True, db_index=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    stock_model = models.CharField(
        blank=True, default=0,
        max_length=150,
        verbose_name="Расходники"
        )
    stock_model_id = models.CharField(
        blank=True, default=0,
        max_length=50,
        verbose_name="ID Расходникa"
        )
    device = models.CharField(
        blank=True, null=True,
        max_length=150,
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
    quantity = models.IntegerField(
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
    note = models.TextField(
        max_length=1000,
        blank=True, null=True,
        help_text="Введите примечание",
        verbose_name="Примечание"
    )

    class Meta:
        verbose_name = 'История расходников'
        verbose_name_plural = 'История расходников'
        ordering = ['-dateInstall', 'stock_model']
