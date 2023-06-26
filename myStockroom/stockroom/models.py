import uuid
from django.db import models
from django.urls import reverse
from workplace.models import Room
from device.models import Device
from consumables.models import Consumables, Accessories
from catalog.utils import ModelMixin


#Расходники
class Stockroom (ModelMixin, models.Model):
    """
    Расширение модели расходников для склада. Номенклатура расходников склада и справочника может различаться, однако количество каждого расходника должно совпадать
    """
    consumables = models.OneToOneField(
        Consumables,
        on_delete = models.CASCADE,
        primary_key = True,
        db_index=True,
        help_text="Введите название расходника",
        verbose_name="Расходники"
        )
    categories = models.ForeignKey(
        'Stock_cat',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите группу",
        verbose_name="группа"
        )
    device = models.CharField(
        max_length=50,
        blank=True, null=True,
        verbose_name="Устройство"
        )
    dateAddToStock = models.DateField(
        null=True, blank=True,
        verbose_name="Дата поступления на склад"
        )
    dateInstall = models.DateField(
        null=True, blank=True,
        verbose_name="Дата установки"
        )
    room = models.ForeignKey(
        Room,
        on_delete = models.SET_NULL,
        blank=True, null=True,
        related_name='StockroomRoom',
        help_text="Укажите помещение",
        verbose_name="помещение"
    )
    rack = models.IntegerField(
        blank=True, null=True,
        help_text="Введите номер стеллажа",
        verbose_name="Стеллаж"
        )
    shelf = models.IntegerField(
        blank=True, null=True,
        help_text="Введите номер полки",
        verbose_name="Полка"
        )

    class Meta:
        verbose_name = 'Склад Расходников'
        verbose_name_plural = 'Склад Расходников'
        ordering = ['consumables']

class Stock_cat(ModelMixin, models.Model):
    """
    Модель группы для расходников
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите название",
        verbose_name="Название"
        )
    slug = models.SlugField(
        max_length=50, unique=True, db_index=True,
        help_text="Введите URL (для работы навигациии)",
        verbose_name="URL"
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stockroom:category', kwargs={'category_slug': self.slug})


    class Meta:
        verbose_name = 'Группа расходников'
        verbose_name_plural = 'Группы расходников'
        ordering = ['name']

class History(models.Model):
        """
        Модель для хранения истории использования расходников
        """
        id = models.UUIDField(
            primary_key=True, db_index=True,
            default=uuid.uuid4,
            help_text="ID"
        )
        consumable = models.CharField(
            blank=True, default=0,
            max_length=50,
            verbose_name="Расходники"
        )
        consumableId = models.CharField(
            blank=True, default=0,
            max_length=50,
            verbose_name="ID Расходникa"
        )
        device = models.CharField(
            blank=True, null=True,
            max_length=50,
            verbose_name="Устройства"
        )
        deviceId = models.CharField(
            blank=True, null=True,
            max_length=50,
            verbose_name="ID Устройства"
        )
        categories = models.ForeignKey(
            'Stock_cat',
            on_delete=models.SET_NULL,
            blank=True, null=True,
            help_text="Укажите группу",
            verbose_name="группа"
        )
        score = models.IntegerField(
            blank=True, default=0,
            verbose_name="Количество",
        )
        dateInstall = models.DateField(
            null=True, blank=True,
            verbose_name="Дата установки"
        )
        user = models.CharField(
            blank=True, default=0,
            max_length=50,
            help_text="Укажите пользователя",
            verbose_name="Пользователь"
        )
        STATUS_CHOISES=[
            ('Приход', 'Приход'),
            ('Расход', 'Расход'),
            ('Удаление', 'Удаление'),
        ]
        status = models.CharField(
            max_length=10,
            choices=STATUS_CHOISES,
            default='Расход',
    )

        class Meta:
            verbose_name = 'История расходников'
            verbose_name_plural = 'История расходников'
            ordering = ['-dateInstall','consumable']


#Комплектующие
class StockAcc (ModelMixin, models.Model):
    """
    Расширение модели комплектующих для склада. Номенклатура комплектующих склада и справочника может различаться, однако количество каждого комплектующего должно совпадать
    """
    accessories = models.OneToOneField(
        Accessories,
        on_delete = models.CASCADE,
        primary_key = True,
        db_index=True,
        help_text="Введите название комплектующего",
        verbose_name="Комплектующие"
        )
    categories = models.ForeignKey(
        'CategoryAcc',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите группу",
        verbose_name="группа"
        )
    device = models.CharField(
        max_length=50,
        blank=True, null=True,
        verbose_name="Устройство"
        )
    dateAddToStock = models.DateField(
        null=True, blank=True,
        verbose_name="Дата поступления на склад"
        )
    dateInstall = models.DateField(
        null=True, blank=True,
        verbose_name="Дата установки"
        )
    room = models.ForeignKey(
        Room,
        on_delete = models.SET_NULL,
        blank=True, null=True,
        related_name='StockAccRoom',
        help_text="Укажите помещение",
        verbose_name="помещение"
    )
    rack = models.IntegerField(
        blank=True, null=True,
        help_text="Введите номер стеллажа",
        verbose_name="Стеллаж"
        )
    shelf = models.IntegerField(
        blank=True, null=True,
        help_text="Введите номер полки",
        verbose_name="Полка"
        )

    class Meta:
        verbose_name = 'Склад комплектующих'
        verbose_name_plural ='Склад комплектующих'
        ordering = ['accessories']

class CategoryAcc(ModelMixin, models.Model):
    """
    Модель группы для комплкеующих
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите название",
        verbose_name="Название"
        )
    slug = models.SlugField(
        max_length=50, unique=True, db_index=True,
        help_text="Введите URL (для работы навигациии)",
        verbose_name="URL"
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stockroom:accessories_category', kwargs={'category_slug': self.slug})


    class Meta:
        verbose_name = 'Группа комплектующих'
        verbose_name_plural = 'Группы комплектующих'
        ordering = ['name']

class HistoryAcc(models.Model):
        """
        Модель для хранения истории использования комплектующих
        """
        id = models.UUIDField(
            primary_key=True, db_index=True,
            default=uuid.uuid4,
            help_text="ID"
        )
        accessories = models.CharField(
            blank=True, default=0,
            max_length=50,
            verbose_name="Комплектующие"
        )
        accessoriesId = models.CharField(
            blank=True, default=0,
            max_length=50,
            verbose_name="ID комплектующего"
        )
        device = models.CharField(
            blank=True, null=True,
            max_length=50,
            verbose_name="Устройства"
        )
        deviceId = models.CharField(
            blank=True, null=True,
            max_length=50,
            verbose_name="ID Устройства"
        )
        categories = models.ForeignKey(
            'CategoryAcc',
            on_delete=models.SET_NULL,
            blank=True, null=True,
            help_text="Укажите группу",
            verbose_name="группа"
        )
        score = models.IntegerField(
            blank=True, default=0,
            verbose_name="Количество",
        )
        dateInstall = models.DateField(
            null=True, blank=True,
            verbose_name="Дата установки"
        )
        user = models.CharField(
            blank=True, default=0,
            max_length=50,
            help_text="Укажите пользователя",
            verbose_name="Пользователь"
        )
        STATUS_CHOISES=[
            ('Приход', 'Приход'),
            ('Расход', 'Расход'),
            ('Удаление', 'Удаление'),
        ]
        status = models.CharField(
            max_length=10,
            choices=STATUS_CHOISES,
            default='Расход',
    )

        class Meta:
            verbose_name = 'История комплектующих'
            verbose_name_plural = 'История комплектующих' 
            ordering = ['-dateInstall','accessories']


#Устройства
class StockDev (ModelMixin, models.Model):
    """
    Расширение модели устройств для склада. Номенклатура устройств склада и справочника может различаться, однако количество и и размещение каждого устройства должно совпадать
    """
    devicies = models.OneToOneField(
        Device,
        on_delete = models.CASCADE,
        primary_key = True,
        db_index=True,
        help_text="Введите название устройства",
        verbose_name="Устройство"
        )
    categories = models.ForeignKey(
        'CategoryDev',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите группу",
        verbose_name="группа"
        )
    dateAddToStock = models.DateField(
        null=True, blank=True,
        verbose_name="Дата поступления на склад"
        )
    dateInstall = models.DateField(
        null=True, blank=True,
        verbose_name="Дата установки"
        )
    rack = models.IntegerField(
        blank=True, null=True,
        help_text="Введите номер стеллажа",
        verbose_name="Стеллаж"
        )
    shelf = models.IntegerField(
        blank=True, null=True,
        help_text="Введите номер полки",
        verbose_name="Полка"
        )

    class Meta:
        verbose_name = 'Склад устройств'
        verbose_name_plural ='Склад устройств'
        ordering = ['devicies']

class CategoryDev(ModelMixin, models.Model):
    """
    Модель группы для устройств
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите название",
        verbose_name="Название"
        )
    slug = models.SlugField(
        max_length=50, unique=True, db_index=True,
        help_text="Введите URL (для работы навигациии)",
        verbose_name="URL"
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stockroom:device_category', kwargs={'category_slug': self.slug})


    class Meta:
        verbose_name = 'Группа устройств'
        verbose_name_plural = 'Группы устройств'
        ordering = ['name']

class HistoryDev(models.Model):
        """
        Модель для хранения истории использования устройств
        """
        id = models.UUIDField(
            primary_key=True, db_index=True,
            default=uuid.uuid4,
            help_text="ID"
        )
        devicies = models.CharField(
            blank=True, default=0,
            max_length=50,
            verbose_name="Устройства"
        )
        deviciesId = models.CharField(
            blank=True, default=0,
            max_length=50,
            verbose_name="ID устройства"
        )
        categories = models.ForeignKey(
            'CategoryDev',
            on_delete=models.SET_NULL,
            blank=True, null=True,
            help_text="Укажите группу",
            verbose_name="группа"
        )
        score = models.IntegerField(
            blank=True, default=0,
            verbose_name="Количество",
        )
        dateInstall = models.DateField(
            null=True, blank=True,
            verbose_name="Дата установки"
        )
        user = models.CharField(
            blank=True, default=0,
            max_length=50,
            help_text="Укажите пользователя",
            verbose_name="Пользователь"
        )
        STATUS_CHOISES=[
            ('Приход', 'Приход'),
            ('Перемещение', 'Перемещение'),
            ('Удаление', 'Удаление'),
        ]
        status = models.CharField(
            max_length=20,
            choices=STATUS_CHOISES,
            default='Перемещение',
    )

        class Meta:
            verbose_name = 'История устройств'
            verbose_name_plural = 'История устройств' 
            ordering = ['-dateInstall','devicies']