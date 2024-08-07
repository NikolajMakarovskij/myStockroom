from django import forms

from .models import Manufacturer


class ManufacturerForm(forms.ModelForm):
    """_ManufacturerForm_
    """
    class Meta:
        """_Class returns form of Manufacturer model_

        Returns:
            model (Manufacturer):
            fields (list[str]): _returns fields of model in form_
            widgets (dict[str,str]): _returns widgets of model in form_
        """
        model = Manufacturer
        fields = ["name", "country", "production"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "country": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "production": forms.TextInput(
                attrs={"class": "form-control form-control-lg"}
            ),
        }
