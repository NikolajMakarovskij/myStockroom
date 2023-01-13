from django.db import models
from django.urls import reverse
import uuid 

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
        return reverse('counterparty:manufacturer-detail', args=[str(self.id)])
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
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
        ordering = [ "name", ]
