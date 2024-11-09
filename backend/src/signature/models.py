import uuid

from django.db import models
from django.urls import reverse

from consumables.models import Consumables
from core.utils import ModelMixin
from device.models import Device
from employee.models import Employee


class Signature(ModelMixin, models.Model):
    """_Signature_:
    Signature model

    Returns:
        Signature (Signature): _description_
    """

    id: models.UUIDField = models.UUIDField(
        primary_key=True, default=uuid.uuid4, db_index=True, help_text="ID"
    )
    name: models.CharField = models.CharField(
        max_length=50, help_text="Введите номер ключа", verbose_name="Ключ"
    )
    licenseKeyFileOpen: models.FileField = models.FileField(
        upload_to="signature/Open/",
        blank=True,
        null=True,
        help_text="Прикрепите файл",
        verbose_name="Открытая часть лицензии",
    )
    licenseKeyFileClose: models.FileField = models.FileField(
        upload_to="signature/Close/",
        blank=True,
        null=True,
        help_text="Прикрепите файл",
        verbose_name="Закрытая часть лицензии",
    )
    periodOpen: models.DateField = models.DateField(
        null=True,
        blank=True,
        help_text="Укажите дату",
        verbose_name="Срок действия открытой части",
    )
    periodClose: models.DateField = models.DateField(
        null=True,
        blank=True,
        help_text="Укажите дату",
        verbose_name="Срок действия закрытой части",
    )
    employeeRegister: models.ForeignKey = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Укажите сотрудника",
        verbose_name="Сотрудник на которого оформлена ЭЦП",
    )
    employeeStorage: models.ForeignKey = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="+",
        help_text="Укажите сотрудника",
        verbose_name="Сотрудник у которого хранится ЭЦП",
    )
    workstation: models.ForeignKey = models.ForeignKey(
        Device,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Укажите рабочую станцию",
        verbose_name="Рабочая станция",
    )
    storage: models.ForeignKey = models.ForeignKey(
        Consumables,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Укажите накопитель",
        verbose_name="накопитель",
    )

    def __str__(self):
        """_Signature __str__ _: _returns name of model_

        Returns:
            Signature__name (str): _returns name_
        """
        return self.name

    def get_absolute_url(self):
        """_Signature url_

        Returns:
            Signature__id (str): _returns url by id_

        Other parameters:
            args (str): self.id
        """
        return reverse("signature:signature-detail", args=[str(self.id)])

    class Meta:
        """_Signature Meta_: _model settings_"""

        verbose_name = "ЭЦП"
        verbose_name_plural = "ЭЦП"
        ordering = [
            "periodOpen",
            "periodClose",
        ]
