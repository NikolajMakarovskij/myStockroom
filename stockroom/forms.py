from django import forms
from consumables.models import cartridge, toner, fotoval, accumulator

CARTRIDGE_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, cartridge.score)]


class StockAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=CARTRIDGE_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)