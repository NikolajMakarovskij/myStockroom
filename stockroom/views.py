from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from consumables.models import Consumables
from django.views import generic
from django.db.models import Q
from .stock import Stock, History
from .forms import StockAddForm, ConsumableInstallForm
from .models import Stockroom, Stock_cat
from django.core.cache import cache
from catalog.utils import DataMixin


#Склад расходников
class stockroomView(DataMixin, generic.ListView):
    template_name = 'stock/stock_list.html'
    model = Stockroom
    def get_context_data(self, *, object_list=None, **kwargs):
        stock_cat = cache.get('stock_cat')
        if not stock_cat:
            stock_cat = Stock_cat.objects.all()
            cache.set('print_cat', stock_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Склад", searchlink='stockroom:stock_search', menu_categories=stock_cat)
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
        stock_cat = cache.get('stock_cat')
        if not stock_cat:
            stock_cat = Stock_cat.objects.all()
            cache.set('print_cat', stock_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Склад", searchlink='stockroom:stock_search', menu_categories=stock_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = Stockroom.objects.filter(categories__slug=self.kwargs['category_slug'])
        return object_list        

#История склада расходников
class HistoryView(DataMixin, generic.ListView):
    template_name = 'stock/history_list.html'
    model = History
    def get_context_data(self, *, object_list=None, **kwargs):
        stock_cat = cache.get('stock_cat')
        if not stock_cat:
            stock_cat = Stock_cat.objects.all()
            cache.set('stock_cat', stock_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="История", searchlink='stockroom:history_search', menu_categories=stock_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = '' 
        object_list = History.objects.filter(
                Q(consumable__icontains=query) | 
                Q(categories__name__icontains=query) |
                Q(dateInstall__icontains=query) |
                Q(user__icontains=query) 
        )
        return object_list

class HistoryCategoriesView(DataMixin, generic.ListView):
    template_name = 'stock/history_list.html'
    model = History
    
    def get_context_data(self, *, object_list=None, **kwargs ):
        stock_cat = cache.get('stock_cat')
        if not stock_cat:
            stock_cat = Stock_cat.objects.all()
            cache.set('stock_cat', stock_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="История", searchlink='stockroom:history_search', menu_categories=stock_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = History.objects.filter(categories__slug=self.kwargs['category_slug'])
        return object_list     


@require_POST
def stock_add_consumable(request, consumable_id):
    username = request.user.username
    stock = Stock(request)
    consumable = get_object_or_404(Consumables, id=consumable_id)
    form = StockAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.add_consumable(consumable=consumable,
                quantity=cd['quantity'],
                number_rack=cd['number_rack'],
                number_shelf=cd['number_shelf'],
                username = username,
                )
    return redirect('stockroom:stock_list')

def stock_remove_consumable(request, consumable_id):
    username = request.user.username
    stock = Stock(request)
    consumable = get_object_or_404(Consumables, id=consumable_id)
    stock.remove_consumable(consumable, username = username,)
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




