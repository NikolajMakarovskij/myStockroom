import uuid

from django.db import models
from django.urls import reverse

from core.utils import ModelMixin
from counterparty.models import Manufacturer


# Расходники
class Categories(ModelMixin, models.Model):
    """_Categories_:
    Consumables categories model

    Returns:
        Categories (Categories): _description_
    """

    id: models.UUIDField = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID")
    name: models.CharField = models.CharField(
        max_length=50, help_text="Введите название", verbose_name="Название"
    )
    slug: models.SlugField = models.SlugField(
        max_length=50,
        unique=True,
        db_index=True,
        help_text="Введите URL (для работы навигации в расходниках)",
        verbose_name="URL",
    )

    def __str__(self):
        """_Categories __str__ _: _returns name of model_

        Returns:
            Categories__name (str): _returns name_
        """
        return self.name

    def get_absolute_url(self):
        """_Categories get self url_

        Returns:
            Categories__slug (str): _returns url by slug_

        Other parameters:
            kwargs (str): self.slug
        """
        return reverse("consumables:category", kwargs={"category_slug": self.slug})

    class Meta:
        """_Categories Meta_: _model settings_
        """
        verbose_name = "Группа расходников"
        verbose_name_plural = "Группы расходников"
        ordering = ["name"]


class Consumables(ModelMixin, models.Model):
    """_Consumables_:
    Consumables model

    Returns:
        Consumables (Consumables): _description_
    """

    id: models.UUIDField = models.UUIDField(
        primary_key=True, default=uuid.uuid4, db_index=True, help_text="ID"
    )
    name: models.CharField = models.CharField(
        max_length=150,
        unique=True,
        help_text="Введите название",
        verbose_name="Название",
    )
    categories: models.ForeignKey = models.ForeignKey(
        "Categories",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Укажите группу",
        verbose_name="Группа",
    )
    serial: models.CharField = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Введите серийный номер",
        verbose_name="Серийный номер",
    )
    serialImg: models.ImageField = models.ImageField(
        upload_to="сonsumables/serial/",
        blank=True,
        null=True,
        help_text="Прикрепите файл",
        verbose_name="Фото серийного номера",
    )
    invent: models.CharField = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Введите инвентаризационный номер",
        verbose_name="Инвентарный номер",
    )
    inventImg: models.ImageField = models.ImageField(
        upload_to="сonsumables/invent/",
        blank=True,
        null=True,
        help_text="Прикрепите файл",
        verbose_name="Фото инвентарного номера",
    )
    manufacturer: models.ForeignKey = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Укажите производителя",
        verbose_name="Производитель",
    )
    quantity: models.IntegerField = models.IntegerField(
        blank=True,
        default=0,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе",
    )
    description: models.TextField = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        help_text="Введите описание",
        verbose_name="Описание",
    )
    note: models.TextField = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        help_text="Введите примечание",
        verbose_name="Примечание",
    )

    def __str__(self):
        """_Consumables __str__ _: _returns name of model_

        Returns:
            Consumables__name (str): _returns name_
        """
        return self.name

    def get_absolute_url(self):
        """_Consumables url_

        Returns:
            Consumables__id (str): _returns url by id_

        Other parameters:
            args (str): self.id
        """
        return reverse("consumables:consumables-detail", args=[str(self.id)])

    def get_difference(self) -> int:
        """_Consumables get_difference_: 
        Returns the difference between the quantity on stock and in balance

        Returns:
            difference (int): _self.quantity - sum(self.consumable.quantity)_
        """
        quantity_all = 0
        for each in self.consumable.all(): # type: ignore[attr-defined]
            quantity_all += each.quantity
        difference = self.quantity - quantity_all
        return difference

    class Meta:
        """_Consumables Meta_: _model settings_
        """
        verbose_name = "Расходник"
        verbose_name_plural = "Расходники"
        ordering = ["name", "categories"]
        permissions = [
            ("can_add_consumable_to_stock", "Добавление на склад"),
            ("can_export_consumable", "Экспорт"),
        ]


# Комплектующие /// accessories
class AccCat(ModelMixin, models.Model):
    """_AccCat_:
    Accessories categories model

    Returns:
        AccCat (AccCat): _description_
    """

    id: models.UUIDField = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID")
    name: models.CharField = models.CharField(
        max_length=50, help_text="Введите название", verbose_name="Название"
    )
    slug: models.SlugField = models.SlugField(
        max_length=50,
        unique=True,
        db_index=True,
        help_text="Введите URL (для работы навигации в комплектующих)",
        verbose_name="URL",
    )

    def __str__(self):
        """_AccCat __str__ _: _returns name of model_

        Returns:
            AccCat__name (str): _returns name_
        """
        return self.name

    def get_absolute_url(self):
        """_AccCat get self url_

        Returns:
            AccCat__slug (str): _returns url by slug_

        Other parameters:
            kwargs (str): self.slug
        """
        return reverse(
            "consumables:category_accessories", kwargs={"category_slug": self.slug}
        )

    class Meta:
        """_AccCat Meta_: _model settings_
        """
        verbose_name = "Группа комплектующих"
        verbose_name_plural = "Группы комплектующих"
        ordering = ["name"]


class Accessories(ModelMixin, models.Model):
    """_Accessories_:
    Accessories model

    Returns:
        Accessories (Accessories): _description_
    """

    id: models.UUIDField = models.UUIDField(
        primary_key=True, default=uuid.uuid4, db_index=True, help_text="ID"
    )
    name: models.CharField = models.CharField(
        max_length=150,
        unique=True,
        help_text="Введите название",
        verbose_name="Название",
    )
    categories: models.ForeignKey = models.ForeignKey(
        "AccCat",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Укажите группу",
        verbose_name="Группа",
    )
    serial: models.CharField = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Введите серийный номер",
        verbose_name="Серийный номер",
    )
    serialImg: models.ImageField = models.ImageField(
        upload_to="accessories/serial/",
        blank=True,
        null=True,
        help_text="Прикрепите файл",
        verbose_name="Фото серийного номера",
    )
    invent: models.CharField = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Введите инвентаризационный номер",
        verbose_name="Инвентарный номер",
    )
    inventImg: models.ImageField = models.ImageField(
        upload_to="accessories/invent/",
        blank=True,
        null=True,
        help_text="Прикрепите файл",
        verbose_name="Фото инвентарного номера",
    )
    manufacturer: models.ForeignKey = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Укажите производителя",
        verbose_name="Производитель",
    )
    quantity: models.IntegerField = models.IntegerField(
        blank=True,
        default=0,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе",
    )
    description: models.TextField = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        help_text="Введите описание",
        verbose_name="Описание",
    )
    note: models.TextField = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        help_text="Введите примечание",
        verbose_name="Примечание",
    )

    def __str__(self):
        """_Accessories __str__ _: _returns name of model_

        Returns:
            Accessories__name (str): _returns name_
        """
        return self.name

    def get_absolute_url(self):
        """_Accessories get self url_

        Returns:
            Accessories__slug (str): _returns url by slug_

        Other parameters:
            args (str): self.id
        """
        return reverse("consumables:accessories-detail", args=[str(self.id)])

    def get_difference(self) -> int:
        """_Accessories get_difference_: 
        Returns the difference between the quantity on stock and in balance

        Returns:
            difference (int): _self.quantity - sum(self.accessories.quantity)_
        """
        quantity_all = 0
        for each in self.accessories.all(): # type: ignore[attr-defined]
            quantity_all += each.quantity
        difference = self.quantity - quantity_all
        return difference

    class Meta:
        """_Accessories Meta_: _model settings_
        """
        verbose_name = "Комплектующее"
        verbose_name_plural = "Комплектующие"
        ordering = ["name", "categories"]
        permissions = [
            ("can_add_accessories_to_stock", "Добавление на склад"),
            ("can_export_accessories", "Экспорт"),
        ]
