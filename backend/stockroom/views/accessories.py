from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.views import generic
from django.views.decorators.http import require_POST

from consumables.models import Accessories
from core.utils import DataMixin
from stockroom.forms import StockAddForm, ConsumableInstallForm
from stockroom.models.accessories import StockAcc, HistoryAcc, CategoryAcc
from stockroom.stock.stock import AccStock


# accessories
class StockAccView(LoginRequiredMixin, DataMixin, generic.ListView):
    template_name = 'stock/stock_acc_list.html'
    model = StockAcc

    def get_context_data(self, *, object_list=None, **kwargs):
        history = HistoryAcc.objects.all()[:5]
        cat_acc = cache.get('cat_acc')
        if not cat_acc:
            cat_acc = CategoryAcc.objects.all()
            cache.set('cat_acc', cat_acc, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Склад комплектующих", searchlink='stockroom:stock_acc_search',
                                      menu_categories=cat_acc, historyacc_list=history)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            query = ''
        object_list = StockAcc.objects.filter(
            Q(stock_model__name__icontains=query) |
            Q(stock_model__manufacturer__name__icontains=query) |
            Q(stock_model__categories__name__icontains=query) |
            Q(stock_model__quantity__icontains=query) |
            Q(stock_model__serial__icontains=query) |
            Q(stock_model__invent__icontains=query) |
            Q(dateInstall__icontains=query) |
            Q(dateAddToStock__icontains=query)
        ).select_related('stock_model','stock_model__categories',).prefetch_related('stock_model__device')
        return object_list


class StockAccCategoriesView(LoginRequiredMixin, DataMixin, generic.ListView):
    template_name = 'stock/stock_acc_list.html'
    model = StockAcc

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_acc = cache.get('cat_acc')
        if not cat_acc:
            cat_acc = CategoryAcc.objects.all()
            cache.set('cat_acc', cat_acc, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Склад комплектующих", searchlink='stockroom:stock_acc_search',
                                      menu_categories=cat_acc)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = StockAcc.objects.filter(categories__slug=self.kwargs['category_slug']).select_related(
            'stock_model','stock_model__categories',).prefetch_related('stock_model__device')
        return object_list


# History
class HistoryAccView(LoginRequiredMixin, DataMixin, generic.ListView):
    template_name = 'stock/history_acc_list.html'
    model = HistoryAcc

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_acc = cache.get('cat_acc')
        if not cat_acc:
            cat_acc = CategoryAcc.objects.all()
            cache.set('cat_acc', cat_acc, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="История комплектующих", searchlink='stockroom:history_acc_search',
                                      menu_categories=cat_acc)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            query = ''
        object_list = HistoryAcc.objects.filter(
            Q(stock_model__icontains=query) |
            Q(device__icontains=query) |
            Q(categories__name__icontains=query) |
            Q(status__icontains=query) |
            Q(dateInstall__icontains=query) |
            Q(user__icontains=query)
        )
        return object_list


class HistoryAccCategoriesView(LoginRequiredMixin, DataMixin, generic.ListView):
    template_name = 'stock/history_acc_list.html'
    model = HistoryAcc

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_acc = cache.get('cat_acc')
        if not cat_acc:
            cat_acc = CategoryAcc.objects.all()
            cache.set('cat_acc', cat_acc, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="История комплектующих", searchlink='stockroom:history_acc_search',
                                      menu_categories=cat_acc)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = HistoryAcc.objects.filter(categories__slug=self.kwargs['category_slug'])
        return object_list


# Methods
@require_POST
def stock_add_accessories(request, accessories_id):
    username = request.user.username
    accessories = get_object_or_404(Accessories, id=accessories_id)
    stock = AccStock
    form = StockAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.add_to_stock(
            stock,
            model_id=accessories.id,
            quantity=cd['quantity'],
            number_rack=cd['number_rack'],
            number_shelf=cd['number_shelf'],
            username=username,
        )
        messages.add_message(request,
                             level=messages.SUCCESS,
                             message=f"Комплектующее {accessories.name} в количестве {str(cd['quantity'])} шт."
                                     f" успешно добавлен на склад",
                             extra_tags='Успешно добавлен'
                             )
    else:
        messages.add_message(request,
                             level=messages.ERROR,
                             message=f"Не удалось добавить {accessories.name} на склад",
                             extra_tags='Ошибка формы'
                             )
    return redirect('stockroom:stock_acc_list')


def stock_remove_accessories(request, accessories_id):
    username = request.user.username
    accessories = get_object_or_404(Accessories, id=accessories_id)
    stock = AccStock
    stock.remove_from_stock(stock, model_id=accessories.id, username=username, )
    messages.add_message(request,
                         level=messages.SUCCESS,
                         message=f"{accessories.name} успешно удален со склада",
                         extra_tags='Успешно удален'
                         )
    return redirect('stockroom:stock_acc_list')


@require_POST
def device_add_accessories(request, accessories_id):
    username = request.user.username
    get_device_id = request.session['get_device_id']
    stock = AccStock
    accessories = get_object_or_404(Accessories, id=accessories_id)
    form = ConsumableInstallForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        if accessories.quantity == 0:
            messages.add_message(request,
                                 level=messages.WARNING,
                                 message=f"Комплектующее {accessories.name} закончилось на складе.",
                                 extra_tags='Нет расходника'
                                 )
        else:
            stock.add_to_device(
                stock,
                model_id=accessories.id,
                device=get_device_id,
                quantity=cd['quantity'],
                note=cd['note'],
                username=username,
            )
            messages.add_message(request,
                                 level=messages.SUCCESS,
                                 message=f"Комплектующее {accessories.name} в количестве {str(cd['quantity'])} шт."
                                         f" успешно списан со склада",
                                 extra_tags='Успешное списание'
                                 )
    else:
        messages.add_message(request,
                             level=messages.ERROR,
                             message=f"Не удалось списать {accessories.name} со склада",
                             extra_tags='Ошибка формы'
                             )
    return redirect('stockroom:stock_acc_list')
