from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from consumables.models import cartridge, fotoval, toner, accumulator
from .stock import Stock
from .forms import StockAddProductForm


@require_POST
def stock_add(request, cartridge_id):
    stock = Stock(request)
    cartridge = get_object_or_404(cartridge, id=cartridge_id)
    form = StockAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.add(cartridge=cartridge,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('stock:stock_detail')

def stock_remove(request, cartridge_id):
    stock = Stock(request)
    cartridge = get_object_or_404(cartridge, id=cartridge_id)
    stock.remove(cartridge)
    return redirect('stock:stock_detail')

def stock_detail(request):
    stock = Stock(request)
    return render(request, 'stock/detail.html', {'stock': stock})
