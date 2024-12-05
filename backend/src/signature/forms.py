from django import forms
from core.utils import BaseModelSelect2WidgetMixin
from consumables.models import Consumables
from device.models import Device
from employee.models import Employee
from .models import Signature


class ConWidget(BaseModelSelect2WidgetMixin):
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
    class Meta:
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
