import uuid

from django.db import models
from django.urls import reverse

from core.utils import ModelMixin


class Room(ModelMixin, models.Model):
    """_Room_:
    Room model

    Returns:
       Room (Room): _description_
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, db_index=True, help_text="ID"
    )
    name = models.CharField(
        max_length=15,
        help_text="Введите номер кабинета",
        verbose_name="Кабинет",
    )
    building = models.CharField(
        max_length=25,
        blank=True,
        help_text="Введите название здания",
        verbose_name="Здание",
    )
    floor = models.CharField(
        max_length=25,
        blank=True,
        help_text="Введите номер этажа",
        verbose_name="Этаж",
    )

    def __str__(self):
        """_Room __str__ _: _returns name of model_

        Returns:
            Room__name (str): _returns name_
        """
        return self.name

    def get_absolute_url(self):
        """_Room url_

        Returns:
            Room__id (str): _returns url by id_

        Other parameters:
            args (str): self.id
        """
        return reverse("workplace:room-detail", args=[str(self.id)])

    class Meta:
        """_Room Meta_: _model settings_"""

        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинеты"
        ordering = ["name", "building"]


class Workplace(ModelMixin, models.Model):
    """_Workplace_:
    Workplace model

    Returns:
       Workplace (Workplace): _description_
    """

    id = models.UUIDField(
        db_index=True, primary_key=True, default=uuid.uuid4, help_text="ID"
    )
    name = models.CharField(
        max_length=50,
        help_text="Введите номер рабочего места",
        verbose_name="Рабочее место",
    )
    room = models.ForeignKey(
        "Room",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="workplace",
        help_text="Выберете номер кабинета",
        verbose_name="Номер кабинета",
    )

    def __str__(self):
        """_Workplace __str__ _: _returns name of model_

        Returns:
            Workplace__name (str): _returns name_
        """
        return self.name

    def get_absolute_url(self):
        """_Workplace url_

        Returns:
            Workplace__id (str): _returns url by id_

        Other parameters:
            args (str): self.id
        """
        return reverse("workplace:workplace-detail", args=[str(self.id)])

    class Meta:
        """_Workplace Meta_: _model settings_"""

        verbose_name = "Рабочее место"
        verbose_name_plural = "Рабочие места"
        ordering = ["room__building", "name"]
