from django import forms
from catalog.utils import WidgetCanAdd
from workplace.models import Workplace
from .models import Employee, Post, Departament


# Сотрудники
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'surname', 'family', 'workplace', 'post', 'employeeEmail']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'surname': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'family': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'workplace': WidgetCanAdd(Workplace, related_url="workplace:new-workplace",
                                      attrs={'class': 'input-group form-select form-select-lg'}),
            'post': WidgetCanAdd(Post, related_url="employee:new-post",
                                 attrs={'class': 'input-group form-select form-select-lg'}),
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
            'departament': WidgetCanAdd(Departament, related_url="employee:new-departament",
                                        attrs={'class': 'input-group form-select form-select-lg'}),
        }


class DepartamentForm(forms.ModelForm):
    class Meta:
        model = Departament
        fields = ['name', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        }
