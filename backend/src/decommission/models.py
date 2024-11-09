import uuid

from django.db import models
from django.urls import reverse

from core.utils import ModelMixin
from device.models import Device


# Decommission
class Decommission(ModelMixin, models.Model):
    """_Decommission_
    Extension of the device model for the decommission.
    The nomenclature of warehouse and decommission and directory devices may differ.
    However, the number and placement of each device must match.

    Returns:
        Decommission (Decommission): _description_
    """

    stock_model: models.OneToOneField = models.OneToOneField(
        Device,
        on_delete=models.CASCADE,
        primary_key=True,
        db_index=True,
        help_text="Введите название устройства",
        verbose_name="Устройство",
    )
    categories: models.ForeignKey = models.ForeignKey(
        "CategoryDec",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Укажите группу",
        verbose_name="группа",
    )
    date: models.DateField = models.DateField(
        null=True, blank=True, verbose_name="Дата списания"
    )

    class Meta:
        """_Decommission Meta_: _model settings_"""

        verbose_name = "Списание устройств"
        verbose_name_plural = "Списание устройств"
        ordering = ["stock_model"]
        permissions = [
            ("add_to_decommission", "Отправить на списание"),
            ("remove_from_decommission", "Удалить из списания"),
            ("can_export_device", "Экспорт устройств"),
        ]


class CategoryDec(ModelMixin, models.Model):
    """_CategoryDec_
    Decommission categories model

    Returns:
        CategoryDec (CategoryDec): _description_
    """

    id: models.UUIDField = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text="ID"
    )
    name: models.CharField = models.CharField(
        max_length=50, help_text="Введите название", verbose_name="Название"
    )
    slug: models.SlugField = models.SlugField(
        max_length=50,
        unique=True,
        db_index=True,
        help_text="Введите URL (для работы навигации)",
        verbose_name="URL",
    )

    def __str__(self):
        """_CategoryDec __str__ _: _returns name of model_

        Returns:
            CategoryDec__name (str): _returns name_
        """
        return self.name

    def get_absolute_url(self):
        """_CategoryDec get self url_

        Returns:
            CategoryDec__slug (str): _returns url by slug_

        Other parameters:
            kwargs (str): self.slug
        """
        return reverse(
            "decommission:decom_category", kwargs={"category_slug": self.slug}
        )

    class Meta:
        """_CategoryDec Meta_: _model settings_"""

        verbose_name = "Группа списания устройств"
        verbose_name_plural = "Группы списания устройств"
        ordering = ["name"]


# Disposal
class Disposal(ModelMixin, models.Model):
    """_ Disposal_
    Extension of the device model for the disposal.
    The nomenclature of warehouse and disposal and directory stock_model may differ.
    However, the number and placement of each device must match.

    Returns:
        Disposal ( Disposal): _description_
    """

    stock_model: models.OneToOneField = models.OneToOneField(
        Device,
        on_delete=models.CASCADE,
        primary_key=True,
        db_index=True,
        help_text="Введите название устройства",
        verbose_name="Устройство",
    )
    categories: models.ForeignKey = models.ForeignKey(
        "CategoryDis",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Укажите группу",
        verbose_name="группа",
    )
    date: models.DateField = models.DateField(
        null=True, blank=True, verbose_name="Дата утилизации"
    )

    class Meta:
        """_ Disposal Meta_: _model settings_"""

        verbose_name = "Утилизация устройств"
        verbose_name_plural = "Утилизация устройств"
        ordering = ["stock_model"]
        permissions = [
            ("add_to_disposal", "Отправить на утилизацию"),
            ("remove_from_disposal", "Удалить из утилизации"),
            ("can_export_device", "Экспорт устройств"),
        ]


class CategoryDis(ModelMixin, models.Model):
    """_CategoryDis_
    CategoryDis categories model

    Returns:
        CategoryDis (CategoryDis): _description_
    """

    id: models.UUIDField = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text="ID"
    )
    name: models.CharField = models.CharField(
        max_length=50, help_text="Введите название", verbose_name="Название"
    )
    slug: models.SlugField = models.SlugField(
        max_length=50,
        unique=True,
        db_index=True,
        help_text="Введите URL (для работы навигации)",
        verbose_name="URL",
    )

    def __str__(self):
        """_CategoryDis __str__ _: _returns name of model_

        Returns:
            CategoryDis__name (str): _returns name_
        """
        return self.name

    def get_absolute_url(self):
        """_CategoryDis get self url_

        Returns:
            CategoryDis__slug (str): _returns url by slug_

        Other parameters:
            kwargs (str): self.slug
        """
        return reverse(
            "decommission:disp_category", kwargs={"category_slug": self.slug}
        )

    class Meta:
        """_CategoryDis Meta_: _model settings_"""

        verbose_name = "Группа утилизации устройств"
        verbose_name_plural = "Группы утилизации устройств"
        ordering = ["name"]
