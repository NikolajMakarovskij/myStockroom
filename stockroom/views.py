from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from consumables.models import Cartridge, Toner, Fotoval, Accumulator, Storage
from .stock import Stock
from .forms import StockAddForm, PrinterAddForm
from catalog.utils import menu

@require_POST
def stock_add_cartridge(request, cartridge_id):
    stock = Stock(request)
    cartridge = get_object_or_404(Cartridge, id=cartridge_id)
    form = StockAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.add_cartridge(cartridge=cartridge,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'],
                 number_rack=cd['number_rack'],
                 number_shelf=cd['number_shelf'],
                 )
    return redirect('stockroom:stock_detail')

def stock_remove_cartridge(request, cartridge_id):
    stock = Stock(request)
    cartridge = get_object_or_404(Cartridge, id=cartridge_id)
    stock.remove_cartrige(cartridge)
    return redirect('stockroom:stock_detail')

@require_POST
def printer_add_cartridge(request, cartridge_id):
    stock = Stock(request)
    cartridge = get_object_or_404(Cartridge, id=cartridge_id)
    form = PrinterAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.printer_install_cartridge(cartridge=cartridge,
                 quantity=cd['quantity'],
                 update_quantity=cd['update']
                 )
    return redirect('stockroom:stock_detail')

@require_POST
def stock_add_toner(request, toner_id):
    stock = Stock(request)
    toner = get_object_or_404(Toner, id=toner_id)
    form = StockAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.add_toner(toner=toner,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'],
                 number_rack=cd['number_rack'],
                 number_shelf=cd['number_shelf'],
                 )
    return redirect('stockroom:stock_detail')

def stock_remove_toner(request, toner_id):
    stock = Stock(request)
    toner = get_object_or_404(Toner, id=toner_id)
    stock.remove_toner(toner)
    return redirect('stockroom:stock_detail')

@require_POST
def printer_add_toner(request, toner_id):
    stock = Stock(request)
    toner = get_object_or_404(Toner, id=toner_id)
    form = PrinterAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.printer_install_toner(toner=toner,
                 quantity=cd['quantity'],
                 update_quantity=cd['update']
                 )
    return redirect('stockroom:stock_detail')

@require_POST
def stock_add_fotoval(request, fotoval_id):
    stock = Stock(request)
    fotoval = get_object_or_404(Fotoval, id=fotoval_id)
    form = StockAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.add_fotoval(fotoval=fotoval,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'],
                 number_rack=cd['number_rack'],
                 number_shelf=cd['number_shelf'],
                 )
    return redirect('stockroom:stock_detail')

def stock_remove_fotoval(request, fotoval_id):
    stock = Stock(request)
    fotoval = get_object_or_404(Fotoval, id=fotoval_id)
    stock.remove_fotoval(fotoval)
    return redirect('stockroom:stock_detail')

@require_POST
def printer_add_fotoval(request, fotoval_id):
    stock = Stock(request)
    fotoval = get_object_or_404(Fotoval, id=fotoval_id)
    form = PrinterAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.printer_install_fotoval(fotoval=fotoval,
                 quantity=cd['quantity'],
                 update_quantity=cd['update']
                 )
    return redirect('stockroom:stock_detail')

@require_POST
def stock_add_accumulator(request, accumulator_id):
    stock = Stock(request)
    accumulator = get_object_or_404(Accumulator, id=accumulator_id)
    form = StockAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.add_accumulator(accumulator=accumulator,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'],
                 number_rack=cd['number_rack'],
                 number_shelf=cd['number_shelf'],
                 )
    return redirect('stockroom:stock_detail')

def stock_remove_accumulator(request, accumulator_id):
    stock = Stock(request)
    accumulator = get_object_or_404(Accumulator, id=accumulator_id)
    stock.remove_accumulator(accumulator)
    return redirect('stockroom:stock_detail')

@require_POST
def ups_add_accumulator(request, accumulator_id):
    stock = Stock(request)
    accumulator = get_object_or_404(Accumulator, id=accumulator_id)
    form = PrinterAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.ups_install_accumulator(accumulator=accumulator,
                 quantity=cd['quantity'],
                 update_quantity=cd['update']
                 )
    return redirect('stockroom:stock_detail')

@require_POST
def stock_add_storage(request, storage_id):
    stock = Stock(request)
    storage = get_object_or_404(Storage, id=storage_id)
    form = StockAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.add_storage(storage=storage,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'],
                 number_rack=cd['number_rack'],
                 number_shelf=cd['number_shelf'],
                 )
    return redirect('stockroom:stock_detail')

def stock_remove_storage(request, storage_id):
    stock = Stock(request)
    storage = get_object_or_404(Storage, id=storage_id)
    stock.remove_storage(storage)
    return redirect('stockroom:stock_detail')

@require_POST
def add_storage(request, storage_id):
    stock = Stock(request)
    storage = get_object_or_404(Storage, id=storage_id)
    form = PrinterAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.install_storage(storage=storage,
                 quantity=cd['quantity'],
                 update_quantity=cd['update']
                 )
    return redirect('stockroom:stock_detail')

def stock_detail(request):
    stock = Stock(request)
    return render(request, 'stock/stock_detail.html', {'stock': stock, 'menu':menu} )
