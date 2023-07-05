from django.db import models
from .utils import ModelMixin
import uuid


class References(ModelMixin, models.Model):
    """
    Модель справочников
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
    linkname = models.CharField(
        max_length=50,
        help_text="Введите ссылку",
        verbose_name="Ссылка"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Справочники'
        verbose_name_plural = 'Справочники'
        ordering = ["name"]
