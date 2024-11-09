import uuid

from django.db import models
from django.urls import reverse

from consumables.models import Accessories, Consumables
from core.utils import ModelMixin


class Categories(ModelMixin, models.Model):
    """_Categories_ The group model for consumables on the balance sheet in accounting.

    Returns:
        Categories (Categories): _returns object "Categories"_
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
        """_Categories url_

        Returns:
            Categories__id (str): _returns url by id_

        Other parameters:
            args (str): self.id
        """
        return reverse("accounting:categories-detail", args=[str(self.id)])

    def get_slug_url(self):
        """_Categories slug url_

        Returns:
            Categories__slug (str): _returns url by slug_

        Other parameters:
            kwargs (str): self.slug
        """
        return reverse("accounting:category", kwargs={"category_slug": self.slug})

    def get_update_url(self):
        """_Categories update url_

        Returns:
            Categories__id (str): _returns url by id_

        Other parameters:
            args (str): self.id
        """

        return reverse("accounting:categories-update", args=[str(self.id)])

    def get_delete_url(self):
        """_Categories delete url_

        Returns:
            Categories__id (str): _returns url by id_

        Other parameters:
            args (str): self.id
        """

        return reverse("accounting:categories-delete", args=[str(self.id)])

    class Meta:
        """_Categories Meta_: _model settings_"""

        verbose_name = "Группа расходников"
        verbose_name_plural = "Группы расходников"
        ordering = ["name"]


class Accounting(ModelMixin, models.Model):
    """_Accounting_: _Accounting model_

    Returns:
         Accounting (Accounting): _returns object "Categories"_
    """

    id: models.UUIDField = models.UUIDField(
        primary_key=True, default=uuid.uuid4, db_index=True, help_text="ID"
    )
    name: models.CharField = models.CharField(
        max_length=500, help_text="Введите название", verbose_name="Название"
    )
    account: models.IntegerField = models.IntegerField(
        blank=True, null=True, help_text="Введите счет", verbose_name="Счет"
    )
    categories: models.ForeignKey = models.ForeignKey(
        "Categories",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Укажите группу",
        verbose_name="Группа",
    )
    consumable: models.ForeignKey = models.ForeignKey(
        Consumables,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="consumable",
        help_text="Укажите расходник",
        verbose_name="Расходник",
    )
    accessories: models.ForeignKey = models.ForeignKey(
        Accessories,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="accessories",
        help_text="Укажите комплектующее",
        verbose_name="Комплектующее",
    )
    code: models.CharField = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Введите код по бухгалтерии",
        verbose_name="Код в бухгалтерии",
    )
    quantity: models.IntegerField = models.IntegerField(
        blank=True,
        default=0,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе",
    )
    cost: models.FloatField = models.FloatField(
        blank=True,
        default=0,
        help_text="Введите стоимость за 1 ед.",
        verbose_name="Стоимость",
    )
    note: models.TextField = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        help_text="Введите примечание",
        verbose_name="Примечание",
    )

    def __str__(self):
        """_Accounting __str__ _: _returns name of model_

        Returns:
            Accounting__name (str): _returns name_
        """
        return self.name

    def get_absolute_url(self):
        """_Accounting get self url_

        Returns:
            Accounting__id (str): _returns url by id_

        Other parameters:
            args (str): self.id
        """
        return reverse("accounting:accounting-detail", args=[str(self.id)])

    def get_cost_all(self):
        """_Accounting cost_all_: _returns cost all consumables or accessories_

        Returns:
            cost_all (float): _Accounting__cost * Accounting__quantity_
        """
        cost_all = self.cost * self.quantity
        return float("{:.2f}".format(cost_all))

    class Meta:
        """_Accounting Meta_: _model settings_"""

        verbose_name = "На балансе"
        verbose_name_plural = "На балансе"
        ordering = ["-account", "name"]
