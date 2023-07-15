from django import forms
from device.models import Device
from workplace.models import Workplace
from core.utils import BaseModelSelect2WidgetMixin, WidgetCanAdd

consumable_score = 11
CONSUMABLE_QUANTITY_CHOICES = [(i, str(i)) for i in range(0, consumable_score)]
rack_score = 10
RACK_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, rack_score)]
shelf_score = 20
SHELF_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, shelf_score)]
device_score = 5
DEVICE_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, device_score)]


class StockAddForm(forms.Form):
    """
    Форма добавляет расходник на склад. Добавляется в template и DetailView расходника 
    """
    quantity = forms.TypedChoiceField(choices=CONSUMABLE_QUANTITY_CHOICES, coerce=int, label='Количество',
                                      widget=forms.Select(
                                          attrs={'class': 'form-select form-select-lg btn-outline-dark'}))
    number_rack = forms.TypedChoiceField(choices=RACK_QUANTITY_CHOICES, coerce=int, label='Стеллаж',
                                         widget=forms.Select(
                                             attrs={'class': 'form-select form-select-lg btn-outline-dark'}))
    number_shelf = forms.TypedChoiceField(choices=SHELF_QUANTITY_CHOICES, coerce=int, label='Полка',
                                          widget=forms.Select(
                                              attrs={'class': 'form-select form-select-lg btn-outline-dark'}))


class ConsumableInstallForm(forms.Form):
    """
    Форма использования расходника в технике. Добавляется в template и DetailView техники
    """
    quantity = forms.TypedChoiceField(choices=DEVICE_QUANTITY_CHOICES, coerce=int, label='Количество',
                                      widget=forms.Select(
                                          attrs={'class': 'form-select form-select-lg btn-outline-dark'}))


class WorkplaceWidget(BaseModelSelect2WidgetMixin):
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
    class Meta:
        model = Device
        fields = ['workplace']
        widgets = {
            'workplace': WidgetCanAdd(Workplace, related_url="workplace:new-workplace",
                                      attrs={'class': 'form-select form-select-lg'}),

        }
