from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.views import generic
from django.views.decorators.http import require_POST
from core.utils import DataMixin
from device.models import Device
#from .forms import StockAddForm, ConsumableInstallForm, MoveDeviceForm
from .models import Decommision, CategoryDec, HistoryDec, Disposal, CategoryDis, HistoryDis
#from .stock import Stock


# Списания устройств
class DecommissionView(LoginRequiredMixin, DataMixin, generic.ListView):
    template_name = 'decom/decom_list.html'
    model = Decommision

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_decom = cache.get('cat_decom')
        if not cat_decom:
            cat_decom = CategoryDec.objects.all()
            cache.set('cat_dev', cat_decom, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Списание устройств", searchlink='decommission:decom_search',
                                      menu_categories=cat_decom)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            query = ''
        object_list = Decommision.objects.filter(
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
    model = Decommision

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_decom = cache.get('cat_decom')
        if not cat_decom:
            cat_decom = CategoryDec.objects.all()
            cache.set('cat_dev', cat_decom, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Списание устройств", searchlink='decommission:decom_search',
                                      menu_categories=cat_decom, )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = CategoryDec.objects.filter(categories__slug=self.kwargs['category_slug'])
        return object_list


# История списания устройств
class HistoryDecView(LoginRequiredMixin, DataMixin, generic.ListView):
    template_name = 'decom/history_decom_list.html'
    model = HistoryDec

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_decom = cache.get('cat_decom')
        if not cat_decom:
            cat_decom = CategoryDec.objects.all()
            cache.set('cat_dev', cat_decom, 300)
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
    template_name = 'stock/history_decom_list.html'
    model = HistoryDec

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_decom = cache.get('cat_decom')
        if not cat_decom:
            cat_decom = CategoryDec.objects.all()
            cache.set('cat_dev', cat_decom, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="История списания устройств",
                                      searchlink='decommission:history_decom_search', menu_categories=cat_decom)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = HistoryDec.objects.filter(categories__slug=self.kwargs['category_slug'])
        return object_list


# Утилизация устройств
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
        object_list = Decommision.objects.filter(
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
        object_list = CategoryDis.objects.filter(categories__slug=self.kwargs['category_slug'])
        return object_list

    # История списания устройств


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
        object_list = HistoryDec.objects.filter(
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