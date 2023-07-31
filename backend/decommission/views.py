from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.views import generic
from core.utils import DataMixin
from device.models import Device
from .models import Decommission, CategoryDec, Disposal, CategoryDis
from .tasks import DecomTasks


# Decommission
class DecommissionView(LoginRequiredMixin, DataMixin, generic.ListView):
    template_name = 'decom/decom_list.html'
    model = Decommission

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_decom = cache.get('cat_decom')
        if not cat_decom:
            cat_decom = CategoryDec.objects.all()
            cache.set('cat_decom', cat_decom, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Списание устройств", searchlink='decommission:decom_search',
                                      menu_categories=cat_decom)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            query = ''
        object_list = Decommission.objects.filter(
            Q(stock_model__name__icontains=query) |
            Q(stock_model__manufacturer__name__icontains=query) |
            Q(stock_model__categories__name__icontains=query) |
            Q(stock_model__quantity__icontains=query) |
            Q(stock_model__serial__icontains=query) |
            Q(stock_model__invent__icontains=query) |
            Q(date__icontains=query)
        ).select_related('stock_model__manufacturer', 'stock_model__categories')
        return object_list


class DecomCategoriesView(LoginRequiredMixin, DataMixin, generic.ListView):
    template_name = 'decom/decom_list.html'
    model = Decommission

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_decom = cache.get('cat_decom')
        if not cat_decom:
            cat_decom = CategoryDec.objects.all()
            cache.set('cat_decom', cat_decom, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Списание устройств", searchlink='decommission:decom_search',
                                      menu_categories=cat_decom, )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = Decommission.objects.filter(categories__slug=self.kwargs['category_slug'])
        return object_list


def add_decommission(request, device_id):
    from decommission.tasks import DecomTasks
    username = request.user.username
    device = get_object_or_404(Device, id=device_id)
    DecomTasks.add_device_decom(device_id=device.id, username=username, status_choice="Списание")
    if not Decommission.objects.filter(stock_model=device):
        messages.add_message(request,
                             level=messages.SUCCESS,
                             message=f"{device.name} успешно списан со склада",
                             extra_tags='Успешно списан'
                             )
    else:
        messages.add_message(request,
                             level=messages.WARNING,
                             message=f"{device.name} находится в списке на списание",
                             extra_tags='Ошибка'
                             )
    return redirect('decommission:decom_list')


def remove_decommission(request, devices_id):
    username = request.user.username
    device = get_object_or_404(Device, id=devices_id)
    DecomTasks.remove_decom(device_id=device.id, username=username, status_choice="Удаление")
    messages.add_message(request,
                         level=messages.SUCCESS,
                         message=f"{device.name} успешно удален из списания",
                         extra_tags='Успешно удален'
                         )
    return redirect('decommission:decom_list')


# Disposal
class DisposalView(LoginRequiredMixin, DataMixin, generic.ListView):
    template_name = 'decom/disp_list.html'
    model = Disposal

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_disp = cache.get('cat_disp')
        if not cat_disp:
            cat_disp = CategoryDis.objects.all()
            cache.set('cat_disp', cat_disp, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Утилизация устройств", searchlink='decommission:disp_search',
                                      menu_categories=cat_disp)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            query = ''
        object_list = Disposal.objects.filter(
            Q(stock_model__name__icontains=query) |
            Q(stock_model__manufacturer__name__icontains=query) |
            Q(stock_model__categories__name__icontains=query) |
            Q(stock_model__quantity__icontains=query) |
            Q(stock_model__serial__icontains=query) |
            Q(stock_model__invent__icontains=query) |
            Q(date__icontains=query)
        ).select_related('stock_model__manufacturer', 'stock_model__categories')
        return object_list


class DispCategoriesView(LoginRequiredMixin, DataMixin, generic.ListView):
    template_name = 'decom/disp_list.html'
    model = Disposal

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_disp = cache.get('cat_disp')
        if not cat_disp:
            cat_disp = CategoryDis.objects.all()
            cache.set('cat_disp', cat_disp, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Утилизация устройств", searchlink='decommission:disp_search',
                                      menu_categories=cat_disp)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = Disposal.objects.filter(categories__slug=self.kwargs['category_slug'])
        return object_list


def add_disposal(request, devices_id):
    username = request.user.username
    device = get_object_or_404(Device, id=devices_id)
    DecomTasks.add_device_disp(device_id=device.id, username=username, status_choice="Утилизация")
    if not Disposal.objects.filter(stock_model=device):
        messages.add_message(request,
                             level=messages.SUCCESS,
                             message=f"{device.name} отправлен на утилизацию",
                             extra_tags='Успешно утилизирован'
                             )
    else:
        messages.add_message(request,
                             level=messages.WARNING,
                             message=f"{device.name} находится в списке на утилизацию",
                             extra_tags='Ошибка'
                             )
    return redirect('decommission:disp_list')


def remove_disposal(request, devices_id):
    username = request.user.username
    device = get_object_or_404(Device, id=devices_id)
    DecomTasks.remove_disp(device_id=device.id, username=username, status_choice="Удален")
    messages.add_message(request,
                         level=messages.SUCCESS,
                         message=f"{device.name} успешно удален из утилизации",
                         extra_tags='Успешно удален'
                         )
    return redirect('decommission:disp_list')
