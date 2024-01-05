from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.core.cache import cache
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.views import generic, View
from django.views.decorators.http import require_POST
from core.utils import DataMixin
from device.models import Device
from stockroom.forms import StockAddForm, MoveDeviceForm, AddHistoryDeviceForm
from stockroom.models.devices import StockDev, HistoryDev, CategoryDev
from stockroom.resources import StockDevResource
from stockroom.stock.stock import DevStock

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from ..serializers.devices import StockDevListSerializer, StockDevCatSerializer

from django.http import HttpResponse
from datetime import datetime


# Devices
class StockDevView(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView):
    permission_required = 'stockroom.view_stockdev'
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
        query = self.request.GET.get('q')
        if not query:
            query = ''
        object_list = StockDev.objects.filter(
            Q(stock_model__name__icontains=query) |
            Q(stock_model__description__icontains=query) |
            Q(stock_model__note__icontains=query) |
            Q(stock_model__manufacturer__name__icontains=query) |
            Q(stock_model__categories__name__icontains=query) |
            Q(stock_model__quantity__icontains=query) |
            Q(stock_model__hostname__icontains=query) |
            Q(stock_model__ip_address__icontains=query) |
            Q(stock_model__serial__icontains=query) |
            Q(stock_model__invent__icontains=query) |
            Q(stock_model__workplace__name__icontains=query) |
            Q(stock_model__workplace__room__name__icontains=query) |
            Q(dateInstall__icontains=query) |
            Q(dateAddToStock__icontains=query)
        ).select_related('stock_model',)
        return object_list


class StockDevCategoriesView(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView):
    permission_required = 'stockroom.view_stockdev'
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
        object_list = StockDev.objects.filter(
            categories__slug=self.kwargs['category_slug']).select_related('stock_model')
        return object_list


class StockDevCatListRestView(DataMixin, viewsets.ModelViewSet):
    queryset = CategoryDev.objects.all()
    serializer_class = StockDevCatSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = CategoryDev.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class StockDevListRestView(DataMixin, viewsets.ModelViewSet):
    queryset = StockDev.objects.all()
    serializer_class = StockDevListSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = StockDev.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


# History
class HistoryDevView(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView):
    permission_required = 'stockroom.view_historydev'
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


class HistoryDevCategoriesView(LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView):
    permission_required = 'stockroom.view_historydev'
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


# Methods
@require_POST
@login_required
@permission_required('stockroom.add_device_to_stock', raise_exception=True)
def stock_add_device(request, device_id):
    username = request.user.username
    stock = DevStock
    device = get_object_or_404(Device, id=device_id)
    form = StockAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.add_to_stock_device(
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


@login_required
@permission_required('stockroom.remove_device_from_stock', raise_exception=True)
def stock_remove_device(request, devices_id):
    username = request.user.username
    device = get_object_or_404(Device, id=devices_id)
    stock = DevStock
    stock.remove_device_from_stock(model_id=device.id, username=username, )
    messages.add_message(request,
                         level=messages.SUCCESS,
                         message=f"{device.name} успешно удален со склада",
                         extra_tags='Успешно удален'
                         )
    return redirect('stockroom:stock_dev_list')


@require_POST
@login_required
@permission_required('stockroom.move_device', raise_exception=True)
def move_device_from_stock(request, device_id):
    username = request.user.username
    device = get_object_or_404(Device, id=device_id)
    stock = DevStock
    form = MoveDeviceForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        workplace_ = cd['workplace']
        note_ = cd['note']
        stock.move_device(
            model_id=device.id,
            workplace_id=workplace_.id,
            note=note_,
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


@require_POST
@login_required
@permission_required('stockroom.add_history_to_device', raise_exception=True)
def add_history_to_device(request, device_id):
    username = request.user.username
    device = get_object_or_404(Device, id=device_id)
    stock = DevStock
    form = AddHistoryDeviceForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        note_ = cd['note']
        stock.create_history_device(
            model_id=device.id,
            quantity=0,
            username=username,
            status_choice='Обслуживание',
            note=note_,

        )
        messages.add_message(request,
                             level=messages.SUCCESS,
                             message=f"Добавлена запись в историю устройства",
                             extra_tags='Успешное списание'
                             )
    else:
        messages.add_message(request,
                             level=messages.ERROR,
                             message=f"Не удалось добавить запись в историю устройства.",
                             extra_tags='Ошибка формы'
                             )
    return redirect('stockroom:stock_dev_list')


class ExportStockDevice(View):
    def get(self, *args, **kwargs):
        resource = StockDevResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response['Content-Disposition'] = 'attachment; filename={filename}.{ext}'.format(
            filename=F'Devices_in_stockroom_{datetime.today().strftime("%Y_%m_%d")}',
            ext='xlsx'
        )
        return response


class ExportStockDeviceCategory(View):
    def get_context_data(self, *, object_list=None, **kwargs):
        cat_dev = cache.get('cat_dev')
        if not cat_dev:
            cat_dev = CategoryDev.objects.all()
            cache.set('cat_dev', cat_dev, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(menu_categories=cat_dev)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
        queryset = StockDev.objects.filter(categories__slug=self.kwargs['category_slug'])
        resource = StockDevResource()
        dataset = resource.export(queryset, *args, **kwargs)
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response['Content-Disposition'] = 'attachment; filename={filename}.{ext}'.format(
            filename=F'Devices_in_stockroom_{datetime.today().strftime("%Y_%m_%d")}',
            ext='xlsx'
        )
        return response
