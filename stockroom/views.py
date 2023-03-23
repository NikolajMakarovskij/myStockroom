from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from consumables.models import Consumables
from django.views import generic
from django.db.models import Q
from .stock import Stock
from .forms import StockAddForm, ConsumableInstallForm
from .models import Stockroom, Categories
from printer.models import Printer
from catalog.utils import DataMixin


#Расходники
class stockroomView(DataMixin, generic.ListView):
    template_name = 'stock/stock_list.html'
    model = Stockroom
    menu_categories = Categories.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        menu_categories = Categories.objects.all()
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Склад", searchlink='stockroom:stock_search', menu_categories=menu_categories)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = Stockroom.objects.filter(
                Q(consumables__name__icontains=query) | 
                Q(consumables__manufacturer__name__icontains=query) |
                Q(consumables__categories__name__icontains=query) |
                Q(consumables__buhCode__icontains=query) |
                Q(consumables__score__icontains=query) |
                Q(consumables__serial__icontains=query) |
                Q(consumables__invent__icontains=query) |
                Q(dateInstall__icontains=query) |
                Q(dateAddToStock__icontains=query) 
        ).select_related('consumables', 'consumables__manufacturer', 'consumables__categories')
        return object_list

class stockroomCategoriesView(DataMixin, generic.ListView):
    template_name = 'stock/stock_list.html'
    model = Stockroom
    
    def get_context_data(self, *, object_list=None, **kwargs ):
        menu_categories = Categories.objects.all()
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Склад", searchlink='stockroom:stock_search', menu_categories=menu_categories)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = Stockroom.objects.filter(categories__slug=self.kwargs['category_slug'])
        return object_list        


@require_POST
def stock_add_consumable(request, consumable_id):
    stock = Stock(request)
    consumable = get_object_or_404(Consumables, id=consumable_id)
    form = StockAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.add_consumable(consumable=consumable,
                 quantity=cd['quantity'],
                 number_rack=cd['number_rack'],
                 number_shelf=cd['number_shelf'],
                 )
    return redirect('stockroom:stock_list')

def stock_remove_consumable(request, consumable_id):
    stock = Stock(request)
    consumable = get_object_or_404(Consumables, id=consumable_id)
    stock.remove_consumable(consumable)
    return redirect('stockroom:stock_list')

@require_POST
def device_add_consumable(request, consumable_id):
    username = request.user.username
    stock = Stock(request)
    consumable = get_object_or_404(Consumables, id=consumable_id)
    form = ConsumableInstallForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.device_add_consumable(consumable=consumable,
                quantity=cd['quantity'],
                username = username,
                )
    return redirect('stockroom:stock_list')


@require_POST
def printer_add_cartridge(request, cartridge_id):
    username = request.user.username
    stock = Stock(request)
    cartridge = get_object_or_404(Consumables, id=cartridge_id)
    form = ConsumableInstallForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.printer_install_consumable(consumable=cartridge,
                quantity=cd['quantity'],
                username = username,
                )
    return redirect('stockroom:stock_list')


@require_POST
def printer_add_toner(request, toner_id):
    username = request.user.username
    stock = Stock(request)
    toner = get_object_or_404(Consumables, id=toner_id)
    form = ConsumableInstallForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.printer_install_consumable(consumable=toner,
                quantity=cd['quantity'],
                username = username,
                )
    return redirect('stockroom:stock_list')


@require_POST
def printer_add_fotoval(request, fotoval_id):
    username = request.user.username
    stock = Stock(request)
    fotoval = get_object_or_404(Consumables, id=fotoval_id)
    form = ConsumableInstallForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.printer_install_consumable(consumable=fotoval,
                quantity=cd['quantity'],
                username =username,
                )
    return redirect('stockroom:stock_list')

@require_POST
def printer_add_fotodrumm(request, fotodrumm_id):
    username = request.user.username
    stock = Stock(request)
    fotodrumm = get_object_or_404(Consumables, id=fotodrumm_id)
    form = ConsumableInstallForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.printer_install_consumable(consumable=fotodrumm,
                quantity=cd['quantity'],
                username = username,
                )
    return redirect('stockroom:stock_list')


@require_POST
def ups_add_accumulator(request, accumulator_id):
    username = request.user.username
    stock = Stock(request)
    accumulator = get_object_or_404(Consumables, id=accumulator_id)
    form = ConsumableInstallForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.printer_install_consumable(consumable=accumulator,
                quantity=cd['quantity'],
                username = username,
                )
    return redirect('stockroom:stock_list')


@require_POST
def add_storage(request, storage_id):
    username = request.user.username
    stock = Stock(request)
    storage = get_object_or_404(Consumables, id=storage_id)
    form = Consumables(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.printer_install_consumable(consumable=storage,
                quantity=cd['quantity'],
                username = username,
                )
    return redirect('stockroom:stock_list')


