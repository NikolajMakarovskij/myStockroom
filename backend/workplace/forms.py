from django import forms
from catalog.utils import BaseModelSelect2WidgetMixin
from .models import Room, Workplace


class RoomWidget(BaseModelSelect2WidgetMixin):
    empty_label = "--выбрать--"
    model = Room
    queryset = Room.objects.all().order_by("name")
    search_fields = [
        "name__icontains",
        "floor__icontains",
        "building__icontains",
    ]


class WorkplaceForm(forms.ModelForm):
    class Meta:
        model = Workplace
        fields = ['name', 'room', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'room': RoomWidget
        }


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'floor', 'building', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'floor': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'building': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        }
