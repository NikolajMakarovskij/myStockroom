from django.db import models
from django.urls import reverse
from counterparty.models import Manufacturer
from catalog.utils import ModelMixin
import uuid 

#Расходники
class Categories(ModelMixin, models.Model):
    """
    Модель группы для расходников. Связи один ко многим с моделями printer, ups, signature
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
        return reverse('consumables:category',kwargs={'category_slug': self.slug})


    class Meta:
        verbose_name = 'Группа расходников'
        verbose_name_plural = 'Группы расходников'
        ordering = ['name']

class Consumables (ModelMixin, models.Model):
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
        max_length=50,
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
    buhCode = models.CharField(
        max_length=50,
        help_text="Введите код по бухгалтерии",
        verbose_name="Код в бухгалтерии"
        )
    score = models.IntegerField(
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

    class Meta:
        verbose_name = 'Расходник'
        verbose_name_plural = 'Расходники'
        ordering = ['name', 'categories']


