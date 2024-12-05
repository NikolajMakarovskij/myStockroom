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
from rest_framework import viewsets

from consumables.models import Consumables
from core.utils import DataMixin
from stockroom.forms import ConsumableInstallForm, StockAddForm
from stockroom.models.consumables import History, StockCat, Stockroom
from stockroom.resources import ConsumableConsumptionResource, StockConResource
from stockroom.serializers import StockModelSerializer
from stockroom.stock.stock import ConStock


class StockroomView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_StockroomView_
    List of stockroom consumables instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (Stockroom): _base model for list_
    """

    permission_required = "stockroom.view_stockroom"
    paginate_by = DataMixin.paginate
    template_name = "stock/stock_list.html"
    model = Stockroom

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, categories for filtering queryset_
        """

        stock_cat = cache.get("stock_cat")
        if not stock_cat:
            stock_cat = StockCat.objects.all()
            cache.set("stock_cat", stock_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Склад расходников",
            searchlink="stockroom:stock_search",
            menu_categories=stock_cat,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_queryset_

        Returns:
            object_list (Stockroom): _description_
        """

        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = (
            Stockroom.objects.filter(
                Q(stock_model__name__icontains=query)
                | Q(stock_model__description__icontains=query)
                | Q(stock_model__note__icontains=query)
                | Q(stock_model__device__name__icontains=query)
                | Q(stock_model__device__workplace__name__icontains=query)
                | Q(stock_model__device__workplace__room__name__icontains=query)
                | Q(stock_model__device__workplace__room__building__icontains=query)
                | Q(stock_model__device__workplace__employee__name__icontains=query)
                | Q(stock_model__device__workplace__employee__surname__icontains=query)
                | Q(
                    stock_model__device__workplace__employee__last_name__icontains=query
                )
                | Q(stock_model__manufacturer__name__icontains=query)
                | Q(stock_model__categories__name__icontains=query)
                | Q(stock_model__quantity__icontains=query)
                | Q(stock_model__serial__icontains=query)
                | Q(stock_model__invent__icontains=query)
                | Q(dateInstall__icontains=query)
                | Q(dateAddToStock__icontains=query)
            )
            .select_related("stock_model", "stock_model__categories")
            .prefetch_related("stock_model__device")
            .distinct()
        )
        return object_list


class StockroomCategoriesView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_StockroomCategoriesView_
    List of consumables instances filtered by categories

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (Stockroom): _base model for list_
    """

    permission_required = "stockroom.view_stockroom"
    paginate_by = DataMixin.paginate
    template_name = "stock/stock_list.html"
    model = Stockroom

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, categories for filtering queryset_
        """

        stock_cat = cache.get("stock_cat")
        if not stock_cat:
            stock_cat = StockCat.objects.all()
            cache.set("stock_cat", stock_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Склад расходников",
            searchlink="stockroom:stock_search",
            menu_categories=stock_cat,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_queryset_

        Returns:
            object_list (Stockroom): _filtered by categories_
        """

        object_list = (
            Stockroom.objects.filter(categories__slug=self.kwargs["category_slug"])
            .select_related("stock_model", "stock_model__categories")
            .prefetch_related("stock_model__device")
            .distinct()
        )
        return object_list


class StockRestView(DataMixin, viewsets.ModelViewSet):
    """_StockRestView_ Stockroom consumables API view

    Other parameters:
        queryset (Stockroom): _description_
        serializer_class (StockModelSerializer): _description_
    """

    queryset = Stockroom.objects.all()
    serializer_class = StockModelSerializer


class ExportStockConsumable(View):
    """_ExportStockConsumable_
    Returns an Excel file with all records of stockroom consumables from the database
    """

    def get(self, *args, **kwargs):
        """extracts all records of stockroom consumables from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_

        Other parameters:
            resource (StockConResource): _dict of consumables for export into an xlsx file_
        """
        resource = StockConResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f'Consumables_in_stockroom_{datetime.today().strftime("%Y_%m_%d")}',
                ext="xlsx",
            )
        )
        return response


class ExportStockConsumableCategory(View):
    """_ExportStockConsumableCategory_
    Returns an Excel file with filtered records by categories of stockroom consumables from the database
    """

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_ The function is used to return a list of categories

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to stockroom consumables list_
        """

        stock_cat = cache.get("stock_cat")
        if not stock_cat:
            stock_cat = StockCat.objects.all()
            cache.set("stock_cat", stock_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(menu_categories=stock_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
        """extracts filtered records by categories of stockroom consumables from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_

        Other parameters:
            resource (StockConResource): _dict of stockroom consumables for export into an xlsx file_
        """
        queryset = (
            Stockroom.objects.filter(categories__slug=self.kwargs["category_slug"])
            .order_by("stock_model")
            .distinct("stock_model")
        )
        resource = StockConResource()
        dataset = resource.export(queryset, *args, **kwargs)
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f'Consumables_in_stockroom_{datetime.today().strftime("%Y_%m_%d")}',
                ext="xlsx",
            )
        )
        return response


# History
class HistoryView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_HistoryView_
    Returns a list of all records of history of stockroom consumables from the database

    Other parameters:
        paginate_by (int): _number of records per page_
        template_name (str): _name of the template_
        model (History): _model of the History_
    """

    permission_required = "stockroom.view_history"
    paginate_by = DataMixin.paginate
    template_name = "stock/history_list.html"
    model = History

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_ The function is used to return a list of categories

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to stockroom consumables list, list of categories_
        """
        stock_cat = cache.get("stock_cat")
        if not stock_cat:
            stock_cat = StockCat.objects.all()
            cache.set("stock_cat", stock_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="История расходников",
            searchlink="stockroom:history_search",
            menu_categories=stock_cat,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_returns queryset_

        Returns:
            object_list (History): _returns queryset_
        """

        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = History.objects.filter(
            Q(stock_model__icontains=query)
            | Q(categories__name__icontains=query)
            | Q(device__icontains=query)
            | Q(status__icontains=query)
            | Q(dateInstall__icontains=query)
            | Q(user__icontains=query)
        )
        return object_list


class HistoryCategoriesView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_HistoryCategoriesView_
    Returns a list of with filtered records by categories of history of stockroom consumables from the database

    Other parameters:
        paginate_by (int): _number of records per page_
        template_name (str): _name of the template_
        model (History): _model of the History_
    """

    permission_required = "stockroom.view_history"
    paginate_by = DataMixin.paginate
    template_name = "stock/history_list.html"
    model = History

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_ The function is used to return a list of categories

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to history of stockroom consumables list_
        """
        stock_cat = cache.get("stock_cat")
        if not stock_cat:
            stock_cat = StockCat.objects.all()
            cache.set("stock_cat", stock_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="История расходников",
            searchlink="stockroom:history_search",
            menu_categories=stock_cat,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_returns queryset_

        Returns:
            object_list (History): _returns queryset_
        """

        object_list = History.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        )
        return object_list


class HistoryConsumptionView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_HistoryConsumptionView_
    Returns a list of with all records of consumption of stockroom consumables from the database

    Other parameters:
        paginate_by (int): _number of records per page_
        template_name (str): _name of the template_
        model (History): _model of the HistoryAcc_
    """

    permission_required = "stockroom.view_history"
    paginate_by = DataMixin.paginate
    template_name = "stock/history_consumption_list.html"
    model = History

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_ The function is used to return a list of categories

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to consumption of stockroom consumables list_
        """

        stock_cat = cache.get("stock_cat")
        if not stock_cat:
            stock_cat = StockCat.objects.all()
            cache.set("stock_cat", stock_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Расход расходников по годам",
            searchlink="stockroom:history_consumption_search",
            menu_categories=stock_cat,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_returns queryset_

        Returns:
            object_list (History): _returns queryset_
        """

        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = (
            History.objects.filter(
                Q(stock_model__icontains=query)
                | Q(categories__name__icontains=query)
                | Q(device__icontains=query)
                | Q(status__icontains=query)
                | Q(dateInstall__icontains=query)
                | Q(user__icontains=query)
            )
            .order_by("stock_model")
            .distinct("stock_model")
        )
        return object_list


class HistoryConsumptionCategoriesView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_HistoryConsumptionCategoriesView_
    Returns a list of with filtered records by categories of consumption of stockroom consumables from the database

    Other parameters:
        paginate_by (int): _number of records per page_
        template_name (str): _name of the template_
        model (History): _model of the History_
    """

    permission_required = "stockroom.view_history"
    paginate_by = DataMixin.paginate
    template_name = "stock/history_consumption_list.html"
    model = History

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_ The function is used to return a list of categories

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to consumption of stockroom consumables list_
        """

        stock_cat = cache.get("stock_cat")
        if not stock_cat:
            stock_cat = StockCat.objects.all()
            cache.set("stock_cat", stock_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Расход расходников по годам",
            searchlink="stockroom:history_consumption_search",
            menu_categories=stock_cat,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_returns queryset_

        Returns:
            object_list (HistoryAcc): _returns queryset_
        """

        object_list = (
            History.objects.filter(categories__slug=self.kwargs["category_slug"])
            .order_by("stock_model")
            .distinct("stock_model")
        )
        return object_list


class ExportConsumptionConsumable(View):
    """_ExportConsumptionConsumable_
    Returns an Excel file with all records of consumption of stockroom consumables from the database
    """

    def get(self, *args, **kwargs):
        """
        extracts all records of consumption of stockroom consumables from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_

        Other parameters:
            resource (ConsumableConsumptionResource): _dict of consumables for export into an xlsx file_
        """

        resource = ConsumableConsumptionResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f'Consumption_consumables_{datetime.today().strftime("%Y_%m_%d")}',
                ext="xlsx",
            )
        )
        return response


class ExportConsumptionConsumableCategory(View):
    """_ExportConsumptionConsumableCategory_
    Returns an Excel file with filtered records by categories of consumption of stockroom consumables from the database
    """

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_ The function is used to return a list of categories

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to stockroom consumables list_
        """

        stock_cat = cache.get("stock_cat")
        if not stock_cat:
            stock_cat = StockCat.objects.all()
            cache.set("stock_cat", stock_cat, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(menu_categories=stock_cat)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
        """
        extracts filtered records by categories of consumption of stockroom consumables from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_

        Other parameters:
            resource (ConsumableConsumptionResource): _dict of consumables for export into an xlsx file_
        """
        queryset = History.objects.filter(categories__slug=self.kwargs["category_slug"])
        resource = ConsumableConsumptionResource()
        dataset = resource.export(queryset, *args, **kwargs)
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f'Consumption_consumables_{datetime.today().strftime("%Y_%m_%d")}',
                ext="xlsx",
            )
        )
        return response


# Methods
@require_POST
@login_required
@permission_required("stockroom.add_consumables_to_stock", raise_exception=True)
def stock_add_consumable(request, consumable_id):
    """
    adds consumables to the stockroom

    Args:
        request (request): _description_
        consumable_id (UUID): _id of the consumables_

    Returns:
        redirect (request): _stockroom:stock_list_

    Other parameters:
        username (str): _username of the user model_
        consumable (Consumables | 404): _consumable model instance_
        stock (ConStock): _stock model_
        form (StockAddForm): _form for adding consumables to the stock_
    """
    username = request.user.username
    consumable = get_object_or_404(Consumables, id=consumable_id)
    stock = ConStock
    form = StockAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.add_to_stock(
            model_id=consumable.id,
            quantity=cd["quantity"],
            number_rack=cd["number_rack"],
            number_shelf=cd["number_shelf"],
            username=username,
        )
        messages.add_message(
            request,
            level=messages.SUCCESS,
            message=f"Расходник {consumable.name} в количестве {str(cd['quantity'])} шт."
            f" успешно добавлен на склад",
            extra_tags="Успешно добавлен",
        )
    else:
        messages.add_message(
            request,
            level=messages.ERROR,
            message=f"Не удалось добавить {consumable.name} на склад",
            extra_tags="Ошибка формы",
        )
    return redirect("stockroom:stock_list")


@login_required
@permission_required("stockroom.remove_consumables_from_stock", raise_exception=True)
def stock_remove_consumable(request, consumable_id):
    """
    remove consumables from the stockroom

    Args:
        request (request): _description_
        consumable_id (UUID): _id of the consumables_

    Returns:
        redirect (request): _stockroom:stock_list_

    Other parameters:
        username (str): _username of the user model_
        consumable (Consumables | 404): _consumable model instance_
        stock (ConStock): _stock model_
        form (remove_from_stock): _form for removing consumables from the stock_
    """

    username = request.user.username
    consumable = get_object_or_404(Consumables, id=consumable_id)
    stock = ConStock
    stock.remove_from_stock(model_id=consumable.id, username=username)
    messages.add_message(
        request,
        level=messages.SUCCESS,
        message=f"{consumable.name} успешно удален со склада",
        extra_tags="Успешно удален",
    )
    return redirect("stockroom:stock_list")


@require_POST
@login_required
@permission_required("stockroom.add_consumables_to_device", raise_exception=True)
def device_add_consumable(request, consumable_id):
    """
    adds consumables to the device

    Args:
        request (request): _description_
        consumable_id (UUID): _id of the consumables_

    Returns:
        redirect (request): _stockroom:stock_list_

    Other parameters:
        username (str): _username of the user model_
        get_device_id (UUID): _id of the device_
        consumable (Consumables | 404): _consumable model instance_
        stock (ConStock): _stock model_
        form (StockAddForm): _form for adding consumables to the device_
    """
    username = request.user.username
    get_device_id = request.session["get_device_id"]
    consumable = get_object_or_404(Consumables, id=consumable_id)
    stock = ConStock
    form = ConsumableInstallForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        if consumable.quantity < cd["quantity"]:
            messages.add_message(
                request,
                level=messages.WARNING,
                message=f"Не достаточно расходников {consumable.name} на складе.",
                extra_tags="Нет расходника",
            )
        else:
            stock.add_to_device(
                model_id=consumable.id,
                device=get_device_id,
                quantity=cd["quantity"],
                note=cd["note"],
                username=username,
            )
            messages.add_message(
                request,
                level=messages.SUCCESS,
                message=f"Расходник {consumable.name} в количестве {str(cd['quantity'])} шт."
                f" успешно списан со склада",
                extra_tags="Успешное списание",
            )
    else:
        messages.add_message(
            request,
            level=messages.ERROR,
            message=f"Не удалось списать {consumable.name} со склада",
            extra_tags="Ошибка формы",
        )
    return redirect("stockroom:stock_list")
