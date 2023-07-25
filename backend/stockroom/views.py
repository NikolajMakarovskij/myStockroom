from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.views import generic
from django.views.decorators.http import require_POST
from core.utils import DataMixin
from consumables.models import Consumables, Accessories
from device.models import Device
from .forms import StockAddForm, ConsumableInstallForm, MoveDeviceForm
from .models import (
    Stockroom, StockDev, StockAcc,
    History, HistoryAcc, HistoryDev,
    StockCat, CategoryAcc, CategoryDev
)
from .tasks import ConStockTasks, AccStockTasks, DevStockTasks


# Stock index
class StockroomIndexView(LoginRequiredMixin, DataMixin, generic.TemplateView):
    """
    Index
    """
    template_name = 'stock/stock_index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Расходники и комплектующие",
            searchlink='stockroom:stock_search',
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


# Stock consumables
class StockroomView(LoginRequiredMixin, DataMixin, generic.ListView):
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
            menu_categories=stock_cat
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            query = ''
        object_list = Stockroom.objects.filter(
            Q(stock_model__name__icontains=query) |
            Q(stock_model__manufacturer__name__icontains=query) |
            Q(stock_model__categories__name__icontains=query) |
            Q(stock_model__buhCode__icontains=query) |
            Q(stock_model__quantity__icontains=query) |
            Q(stock_model__serial__icontains=query) |
            Q(stock_model__invent__icontains=query) |
            Q(dateInstall__icontains=query) |
            Q(dateAddToStock__icontains=query)
        ).select_related(
            'stock_model',
            'stock_model__manufacturer',
            'stock_model__categories'
        )
        return object_list


class StockroomCategoriesView(LoginRequiredMixin, DataMixin, generic.ListView):
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
            menu_categories=stock_cat
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = Stockroom.objects.filter(
            categories__slug=self.kwargs['category_slug'])
        return object_list


# History of stock_model stock
class HistoryView(LoginRequiredMixin, DataMixin, generic.ListView):
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


class HistoryCategoriesView(LoginRequiredMixin, DataMixin, generic.ListView):
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


@require_POST
def stock_add_consumable(request, consumable_id):
    username = request.user.username
    consumable = get_object_or_404(Consumables, id=consumable_id)
    stock = ConStockTasks
    form = StockAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.add_to_stock(
            stock,
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


def stock_remove_consumable(request, consumable_id):
    username = request.user.username
    consumable = get_object_or_404(Consumables, id=consumable_id)
    stock = ConStockTasks
    stock.remove_from_stock(stock, model_id=consumable.id, username=username)
    messages.add_message(
        request,
        level=messages.SUCCESS,
        message=f"{consumable.name} успешно удален со склада",
        extra_tags='Успешно удален'
    )
    return redirect('stockroom:stock_list')


@require_POST
def device_add_consumable(request, consumable_id):
    username = request.user.username
    get_device_id = request.session['get_device_id']
    consumable = get_object_or_404(Consumables, id=consumable_id)
    stock = ConStockTasks
    form = ConsumableInstallForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.add_to_device(
            stock,
            model_id=consumable.id,
            device=get_device_id,
            quantity=cd['quantity'],
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


# Stock stock_model
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
            Q(stock_model__buhCode__icontains=query) |
            Q(stock_model__quantity__icontains=query) |
            Q(stock_model__serial__icontains=query) |
            Q(stock_model__invent__icontains=query) |
            Q(dateInstall__icontains=query) |
            Q(dateAddToStock__icontains=query)
        ).select_related('stock_model', 'stock_model__manufacturer', 'stock_model__categories')
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
        object_list = StockAcc.objects.filter(categories__slug=self.kwargs['category_slug'])
        return object_list


# History of stock_model stock
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


@require_POST
def stock_add_accessories(request, accessories_id):
    username = request.user.username
    accessories = get_object_or_404(Accessories, id=accessories_id)
    stock = AccStockTasks
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
    stock = AccStockTasks
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
    stock = AccStockTasks
    accessories = get_object_or_404(Accessories, id=accessories_id)
    form = ConsumableInstallForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.add_to_device(
            stock,
            model_id=accessories.id,
            device=get_device_id,
            quantity=cd['quantity'],
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


# Device stock
class StockDevView(LoginRequiredMixin, DataMixin, generic.ListView):
    template_name = 'stock/stock_dev_list.html'
    model = StockDev

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_dev = cache.get('cat_dev')
        if not cat_dev:
            cat_dev = CategoryDev.objects.all()
            cache.set('cat_dev', cat_dev, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Склад устройств", searchlink='stockroom:stock_dev_search',
                                      menu_categories=cat_dev)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            query = ''
        object_list = StockDev.objects.filter(
            Q(stock_model__name__icontains=query) |
            Q(stock_model__manufacturer__name__icontains=query) |
            Q(stock_model__categories__name__icontains=query) |
            Q(stock_model__quantity__icontains=query) |
            Q(stock_model__serial__icontains=query) |
            Q(stock_model__invent__icontains=query) |
            Q(dateInstall__icontains=query) |
            Q(dateAddToStock__icontains=query)
        ).select_related('stock_model__manufacturer', 'stock_model__categories')
        return object_list


class StockDevCategoriesView(LoginRequiredMixin, DataMixin, generic.ListView):
    template_name = 'stock/stock_dev_list.html'
    model = StockDev

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_dev = cache.get('cat_dev')
        if not cat_dev:
            cat_dev = CategoryDev.objects.all()
            cache.set('cat_dev', cat_dev, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Склад устройств", searchlink='stockroom:stock_dev_search',
                                      menu_categories=cat_dev, )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = StockDev.objects.filter(categories__slug=self.kwargs['category_slug'])
        return object_list


# History of device stock
class HistoryDevView(LoginRequiredMixin, DataMixin, generic.ListView):
    template_name = 'stock/history_dev_list.html'
    model = HistoryDev

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_dev = cache.get('cat_dev')
        if not cat_dev:
            cat_dev = CategoryDev.objects.all()
            cache.set('cat_dev', cat_dev, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="История устройств", searchlink='stockroom:history_dev_search',
                                      menu_categories=cat_dev)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            query = ''
        object_list = HistoryDev.objects.filter(
            Q(stock_model__icontains=query) |
            Q(categories__name__icontains=query) |
            Q(status__icontains=query) |
            Q(dateInstall__icontains=query) |
            Q(user__icontains=query)
        )
        return object_list


class HistoryDevCategoriesView(LoginRequiredMixin, DataMixin, generic.ListView):
    template_name = 'stock/history_dev_list.html'
    model = HistoryDev

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_dev = cache.get('cat_dev')
        if not cat_dev:
            cat_dev = CategoryDev.objects.all()
            cache.set('cat_dev', cat_dev, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="История устройств", searchlink='stockroom:history_dev_search',
                                      menu_categories=cat_dev)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = HistoryDev.objects.filter(categories__slug=self.kwargs['category_slug'])
        return object_list


@require_POST
def stock_add_device(request, device_id):
    username = request.user.username
    stock = DevStockTasks
    device = get_object_or_404(Device, id=device_id)
    form = StockAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.add_to_stock_device(
            stock,
            model_id=device.id,
            quantity=cd['quantity'],
            number_rack=cd['number_rack'],
            number_shelf=cd['number_shelf'],
            username=username,
        )
        messages.add_message(request,
                             level=messages.SUCCESS,
                             message=f"Устройство {device.name} в количестве {str(cd['quantity'])} шт."
                                     f"успешно добавлено на склад",
                             extra_tags='Успешно добавлен'
                             )
    else:
        messages.add_message(request,
                             level=messages.ERROR,
                             message=f"Не удалось добавить {device.name} на склад",
                             extra_tags='Ошибка формы'
                             )
    return redirect('stockroom:stock_dev_list')


def stock_remove_device(request, devices_id):
    username = request.user.username
    device = get_object_or_404(Device, id=devices_id)
    stock = DevStockTasks
    stock.remove_device_from_stock(stock, model_id=device.id, username=username, )
    messages.add_message(request,
                         level=messages.SUCCESS,
                         message=f"{device.name} успешно удален со склада",
                         extra_tags='Успешно удален'
                         )
    return redirect('stockroom:stock_dev_list')


@require_POST
def move_device_from_stock(request, device_id):
    username = request.user.username
    device = get_object_or_404(Device, id=device_id)
    stock = DevStockTasks
    form = MoveDeviceForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        workplace_ = cd['workplace']
        stock.move_device(
            stock,
            model_id=device.id,
            workplace=workplace_.name,
            username=username,
        )
        messages.add_message(request,
                             level=messages.SUCCESS,
                             message=f"Устройство перемещено на рабочее место.",
                             extra_tags='Успешное списание'
                             )
    else:
        messages.add_message(request,
                             level=messages.ERROR,
                             message=f"Не удалось переместить устройство.",
                             extra_tags='Ошибка формы'
                             )
    return redirect('stockroom:stock_dev_list')
