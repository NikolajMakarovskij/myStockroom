import uuid

from django.db import models
from django.urls import reverse

from core.utils import ModelMixin
from counterparty.models import Manufacturer


class Software(ModelMixin, models.Model):
    """_Software_:
    Software model

    Returns:
        Software (Software): _description_
    """

    id: models.UUIDField = models.UUIDField(
        primary_key=True, default=uuid.uuid4, db_index=True, help_text="ID"
    )
    name: models.CharField = models.CharField(
        max_length=50,
        help_text="Введите название ПО",
        verbose_name="Программное обеспечение",
    )
    manufacturer: models.ForeignKey = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Укажите производителя",
        verbose_name="Производитель",
    )
    version: models.CharField = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Укажите версию",
        verbose_name="Версия",
    )
    bitDepth: models.CharField = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Укажите разрядность",
        verbose_name="разрядность",
    )
    licenseKeyText: models.CharField = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Введите лицензионный ключ",
        verbose_name="Введите ключ",
    )
    licenseKeyImg: models.ImageField = models.ImageField(
        upload_to="software/soft/",
        blank=True,
        null=True,
        help_text="прикрепите файл",
        verbose_name="Фото ключа",
    )
    licenseKeyFile: models.FileField = models.FileField(
        upload_to="software/soft/",
        blank=True,
        null=True,
        help_text="прикрепите файл",
        verbose_name="Файл лицензии",
    )

    def __str__(self):
        """_Software __str__ _: _returns name of model_

        Returns:
            Software__name (str): _returns name_
        """
        return self.name

    def get_absolute_url(self):
        """_Software url_

        Returns:
            Software__id (str): _returns url by id_

        Other parameters:
            args (str): self.id
        """
        return reverse("software:software-detail", args=[str(self.id)])

    class Meta:
        """_Software Meta_: _model settings_"""

        verbose_name = "Программное обеспечение"
        verbose_name_plural = "Программное обеспечение"
        ordering = [
            "name",
        ]


class Os(ModelMixin, models.Model):
    """_Os_:
    OS model

    Returns:
        OS (OS): _description_
    """

    id: models.UUIDField = models.UUIDField(
        primary_key=True, default=uuid.uuid4, db_index=True, help_text="ID"
    )
    name: models.CharField = models.CharField(
        max_length=50,
        help_text="Введите название ОС",
        verbose_name="Операционная система",
    )
    manufacturer: models.ForeignKey = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Укажите производителя",
        verbose_name="Производитель",
    )
    version: models.CharField = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Укажите версию",
        verbose_name="Версия",
    )
    bitDepth: models.CharField = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Укажите разрядность",
        verbose_name="разрядность",
    )
    licenseKeyText: models.CharField = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Введите лицензионный ключ",
        verbose_name="Лицензионный ключ",
    )
    licenseKeyImg: models.ImageField = models.ImageField(
        upload_to="software/OS/",
        blank=True,
        null=True,
        help_text="прикрепите файл",
        verbose_name="Фото ключа",
    )
    licenseKeyFile: models.FileField = models.FileField(
        upload_to="software/OS/",
        blank=True,
        null=True,
        help_text="прикрепите файл",
        verbose_name="Файл лицензии",
    )

    def __str__(self):
        """_OS __str__ _: _returns name of model_

        Returns:
            OS__name (str): _returns name_
        """
        return self.name

    def get_absolute_url(self):
        """_OS url_

        Returns:
            OS__id (str): _returns url by id_

        Other parameters:
            args (str): self.id
        """
        return reverse("software:OS-detail", args=[str(self.id)])

    class Meta:
        """_OS Meta_: _model settings_"""

        verbose_name = "Операционная система"
        verbose_name_plural = "Операционные системы"
        ordering = ["name"]
