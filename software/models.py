from django.db import models
from counterparty.models import Manufacturer
from django.urls import reverse
import uuid 
from catalog.utils import ModelMixin

class Software (ModelMixin, models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите название ПО",
        verbose_name="Програмное обеспечение"
        )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите производителя",
        verbose_name="Производитель"
        )
    version = models.CharField(
        max_length=200,
        blank=True, null=True,
        help_text="Укажите версию",
        verbose_name="Версия"
        )
    bitDepth = models.CharField(
        max_length=200,
        blank=True, null=True,
        help_text="Укажите разрядность",
        verbose_name="разрядность"
        )
    licenseKeyText = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите лицензтонный ключ",
        verbose_name="Введите ключ"
        )
    licenseKeyImg = models.ImageField(
        upload_to='software/soft/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Фото ключа"
        )
    licenseKeyFile = models.FileField(
        upload_to='software/soft/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Файл лицензии"
        )


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('software:software-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Програмное обеспечение'
        verbose_name_plural = 'Програмное обеспечение'
        ordering = [ "name", ]

class Os (ModelMixin, models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите название ОС",
        verbose_name="Операционная система"
        )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите производителя",
        verbose_name="Производитель"
        )
    version = models.CharField(
        max_length=200,
        blank=True, null=True,
        help_text="Укажите версию",
        verbose_name="Версия"
        )
    bitDepth = models.CharField(
        max_length=200,
        blank=True, null=True,
        help_text="Укажите разрядность",
        verbose_name="разрядность"
        )
    licenseKeyText = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите лицензтонный ключ",
        verbose_name="Лицензионный ключ"
        )
    licenseKeyImg = models.ImageField(
        upload_to='software/OS/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Фото ключа"
        )
    licenseKeyFile = models.FileField(
        upload_to='software/OS/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Файл лицензии"
        )
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('software:OS-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Операционная система'
        verbose_name_plural = 'Операционные системы'