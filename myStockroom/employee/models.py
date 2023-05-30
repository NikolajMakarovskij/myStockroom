from django.db import models
from django.urls import reverse
from workplace.models import Workplace
import uuid 
from catalog.utils import ModelMixin

class Employee(ModelMixin, models.Model):
    """
    Модель сотрудника. Связи один ко многим с моделями workstatio, signature
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        db_index=True,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите имя сотрудника",
        verbose_name="Имя сотрудника"
        )
    sername = models.CharField(
        max_length=50,
        blank=True, 
        help_text="Введите отчество сотрудника",
        verbose_name="Отчество сотрудника"
        )
    family = models.CharField(
        max_length=50,
        blank=True, 
        help_text="Введите фамилию сотрудника",
        verbose_name="Фамилия сотрудника"
        )
    workplace = models.ForeignKey(
        Workplace,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Выберете рабочее место",
        verbose_name="Рабочее место"
        )
    post = models.ForeignKey(
        'Post',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Выберете должность", 
        verbose_name="Должность"
        )
    employeeEmail = models.EmailField(
        blank=True, null=True, unique=True,
        help_text="Введие e-mail", 
        verbose_name="e-mail"
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('employee:employee-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ["name", "-workplace"]

class Departament(ModelMixin, models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите название отдела",
        verbose_name="Отдел"
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('employee:departament-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
        ordering = ["name", ]

class Post(ModelMixin, models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите должность",
        verbose_name="Должность"
        )
    departament = models.ForeignKey(
        'Departament',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Введите название отдела",
        verbose_name="Отдел"
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('employee:post-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ["name",]
