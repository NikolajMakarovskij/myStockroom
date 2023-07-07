from django import forms
from catalog.utils import WidgetCanAdd
from consumables.models import Consumables
from device.models import Device
from employee.models import Employee
from .models import Signature


class SignatureForm(forms.ModelForm):
    class Meta:
        model = Signature
        fields = ['name', 'licenseKeyFileOpen', 'licenseKeyFileClose', 'periodOpen', 'periodClose', 'employeeRegister',
                  'employeeStorage', 'workstation', 'storage']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'licenseKeyFileOpen': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'licenseKeyFileClose': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'periodOpen': forms.DateInput(format='%Y-%m-%d',
                                          attrs={'class': 'datepicker form-control form-control-lg  ', 'type': 'date'}),
            'periodClose': forms.DateInput(format='%Y-%m-%d',
                                           attrs={'class': 'datepicker form-control form-control-lg  ',
                                                  'type': 'date'}),
            'employeeRegister': WidgetCanAdd(Employee, related_url="employee:new-employee",
                                             attrs={'class': 'form-select form-select-lg'}),
            'employeeStorage': WidgetCanAdd(Employee, related_url="employee:new-employee",
                                            attrs={'class': 'form-select form-select-lg'}),
            'workstation': WidgetCanAdd(Device, related_url="device:new-device",
                                        attrs={'class': 'form-select form-select-lg'}),
            'storage': WidgetCanAdd(Consumables, related_url="consumables:new-consumables",
                                    attrs={'class': 'form-select form-select-lg'}),
            # 'score': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        }
