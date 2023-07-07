from django import forms
from catalog.utils import WidgetCanAdd
from .models import Room, Workplace


class WorkplaceForm(forms.ModelForm):
    class Meta:
        model = Workplace
        fields = ['name', 'room', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'room': WidgetCanAdd(Room, related_url="workplace:new-room",
                                 attrs={'class': 'input-group form-select form-select-lg'}),
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
