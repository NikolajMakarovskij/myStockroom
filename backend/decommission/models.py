import uuid
from django.db import models
from django.urls import reverse
from device.models import Device
from core.utils import ModelMixin


# Decommission
class Decommission (ModelMixin, models.Model):
    """
    Extension of the device model for the decommission.
    The nomenclature of warehouse and decommission and directory device may differ,
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
        'CategoryDec',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите группу",
        verbose_name="группа"
        )
    date = models.DateField(
        null=True, blank=True,
        verbose_name="Дата списания"
        )

    class Meta:
        verbose_name = 'Списание устройств'
        verbose_name_plural = 'Списание устройств'
        ordering = ['stock_model']
        permissions = [
            ('add_to_decommission', 'Отправить на списание'),
            ('remove_from_decommission', 'Удалить из списания'),
            ('can_export_device', 'Экспорт устройств'),
        ]


class CategoryDec(ModelMixin, models.Model):
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
            'decommission:decom_category',
            kwargs={'category_slug': self.slug}
            )

    class Meta:
        verbose_name = 'Группа списания устройств'
        verbose_name_plural = 'Группы списания устройств'
        ordering = ['name']


# Disposal
class Disposal(ModelMixin, models.Model):
    """
    Extension of the device model for the disposal.
    The nomenclature of warehouse and disposal and directory stock_model may differ,
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
        'CategoryDis',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите группу",
        verbose_name="группа"
        )
    date = models.DateField(
        null=True, blank=True,
        verbose_name="Дата утилизации"
        )

    class Meta:
        verbose_name = 'Утилизация устройств'
        verbose_name_plural = 'Утилизация устройств'
        ordering = ['stock_model']


class CategoryDis(ModelMixin, models.Model):
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
            'decommission:disp_category',
            kwargs={'category_slug': self.slug}
            )

    class Meta:
        verbose_name = 'Группа утилизации устройств'
        verbose_name_plural = 'Группы утилизации устройств'
        ordering = ['name']
        permissions = [
            ('add_to_disposal', 'Отправить на утилизацию'),
            ('remove_from_disposal', 'Удалить из утилизации'),
        ]
