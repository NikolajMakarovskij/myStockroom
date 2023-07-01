from django.db import models
from django.urls import reverse
from workplace.models import Workplace
from consumables.models import Consumables, Accessories
from counterparty.models import Manufacturer
from catalog.utils import ModelMixin
import uuid 


class Device_cat(ModelMixin, models.Model):
    """
    Модель группы для устройств
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
        help_text="Введите URL (для работы навигациии в расходниках)",
        verbose_name="URL"
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('device:category',kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Группа устройств'
        verbose_name_plural = 'Группы устройств'
        ordering = ['name']


class Device(ModelMixin, models.Model):
    """
    Модель устройства
    """
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4,
        db_index=True,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите название устройства",
        verbose_name="Название"
        )
    categories = models.ForeignKey(
        'Device_cat',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите группу",
        verbose_name="Группа"
        )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите производителя",
        verbose_name="Производитель"
        )
    serial = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите серийный номер",
        verbose_name="Серийный номер"
        )
    serialImg = models.ImageField(
        upload_to='device/serial/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Фото серийного номера"
        )
    invent = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите инвентарный номер",
        verbose_name="Инвентарный номер"
        )
    inventImg = models.ImageField(
        upload_to='device/invent/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Фото инвентарного номера"
        )
    description = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите описание устройства",
        verbose_name="Описание"
        )
    workplace = models.ForeignKey(
        Workplace,
        on_delete=models.SET_NULL,
        related_name='device',
        blank=True, null=True,
        help_text="Укажите рабочее место",
        verbose_name="Рабочее место"
        )
    consumable = models.ForeignKey(
        Consumables, 
        blank=True, null=True,
        on_delete=models.CASCADE,
        related_name='device',
        help_text="Укажите расходник",
        verbose_name="Расходник"
        )
    accessories = models.ForeignKey(
        Accessories, 
        blank=True, null=True,
        on_delete=models.CASCADE,
        related_name='device',
        help_text="Укажите комплектующее",
        verbose_name="Комплектующее"
        )
    score = models.IntegerField(
        blank=True, default=0,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе"
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
        return reverse('device:device-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Устройства'
        verbose_name_plural = 'Устройства'
        ordering = ["name"]
