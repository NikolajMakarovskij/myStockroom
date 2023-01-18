from django.db import models
from django.urls import reverse
from workplace.models import workplace
from consumables.models import Cartridge, Fotoval, Toner
from counterparty.models import manufacturer
from catalog.utils import ModelMixin
import uuid 

class printer (ModelMixin, models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите название принтера",
        verbose_name="Название"
        )
    modelPrinter = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите модель принтера",
        verbose_name="Модель"
        )
    manufacturer = models.ForeignKey(
        manufacturer,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите производителя",
        verbose_name="Производитель"
        )
    serial = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите серийный номер",
        verbose_name="Серийный номер"
        )
    serialImg = models.ImageField(
        upload_to='printer/serial/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Фото серийного номера"
        )
    invent = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите инвентарный номер",
        verbose_name="Инвентарный номер"
        )
    inventImg = models.ImageField(
        upload_to='printer/invent/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Фото инвентарного номера"
        )
    usbPort = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество и тип",
        verbose_name="USB"
        )
    lanPort = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите количество",
        verbose_name="LAN"
        )
    FORMAT = (
        ('A4', 'A4'),
        ('A3', 'A3'),
        ('A2', 'A2'),
        ('A1', 'A1'),
        ('A0', 'A0'),
        ('A5', 'A5'),
        ('Конверт', 'Конверт'),
        ('Отсутствует', 'Отсутствует'),
        )
    tray1 = models.TextField(
        max_length=15,
        choices=FORMAT,
        default='A4',
        help_text="Укажите формат бумаги",
        verbose_name="Лоток №1 для подачи бумаги"
        )
    tray2 = models.TextField(
        max_length=15,
        choices=FORMAT,
        default='A3',
        help_text="Укажите формат бумаги",
        verbose_name="Лоток №2 для подачи бумаги"
        )
    tray3 = models.TextField(
        max_length=15,
        choices=FORMAT,
        default='Отсутствует',
        help_text="Укажите формат бумаги",
        verbose_name="Лоток №3 для подачи бумаги"
        )
    traySide = models.TextField(
        max_length=15,
        choices=FORMAT,
        default='A4',
        help_text="Укажите формат бумаги",
        verbose_name="Боковой лоток для подачи бумаги"
        )
    workplace = models.ForeignKey(
        workplace,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите рабочее место",
        verbose_name="Рабочее место"
        )
    cartridge = models.ForeignKey(
        Cartridge,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите картридж",
        verbose_name="Картридж"
        )
    fotoval = models.ForeignKey(
        Fotoval,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите фотовал",
        verbose_name="Фотовал"
        )
    toner = models.ForeignKey(
        Toner,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите тонер",
        verbose_name="Тонер"
        )
    score = models.IntegerField(
        blank=True, null=True,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе"
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('printer:printer-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Принтер'
        verbose_name_plural = 'Принтеры'
        ordering = ["name"]
