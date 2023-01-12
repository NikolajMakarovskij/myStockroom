from django.db import models
from django.urls import reverse
import uuid 
from consumables.models import accumulator
from catalog.models.models import manufacturer

class ups (models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите название модели",
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
        upload_to='gpu/serial/',
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
        upload_to='gpu/invent/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Фото инвентарного номера"
        )
    power = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите мощность",
        verbose_name="Мощность"
        )
    voltage = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите напряжение",
        verbose_name="Напряжение"
        )
    current = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите ток",
        verbose_name="Ток"
        )
    accumulator1 = models.ForeignKey(
        accumulator,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите аккумулятор",
        verbose_name="Аккумулятор № 1"
        )
    accumulator2 = models.ForeignKey(
        accumulator,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True, null=True,
        help_text="Укажите аккумулятор",
        verbose_name="Аккумулятор № 2"
        )
    accumulator3 = models.ForeignKey(
        accumulator,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True, null=True,
        help_text="Укажите аккумулятор",
        verbose_name="Аккумулятор № 3"
        )
    accumulator4 = models.ForeignKey(
        accumulator,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True, null=True,
        help_text="Укажите аккумулятор",
        verbose_name="Аккумулятор № 4"
        )
    cassette1 = models.ForeignKey(
        'cassette',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите кассету",
        verbose_name="Кассета № 1"
        )
    cassette2 = models.ForeignKey(
        'cassette',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True, null=True,
        help_text="Укажите кассету",
        verbose_name="Кассета № 2"
        )
    cassette3 = models.ForeignKey(
        'cassette',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True, null=True,
        help_text="Укажите кассету",
        verbose_name="Кассета № 3"
        )
    cassette4 = models.ForeignKey(
        'cassette',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True, null=True,
        help_text="Укажите кассету",
        verbose_name="Кассета № 4"
        )
    score = models.IntegerField(
        blank=True, null=True,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе"
        )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ups:ups-detail', args=[str(self.id)])
    def get_all_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for f in self._meta.fields:

            fname = f.name        
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+fname+'_display'
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, fname)
                except AttributeError:
                    value = None

            # only display fields with values and skip some fields entirely
            if f.editable and value and f.name not in ('id', ) :

                fields.append(
                    {
                    'label':f.verbose_name, 
                    'name':f.name, 
                    'value':value,
                    }
                )
        return fields
    class Meta:
        verbose_name = 'ИБП'
        verbose_name_plural = 'ИБП'
        ordering = ['name']

class cassette (models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите название модели",
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
        upload_to='gpu/serial/',
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
        upload_to='gpu/invent/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Фото инвентарного номера"
        )
    power = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите мощность",
        verbose_name="Мощность"
        )
    voltage = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите напряжение",
        verbose_name="Напряжение"
        )
    current = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Укажите ток",
        verbose_name="Ток"
        )
    accumulator1 = models.ForeignKey(
        accumulator,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите аккумулятор",
        verbose_name="Аккумулятор № 1"
        )
    accumulator2 = models.ForeignKey(
        accumulator,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True, null=True,
        help_text="Укажите аккумулятор",
        verbose_name="Аккумулятор № 2"
        )
    accumulator3 = models.ForeignKey(
        accumulator,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True, null=True,
        help_text="Укажите аккумулятор",
        verbose_name="Аккумулятор № 3"
        )
    accumulator4 = models.ForeignKey(
        accumulator,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True, null=True,
        help_text="Укажите аккумулятор",
        verbose_name="Аккумулятор № 4"
        )
    accumulator5 = models.ForeignKey(
        accumulator,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True, null=True,
        help_text="Укажите аккумулятор",
        verbose_name="Аккумулятор № 5"
        )
    accumulator6 = models.ForeignKey(
        accumulator,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True, null=True,
        help_text="Укажите аккумулятор",
        verbose_name="Аккумулятор № 6"
        )
    accumulator7 = models.ForeignKey(
        accumulator,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True, null=True,
        help_text="Укажите аккумулятор",
        verbose_name="Аккумулятор № 7"
        )
    accumulator8 = models.ForeignKey(
        accumulator,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True, null=True,
        help_text="Укажите аккумулятор",
        verbose_name="Аккумулятор № 8"
        )
    accumulator9 = models.ForeignKey(
        accumulator,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True, null=True,
        help_text="Укажите аккумулятор",
        verbose_name="Аккумулятор № 9"
        )
    accumulator10 = models.ForeignKey(
        accumulator,
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True, null=True,
        help_text="Укажите аккумулятор",
        verbose_name="Аккумулятор № 10"
        )
    score = models.IntegerField(
        blank=True, null=True,
        help_text="Введите количество на складе",
        verbose_name="Остаток на складе"
        )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ups:cassette-detail', args=[str(self.id)])
    def get_all_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for f in self._meta.fields:

            fname = f.name        
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+fname+'_display'
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, fname)
                except AttributeError:
                    value = None

            # only display fields with values and skip some fields entirely
            if f.editable and value and f.name not in ('id', ) :

                fields.append(
                    {
                    'label':f.verbose_name, 
                    'name':f.name, 
                    'value':value,
                    }
                )
        return fields
    class Meta:
        verbose_name = 'Кассета'
        verbose_name_plural = 'Кассеты'
        ordering = ['name']

