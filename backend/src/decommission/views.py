from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views import View, generic

from core.utils import DataMixin
from device.models import Device

from .models import CategoryDec, CategoryDis, Decommission, Disposal
from .resources import DecommissionResource, DisposalResource
from .tasks import DecomTasks


# Decommission
class DecommissionView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    permission_required = "decommission.view_decommission"
    template_name = "decom/decom_list.html"
    model = Decommission

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_decom = cache.get("cat_decom")
        if not cat_decom:
            cat_decom = CategoryDec.objects.all()
            cache.set("cat_decom", cat_decom, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Списание устройств",
            searchlink="decommission:decom_search",
            menu_categories=cat_decom,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = Decommission.objects.filter(
            Q(stock_model__name__icontains=query)
            | Q(stock_model__manufacturer__name__icontains=query)
            | Q(stock_model__categories__name__icontains=query)
            | Q(stock_model__quantity__icontains=query)
            | Q(stock_model__serial__icontains=query)
            | Q(stock_model__invent__icontains=query)
            | Q(date__icontains=query)
        ).select_related(
            "stock_model", "stock_model__manufacturer", "stock_model__categories"
        )
        return object_list


class DecomCategoriesView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    permission_required = "decommission.view_decommission"
    template_name = "decom/decom_list.html"
    model = Decommission

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_decom = cache.get("cat_decom")
        if not cat_decom:
            cat_decom = CategoryDec.objects.all()
            cache.set("cat_decom", cat_decom, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Списание устройств",
            searchlink="decommission:decom_search",
            menu_categories=cat_decom,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = Decommission.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        ).select_related(
            "stock_model", "stock_model__manufacturer", "stock_model__categories"
        )
        return object_list


@login_required
@permission_required("decommission.add_to_decommission", raise_exception=True)
def add_decommission(request, device_id):
    from decommission.tasks import DecomTasks

    username = request.user.username
    device = get_object_or_404(Device, id=device_id)

    if not Decommission.objects.filter(stock_model=device):
        messages.add_message(
            request,
            level=messages.SUCCESS,
            message=f"{device.name} успешно списан со склада",
            extra_tags="Успешно списан",
        )
        DecomTasks.add_device_decom(
            device_id=device.id, username=username, status_choice="Списание"
        )
    else:
        messages.add_message(
            request,
            level=messages.WARNING,
            message=f"{device.name} находится в списке на списание",
            extra_tags="Ошибка",
        )
    return redirect("decommission:decom_list")


@login_required
@permission_required("decommission.remove_from_decommission", raise_exception=True)
def remove_decommission(request, devices_id):
    username = request.user.username
    device = get_object_or_404(Device, id=devices_id)
    DecomTasks.remove_decom(
        device_id=device.id, username=username, status_choice="Удаление"
    )
    messages.add_message(
        request,
        level=messages.SUCCESS,
        message=f"{device.name} успешно удален из списания",
        extra_tags="Успешно удален",
    )
    return redirect("decommission:decom_list")


class ExportDecomDevice(View):
    def get(self, *args, **kwargs):
        resource = DecommissionResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f"Devices_in_decommission_{datetime.today().strftime('%Y_%m_%d')}",
                ext="xlsx",
            )
        )
        return response


class ExportDecomDeviceCategory(View):
    def get_context_data(self, *, object_list=None, **kwargs):
        cat_decom = cache.get("cat_decom")
        if not cat_decom:
            cat_decom = CategoryDec.objects.all()
            cache.set("cat_decom", cat_decom, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(menu_categories=cat_decom)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
        queryset = Decommission.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        )
        resource = DecommissionResource()
        dataset = resource.export(queryset, *args, **kwargs)
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f"Devices_in_decommission_{datetime.today().strftime('%Y_%m_%d')}",
                ext="xlsx",
            )
        )
        return response


# Disposal
class DisposalView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    permission_required = "decommission.view_disposal"
    template_name = "decom/disp_list.html"
    model = Disposal

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_disp = cache.get("cat_disp")
        if not cat_disp:
            cat_disp = CategoryDis.objects.all()
            cache.set("cat_disp", cat_disp, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Утилизация устройств",
            searchlink="decommission:disp_search",
            menu_categories=cat_disp,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = Disposal.objects.filter(
            Q(stock_model__name__icontains=query)
            | Q(stock_model__manufacturer__name__icontains=query)
            | Q(stock_model__categories__name__icontains=query)
            | Q(stock_model__quantity__icontains=query)
            | Q(stock_model__serial__icontains=query)
            | Q(stock_model__invent__icontains=query)
            | Q(date__icontains=query)
        ).select_related(
            "stock_model", "stock_model__manufacturer", "stock_model__categories"
        )
        return object_list


class DispCategoriesView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    permission_required = "decommission.view_disposal"
    template_name = "decom/disp_list.html"
    model = Disposal

    def get_context_data(self, *, object_list=None, **kwargs):
        cat_disp = cache.get("cat_disp")
        if not cat_disp:
            cat_disp = CategoryDis.objects.all()
            cache.set("cat_disp", cat_disp, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Утилизация устройств",
            searchlink="decommission:disp_search",
            menu_categories=cat_disp,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        object_list = Disposal.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        ).select_related(
            "stock_model", "stock_model__manufacturer", "stock_model__categories"
        )
        return object_list


@login_required
@permission_required("decommission.add_to_disposal", raise_exception=True)
def add_disposal(request, devices_id):
    username = request.user.username
    device = get_object_or_404(Device, id=devices_id)

    if not Disposal.objects.filter(stock_model=device):
        messages.add_message(
            request,
            level=messages.SUCCESS,
            message=f"{device.name} отправлен на утилизацию",
            extra_tags="Успешно утилизирован",
        )
        DecomTasks.add_device_disp.delay(
            device_id=device.id, username=username, status_choice="Утилизация"
        )
    else:
        messages.add_message(
            request,
            level=messages.WARNING,
            message=f"{device.name} находится в списке на утилизацию",
            extra_tags="Ошибка",
        )
    return redirect("decommission:disp_list")


@login_required
@permission_required("decommission.remove_from_disposal", raise_exception=True)
def remove_disposal(request, devices_id):
    username = request.user.username
    device = get_object_or_404(Device, id=devices_id)
    DecomTasks.remove_disp.delay(
        device_id=device.id, username=username, status_choice="Удален"
    )
    messages.add_message(
        request,
        level=messages.SUCCESS,
        message=f"{device.name} успешно удален из утилизации",
        extra_tags="Успешно удален",
    )
    return redirect("decommission:disp_list")


class ExportDispDevice(View):
    def get(self, *args, **kwargs):
        resource = DisposalResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f"Devices_in_disposal_{datetime.today().strftime('%Y_%m_%d')}",
                ext="xlsx",
            )
        )
        return response


class ExportDispDeviceCategory(View):
    def get_context_data(self, *, object_list=None, **kwargs):
        cat_disp = cache.get("cat_disp")
        if not cat_disp:
            cat_disp = CategoryDis.objects.all()
            cache.set("cat_disp", cat_disp, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(menu_categories=cat_disp)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
        queryset = Disposal.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        )
        resource = DisposalResource()
        dataset = resource.export(queryset, *args, **kwargs)
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f"Devices_in_disposal_{datetime.today().strftime('%Y_%m_%d')}",
                ext="xlsx",
            )
        )
        return response
