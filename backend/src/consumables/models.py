import uuid

from django.db import models
from django.urls import reverse

from core.utils import ModelMixin
from counterparty.models import Manufacturer


# Расходники
class Categories(ModelMixin, models.Model):
    """
    Модель группы для расходников.
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
        help_text="Введите URL (для работы навигации в расходниках)",
        verbose_name="URL"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('consumables:category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Группа расходников'
        verbose_name_plural = 'Группы расходников'
        ordering = ['name']


class Consumables(ModelMixin, models.Model):
    """
    Модель расходников
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        db_index=True,
        help_text="ID"
    )
    name = models.CharField(
        max_length=150,
        unique=True,
        help_text="Введите название",
        verbose_name="Название"
    )
    categories = models.ForeignKey(
        'Categories',
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
    quantity = models.IntegerField(
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

    def get_difference(self) -> int:
        quantity_all = 0
        for each in self.consumable.all():
            quantity_all += each.quantity
        difference = self.quantity - quantity_all
        return difference

    class Meta:
        verbose_name = 'Расходник'
        verbose_name_plural = 'Расходники'
        ordering = ['name', 'categories']
        permissions = [
            ('can_add_consumable_to_stock', 'Добавление на склад'),
            ('can_export_consumable', 'Экспорт'),
        ]


# Комплектующие /// accessories
class AccCat(ModelMixin, models.Model):
    """
    Модель группы для комплектующих. 
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
        help_text="Введите URL (для работы навигации в комплектующих)",
        verbose_name="URL"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('consumables:category_accessories', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Группа комплектующих'
        verbose_name_plural = 'Группы комплектующих'
        ordering = ['name']


class Accessories(ModelMixin, models.Model):
    """
    Модель комплектующих
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        db_index=True,
        help_text="ID"
    )
    name = models.CharField(
        max_length=150,
        unique=True,
        help_text="Введите название",
        verbose_name="Название"
    )
    categories = models.ForeignKey(
        'AccCat',
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
        upload_to='accessories/serial/',
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
        upload_to='accessories/invent/',
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
    quantity = models.IntegerField(
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
        return reverse('consumables:accessories-detail', args=[str(self.id)])

    def get_difference(self) -> int:
        quantity_all = 0
        for each in self.accessories.all():
            quantity_all += each.quantity
        difference = self.quantity - quantity_all
        return difference

    class Meta:
        verbose_name = 'Комплектующее'
        verbose_name_plural = 'Комплектующие'
        ordering = ['name', 'categories']
        permissions = [
            ('can_add_accessories_to_stock', 'Добавление на склад'),
            ('can_export_accessories', 'Экспорт'),
        ]

