from django import forms

from .models import Manufacturer


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ["name", "country", "production"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "country": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "production": forms.TextInput(
                attrs={"class": "form-control form-control-lg"}
            ),
        }
