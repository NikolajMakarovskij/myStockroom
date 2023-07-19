from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.views import generic
from core.utils import DataMixin
from device.models import Device
from .models import Decommission, CategoryDec, HistoryDec, Disposal, CategoryDis, HistoryDis
from .decom import Decom


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
            Q(devices__name__icontains=query) |
            Q(devices__manufacturer__name__icontains=query) |
            Q(devices__categories__name__icontains=query) |
            Q(devices__score__icontains=query) |
            Q(devices__serial__icontains=query) |
            Q(devices__invent__icontains=query) |
            Q(date__icontains=query)
        ).select_related('devices__manufacturer', 'devices__categories')
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


# Decommission history
class HistoryDecView(LoginRequiredMixin, DataMixin, generic.ListView):
    template_name = 'decom/history_decom_list.html'
    model = HistoryDec

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_decom = cache.get('cat_decom')
        if not cat_decom:
            cat_decom = CategoryDec.objects.all()
            cache.set('cat_decom', cat_decom, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="История списания устройств",
                                      searchlink='decommission:history_decom_search', menu_categories=cat_decom)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            query = ''
        object_list = HistoryDec.objects.filter(
            Q(devices__icontains=query) |
            Q(categories__name__icontains=query) |
            Q(date__icontains=query) |
            Q(user__icontains=query)
        )
        return object_list


class HistoryDecCategoriesView(LoginRequiredMixin, DataMixin, generic.ListView):
    template_name = 'decom/history_decom_list.html'
    model = HistoryDec

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_decom = cache.get('cat_decom')
        if not cat_decom:
            cat_decom = CategoryDec.objects.all()
            cache.set('cat_decom', cat_decom, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="История списания устройств",
                                      searchlink='decommission:history_decom_search', menu_categories=cat_decom)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = HistoryDec.objects.filter(categories__slug=self.kwargs['category_slug'])
        return object_list


def add_decommission(request, device_id):
    username = request.user.username
    decom = Decom(request)
    device = get_object_or_404(Device, id=device_id)
    decom.add_device_decom(device, username=username, status_choice="Списание")
    messages.add_message(request,
                         level=messages.SUCCESS,
                         message=f"{device.name} успешно списан со склада",
                         extra_tags='Успешно списан'
                         )
    return redirect('decommission:decom_list')


def remove_decommission(request, devices_id):
    username = request.user.username
    decom = Decom(request)
    device = get_object_or_404(Device, id=devices_id)
    decom.remove_decom(device, username=username, status_choise="Удаление")
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
            Q(devices__name__icontains=query) |
            Q(devices__manufacturer__name__icontains=query) |
            Q(devices__categories__name__icontains=query) |
            Q(devices__score__icontains=query) |
            Q(devices__serial__icontains=query) |
            Q(devices__invent__icontains=query) |
            Q(date__icontains=query)
        ).select_related('devices__manufacturer', 'devices__categories')
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
    decom = Decom(request)
    device = get_object_or_404(Device, id=devices_id)
    decom.add_device_disp(device, username=username, status_choice="Утилизация")
    messages.add_message(request,
                         level=messages.SUCCESS,
                         message=f"{device.name} отправлен на утилизацию",
                         extra_tags='Успешно отправлен'
                         )
    return redirect('decommission:disp_list')


def remove_disposal(request, devices_id):
    username = request.user.username
    decom = Decom(request)
    device = get_object_or_404(Device, id=devices_id)
    decom.remove_disp(device, username=username, status_choice="Удален")
    messages.add_message(request,
                         level=messages.SUCCESS,
                         message=f"{device.name} успешно удален из утилизации",
                         extra_tags='Успешно удален'
                         )
    return redirect('decommission:disp_list')


# Disposal history
class HistoryDisView(LoginRequiredMixin, DataMixin, generic.ListView):
    template_name = 'decom/history_disp_list.html'
    model = HistoryDis

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_disp = cache.get('cat_disp')
        if not cat_disp:
            cat_disp = CategoryDis.objects.all()
            cache.set('cat_disp', cat_disp, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="История утилизации устройств",
                                      searchlink='decommission:history_dis_search', menu_categories=cat_disp)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            query = ''
        object_list = HistoryDis.objects.filter(
            Q(devices__icontains=query) |
            Q(categories__name__icontains=query) |
            Q(date__icontains=query) |
            Q(user__icontains=query)
        )
        return object_list


class HistoryDisCategoriesView(LoginRequiredMixin, DataMixin, generic.ListView):
    template_name = 'decom/history_disp_list.html'
    model = HistoryDis

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_disp = cache.get('cat_disp')
        if not cat_disp:
            cat_disp = CategoryDis.objects.all()
            cache.set('cat_disp', cat_disp, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="История утилизации устройств",
                                      searchlink='decommission:history_dis_search', menu_categories=cat_disp)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = HistoryDis.objects.filter(categories__slug=self.kwargs['category_slug'])
        return object_list
