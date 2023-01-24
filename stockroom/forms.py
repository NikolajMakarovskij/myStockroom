from django import forms
cartridge_score = 10
CARTRIDGE_QUANTITY_CHOICES = [(i, str(i)) for i in range(0, cartridge_score)]
rack_score = 10
RACK_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, rack_score)]
shelf_score = 20
SHELF_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, shelf_score)]
printer_score = 5
PRINTER_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, printer_score)]


class StockAddForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=CARTRIDGE_QUANTITY_CHOICES, coerce=int, label='Количество', 
                                            widget=forms.Select(attrs={'class':'form-select form-select-lg btn-outline-dark'}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput, label='Обновить')
    number_rack = forms.TypedChoiceField(choices=RACK_QUANTITY_CHOICES, coerce=int, label='Стеллаж', 
                                            widget=forms.Select(attrs={'class':'form-select form-select-lg btn-outline-dark'}))
    number_shelf = forms.TypedChoiceField(choices=SHELF_QUANTITY_CHOICES, coerce=int, label='Полка', 
                                            widget=forms.Select(attrs={'class':'form-select form-select-lg btn-outline-dark'}))

class PrinterAddForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRINTER_QUANTITY_CHOICES, coerce=int, label='Количество', 
                                            widget=forms.Select(attrs={'class':'form-select form-select-lg btn-outline-dark'}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput, label='Обновить')

