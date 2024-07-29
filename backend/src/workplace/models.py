import uuid

from django.db import models
from django.urls import reverse

from core.utils import ModelMixin


class Room(ModelMixin, models.Model):
    id: models.UUIDField = models.UUIDField(
        primary_key=True, default=uuid.uuid4, db_index=True, help_text="ID"
    )
    name: models.CharField = models.CharField(
        max_length=15,
        help_text="Введите номер кабинета",
        verbose_name="Кабинет",
    )
    building: models.CharField = models.CharField(
        max_length=25,
        blank=True,
        help_text="Введите название здания",
        verbose_name="Здание",
    )
    floor: models.CharField = models.CharField(
        max_length=25,
        blank=True,
        help_text="Введите номер этажа",
        verbose_name="Этаж",
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("workplace:room-detail", args=[str(self.id)])

    class Meta:
        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинеты"
        ordering = ["name", "building"]


class Workplace(ModelMixin, models.Model):
    """
    Модель рабочего места. Используется в workstation
    """

    id: models.UUIDField = models.UUIDField(
        db_index=True, primary_key=True, default=uuid.uuid4, help_text="ID"
    )
    name: models.CharField = models.CharField(
        max_length=50,
        help_text="Введите номер рабочего места",
        verbose_name="Рабочее место",
    )
    room: models.ForeignKey = models.ForeignKey(
        "Room",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="workplace",
        help_text="Выберете номер кабинета",
        verbose_name="Номер кабинета",
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("workplace:workplace-detail", args=[str(self.id)])

    class Meta:
        verbose_name = "Рабочее место"
        verbose_name_plural = "Рабочие места"
        ordering = ["room__building", "name"]
