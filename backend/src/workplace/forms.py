from django import forms

from core.utils import BaseModelSelect2WidgetMixin

from .models import Room, Workplace


class RoomWidget(BaseModelSelect2WidgetMixin):
    """_RoomWidget_
    Autocomplete plugin for the room selection field

    Returns:
        empty_label (str): _value of empty_label_
        model (Room):
        querysets (Room): _returns querysets of model in form_
        search_fields (list[str]): _fields of the model to search for are specified_
    """

    empty_label = "--выбрать--"
    model = Room
    queryset = Room.objects.all().order_by("name")
    search_fields = [
        "name__icontains",
        "floor__icontains",
        "building__icontains",
    ]


class WorkplaceForm(forms.ModelForm):
    """_WorkplaceForm_"""

    class Meta:
        """_Class returns form of Workplace model_

        Returns:
            model (Workplace):
            fields (list[str]): _returns fields of model in form_
            widgets (dict[str,str]): _returns widgets of model in form_
        """

        model = Workplace
        fields = [
            "name",
            "room",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "room": RoomWidget,
        }


class RoomForm(forms.ModelForm):
    """_RoomForm_"""

    class Meta:
        """_Class returns form of Room model_

        Returns:
            model (Room):
            fields (list[str]): _returns fields of model in form_
            widgets (dict[str,str]): _returns widgets of model in form_
        """

        model = Room
        fields = [
            "name",
            "floor",
            "building",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "floor": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "building": forms.TextInput(
                attrs={"class": "form-control form-control-lg"}
            ),
        }
