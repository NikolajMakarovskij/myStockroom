import datetime
from django.db import models
from .employee_model import *
from .workplace_model import *
from .software_model import *
from .workstation_model import *
from .printer_model import *
from .signature import *
from django.urls import reverse
import uuid 

class digitalSignature (models.Model): #electronic digital signature
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
    licenseKeyText = models.CharField(
        blank=True, null=True,
        max_length=50,
        help_text="Введите лицензионный ключ",
        )
    licenseKeyImg = models.ImageField(
        upload_to='OS/',
        blank=True, null=True,
        help_text="прикрепите файл"
        )
    licenseKeyFile = models.FileField(
        upload_to='soft/',
        blank=True, null=True,
        help_text="прикрепите файл"
        )
    workplace = models.ForeignKey(
        'Workplace',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Рабочее место"
        )
    employee = models.ForeignKey(
        'Employee',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Сотрудник"
        )
    workstation = models.ForeignKey(
        'workstation',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Рабочая станция"
        )
    validityPeriod = models.DateField(
        null=True, blank=True
        )


    def __str__(self):
        return self.name  

    def get_absolute_url(self):
        return reverse('digitalsignature-detail', args=[str(self.id)])
    
    #@property
    #def dangerDay(self, request):
    #    from django.contrib import messages
    #    if self.validityPeriod <= date.today:
    #        messages.add_message(request, messages.INFO, 'weagEG' , extra_tags='danger_date' )
    #    return self.dangerDay 
    
    #def get_validityPeriod(request, self):
    #    from django.contrib import messages
    #    if self.validityPeriod == date.today():
    #        return messages.add_message(request, messages.INFO, 'сегодня' , extra_tags='danger_date' )
        
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
        ordering = [ "validityPeriod",]