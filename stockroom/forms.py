from django import forms
from consumables.models import Cartridge
cartridge_score = 10
CARTRIDGE_QUANTITY_CHOICES = [(i, str(i)) for i in range(-10, cartridge_score)]


class StockAddCartridgeForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=CARTRIDGE_QUANTITY_CHOICES, coerce=int, label='Количество' )
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput, label='Обновить')
