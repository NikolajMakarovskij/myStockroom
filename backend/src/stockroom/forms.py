from typing import List
from django import forms

from core.utils import BaseModelSelect2WidgetMixin
from device.models import Device
from workplace.models import Workplace

consumable_score: int = 11
CONSUMABLE_QUANTITY_CHOICES: List[tuple[int, str]] = [
    (i, str(i)) for i in range(0, consumable_score)
]
"""_CONSUMABLE_QUANTITY_CHOICES_

Other parameters:
    consumable_score (int): 

Returns:
    choices (List[tuple[int, str]]): _quantity_
"""

rack_score: int = 10
RACK_QUANTITY_CHOICES: List[tuple[int, str]] = [(i, str(i)) for i in range(1, rack_score)]
"""_RACK_QUANTITY_CHOICES_

Other parameters:
    rack_score (int): 

Returns:
    choices (List[tuple[int, str]]): _quantity_
"""

shelf_score: int = 20
SHELF_QUANTITY_CHOICES: List[tuple[int, str]] = [(i, str(i)) for i in range(1, shelf_score)]
"""_SHELF_QUANTITY_CHOICES_

Other parameters:
    shelf_score (int): 

Returns:
    choices (List[tuple[int, str]]): _quantity_
"""

device_score: int = 5
DEVICE_QUANTITY_CHOICES: List[tuple[int, str]] = [(i, str(i)) for i in range(1, device_score)]
"""_DEVICE_QUANTITY_CHOICES_

Other parameters:
    device_score (int): 

Returns:
    choices (List[tuple[int, str]]): _quantity_
"""


class StockAddForm(forms.Form):
    """_StockAddForm_
    the class returns a form for adding Accessories, Consumables or Device to the Stockroom

    Returns:
        quantity (TypedChoiceField): _quantity_
        number_rack (TypedChoiceField): _rack number_
        number_shelf (TypedChoiceField): _shelf number_
    """

    quantity = forms.TypedChoiceField(
        choices=CONSUMABLE_QUANTITY_CHOICES,
        coerce=int,
        label="Количество",
        widget=forms.Select(
            attrs={"class": "form-select form-select-lg btn-outline-dark"}
        ),
    )
    number_rack = forms.TypedChoiceField(
        choices=RACK_QUANTITY_CHOICES,
        coerce=int,
        label="Стеллаж",
        widget=forms.Select(
            attrs={"class": "form-select form-select-lg btn-outline-dark"}
        ),
    )
    number_shelf = forms.TypedChoiceField(
        choices=SHELF_QUANTITY_CHOICES,
        coerce=int,
        label="Полка",
        widget=forms.Select(
            attrs={"class": "form-select form-select-lg btn-outline-dark"}
        ),
    )


class ConsumableInstallForm(forms.Form):
    """_ConsumableInstallForm_
    the class returns a form for adding Accessories or Consumables to the Device

    Returns:
        quantity (TypedChoiceField): _quantity_
        note (CharField): _note_
    """

    quantity = forms.TypedChoiceField(
        choices=DEVICE_QUANTITY_CHOICES,
        coerce=int,
        label="Количество",
        widget=forms.Select(
            attrs={"class": "form-select form-select-lg btn-outline-dark"}
        ),
    )
    note = forms.CharField(
        required=False,
        label="Примечание",
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg btn-outline-dark"}
        ),
    )


class AddHistoryDeviceForm(forms.Form):
    """_AddHistoryDeviceForm_
    the class returns a form for adding history to the Device

    Returns:
        note (CharField): _note_
    """

    note = forms.CharField(
        required=False,
        label="Примечание",
        widget=forms.TextInput(
            attrs={"class": "form-control form-control-lg btn-outline-dark"}
        ),
    )


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


class MoveDeviceForm(forms.ModelForm):
    """_MoveDeviceFor_"""

    class Meta:
        """_Class returns form to moves the device to the workplace_

        Returns:
            model (Device):
            fields (list[str]): _returns fields of model in form_
            widgets (dict[str,str]): _returns widgets of model in form_
        """

        model = Device
        fields = ["workplace", "note"]
        widgets = {
            "workplace": WorkplaceWidget,
            "note": forms.TextInput(
                attrs={
                    "class": "js-example-placeholder-single js-states form-control form-control-lg",
                    "style": "width:100%",
                }
            ),
        }
