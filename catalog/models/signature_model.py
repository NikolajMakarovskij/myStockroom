import datetime
from django.db import models
from .models import *
from django.urls import reverse
import uuid 

class signature (models.Model): #electronic digital signature
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        blank=True, null=True,
        help_text="Введите номер ключа",
        verbose_name="Ключ"
        )
    licenseKeyFileOpen = models.FileField(
        upload_to='signature/Open/',
        blank=True, null=True,
        help_text="Прикрепите файл",
        verbose_name="Открытая часть лицензии"
        )
    licenseKeyFileClose = models.FileField(
        upload_to='signature/Close/',
        blank=True, null=True,
        help_text="Прикрепите файл",
        verbose_name="Закрытая часть лицензии"
        )
    periodOpen = models.DateField(
        null=True, blank=True,
        help_text="Укажите дату",
        verbose_name="Срок действия открытой части"
        )
    periodClose = models.DateField(
        null=True, blank=True,
        help_text="Укажите дату",
        verbose_name="Срок действия закрытой части"
        )
    employeeRegister = models.ForeignKey(
        'employee',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите сотрудника",
        verbose_name="Сотрудник на которого оформлена ЭЦП"
        )
    employeeStorage = models.ForeignKey(
        'employee',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='+',
        help_text="Укажите сотрудника",
        verbose_name="Сотрудник у которого хранится ЭЦП"
        )
    workstation = models.ForeignKey(
        'workstation',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите рабочую станцию",
        verbose_name="Рабочая станция"
        )
    storage = models.ForeignKey(
        'storage',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите накопитель",
        verbose_name="накопитель"
        )

    def __str__(self):
        return self.name  
    def get_absolute_url(self):
        return reverse('signature-detail', args=[str(self.id)])
        
    def dangerDay(self):

        return self.dangerDay and datetime.date.today() 

    def warningOneWeek(self):

        return self.warningOneWeek and (datetime.date.today() + datetime.timedelta(weeks=1))

    def warningTwoWeeks(self):
        return self.warningTwoWeeks and (datetime.date.today() + datetime.timedelta(weeks=2))

    def warningThreeWeeks(self):
        return self.warningThreeWeeks and (datetime.date.today() + datetime.timedelta(weeks=3))

    def warningOneMounth(self):
        return self.warningOneMounth and (datetime.date.today() + datetime.timedelta(weeks=4))
    
    def warningTwoMounth(self):
        return self.warningTwoMounth and (datetime.date.today() + datetime.timedelta(weeks=8))
        
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
        verbose_name_plural = 'ЭЦП'
        ordering = [ "periodOpen","periodClose",]