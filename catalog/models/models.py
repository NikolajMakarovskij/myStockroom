from django.db import models
from django.urls import reverse
import uuid 
from employee.models import employee

class manufacturer (models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=150,
        help_text="Введите наименование производителя",
        verbose_name="Производитель"
        )
    country = models.CharField(
        max_length=150,
        help_text="Введите название страны",
        verbose_name="Страна"
        )
    production = models.CharField(
        max_length=150,
        help_text="Введите страну производства",
        verbose_name="Страна производства"
        )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('manufacturer-detail', args=[str(self.id)])
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
        verbose_name_plural = 'Производитель'
        ordering = [ "name", ]        

class storage(models.Model):
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
    manufacturer = models.ForeignKey(
        'manufacturer',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите производителя",
        verbose_name="Производитель"
        )
    modelStorage = models.CharField(
        max_length=200,
        blank=True, null=True,
        help_text="Введите название модели",
        verbose_name="Модель"
        )
    serial = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите серийный номер",
        verbose_name="Серийный номер"
        )
    serialImg = models.ImageField(
        upload_to='storage/serial/',
        blank=True, null=True,
        help_text="Прикрепите файл",
        verbose_name="Фото серийного номера"
        )
    invent = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите инвентаризационный номер",
        verbose_name="Инвентарный номер"
        )
    inventImg = models.ImageField(
        upload_to='storage/invent/',
        blank=True, null=True,
        help_text="Прикрепите файл",
        verbose_name="Фото инвентарного номера"
        )
    plug = models.TextField(
        max_length=20,
        blank=True, null=True,
        help_text="Укажите тип подключения",
        verbose_name="Тип подключения"
        )
    typeMemory = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Укажите тип памяти",
        verbose_name="Тип памяти"
        )
    volumeMemory = models.TextField(
        max_length=200,
        blank=True, null=True,
        help_text="Укажите объем памяти",
        verbose_name="Объем памяти"
        )
    employee = models.ForeignKey(
        employee,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите сотрудника",
        verbose_name="Сотрудник"
        )
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('storage-detail', args=[str(self.id)])
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
        verbose_name_plural = 'Накопитель'
        ordering = ["employee", "name", ]

class references(models.Model):
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
    linkname = models.CharField(
        max_length=50,
        help_text="Введите ссылку",
        verbose_name="Ссылка"
        )

    def __str__(self):
        return self.name
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
        verbose_name_plural = 'Справочники'
        ordering = ["name", ]