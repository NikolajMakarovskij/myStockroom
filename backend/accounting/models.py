import uuid

from django.db import models
from django.urls import reverse

from consumables.models import Consumables, Accessories
from core.utils import ModelMixin


class Categories(ModelMixin, models.Model):
    """
        Модель группы для расходников на балансе в бухгалтерии.
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
        return reverse('accounting:categories-detail', args=[str(self.id)])

    def get_slug_url(self):
        return reverse('accounting:category', kwargs={'category_slug': self.slug})

    def get_update_url(self):
        return reverse('accounting:categories-update', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('accounting:categories-delete', args=[str(self.id)])

    class Meta:
        verbose_name = 'Группа расходников'
        verbose_name_plural = 'Группы расходников'
        ordering = ['name']


class Accounting(ModelMixin, models.Model):
    """
    Accounting model
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        db_index=True,
        help_text="ID"
    )
    name = models.CharField(
        max_length=500,
        help_text="Введите название",
        verbose_name="Название"
    )
    account = models.IntegerField(
        blank=True, null=True,
        help_text="Введите счет",
        verbose_name="Счет"
    )
    categories = models.ForeignKey(
        'Categories',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите группу",
        verbose_name="Группа"
    )
    consumable = models.ForeignKey(
        Consumables,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='consumable',
        help_text="Укажите расходник",
        verbose_name="Расходник"
    )
    accessories = models.ForeignKey(
        Accessories,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='accessories',
        help_text="Укажите комплектующее",
        verbose_name="Комплектующее"
    )
    code = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите код по бухгалтерии",
        verbose_name="Код в бухгалтерии"
    )
    quantity = models.IntegerField(
        blank=True, default=0,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе",
    )
    cost = models.FloatField(
        blank=True, default=0,
        help_text="Введите стоимость за 1 ед.",
        verbose_name="Стоимость",
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
        return reverse('accounting:accounting-detail', args=[str(self.id)])

    def get_cost_all(self):
        cost_all = self.cost * self.quantity
        return float("{:.2f}".format(cost_all))

    class Meta:
        verbose_name = 'На балансе'
        verbose_name_plural = 'На балансе'
        ordering = ['-account', 'name']
