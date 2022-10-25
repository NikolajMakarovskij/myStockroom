from tabnanny import verbose
from django.db import models
from .models import *
from django.urls import reverse
import uuid 

class Room(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=15,
        blank=True,
        help_text="Введите номер кабинета",
        verbose_name="Кабинет",
        )
    Building = models.CharField(
        max_length=25,
        blank=True,
        help_text="Введите название здания",
        verbose_name="Здание",
        )
    Floor = models.CharField(
        max_length=25,
        blank=True,
        help_text="Введите номер этажа",
        verbose_name="Этаж",
        )

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('room-detail', args=[str(self.id)])
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
        verbose_name_plural = 'Кабинет'
        ordering = ["Building", "Floor", "name"]

class Workplace(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID",
        verbose_name="Введите уникальный UUID4)"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите номер рабочего места",
        verbose_name="Рабочее место"
        )
    Room = models.ForeignKey(
        'Room',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Выберете номер кабинета",
        verbose_name="Номер кабинета"
        )  
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('workplace-detail', args=[str(self.id)])
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
            if f.editable and value and f.name not in ('id', 'Room') :

                fields.append(
                    {
                    'label':f.verbose_name, 
                    'name':f.name, 
                    'value':value,
                    }
                )
        return fields
    class Meta:
        verbose_name_plural = 'Рабочее место'
        ordering = ["Room", ]
