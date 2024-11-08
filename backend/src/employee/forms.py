from django import forms

from core.utils import BaseModelSelect2WidgetMixin
from workplace.models import Workplace

from .models import Departament, Employee, Post


class WorkplaceWidget(BaseModelSelect2WidgetMixin):
    """_WorkplaceWidget_ 
    Autocomplete plugin for the workplace selection field

    Returns:
        empty_label (str): _value of empty_label_
        model (Workplace):
        querysets (Workplace): _returns querysets of model in form_
        search_fields (list[str]): _fields of the model to search for are specified_
    """
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
    """_PostWidget_ 
    Autocomplete plugin for the post selection field

    Returns:
        empty_label (str): _value of empty_label_
        model (Post):
        querysets (Post): _returns querysets of model in form_
        search_fields (list[str]): _fields of the model to search for are specified_
    """
    empty_label = "--выбрать--"
    model = Post
    queryset = Post.objects.all().order_by("name")
    search_fields = [
        "name__icontains",
        "departament__name__icontains",
    ]


class DepartamentWidget(BaseModelSelect2WidgetMixin):
    """_DepartamentWidget_ 
    Autocomplete plugin for the departament selection field

    Returns:
        empty_label (str): _value of empty_label_
        model (Departament):
        querysets (Departament): _returns querysets of model in form_
        search_fields (list[str]): _fields of the model to search for are specified_
    """
    empty_label = "--выбрать--"
    model = Departament
    queryset = Departament.objects.all().order_by("name")
    search_fields = [
        "name__icontains",
    ]


# Сотрудники
class EmployeeForm(forms.ModelForm):
    """_EmployeeForm_
    """
    class Meta:
        """_Class returns form of Employee model_

        Returns:
            model (Employee):
            fields (list[str]): _returns fields of model in form_
            widgets (dict[str,str]): _returns widgets of model in form_
            error_messages (str): _returns error messages of model field in form_
        """
        model = Employee
        fields = ["surname", "name", "last_name", "workplace", "post", "employeeEmail"]
        widgets = {
            "surname": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "name": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "last_name": forms.TextInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "workplace": WorkplaceWidget,
            "post": PostWidget,
            "employeeEmail": forms.EmailInput(
                attrs={"class": "form-control form-control-lg"}
            ),
        }
        error_messages = {
            "employeeEmail": {
                "unique": "Такой адрес почты уже существует",
            },
        }


class PostForm(forms.ModelForm):
    """_PostForm_
    """
    class Meta:
        """_Class returns form of Employee model_

        Returns:
            model (Post):
            fields (list[str]): _returns fields of model in form_
            widgets (dict[str,str]): _returns widgets of model in form_
        """
        model = Post
        fields = [
            "name",
            "departament",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "departament": DepartamentWidget,
        }


class DepartamentForm(forms.ModelForm):
    """_DepartamentForm_
    """
    class Meta:
        """_Class returns form of Departament model_

        Returns:
            model (Departament):
            fields (list[str]): _returns fields of model in form_
            widgets (dict[str,str]): _returns widgets of model in form_
        """
        model = Departament
        fields = [
            "name",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
        }
