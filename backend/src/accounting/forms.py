from django import forms

from consumables.models import Accessories, Consumables
from core.utils import BaseModelSelect2WidgetMixin

from .models import Accounting, Categories


class CategoryWidget(BaseModelSelect2WidgetMixin):
    """_CategoryWidget_
    Autocomplete plugin for the category selection field

    Returns:
        empty_label (str): _value of empty_label_
        model (Categories):
        querysets (Categories): _returns querysets of model in form_
        search_fields (list[str]): _fields of the model to search for are specified_
    """

    empty_label = "--выбрать--"
    model = Categories
    queryset = Categories.objects.all().order_by("name")
    search_fields = ["name__icontains"]


class ConsumablesWidget(BaseModelSelect2WidgetMixin):
    """_ConsumablesWidget_
    Autocomplete plugin for the consumable selection field

    Returns:
        empty_label (str): _value of empty_label_
        model (Categories):
        querysets (Categories): _returns querysets of model in form_
        search_fields (list[str]): _fields of the model to search for are specified_
    """

    empty_label = "--выбрать--"
    model = Consumables
    queryset = Consumables.objects.all().order_by("name")
    search_fields = [
        "name__icontains",
        "categories__name__icontains",
    ]


class AccessoriesWidget(BaseModelSelect2WidgetMixin):
    """_AccessoriesWidget_
    Autocomplete plugin for the accessories selection field

    Returns:
        empty_label (str): _value of empty_label_
        model (Accessories):
        querysets (Accessories): _returns querysets of model in form_
        search_fields (list[str]): _fields of the model to search for are specified_
    """

    empty_label = "--выбрать--"
    model = Accessories
    queryset = Accessories.objects.all().order_by("name")
    search_fields = [
        "name__icontains" "categories__name__icontains",
    ]


class AccountingForm(forms.ModelForm):
    """_AccountingForm_"""

    class Meta:
        """_Class returns form of Accounting model_

        Returns:
            model (Accounting):
            fields (list[str]): _returns fields of model in form_
            widgets (dict[str,str]): _returns widgets of model in form_
        """

        model = Accounting
        fields = [
            "name",
            "note",
            "categories",
            "account",
            "consumable",
            "accessories",
            "code",
            "quantity",
            "cost",
        ]
        widgets = {
            "name": forms.Textarea(attrs={"class": "form-control form-control-lg"}),
            "categories": CategoryWidget,
            "account": forms.NumberInput(
                attrs={
                    "class": "form-control form-control-lg",
                }
            ),
            "consumable": ConsumablesWidget,
            "accessories": AccessoriesWidget,
            "quantity": forms.NumberInput(
                attrs={
                    "class": "form-control form-control-lg",
                }
            ),
            "note": forms.Textarea(
                attrs={
                    "class": "form-control form-control-lg",
                }
            ),
            "code": forms.NumberInput(attrs={"class": "form-control form-control-lg"}),
            "cost": forms.NumberInput(attrs={"class": "form-control form-control-lg"}),
        }


class CategoriesForm(forms.ModelForm):
    """_CategoriesForm_"""

    class Meta:
        """_Class returns form of Categories model_

        Returns:
            model (Categories):
            fields (list[str]): _returns fields of model in form_
            widgets (dict[str,str]): _returns widgets of model in form_
        """

        model = Categories
        fields = ["name", "slug"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "slug": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
        }
