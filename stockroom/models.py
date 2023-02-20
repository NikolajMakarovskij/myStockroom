import uuid
from django.db import models
from django.urls import reverse
from consumables.models import Consumables
from catalog.utils import ModelMixin

class Stockroom (ModelMixin, models.Model):
    consumables = models.OneToOneField(
        Consumables,
        on_delete = models.CASCADE,
        primary_key = True,
        help_text="Введите название расходника",
        verbose_name="Расходники"
        )
    categories = models.ForeignKey(
        'Categories',
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
    def __str__(self):
        return self.consumables

    def get_absolute_url(self):
        return reverse('stockroom:stock-detail', args=[str(self.consumables)])

    class Meta:
        verbose_name = 'Кассета'
        verbose_name_plural = 'Кассеты'
        ordering = ['consumables']

class Categories(ModelMixin, models.Model):
    """
    Модель группы для расходников
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
        return reverse('stockroom:category',kwargs={'category_slug': self.slug})


    class Meta:
        verbose_name = 'Группа расходников'
        verbose_name_plural = 'Группы расходников'
        ordering = ['name']

#class History(models.Model):
#        id = models.UUIDField(
#        primary_key=True,
#        default=uuid.uuid4,
#        help_text="ID"
#        )