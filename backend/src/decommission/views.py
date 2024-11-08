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
    """_DecommissionView_
    List of Decommission instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (Decommission): _base model for list_
    """
    permission_required = "decommission.view_decommission"
    paginate_by = DataMixin.paginate
    template_name = "decom/decom_list.html"
    model = Decommission

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, link to create decommission, categories for filtering queryset_
        """
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
        """_queryset_ 

        Returns:
            object_list (Decommission): _description_
        """
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
    """_DecomCategoriesView_
    List of Decommission instances filtered by categories

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (Decommission): _base model for list_
    """

    permission_required = "decommission.view_decommission"
    paginate_by = DataMixin.paginate
    template_name = "decom/decom_list.html"
    model = Decommission

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, link to create decommission, categories for filtering queryset_
        """
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
        """_queryset_ 

        Returns:
            object_list (Decommission): _filtered by categories_
        """
        object_list = Decommission.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        ).select_related(
            "stock_model", "stock_model__manufacturer", "stock_model__categories"
        )
        return object_list


@login_required
@permission_required("decommission.add_to_decommission", raise_exception=True)
def add_decommission(request, device_id):
    """_add_decommission_
    View for the task "add_device_decom"

    Args:
        request (request): _description_
        device_id (str): _uuid of the Device model_

    Returns:
        redirect (url): _url to decommission list_
    """

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
    """_remove_decommission_
    View for the task "remove_decommission"
    
    Args:
        request (request): _description_
        devices_id (str): _uuid of the Device model_

    Returns:
        redirect (url): _url to decommission list_
    """
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
    """_ExportDecomDevice_
    Returns an Excel file with all records of Decommission from the database
    """
    def get(self, *args, **kwargs):
        """extracts all records of Decommission from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_
        
        Other parameters:
            resource (DecommissionResource): _dict of Decommission for export into an xlsx file_
        """
        resource = DecommissionResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f'Devices_in_decommission_{datetime.today().strftime("%Y_%m_%d")}',
                ext="xlsx",
            )
        )
        return response


class ExportDecomDeviceCategory(View):
    """_ExportConsumableCategory_
    Returns an Excel file with filtered records by categories of Decommission from the database
    """
    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_ The function is used to return a list of categories

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to decommission list_
        """
        cat_decom = cache.get("cat_decom")
        if not cat_decom:
            cat_decom = CategoryDec.objects.all()
            cache.set("cat_decom", cat_decom, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(menu_categories=cat_decom)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
        """extracts filtered records by categories of Decommission from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_
        
        Other parameters:
            resource (DecommissionResource): _dict of Decommission for export into an xlsx file_
        """
        queryset = Decommission.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        )
        resource = DecommissionResource()
        dataset = resource.export(queryset, *args, **kwargs)
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f'Devices_in_decommission_{datetime.today().strftime("%Y_%m_%d")}',
                ext="xlsx",
            )
        )
        return response


# Disposal
class DisposalView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_DisposalView_
    List of Disposal instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (Disposal): _base model for list_
    """
    permission_required = "decommission.view_disposal"
    paginate_by = DataMixin.paginate
    template_name = "decom/disp_list.html"
    model = Disposal

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, link to create disposal, categories for filtering queryset_
        """
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
        """_queryset_ 

        Returns:
            object_list (Disposal): _description_
        """
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
    """_DispCategoriesView_
    List of Disposal instances filtered by categories

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (Disposal): _base model for list_
    """
    permission_required = "decommission.view_disposal"
    paginate_by = DataMixin.paginate
    template_name = "decom/disp_list.html"
    model = Disposal

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, link to create disposal, categories for filtering queryset_
        """
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
        """_queryset_ 

        Returns:
            object_list (Disposal): _filtered by categories_
        """
        object_list = Disposal.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        ).select_related(
            "stock_model", "stock_model__manufacturer", "stock_model__categories"
        )
        return object_list


@login_required
@permission_required("decommission.add_to_disposal", raise_exception=True)
def add_disposal(request, devices_id):
    """_add_disposal_
    View for the task "add_device_disp"

    Args:
        request (request): _description_
        devices_id (str): _uuid of the Device model_

    Returns:
        redirect (url): _url to disposal list_
    """
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
    """_remove_disposal_
    View for the task "remove_disp"

    Args:
        request (request): _description_
        devices_id (str): _uuid of the Device model_

    Returns:
        redirect (url): _url to disposal list_
    """

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
    """_ExportDecomDevice_
    Returns an Excel file with all records of Disposal from the database
    """
    def get(self, *args, **kwargs):
        """extracts all records of Disposal from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_
        
        Other parameters:
            resource (DisposalResource): _dict of Disposal for export into an xlsx file_
        """
        resource = DisposalResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f'Devices_in_disposal_{datetime.today().strftime("%Y_%m_%d")}',
                ext="xlsx",
            )
        )
        return response


class ExportDispDeviceCategory(View):
    """_ExportConsumableCategory_
    Returns an Excel file with filtered records by categories of Disposal from the database
    """
    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_ The function is used to return a list of categories

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to disposal list_
        """
        cat_disp = cache.get("cat_disp")
        if not cat_disp:
            cat_disp = CategoryDis.objects.all()
            cache.set("cat_disp", cat_disp, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(menu_categories=cat_disp)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
        """extracts filtered records by categories of Disposal from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_
        
        Other parameters:
            resource (DisposalResource): _dict of Disposal for export into an xlsx file_
        """
        queryset = Disposal.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        )
        resource = DisposalResource()
        dataset = resource.export(queryset, *args, **kwargs)
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f'Devices_in_disposal_{datetime.today().strftime("%Y_%m_%d")}',
                ext="xlsx",
            )
        )
        return response
