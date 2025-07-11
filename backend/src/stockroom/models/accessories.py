import uuid

from django.db import models

from consumables.models import Accessories
from core.utils import ModelMixin


# Accessories
class StockAcc(ModelMixin, models.Model):
    """_StockAcc_:
    Expansion of the model of components for the warehouse.
    The nomenclature of components of the warehouse and the directory may differ;
    however, the quantity of each component must match

    Returns:
        StockAcc (StockAcc): The stockroom accessories model
    """

    stock_model = models.OneToOneField(
        Accessories,
        on_delete=models.CASCADE,
        primary_key=True,
        db_index=True,
        help_text="Введите название комплектующего",
        verbose_name="Комплектующие",
    )
    categories = models.ForeignKey(
        "CategoryAcc",
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
        """_StockAcc Meta_: _model settings_"""

        verbose_name = "Склад комплектующих"
        verbose_name_plural = "Склад комплектующих"
        ordering = ["rack", "shelf"]
        permissions = [
            ("remove_accessories_from_stock", "Удалить co склада"),
            ("add_accessories_to_stock", "Добавить на склада"),
            ("add_accessories_to_device", "Установить в устройство"),
            ("can_export_device", "Экспорт"),
        ]


class CategoryAcc(ModelMixin, models.Model):
    """_CategoryAcc_:
    stock_model categories

    Returns:
        CategoryAcc (CategoryAcc): _description_
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
        """_CategoryAcc __str__ _: _returns name of model_

        Returns:
            CategoryAcc__name (str): _returns name_
        """

        return self.name

    class Meta:
        """_CategoryAcc Meta_: _model settings_"""

        verbose_name = "Группа комплектующих"
        verbose_name_plural = "Группы комплектующих"
        ordering = ["name"]


class HistoryAcc(models.Model):
    """_HistoryAcc_:
    Model for storing the history of the use of accessories

    Returns:
        HistoryAcc (HistoryAcc): The stockroom model
    """

    id = models.UUIDField(
        primary_key=True, db_index=True, default=uuid.uuid4, help_text="ID"
    )
    stock_model = models.CharField(
        blank=True, default=0, max_length=150, verbose_name="Комплектующие"
    )
    stock_model_id = models.CharField(
        blank=True, default=0, max_length=50, verbose_name="ID комплектующего"
    )
    device = models.CharField(
        blank=True, null=True, max_length=150, verbose_name="Устройства"
    )
    deviceId = models.CharField(
        blank=True, null=True, max_length=50, verbose_name="ID Устройства"
    )
    categories = models.ForeignKey(
        "CategoryAcc",
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
    STATUS_CHOICES = [
        ("Приход", "Приход"),
        ("Расход", "Расход"),
        ("Удаление", "Удаление"),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="Расход",
    )
    note = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        help_text="Введите примечание",
        verbose_name="Примечание",
    )

    class Meta:
        """_HistoryAcc Meta_: _model settings_"""

        verbose_name = "История комплектующих"
        verbose_name_plural = "История комплектующих"
        ordering = ["-dateInstall", "stock_model"]
