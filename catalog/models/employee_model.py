from django.db import models
from django.urls import reverse
import uuid 

class employee(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        blank=True, 
        help_text="Введите имя сотрудника",
        verbose_name="Имя сотрудника"
        )
    sername = models.CharField(
        max_length=50,
        blank=True, 
        help_text="Введите отчество сотрудника",
        verbose_name="Отчество сотрудника"
        )
    family = models.CharField(
        max_length=50,
        blank=True, 
        help_text="Введите фамилию сотрудника",
        verbose_name="Фамилия сотрудника"
        )
    workplace = models.ForeignKey(
        'Workplace',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Выберете рабочее место",
        verbose_name="Рабочее место"
        )
    post = models.ForeignKey(
        'Post',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Выберете должность", 
        verbose_name="Должность"
        )
    employeeEmail = models.EmailField(
        blank=True, null=True, unique=True,
        help_text="Введие e-mail", 
        verbose_name="e-mail"
        )

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('employee-detail', args=[str(self.id)])
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
            if f.editable and value and f.name not in ('id', 'Workplace', 'post') :

                fields.append(
                    {
                    'label':f.verbose_name, 
                    'name':f.name, 
                    'value':value,
                    }
                )
        return fields
    class Meta:
        verbose_name_plural = 'Сотрудник'
        ordering = ["name", "-workplace"]

class departament(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите название отдела",
        verbose_name="Отдел"
        )

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('departament-detail', args=[str(self.id)])
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
        verbose_name_plural = 'Отдел'
        ordering = ["name", ]

class post(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="ID"
        )
    name = models.CharField(
        max_length=50,
        help_text="Введите должность",
        verbose_name="Должность"
        )
    departament = models.ForeignKey(
        'departament',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        help_text="Введите название отдела",
        verbose_name="Отдел"
        )

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])
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
        verbose_name_plural = 'Должность'
        ordering = ["name",]