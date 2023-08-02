import uuid

from django.db import models
from django.urls import reverse

from core.utils import ModelMixin
from device.models import Device


# Devices
class StockDev (ModelMixin, models.Model):
    """
    Extension of the device model for the warehouse.
    The nomenclature of warehouse and directory stock_model may differ,
    however, the number and placement of each device must match
    """
    stock_model = models.OneToOneField(
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
        ordering = ['stock_model__workplace__room__building', 'stock_model__workplace__room__name']


class CategoryDev(ModelMixin, models.Model):
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
    stock_model = models.CharField(
        blank=True, default=0,
        max_length=50,
        verbose_name="Устройства"
        )
    stock_model_id = models.CharField(
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
    status = models.CharField(
        blank=True, default=0,
        max_length=50,
        verbose_name="Статус"
    )

    class Meta:
        verbose_name = 'История устройств'
        verbose_name_plural = 'История устройств'
        ordering = ['-dateInstall', 'stock_model']
