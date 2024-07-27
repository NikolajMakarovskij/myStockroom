import uuid

from django.db import models
from django.urls import reverse

from core.utils import ModelMixin


class Manufacturer(ModelMixin, models.Model):
    """
    The manufacturers' model.
    """

    id: models.UUIDField = models.UUIDField(
        primary_key=True, default=uuid.uuid4, db_index=True, help_text="ID"
    )
    name: models.CharField = models.CharField(
        max_length=150,
        help_text="Введите наименование производителя",
        verbose_name="Производитель",
    )
    country: models.CharField = models.CharField(
        max_length=150, help_text="Введите название страны", verbose_name="Страна"
    )
    production: models.CharField = models.CharField(
        max_length=150,
        help_text="Введите страну производства",
        verbose_name="Страна производства",
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("counterparty:manufacturer-detail", args=[str(self.id)])

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"
        ordering = [
            "name",
        ]
