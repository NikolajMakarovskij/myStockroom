from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from consumables.models import Consumables #Cartridge, Toner, Fotoval, Accumulator, Storage
from .stock import Stock
from .forms import StockAddForm, ConsumableInstallForm
from catalog.utils import menu


def stock(request):
    stock = Stock(request)
    return render(request, 'stock/stock_detail.html', {'stock': stock, 'menu':menu} )


@require_POST
def stock_add_consumable(request, consumable_id):
    stock = Stock(request)
    consumable = get_object_or_404(Consumables, id=consumable_id)
    form = StockAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.add_consumable(consumable=consumable,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'],
                 number_rack=cd['number_rack'],
                 number_shelf=cd['number_shelf'],
                 )
    return redirect('stockroom:stock')

def stock_remove_consumable(request, consumable_id):
    stock = Stock(request)
    consumable = get_object_or_404(Consumables, id=consumable_id)
    stock.remove_consumable(consumable)
    return redirect('stockroom:stock')

@require_POST
def printer_add_consumable(request, consumable_id):
    stock = Stock(request)
    consumable = get_object_or_404(Consumables, id=consumable_id)
    form = ConsumableInstallForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.printer_install_consumable(consumable=consumable,
                 quantity=cd['quantity'],
                 update_quantity=cd['update']
                 )
    return redirect('stockroom:stock')


@require_POST
def printer_add_cartridge(request, cartridge_id):
    stock = Stock(request)
    cartridge = get_object_or_404(Consumables, id=cartridge_id)
    form = ConsumableInstallForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.printer_install_consumable(consumable=cartridge,
                 quantity=cd['quantity'],
                 update_quantity=cd['update']
                 )
    return redirect('stockroom:stock')


@require_POST
def printer_add_toner(request, toner_id):
    stock = Stock(request)
    toner = get_object_or_404(Consumables, id=toner_id)
    form = ConsumableInstallForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.printer_install_consumable(consumable=toner,
                 quantity=cd['quantity'],
                 update_quantity=cd['update']
                 )
    return redirect('stockroom:stock')


@require_POST
def printer_add_fotoval(request, fotoval_id):
    stock = Stock(request)
    fotoval = get_object_or_404(Consumables, id=fotoval_id)
    form = ConsumableInstallForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.printer_install_consumable(consumable=fotoval,
                 quantity=cd['quantity'],
                 update_quantity=cd['update']
                 )
    return redirect('stockroom:stock')

@require_POST
def printer_add_fotodrumm(request, fotodrumm_id):
    stock = Stock(request)
    fotodrumm = get_object_or_404(Consumables, id=fotodrumm_id)
    form = ConsumableInstallForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.printer_install_consumable(consumable=fotodrumm,
                 quantity=cd['quantity'],
                 update_quantity=cd['update']
                 )
    return redirect('stockroom:stock')


@require_POST
def ups_add_accumulator(request, accumulator_id):
    stock = Stock(request)
    accumulator = get_object_or_404(Consumables, id=accumulator_id)
    form = ConsumableInstallForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.printer_install_consumable(consumable=accumulator,
                 quantity=cd['quantity'],
                 update_quantity=cd['update']
                 )
    return redirect('stockroom:stock_detail')


@require_POST
def add_storage(request, storage_id):
    stock = Stock(request)
    storage = get_object_or_404(Consumables, id=storage_id)
    form = Consumables(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.printer_install_consumable(consumable=storage,
                 quantity=cd['quantity'],
                 update_quantity=cd['update']
                 )
    return redirect('stockroom:stock_detail')


