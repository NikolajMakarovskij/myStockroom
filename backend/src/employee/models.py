import uuid

from django.db import models

from core.utils import ModelMixin
from workplace.models import Workplace


class Employee(ModelMixin, models.Model):
    """
    Модель сотрудника. Связи один ко многим с моделями workstation, signature
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, db_index=True, help_text="ID"
    )
    name = models.CharField(max_length=50, help_text="Введите имя", verbose_name="Имя")
    last_name = models.CharField(
        max_length=50, blank=True, help_text="Введите отчество", verbose_name="Отчество"
    )
    surname = models.CharField(
        max_length=50, blank=True, help_text="Введите фамилию", verbose_name="Фамилия"
    )
    workplace = models.ForeignKey(
        Workplace,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="employee",
        help_text="Выберете рабочее место",
        verbose_name="Рабочее место",
    )
    post = models.ForeignKey(
        "Post",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Выберете должность",
        verbose_name="Должность",
    )
    employeeEmail = models.EmailField(
        blank=True,
        null=True,
        unique=True,
        help_text="Введите e-mail",
        verbose_name="e-mail",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = [
            "surname",
            "workplace__name",
            "post__departament__name",
        ]


class Departament(ModelMixin, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID")
    name = models.CharField(
        max_length=50, help_text="Введите название отдела", verbose_name="Отдел"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"
        ordering = [
            "name",
        ]


class Post(ModelMixin, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID")
    name = models.CharField(
        max_length=50, help_text="Введите должность", verbose_name="Должность"
    )
    departament = models.ForeignKey(
        "Departament",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Введите название отдела",
        verbose_name="Отдел",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
        ordering = [
            "name",
        ]
