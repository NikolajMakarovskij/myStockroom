import uuid

from django.db import models

from core.utils import ModelMixin


class Manufacturer(ModelMixin, models.Model):
    """_Manufacturer_: _Manufacturer model_

    Returns:
         Manufacturer (Manufacturer): _returns object "Manufacturer"_
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, db_index=True, help_text="ID"
    )
    name = models.CharField(
        max_length=150,
        help_text="Введите наименование производителя",
        verbose_name="Производитель",
    )
    country = models.CharField(
        max_length=150, help_text="Введите название страны", verbose_name="Страна"
    )
    production = models.CharField(
        max_length=150,
        help_text="Введите страну производства",
        verbose_name="Страна производства",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"
        ordering = [
            "name",
        ]
        ordering = [
            "name",
        ]
