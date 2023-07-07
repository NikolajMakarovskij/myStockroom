from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from consumables.models import Consumables, Accessories
from device.models import Device
from django.views import generic
from django.db.models import Q
from .stock import Stock
from .forms import StockAddForm, ConsumableInstallForm
from .models import (
    Stockroom, StockDev, StockAcc,
    History, HistoryAcc, HistoryDev,
    StockCat, CategoryAcc, CategoryDev
)
from django.core.cache import cache
from catalog.utils import DataMixin, menu
from django.contrib import messages


# Склад главная
class StockroomIndexView(generic.TemplateView):
    """
    Главная
    """
    template_name = 'stock/stock_index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Расходники и комплектующие'
        context['menu'] = menu
        return context


# Склад расходников
class StockroomView(DataMixin, generic.ListView):
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
            Q(consumables__name__icontains=query) |
            Q(consumables__manufacturer__name__icontains=query) |
            Q(consumables__categories__name__icontains=query) |
            Q(consumables__buhCode__icontains=query) |
            Q(consumables__score__icontains=query) |
            Q(consumables__serial__icontains=query) |
            Q(consumables__invent__icontains=query) |
            Q(dateInstall__icontains=query) |
            Q(dateAddToStock__icontains=query) |
            Q(room__name__icontains=query)
        ).select_related(
            'consumables',
            'consumables__manufacturer',
            'consumables__categories'
        )
        return object_list


class StockroomCategoriesView(DataMixin, generic.ListView):
    template_name = 'stock/stock_list.html'
    model = Stockroom

    def get_context_data(self, *, object_list=None, **kwargs):
        stock_cat = cache.get('stock_cat')
        if not stock_cat:
            stock_cat = StockCat.objects.all()
            cache.set('stock_cat', stock_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Склад",
            searchlink='stockroom:stock_search',
            menu_categories=stock_cat
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = Stockroom.objects.filter(
            categories__slug=self.kwargs['category_slug'])
        return object_list


# История склада расходников
class HistoryView(DataMixin, generic.ListView):
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
            Q(consumable__icontains=query) |
            Q(categories__name__icontains=query) |
            Q(device__icontains=query) |
            Q(status__icontains=query) |
            Q(dateInstall__icontains=query) |
            Q(user__icontains=query)
        )
        return object_list


class HistoryCategoriesView(DataMixin, generic.ListView):
    template_name = 'stock/history_list.html'
    model = History

    def get_context_data(self, *, object_list=None, **kwargs):
        stock_cat = cache.get('stock_cat')
        if not stock_cat:
            stock_cat = StockCat.objects.all()
            cache.set('stock_cat', stock_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="История",
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
    stock = Stock(request)
    consumable = get_object_or_404(Consumables, id=consumable_id)
    form = StockAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.add_consumable(
            consumable=consumable,
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
    stock = Stock(request)
    consumable = get_object_or_404(Consumables, id=consumable_id)
    stock.remove_consumable(consumable, username=username)
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
    stock = Stock(request)
    consumable = get_object_or_404(Consumables, id=consumable_id)
    form = ConsumableInstallForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.device_add_consumable(consumable=consumable,
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


# Склад комплектующих
class StockAccView(DataMixin, generic.ListView):
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
            Q(accessories__name__icontains=query) |
            Q(accessories__manufacturer__name__icontains=query) |
            Q(accessories__categories__name__icontains=query) |
            Q(accessories__buhCode__icontains=query) |
            Q(accessories__score__icontains=query) |
            Q(accessories__serial__icontains=query) |
            Q(accessories__invent__icontains=query) |
            Q(dateInstall__icontains=query) |
            Q(dateAddToStock__icontains=query) |
            Q(room__name__icontains=query)
        ).select_related('accessories', 'accessories__manufacturer', 'accessories__categories')
        return object_list


class StockAccCategoriesView(DataMixin, generic.ListView):
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

    # История склада комплектующих


class HistoryAccView(DataMixin, generic.ListView):
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
            Q(accessories__icontains=query) |
            Q(device__icontains=query) |
            Q(categories__name__icontains=query) |
            Q(status__icontains=query) |
            Q(dateInstall__icontains=query) |
            Q(user__icontains=query)
        )
        return object_list


class HistoryAccCategoriesView(DataMixin, generic.ListView):
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
    stock = Stock(request)
    accessories = get_object_or_404(Accessories, id=accessories_id)
    form = StockAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.add_accessories(accessories=accessories,
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
    stock = Stock(request)
    accessories = get_object_or_404(Accessories, id=accessories_id)
    stock.remove_accessories(accessories, username=username, )
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
    stock = Stock(request)
    accessories = get_object_or_404(Accessories, id=accessories_id)
    form = ConsumableInstallForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.device_add_accessories(accessories=accessories,
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


# Склад устройств
class StockDevView(DataMixin, generic.ListView):
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
            Q(devices__name__icontains=query) |
            Q(devices__manufacturer__name__icontains=query) |
            Q(devices__categories__name__icontains=query) |
            Q(devices__score__icontains=query) |
            Q(devices__serial__icontains=query) |
            Q(devices__invent__icontains=query) |
            Q(dateInstall__icontains=query) |
            Q(dateAddToStock__icontains=query)
        ).select_related('devices__manufacturer', 'devices__categories')
        return object_list


class StockDevCategoriesView(DataMixin, generic.ListView):
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

    # История склада устройств


class HistoryDevView(DataMixin, generic.ListView):
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
            Q(devices__icontains=query) |
            Q(categories__name__icontains=query) |
            Q(status__icontains=query) |
            Q(dateInstall__icontains=query) |
            Q(user__icontains=query)
        )
        return object_list


class HistoryDevCategoriesView(DataMixin, generic.ListView):
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
    stock = Stock(request)
    device = get_object_or_404(Device, id=device_id)
    form = StockAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.add_device(device=device,
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
    stock = Stock(request)
    device = get_object_or_404(Device, id=devices_id)
    stock.remove_device(device, username=username, )
    messages.add_message(request,
                         level=messages.SUCCESS,
                         message=f"{device.name} успешно удален со склада",
                         extra_tags='Успешно удален'
                         )
    return redirect('stockroom:stock_dev_list')

# @require_POST
# def move_device(request, device_id):
#    username = request.user.username
#    get_device_id = request.session['get_device_id']
#    stock = Stock(request)
#    accessories = get_object_or_404(Accessories, id=accessories_id)
#    form = ConsumableInstallForm(request.POST)
#    if form.is_valid():
#        cd = form.cleaned_data
#        stock.device_add_accessories(accessories=accessories,
#                                    device=get_device_id,
#                                    quantity=cd['quantity'],
#                                    username = username,
#                                    )
#        messages.add_message(request,
#                            level = messages.SUCCESS,
#                            message = f"Комплектующее {accessories.name} в количестве {str(cd['quantity'])} шт."
#                            f"успешно списан со склада",
#                            extra_tags = 'Успешное списание'
#                            )
#    else:
#        messages.add_message(request,
#                            level = messages.ERROR,
#                            message = 'Не удалось списать ' + accessories.name +  ' со склада',
#                            extra_tags = 'Ошибка формы'
#                            )
#    return redirect('stockroom:stock_acc_list')
