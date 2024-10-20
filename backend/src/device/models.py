import uuid

from django.db import models

from consumables.models import Accessories, Consumables
from core.utils import ModelMixin
from counterparty.models import Manufacturer
from workplace.models import Workplace


class DeviceCat(ModelMixin, models.Model):
    """
    Group model for devices
    """

    id: models.UUIDField = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text="ID"
    )
    name: models.CharField = models.CharField(
        max_length=50, help_text="Введите название", verbose_name="Название"
    )
    slug: models.SlugField = models.SlugField(
        max_length=50,
        unique=True,
        db_index=True,
        help_text="Введите URL (для работы навигациии в расходниках)",
        verbose_name="URL",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Группа устройств"
        verbose_name_plural = "Группы устройств"
        ordering = ["name"]


class Device(ModelMixin, models.Model):
    """
    Модель устройства
    """

    id: models.UUIDField = models.UUIDField(
        primary_key=True, default=uuid.uuid4, db_index=True, help_text="ID"
    )
    name: models.CharField = models.CharField(
        max_length=150, help_text="Введите название устройства", verbose_name="Название"
    )
    hostname: models.CharField = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Введите имя хоста",
        verbose_name="Имя хоста",
    )
    ip_address: models.URLField = models.URLField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Введите IP адрес",
        verbose_name="IP адрес",
    )
    login: models.CharField = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Введите логин",
        verbose_name="Логин",
    )
    pwd: models.CharField = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Введите пароль",
        verbose_name="Пароль",
    )
    categories: models.ForeignKey = models.ForeignKey(
        "DeviceCat",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Укажите группу",
        verbose_name="Группа",
    )
    manufacturer: models.ForeignKey = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Укажите производителя",
        verbose_name="Производитель",
    )
    serial: models.CharField = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Введите серийный номер",
        verbose_name="Серийный номер",
    )
    serialImg: models.ImageField = models.ImageField(
        upload_to="device/serial/",
        blank=True,
        null=True,
        help_text="прикрепите файл",
        verbose_name="Фото серийного номера",
    )
    invent: models.CharField = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Введите инвентарный номер",
        verbose_name="Инвентарный номер",
    )
    inventImg: models.ImageField = models.ImageField(
        upload_to="device/invent/",
        blank=True,
        null=True,
        help_text="прикрепите файл",
        verbose_name="Фото инвентарного номера",
    )
    description: models.TextField = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Введите описание устройства",
        verbose_name="Описание",
    )
    workplace: models.ForeignKey = models.ForeignKey(
        Workplace,
        on_delete=models.SET_NULL,
        related_name="device",
        blank=True,
        null=True,
        help_text="Укажите рабочее место",
        verbose_name="Рабочее место",
    )
    consumable: models.ManyToManyField = models.ManyToManyField(
        Consumables,
        blank=True,
        related_name="device",
        help_text="Укажите расходник",
        verbose_name="Расходник",
    )
    accessories: models.ManyToManyField = models.ManyToManyField(
        Accessories,
        blank=True,
        related_name="device",
        help_text="Укажите комплектующее",
        verbose_name="Комплектующее",
    )
    quantity: models.IntegerField = models.IntegerField(
        blank=True,
        default=0,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе",
    )
    cost: models.FloatField = models.FloatField(
        blank=True,
        default=0,
        help_text="Введите стоимость",
        verbose_name="стоимость, \u20bd",
    )
    resource: models.IntegerField = models.IntegerField(
        blank=True,
        default=0,
        help_text="Введите выработанный ресурс",
        verbose_name="Выработанный ресурс",
    )
    note: models.TextField = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        help_text="Введите примечание",
        verbose_name="Примечание",
    )

    def __str__(self):
        return self.name

    # TODO valid method to ip_address field

    class Meta:
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
