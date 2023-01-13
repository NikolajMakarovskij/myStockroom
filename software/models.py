from django.db import models
from catalog.models import manufacturer
from django.urls import reverse
import uuid 

class software (models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите название ПО",
        verbose_name="Програмное обеспечение"
        )
    manufacturer = models.ForeignKey(
        manufacturer,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите производителя",
        verbose_name="Производитель"
        )
    version = models.CharField(
        max_length=200,
        blank=True, null=True,
        help_text="Укажите версию",
        verbose_name="Версия"
        )
    bitDepth = models.CharField(
        max_length=200,
        blank=True, null=True,
        help_text="Укажите разрядность",
        verbose_name="разрядность"
        )
    licenseKeyText = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите лицензтонный ключ",
        verbose_name="Введите ключ"
        )
    licenseKeyImg = models.ImageField(
        upload_to='software/soft/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Фото ключа"
        )
    licenseKeyFile = models.FileField(
        upload_to='software/soft/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Файл лицензии"
        )


    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('software:software-detail', args=[str(self.id)])
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
        verbose_name = 'Програмное обеспечение'
        verbose_name_plural = 'Програмное обеспечение'
        ordering = [ "name", ]

class os (models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите название ОС",
        verbose_name="Операционная система"
        )
    manufacturer = models.ForeignKey(
        manufacturer,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите производителя",
        verbose_name="Производитель"
        )
    version = models.CharField(
        max_length=200,
        blank=True, null=True,
        help_text="Укажите версию",
        verbose_name="Версия"
        )
    bitDepth = models.CharField(
        max_length=200,
        blank=True, null=True,
        help_text="Укажите разрядность",
        verbose_name="разрядность"
        )
    licenseKeyText = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите лицензтонный ключ",
        verbose_name="Лицензионный ключ"
        )
    licenseKeyImg = models.ImageField(
        upload_to='software/OS/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Фото ключа"
        )
    licenseKeyFile = models.FileField(
        upload_to='software/OS/',
        blank=True, null=True,
        help_text="прикрепите файл",
        verbose_name="Файл лицензии"
        )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('software:OS-detail', args=[str(self.id)])
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
        verbose_name = 'Операционная система'
        verbose_name_plural = 'Операционные системы'