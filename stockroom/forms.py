from django import forms
from consumables.models import Cartridge
cartridge_score = 5
CARTRIDGE_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, cartridge_score)]


class StockAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=CARTRIDGE_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)