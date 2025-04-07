import uuid

from django.db import models
from django.urls import reverse

from core.utils import ModelMixin
from workplace.models import Workplace


class Employee(ModelMixin, models.Model):
    """_Employee_:
    Employee model

    Returns:
        Employee (Employee): _description_
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
        """_Employee __str__ _: _returns name of model_

        Returns:
            Employee__name (str): _returns name_
        """
        return self.name

    def get_absolute_url(self):
        """_Employee url_

        Returns:
            Employee__id (str): _returns url by id_

        Other parameters:
            args (str): self.id
        """
        return reverse("employee:employee-detail", args=[str(self.id)])

    class Meta:
        """_Employee Meta_: _model settings_"""

        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = [
            "surname",
            "workplace__name",
            "post__departament__name",
        ]


class Departament(ModelMixin, models.Model):
    """_Departament_:
    Departament model

    Returns:
        Departament (Departament): _description_
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID")
    name = models.CharField(
        max_length=50, help_text="Введите название отдела", verbose_name="Отдел"
    )

    def __str__(self):
        """_Departament __str__ _: _returns name of model_

        Returns:
            Departament__name (str): _returns name_
        """
        return self.name

    def get_absolute_url(self):
        """_Departament url_

        Returns:
            Departament__id (str): _returns url by id_

        Other parameters:
            args (str): self.id
        """
        return reverse("employee:departament-detail", args=[str(self.id)])

    class Meta:
        """_Departament Meta_: _model settings_"""

        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"
        ordering = [
            "name",
        ]


class Post(ModelMixin, models.Model):
    """_Post_:
    Post model

    Returns:
        Post (Post): _description_
    """

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
        """_Post __str__ _: _returns name of model_

        Returns:
            Post__name (str): _returns name_
        """
        return self.name

    def get_absolute_url(self):
        """_Post url_

        Returns:
            Post__id (str): _returns url by id_

        Other parameters:
            args (str): self.id
        """
        return reverse("employee:post-detail", args=[str(self.id)])

    class Meta:
        """_Post Meta_: _model settings_"""

        verbose_name = "Должность"
        verbose_name_plural = "Должности"
        ordering = [
            "name",
        ]
