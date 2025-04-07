import uuid

from django.db import models
from django.urls import reverse

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
        """_Manufacturer __str__ _: _returns name of model_

        Returns:
            Manufacturer__name (str): _returns name_
        """
        return self.name

    def get_absolute_url(self):
        """_Manufacturer get self url_

        Returns:
            Manufacturer__id (str): _returns url by id_

        Other parameters:
            args (str): self.id
        """
        return reverse("counterparty:manufacturer-detail", args=[str(self.id)])

    class Meta:
        """_Manufacturer Meta_: _model settings_"""

        verbose_name = "Производитель"
        verbose_name_plural = "Производители"
        ordering = [
            "name",
        ]
