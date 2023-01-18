from django.db import models
from django.urls import reverse
import uuid 
from catalog.utils import ModelMixin

class Manufacturer (ModelMixin, models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=150,
        help_text="Введите наименование производителя",
        verbose_name="Производитель"
        )
    country = models.CharField(
        max_length=150,
        help_text="Введите название страны",
        verbose_name="Страна"
        )
    production = models.CharField(
        max_length=150,
        help_text="Введите страну производства",
        verbose_name="Страна производства"
        )
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('counterparty:manufacturer-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
        ordering = [ "name", ]
