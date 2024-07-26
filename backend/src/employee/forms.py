from django import forms

from core.utils import BaseModelSelect2WidgetMixin
from workplace.models import Workplace

from .models import Departament, Employee, Post


class WorkplaceWidget(BaseModelSelect2WidgetMixin):
    empty_label = "--выбрать--"
    model = Workplace
    queryset = Workplace.objects.all().order_by("name")
    search_fields = [
        "name__icontains",
        "room__name__icontains",
        "room__floor__icontains",
        "room__building__icontains",
    ]


class PostWidget(BaseModelSelect2WidgetMixin):
    empty_label = "--выбрать--"
    model = Post
    queryset = Post.objects.all().order_by("name")
    search_fields = [
        "name__icontains",
        "departament__name__icontains",
    ]


class DepartamentWidget(BaseModelSelect2WidgetMixin):
    empty_label = "--выбрать--"
    model = Departament
    queryset = Departament.objects.all().order_by("name")
    search_fields = [
        "name__icontains",
    ]


# Сотрудники
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['surname', 'name',  'last_name', 'workplace', 'post', 'employeeEmail']
        widgets = {
            'surname': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'workplace': WorkplaceWidget,
            'post': PostWidget,
            'employeeEmail': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
        }
        error_messages = {
            'employeeEmail': {
                'unique': "Такой адрес почты уже существует",
            },
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'departament', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'departament': DepartamentWidget,
        }


class DepartamentForm(forms.ModelForm):
    class Meta:
        model = Departament
        fields = ['name', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        }
