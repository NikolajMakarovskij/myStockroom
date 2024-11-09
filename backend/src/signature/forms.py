from django import forms

from consumables.models import Consumables
from core.utils import BaseModelSelect2WidgetMixin
from device.models import Device
from employee.models import Employee

from .models import Signature


class ConWidget(BaseModelSelect2WidgetMixin):
    """_ConWidget_
    Autocomplete plugin for the consumable selection field

    Returns:
        empty_label (str): _value of empty_label_
        model (Consumables):
        querysets (Consumables): _returns querysets of model in form_
        search_fields (list[str]): _fields of the model to search for are specified_
    """

    empty_label = "--выбрать--"
    model = Consumables
    queryset = Consumables.objects.all().order_by("name")
    search_fields = [
        "name__icontains",
        "categories__name__icontains",
        "description__icontains",
        "note__icontains",
        "buhCode__icontains",
        "manufacturer__name__icontains",
        "manufacturer__country__icontains",
        "manufacturer__production__icontains",
    ]


class DeviceWidget(BaseModelSelect2WidgetMixin):
    """_DeviceWidget_
    Autocomplete plugin for the device selection field

    Returns:
        empty_label (str): _value of empty_label_
        model (Device):
        querysets (Device): _returns querysets of model in form_
        search_fields (list[str]): _fields of the model to search for are specified_
    """

    empty_label = "--выбрать--"
    model = Device
    queryset = Device.objects.all().order_by("name")
    search_fields = [
        "name__icontains",
        "categories__name__icontains",
        "description__icontains",
        "note__icontains",
        "manufacturer__name__icontains",
        "manufacturer__country__icontains",
        "manufacturer__production__icontains",
        "workplace__name__icontains",
        "workplace__room__name__icontains",
        "workplace__room__floor__icontains",
        "workplace__room__building__icontains",
    ]


class EmployeeWidget(BaseModelSelect2WidgetMixin):
    """_EmployeeWidget_
    Autocomplete plugin for the employee selection field

    Returns:
        empty_label (str): _value of empty_label_
        model (Employee):
        querysets (Employee): _returns querysets of model in form_
        search_fields (list[str]): _fields of the model to search for are specified_
    """

    empty_label = "--выбрать--"
    model = Employee
    queryset = Employee.objects.all().order_by("name")
    search_fields = [
        "name__icontains",
        "surname__icontains",
        "family__icontains",
        "workplace__name__icontains",
        "workplace__room__name__icontains",
        "workplace__room__building__icontains",
        "workplace__room__floor__icontains",
        "post__name__icontains",
        "post__departament__name__icontains",
        "employeeEmail__icontains",
    ]


class SignatureForm(forms.ModelForm):
    """_SignatureForm_"""

    class Meta:
        """_Class returns form of Signature model_

        Returns:
            model (Signature):
            fields (list[str]): _returns fields of model in form_
            widgets (dict[str,str]): _returns widgets of model in form_
            error_messages (str): _returns error messages of model field in form_
        """

        model = Signature
        fields = [
            "name",
            "licenseKeyFileOpen",
            "licenseKeyFileClose",
            "periodOpen",
            "periodClose",
            "employeeRegister",
            "employeeStorage",
            "workstation",
            "storage",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "licenseKeyFileOpen": forms.FileInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "licenseKeyFileClose": forms.FileInput(
                attrs={"class": "form-control form-control-lg"}
            ),
            "periodOpen": forms.DateInput(
                format="%Y-%m-%d",
                attrs={
                    "class": "datepicker form-control form-control-lg  ",
                    "type": "date",
                },
            ),
            "periodClose": forms.DateInput(
                format="%Y-%m-%d",
                attrs={
                    "class": "datepicker form-control form-control-lg  ",
                    "type": "date",
                },
            ),
            "employeeRegister": EmployeeWidget,
            "employeeStorage": EmployeeWidget,
            "workstation": DeviceWidget,
            "storage": ConWidget,
            # 'quantity': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        }
