import uuid

from django.db import models

from consumables.models import Accessories, Consumables
from core.utils import ModelMixin
from counterparty.models import Manufacturer
from workplace.models import Workplace


class DeviceCat(ModelMixin, models.Model):
    """_DeviceCat_:
    Device categories model

    Returns:
        DeviceCat (DeviceCat): _description_
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID")
    name = models.CharField(
        max_length=50, help_text="Введите название", verbose_name="Название"
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        db_index=True,
        help_text="Введите URL (для работы навигациии в расходниках)",
        verbose_name="URL",
    )

    def __str__(self):
        """_DeviceCat __str__ _: _returns name of model_

        Returns:
            DeviceCat__name (str): _returns name_
        """

        return self.name

    class Meta:
        """_DeviceCat Meta_: _model settings_"""

        verbose_name = "Группа устройств"
        verbose_name_plural = "Группы устройств"
        ordering = ["name"]


class Device(ModelMixin, models.Model):
    """_Device_:
    Device model

    Returns:
        Device (Device): _description_
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, db_index=True, help_text="ID"
    )
    name = models.CharField(
        max_length=150, help_text="Введите название устройства", verbose_name="Название"
    )
    hostname = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Введите имя хоста",
        verbose_name="Имя хоста",
    )
    ip_address = models.URLField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Введите IP адрес",
        verbose_name="IP адрес",
    )
    login = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Введите логин",
        verbose_name="Логин",
    )
    pwd = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Введите пароль",
        verbose_name="Пароль",
    )
    categories = models.ForeignKey(
        "DeviceCat",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Укажите группу",
        verbose_name="Группа",
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Укажите производителя",
        verbose_name="Производитель",
    )
    serial = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Введите серийный номер",
        verbose_name="Серийный номер",
    )
    serialImg = models.ImageField(
        upload_to="device/serial/",
        blank=True,
        null=True,
        help_text="прикрепите файл",
        verbose_name="Фото серийного номера",
    )
    invent = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Введите инвентарный номер",
        verbose_name="Инвентарный номер",
    )
    inventImg = models.ImageField(
        upload_to="device/invent/",
        blank=True,
        null=True,
        help_text="прикрепите файл",
        verbose_name="Фото инвентарного номера",
    )
    description = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Введите описание устройства",
        verbose_name="Описание",
    )
    workplace = models.ForeignKey(
        Workplace,
        on_delete=models.SET_NULL,
        related_name="device",
        blank=True,
        null=True,
        help_text="Укажите рабочее место",
        verbose_name="Рабочее место",
    )
    consumable = models.ManyToManyField(
        Consumables,
        blank=True,
        related_name="device",
        help_text="Укажите расходник",
        verbose_name="Расходник",
    )
    accessories = models.ManyToManyField(
        Accessories,
        blank=True,
        related_name="device",
        help_text="Укажите комплектующее",
        verbose_name="Комплектующее",
    )
    quantity = models.IntegerField(
        blank=True,
        default=0,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе",
    )
    cost = models.FloatField(
        blank=True,
        default=0,
        help_text="Введите стоимость",
        verbose_name="стоимость, \u20bd",
    )
    resource = models.IntegerField(
        blank=True,
        default=0,
        help_text="Введите выработанный ресурс",
        verbose_name="Выработанный ресурс",
    )
    note = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        help_text="Введите примечание",
        verbose_name="Примечание",
    )

    def __str__(self):
        """_Device __str__ _: _returns name of model_

        Returns:
            Device__name (str): _returns name_
        """

        return self.name

    class Meta:
        """_Device Meta_: _model settings_"""

        verbose_name = "Устройства"
        verbose_name_plural = "Устройства"
        ordering = ["workplace__room__building", "workplace__name"]
        permissions = [
            ("can_move_device", "Перемещение"),
            ("can_add_stock", "Добавление на склад"),
            ("can_install_consumable", "Установка расходника"),
            ("can_install_accessories", "Установка комплектующего"),
            ("can_add_history", "Добавление истории"),
            ("can_export", "Экспорт"),
        ]
