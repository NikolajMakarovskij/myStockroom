from django import forms
from core.utils import BaseModelSelect2WidgetMixin
from .models import Categories, Accounting
from consumables.models import Consumables, Accessories


class CategoryWidget(BaseModelSelect2WidgetMixin):
    empty_label = "--выбрать--"
    model = Categories
    queryset = Categories.objects.all().order_by("name")
    search_fields = [
        "name__icontains"
    ]


class ConsumablesWidget(BaseModelSelect2WidgetMixin):
    empty_label = "--выбрать--"
    model = Consumables
    queryset = Consumables.objects.all().order_by("name")
    search_fields = [
        "name__icontains",
        "categories__name__icontains",
    ]


class AccessoriesWidget(BaseModelSelect2WidgetMixin):
    empty_label = "--выбрать--"
    model = Accessories
    queryset = Accessories.objects.all().order_by("name")
    search_fields = [
        "name__icontains"
        "categories__name__icontains",
    ]


class AccountingForm(forms.ModelForm):
    class Meta:
        model = Accounting
        fields = ['name', 'categories', 'account', 'consumable', 'accessories',
                  'code', 'quantity', 'cost', 'note']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'categories': CategoryWidget,
            'account': forms.NumberInput(attrs={'class': 'form-control form-control-lg', }),
            'consumable': ConsumablesWidget,
            'accessories': AccessoriesWidget,
            'quantity': forms.NumberInput(attrs={'class': 'form-control form-control-lg', }),
            'note': forms.Textarea(attrs={'class': 'form-control form-control-lg', }),
            'code': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        }


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name', 'slug']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'slug': forms.TextInput(attrs={'class': 'form-control form-control-lg'})
        }
