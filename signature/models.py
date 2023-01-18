import datetime
from django.db import models
from django.urls import reverse
from employee.models import Employee
from workstation.models import Workstation
from consumables.models import Storage
from catalog.utils import ModelMixin
import uuid 

class Signature (ModelMixin, models.Model): #electronic digital signature
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
        Employee,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите сотрудника",
        verbose_name="Сотрудник на которого оформлена ЭЦП"
        )
    employeeStorage = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='+',
        help_text="Укажите сотрудника",
        verbose_name="Сотрудник у которого хранится ЭЦП"
        )
    workstation = models.ForeignKey(
        Workstation,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите рабочую станцию",
        verbose_name="Рабочая станция"
        )
    storage = models.ForeignKey(
        Storage,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Укажите накопитель",
        verbose_name="накопитель"
        )

    def __str__(self):
        return self.name  

    def get_absolute_url(self):
        return reverse('signature:signature-detail', args=[str(self.id)])
        
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
        
    class Meta:
        verbose_name = 'ЭЦП'
        verbose_name_plural = 'ЭЦП'
        ordering = [ "periodOpen","periodClose",]
