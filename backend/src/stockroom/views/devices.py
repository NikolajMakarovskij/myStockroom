from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views import View, generic
from django.views.decorators.http import require_POST

from core.utils import DataMixin
from device.models import Device
from stockroom.forms import AddHistoryDeviceForm, MoveDeviceForm, StockAddForm
from stockroom.models.devices import CategoryDev, HistoryDev, StockDev
from stockroom.resources import StockDevResource
from stockroom.stock.stock import DevStock


# Devices
class StockDevView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView # type: ignore[type-arg]
):
    """_StockDevView_
    List of stockroom devices instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (StockDev): _base model for list_
    """

    permission_required = "stockroom.view_stockdev"
    paginate_by = DataMixin.paginate
    template_name = "stock/stock_dev_list.html"
    model = StockDev

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, categories for filtering queryset_
        """

        cat_dev = cache.get("cat_dev")
        if not cat_dev:
            cat_dev = CategoryDev.objects.all()
            cache.set("cat_dev", cat_dev, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Склад устройств",
            searchlink="stockroom:stock_dev_search",
            menu_categories=cat_dev,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_queryset_

        Returns:
            object_list (StockDev): _description_
        """

        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = StockDev.objects.filter(
            Q(stock_model__name__icontains=query)
            | Q(stock_model__description__icontains=query)
            | Q(stock_model__note__icontains=query)
            | Q(stock_model__manufacturer__name__icontains=query)
            | Q(stock_model__categories__name__icontains=query)
            | Q(stock_model__quantity__icontains=query)
            | Q(stock_model__hostname__icontains=query)
            | Q(stock_model__ip_address__icontains=query)
            | Q(stock_model__serial__icontains=query)
            | Q(stock_model__invent__icontains=query)
            | Q(stock_model__workplace__name__icontains=query)
            | Q(stock_model__workplace__room__name__icontains=query)
            | Q(dateInstall__icontains=query)
            | Q(dateAddToStock__icontains=query)
        ).select_related(
            "stock_model",
        )
        return object_list


class StockDevCategoriesView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView # type: ignore[type-arg]
):
    """_StockDevCategoriesView_
    List of stockroom devices instances filtered by categories

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (StockDev): _base model for list_
    """

    permission_required = "stockroom.view_stockdev"
    paginate_by = DataMixin.paginate
    template_name = "stock/stock_dev_list.html"
    model = StockDev

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, categories for filtering queryset_
        """

        cat_dev = cache.get("cat_dev")
        if not cat_dev:
            cat_dev = CategoryDev.objects.all()
            cache.set("cat_dev", cat_dev, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Склад устройств",
            searchlink="stockroom:stock_dev_search",
            menu_categories=cat_dev,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_queryset_

        Returns:
            object_list (StockDev): _filtered by categories_
        """

        object_list = StockDev.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        ).select_related("stock_model")
        return object_list


# History
class HistoryDevView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView # type: ignore[type-arg]
):
    """_HistoryDevView_
    Returns a list of all records of history of stockroom devices from the database

    Other parameters:
        paginate_by (int): _number of records per page_
        template_name (str): _name of the template_
        model (HistoryDev): _model of the HistoryDev_
    """

    permission_required = "stockroom.view_historydev"
    paginate_by = DataMixin.paginate
    template_name = "stock/history_dev_list.html"
    model = HistoryDev

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_ The function is used to return a list of categories

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to stockroom devices list, list of categories_
        """

        cat_dev = cache.get("cat_dev")
        if not cat_dev:
            cat_dev = CategoryDev.objects.all()
            cache.set("cat_dev", cat_dev, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="История устройств",
            searchlink="stockroom:history_dev_search",
            menu_categories=cat_dev,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_returns queryset_

        Returns:
            object_list (HistoryDev): _returns queryset_
        """

        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = HistoryDev.objects.filter(
            Q(stock_model__icontains=query)
            | Q(categories__name__icontains=query)
            | Q(status__icontains=query)
            | Q(dateInstall__icontains=query)
            | Q(user__icontains=query)
        )
        return object_list


class HistoryDevCategoriesView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView # type: ignore[type-arg]
):
    """_HistoryDevCategoriesView_
    Returns a list of with filtered records by categories of history of stockroom devices from the database

    Other parameters:
        paginate_by (int): _number of records per page_
        template_name (str): _name of the template_
        model (HistoryDev): _model of the HistoryDev_
    """

    permission_required = "stockroom.view_historydev"
    paginate_by = DataMixin.paginate
    template_name = "stock/history_dev_list.html"
    model = HistoryDev

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_ The function is used to return a list of categories

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to history of stockroom devices list_
        """
        cat_dev = cache.get("cat_dev")
        if not cat_dev:
            cat_dev = CategoryDev.objects.all()
            cache.set("cat_dev", cat_dev, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="История устройств",
            searchlink="stockroom:history_dev_search",
            menu_categories=cat_dev,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_returns queryset_

        Returns:
            object_list (HistoryDev): _returns queryset_
        """

        object_list = HistoryDev.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        )
        return object_list


# Methods
@require_POST
@login_required
@permission_required("stockroom.add_device_to_stock", raise_exception=True)
def stock_add_device(request, device_id):
    """
    adds device to the stockroom

    Args:
        request (request): _description_
        device_id (UUID): _id of the device_

    Returns:
        redirect (request): _stockroom:stock_dev_list_

    Other parameters:
        username (str): _username of the user model_
        device (Device | 404): _device model instance_
        stock (DevStock): _stock model_
        form (StockAddForm): _form for adding devices to the stock_
    """
    username = request.user.username
    stock = DevStock
    device = get_object_or_404(Device, id=device_id)
    form = StockAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.add_to_stock_device(
            model_id=device.id,
            quantity=cd["quantity"],
            number_rack=cd["number_rack"],
            number_shelf=cd["number_shelf"],
            username=username,
        )
        messages.add_message(
            request,
            level=messages.SUCCESS,
            message=f"Устройство {device.name} в количестве {str(cd['quantity'])} шт."
            f"успешно добавлено на склад",
            extra_tags="Успешно добавлен",
        )
    else:
        messages.add_message(
            request,
            level=messages.ERROR,
            message=f"Не удалось добавить {device.name} на склад",
            extra_tags="Ошибка формы",
        )
    return redirect("stockroom:stock_dev_list")


@login_required
@permission_required("stockroom.remove_device_from_stock", raise_exception=True)
def stock_remove_device(request, devices_id):
    """
    remove device from the stockroom

    Args:
        request (request): _description_
        devices_id (UUID): _id of the device_

    Returns:
        redirect (request): _stockroom:stock_dev_list_

    Other parameters:
        username (str): _username of the user model_
        device (Device | 404): _device model instance_
        stock (DevStock): _stock model_
        form (remove_device_from_stock): _form for removing device from the stock_
    """
    username = request.user.username
    device = get_object_or_404(Device, id=devices_id)
    stock = DevStock
    stock.remove_device_from_stock(
        model_id=device.id,
        username=username,
    )
    messages.add_message(
        request,
        level=messages.SUCCESS,
        message=f"{device.name} успешно удален со склада",
        extra_tags="Успешно удален",
    )
    return redirect("stockroom:stock_dev_list")


@require_POST
@login_required
@permission_required("stockroom.move_device", raise_exception=True)
def move_device_from_stock(request, device_id):
    """
    moves device to workplace

    Args:
        request (request): _description_
        device_id (UUID): _id of the device_

    Returns:
        redirect (request): _stockroom:stock_dev_list_

    Other parameters:
        username (str): _username of the user model_
        device (Device | 404): _device model instance_
        stock (DevStock): _stock model_
        form (MoveDeviceForm): _form for moving device to workplace_
    """
    username = request.user.username
    device = get_object_or_404(Device, id=device_id)
    stock = DevStock
    form = MoveDeviceForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        workplace_ = cd["workplace"]
        note_ = cd["note"]
        stock.move_device(
            model_id=device.id,
            workplace_id=workplace_.id,
            note=note_,
            username=username,
        )
        messages.add_message(
            request,
            level=messages.SUCCESS,
            message="Устройство перемещено на рабочее место.",
            extra_tags="Успешное списание",
        )
    else:
        messages.add_message(
            request,
            level=messages.ERROR,
            message="Не удалось переместить устройство.",
            extra_tags="Ошибка формы",
        )
    return redirect("stockroom:stock_dev_list")


@require_POST
@login_required
@permission_required("stockroom.add_history_to_device", raise_exception=True)
def add_history_to_device(request, device_id):
    """
    adds history to device

    Args:
        request (request): _description_
        device_id (UUID): _id of the device_

    Returns:
        redirect (request): _stockroom:stock_dev_list_

    Other parameters:
        username (str): _username of the user model_
        device (Device | 404): _device model instance_
        stock (DevStock): _stock model_
        form (AddHistoryDeviceForm): _form for adding history to device_
    """
    username = request.user.username
    device = get_object_or_404(Device, id=device_id)
    stock = DevStock
    form = AddHistoryDeviceForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        note_ = cd["note"]
        stock.create_history_device(
            model_id=device.id,
            quantity=0,
            username=username,
            status_choice="Обслуживание",
            note=note_,
        )
        messages.add_message(
            request,
            level=messages.SUCCESS,
            message="Добавлена запись в историю устройства",
            extra_tags="Успешное списание",
        )
    else:
        messages.add_message(
            request,
            level=messages.ERROR,
            message="Не удалось добавить запись в историю устройства.",
            extra_tags="Ошибка формы",
        )
    return redirect("stockroom:stock_dev_list")


class ExportStockDevice(View):
    """_ExportStockConsumable_
    Returns an Excel file with all records of stockroom devices from the database
    """

    def get(self, *args, **kwargs):
        """extracts all records of stockroom device from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_

        Other parameters:
            resource (StockDevResource): _dict of device for export into an xlsx file_
        """
        resource = StockDevResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f'Devices_in_stockroom_{datetime.today().strftime("%Y_%m_%d")}',
                ext="xlsx",
            )
        )
        return response


class ExportStockDeviceCategory(View):
    """_ExportStockDeviceCategory_
    Returns an Excel file with filtered records by categories of stockroom devices from the database
    """

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_ The function is used to return a list of categories

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to stockroom devices list_
        """

        cat_dev = cache.get("cat_dev")
        if not cat_dev:
            cat_dev = CategoryDev.objects.all()
            cache.set("cat_dev", cat_dev, 300) 
        context = super().get_context_data(**kwargs) # type: ignore[misc]
        c_def = self.get_user_context(menu_categories=cat_dev) # type: ignore[attr-defined]
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
        """extracts filtered records by categories of stockroom device from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_

        Other parameters:
            resource (StockConResource): _dict of stockroom device for export into an xlsx file_
        """

        queryset = StockDev.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        )
        resource = StockDevResource()
        dataset = resource.export(queryset, *args, **kwargs)
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f'Devices_in_stockroom_{datetime.today().strftime("%Y_%m_%d")}',
                ext="xlsx",
            )
        )
        return response
