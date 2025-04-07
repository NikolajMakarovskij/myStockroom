import uuid

from django.db import models
from django.urls import reverse

from core.utils import ModelMixin
from device.models import Device


# Devices
class StockDev(ModelMixin, models.Model):
    """_StockDev_:
    Extension of the device model for the warehouse.
    The nomenclature of warehouse and directory stock_model may differ;
    however, the number and placement of each device must match

    Returns:
        StockDev (StockDev): The stockroom device model
    """

    stock_model = models.OneToOneField(
        Device,
        on_delete=models.CASCADE,
        primary_key=True,
        db_index=True,
        help_text="Введите название устройства",
        verbose_name="Устройство",
    )
    categories = models.ForeignKey(
        "CategoryDev",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Укажите группу",
        verbose_name="группа",
    )
    dateAddToStock = models.DateField(
        null=True, blank=True, verbose_name="Дата поступления на склад"
    )
    dateInstall = models.DateField(null=True, blank=True, verbose_name="Дата установки")
    rack = models.IntegerField(
        blank=True,
        null=True,
        help_text="Введите номер стеллажа",
        verbose_name="Стеллаж",
    )
    shelf = models.IntegerField(
        blank=True, null=True, help_text="Введите номер полки", verbose_name="Полка"
    )

    class Meta:
        """_StockDev_: _model settings_"""

        verbose_name = "Склад устройств"
        verbose_name_plural = "Склад устройств"
        ordering = [
            "stock_model__workplace__room__building",
            "stock_model__workplace__name",
        ]
        permissions = [
            ("remove_device_from_stock", "Удалить co склада"),
            ("add_device_to_stock", "Добавить на склада"),
            ("move_device", "Переместить устройство"),
            ("add_history_to_device", "Добавить историю"),
            ("can_export_device", "Экспорт устройств"),
        ]


class CategoryDev(ModelMixin, models.Model):
    """_CategoryDev_:
    stockroom categories for device

    Returns:
        CategoryDev (CategoryDev): _description_
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID")
    name = models.CharField(
        max_length=50, help_text="Введите название", verbose_name="Название"
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        db_index=True,
        help_text="Введите URL (для работы навигации)",
        verbose_name="URL",
    )

    def __str__(self):
        """_CategoryDev __str__ _: _returns name of model_

        Returns:
            CategoryDev__name (str): _returns name_
        """
        return self.name

    def get_absolute_url(self):
        """_CategoryDev get self url_

        Returns:
            CategoryDev__slug (str): _returns url by slug_

        Other parameters:
            kwargs (str): self.slug
        """
        return reverse(
            "stockroom:devices_category", kwargs={"category_slug": self.slug}
        )

    class Meta:
        """_StockCat Meta_: _model settings_"""

        verbose_name = "Группа устройств"
        verbose_name_plural = "Группы устройств"
        ordering = ["name"]


class HistoryDev(models.Model):
    """_HistoryDev_:
    Model for storing the history of the use of device

    Returns:
        HistoryDev (HistoryDev): The stockroom model
    """

    id = models.UUIDField(
        primary_key=True, db_index=True, default=uuid.uuid4, help_text="ID"
    )
    stock_model = models.CharField(
        blank=True, default=0, max_length=150, verbose_name="Устройства"
    )
    stock_model_id = models.CharField(
        blank=True, default=0, max_length=50, verbose_name="ID устройства"
    )
    categories = models.ForeignKey(
        "CategoryDev",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Укажите группу",
        verbose_name="группа",
    )
    quantity = models.IntegerField(
        blank=True,
        default=0,
        verbose_name="Количество",
    )
    dateInstall = models.DateField(null=True, blank=True, verbose_name="Дата установки")
    user = models.CharField(
        blank=True,
        default=0,
        max_length=50,
        help_text="Укажите пользователя",
        verbose_name="Пользователь",
    )
    status = models.CharField(
        blank=True, default=0, max_length=50, verbose_name="Статус"
    )
    note = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        help_text="Введите примечание",
        verbose_name="Примечание",
    )

    class Meta:
        """_HistoryDev Meta_: _model settings_"""

        verbose_name = "История устройств"
        verbose_name_plural = "История устройств"
        ordering = ["-dateInstall", "stock_model"]
