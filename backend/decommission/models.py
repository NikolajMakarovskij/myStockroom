import uuid
from django.db import models
from django.urls import reverse
from device.models import Device
from core.utils import ModelMixin


# Decommission
class Decommission (ModelMixin, models.Model):
    """
    Extension of the device model for the decommission.
    The nomenclature of warehouse and decommision and directory devices may differ,
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
        ordering = ['devices']


class CategoryDec(ModelMixin, models.Model):
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
            'decommission:decom_category',
            kwargs={'category_slug': self.slug}
            )

    class Meta:
        verbose_name = 'Группа списания устройств'
        verbose_name_plural = 'Группы списания устройств'
        ordering = ['name']


class HistoryDec(models.Model):
    """
    Model for decommissing device usage history
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
        'CategoryDec',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите группу",
        verbose_name="группа"
        )
    score = models.IntegerField(
        blank=True, default=0,
        verbose_name="Количество",
        )
    date = models.DateField(
        null=True, blank=True,
        verbose_name="Дата списания"
        )
    user = models.CharField(
        blank=True, default=0,
        max_length=50,
        help_text="Укажите пользователя",
        verbose_name="Пользователь"
        )

    class Meta:
        verbose_name = 'История списания'
        verbose_name_plural = 'История списания'
        ordering = ['-date', 'devices']


# Disposal
class Disposal(ModelMixin, models.Model):
    """
    Extension of the device model for the disposal.
    The nomenclature of warehouse and disposal and directory devices may differ,
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
        ordering = ['devices']


class CategoryDis(ModelMixin, models.Model):
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
            'decommission:disp_category',
            kwargs={'category_slug': self.slug}
            )

    class Meta:
        verbose_name = 'Группа утилизации устройств'
        verbose_name_plural = 'Группы утилизации устройств'
        ordering = ['name']


class HistoryDis(models.Model):
    """
    Model for disposal device usage history
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
    user = models.CharField(
        blank=True, default=0,
        max_length=50,
        help_text="Укажите пользователя",
        verbose_name="Пользователь"
        )

    class Meta:
        verbose_name = 'История утилизации'
        verbose_name_plural = 'История утилизации'
        ordering = ['-date', 'devices']
