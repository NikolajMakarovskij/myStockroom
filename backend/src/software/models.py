import uuid

from django.db import models

from core.utils import ModelMixin
from counterparty.models import Manufacturer


class Software(ModelMixin, models.Model):
    """
    Модель софта
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, db_index=True, help_text="ID"
    )
    name = models.CharField(
        max_length=50,
        help_text="Введите название ПО",
        verbose_name="Программное обеспечение",
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Укажите производителя",
        verbose_name="Производитель",
    )
    version = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Укажите версию",
        verbose_name="Версия",
    )
    bitDepth = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Укажите разрядность",
        verbose_name="разрядность",
    )
    licenseKeyText = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Введите лицензионный ключ",
        verbose_name="Введите ключ",
    )
    licenseKeyImg = models.ImageField(
        upload_to="software/soft/",
        blank=True,
        null=True,
        help_text="прикрепите файл",
        verbose_name="Фото ключа",
    )
    licenseKeyFile = models.FileField(
        upload_to="software/soft/",
        blank=True,
        null=True,
        help_text="прикрепите файл",
        verbose_name="Файл лицензии",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Программное обеспечение"
        verbose_name_plural = "Программное обеспечение"
        ordering = [
            "name",
        ]


class Os(ModelMixin, models.Model):
    """
    Модель ОС
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, db_index=True, help_text="ID"
    )
    name = models.CharField(
        max_length=50,
        help_text="Введите название ОС",
        verbose_name="Операционная система",
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Укажите производителя",
        verbose_name="Производитель",
    )
    version = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Укажите версию",
        verbose_name="Версия",
    )
    bitDepth = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Укажите разрядность",
        verbose_name="разрядность",
    )
    licenseKeyText = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Введите лицензионный ключ",
        verbose_name="Лицензионный ключ",
    )
    licenseKeyImg = models.ImageField(
        upload_to="software/OS/",
        blank=True,
        null=True,
        help_text="прикрепите файл",
        verbose_name="Фото ключа",
    )
    licenseKeyFile = models.FileField(
        upload_to="software/OS/",
        blank=True,
        null=True,
        help_text="прикрепите файл",
        verbose_name="Файл лицензии",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Операционная система"
        verbose_name_plural = "Операционные системы"
        ordering = ["name"]
