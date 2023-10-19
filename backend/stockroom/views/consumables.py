from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.core.cache import cache
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.views import generic
from django.views.decorators.http import require_POST
from rest_framework import viewsets
from consumables.models import Consumables
from core.utils import DataMixin
from stockroom.forms import StockAddForm, ConsumableInstallForm
from stockroom.models.consumables import Stockroom, History, StockCat
from stockroom.serializers.consumables import StockModelSerializer
from stockroom.stock.stock import ConStock


class StockroomView(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView):
    permission_required = 'stockroom.view_stockroom'
    template_name = 'stock/stock_list.html'
    model = Stockroom

    def get_context_data(self, *, object_list=None, **kwargs):
        stock_cat = cache.get('stock_cat')
        if not stock_cat:
            stock_cat = StockCat.objects.all()
            cache.set('stock_cat', stock_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Склад расходников",
            searchlink='stockroom:stock_search',
            menu_categories=stock_cat,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            query = ''
        object_list = Stockroom.objects.filter(
            Q(stock_model__name__icontains=query) |
            Q(stock_model__description__icontains=query) |
            Q(stock_model__note__icontains=query) |
            Q(stock_model__device__name__icontains=query) |
            Q(stock_model__device__workplace__name__icontains=query) |
            Q(stock_model__device__workplace__room__name__icontains=query) |
            Q(stock_model__device__workplace__room__building__icontains=query) |
            Q(stock_model__device__workplace__employee__name__icontains=query) |
            Q(stock_model__device__workplace__employee__surname__icontains=query) |
            Q(stock_model__device__workplace__employee__last_name__icontains=query) |
            Q(stock_model__manufacturer__name__icontains=query) |
            Q(stock_model__categories__name__icontains=query) |
            Q(stock_model__quantity__icontains=query) |
            Q(stock_model__serial__icontains=query) |
            Q(stock_model__invent__icontains=query) |
            Q(dateInstall__icontains=query) |
            Q(dateAddToStock__icontains=query)
        ).select_related('stock_model', 'stock_model__categories').prefetch_related('stock_model__device').distinct()
        return object_list


class StockroomCategoriesView(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView):
    permission_required = 'stockroom.view_stockroom'
    template_name = 'stock/stock_list.html'
    model = Stockroom

    def get_context_data(self, *, object_list=None, **kwargs):
        stock_cat = cache.get('stock_cat')
        if not stock_cat:
            stock_cat = StockCat.objects.all()
            cache.set('stock_cat', stock_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Склад расходников",
            searchlink='stockroom:stock_search',
            menu_categories=stock_cat,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = Stockroom.objects.filter(
            categories__slug=self.kwargs['category_slug']).select_related(
            'stock_model', 'stock_model__categories').prefetch_related('stock_model__device').distinct()
        return object_list


class StockRestView(DataMixin, viewsets.ModelViewSet):
    queryset = Stockroom.objects.all()
    serializer_class = StockModelSerializer


# History
class HistoryView(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView):
    permission_required = 'stockroom.view_history'
    template_name = 'stock/history_list.html'
    model = History

    def get_context_data(self, *, object_list=None, **kwargs):
        stock_cat = cache.get('stock_cat')
        if not stock_cat:
            stock_cat = StockCat.objects.all()
            cache.set('stock_cat', stock_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="История расходников",
            searchlink='stockroom:history_search',
            menu_categories=stock_cat)
        context = dict(list(context.items()) + list(c_def.items())
                       )
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            query = ''
        object_list = History.objects.filter(
            Q(stock_model__icontains=query) |
            Q(categories__name__icontains=query) |
            Q(device__icontains=query) |
            Q(status__icontains=query) |
            Q(dateInstall__icontains=query) |
            Q(user__icontains=query)
        )
        return object_list


class HistoryCategoriesView(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView):
    permission_required = 'stockroom.view_history'
    template_name = 'stock/history_list.html'
    model = History

    def get_context_data(self, *, object_list=None, **kwargs):
        stock_cat = cache.get('stock_cat')
        if not stock_cat:
            stock_cat = StockCat.objects.all()
            cache.set('stock_cat', stock_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="История расходников",
            searchlink='stockroom:history_search',
            menu_categories=stock_cat
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = History.objects.filter(
            categories__slug=self.kwargs['category_slug'])
        return object_list


# Methods
@require_POST
@login_required
@permission_required('stockroom.add_consumables_to_stock', raise_exception=True)
def stock_add_consumable(request, consumable_id):
    username = request.user.username
    consumable = get_object_or_404(Consumables, id=consumable_id)
    stock = ConStock
    form = StockAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.add_to_stock(
            model_id=consumable.id,
            quantity=cd['quantity'],
            number_rack=cd['number_rack'],
            number_shelf=cd['number_shelf'],
            username=username,
        )
        messages.add_message(
            request,
            level=messages.SUCCESS,
            message=f"Расходник {consumable.name} в количестве {str(cd['quantity'])} шт."
                    f" успешно добавлен на склад",
            extra_tags='Успешно добавлен'
        )
    else:
        messages.add_message(
            request,
            level=messages.ERROR,
            message=f"Не удалось добавить {consumable.name} на склад",
            extra_tags='Ошибка формы'
        )
    return redirect('stockroom:stock_list')


@login_required
@permission_required('stockroom.remove_consumables_from_stock', raise_exception=True)
def stock_remove_consumable(request, consumable_id):
    username = request.user.username
    consumable = get_object_or_404(Consumables, id=consumable_id)
    stock = ConStock
    stock.remove_from_stock(model_id=consumable.id, username=username)
    messages.add_message(
        request,
        level=messages.SUCCESS,
        message=f"{consumable.name} успешно удален со склада",
        extra_tags='Успешно удален'
    )
    return redirect('stockroom:stock_list')


@require_POST
@login_required
@permission_required('stockroom.add_consumables_to_device', raise_exception=True)
def device_add_consumable(request, consumable_id):
    username = request.user.username
    get_device_id = request.session['get_device_id']
    consumable = get_object_or_404(Consumables, id=consumable_id)
    stock = ConStock
    form = ConsumableInstallForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        if consumable.quantity < cd['quantity']:
            messages.add_message(request,
                                 level=messages.WARNING,
                                 message=f"Не достаточно расходников {consumable.name} на складе.",
                                 extra_tags='Нет расходника'
                                 )
        else:
            stock.add_to_device(
                model_id=consumable.id,
                device=get_device_id,
                quantity=cd['quantity'],
                note=cd['note'],
                username=username,
            )
            messages.add_message(request,
                                 level=messages.SUCCESS,
                                 message=f"Расходник {consumable.name} в количестве {str(cd['quantity'])} шт."
                                         f" успешно списан со склада",
                                 extra_tags='Успешное списание'
                                 )
    else:
        messages.add_message(request,
                             level=messages.ERROR,
                             message=f"Не удалось списать {consumable.name} со склада",
                             extra_tags='Ошибка формы'
                             )
    return redirect('stockroom:stock_list')
