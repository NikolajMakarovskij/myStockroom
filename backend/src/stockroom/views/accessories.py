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

from consumables.models import Accessories
from core.utils import DataMixin
from stockroom.forms import ConsumableInstallForm, StockAddForm
from stockroom.models.accessories import CategoryAcc, HistoryAcc, StockAcc
from stockroom.resources import AccessoriesConsumptionResource, StockAccResource
from stockroom.stock.stock import AccStock


# accessories
class StockAccView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_StockAccView_
    List of stockroom accessories instances

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (StockAcc): _base model for list_
    """

    permission_required = "stockroom.view_stockacc"
    paginate_by = DataMixin.paginate
    template_name = "stock/stock_acc_list.html"
    model = StockAcc

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, categories for filtering queryset_
        """

        cat_acc = cache.get("cat_acc")
        if not cat_acc:
            cat_acc = CategoryAcc.objects.all()
            cache.set("cat_acc", cat_acc, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Склад комплектующих",
            searchlink="stockroom:stock_acc_search",
            menu_categories=cat_acc,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_queryset_

        Returns:
            object_list (StockAcc): _description_
        """

        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = (
            StockAcc.objects.filter(
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
            .select_related(
                "stock_model",
                "stock_model__categories",
            )
            .prefetch_related("stock_model__device")
            .distinct()
        )
        return object_list


class StockAccCategoriesView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_StockAccCategoriesView_
    List of stockroom accessories instances filtered by categories

    Other parameters:
        template_name (str): _path to template_
        permission_required (str): _permissions_
        paginate_by (int, optional): _add pagination_
        model (StockAcc): _base model for list_
    """

    permission_required = "stockroom.view_stockacc"
    paginate_by = DataMixin.paginate
    template_name = "stock/stock_acc_list.html"
    model = StockAcc

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, side menu, link for search, categories for filtering queryset_
        """

        cat_acc = cache.get("cat_acc")
        if not cat_acc:
            cat_acc = CategoryAcc.objects.all()
            cache.set("cat_acc", cat_acc, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Склад комплектующих",
            searchlink="stockroom:stock_acc_search",
            menu_categories=cat_acc,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_queryset_

        Returns:
            object_list (StockAcc): _filtered by categories_
        """

        object_list = (
            StockAcc.objects.filter(categories__slug=self.kwargs["category_slug"])
            .select_related(
                "stock_model",
                "stock_model__categories",
            )
            .prefetch_related("stock_model__device")
            .distinct()
        )
        return object_list


class ExportStockAccessories(View):
    """_ExportAccessories_
    Returns an Excel file with all records of stockroom accessories from the database
    """

    def get(self, *args, **kwargs):
        """extracts all records of stockroom accessories from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_

        Other parameters:
            resource (StockAccResource): _dict of accessories for export into an xlsx file_
        """

        resource = StockAccResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f'Accessories_in_stockroom_{datetime.today().strftime("%Y_%m_%d")}',
                ext="xlsx",
            )
        )
        return response


class ExportStockAccessoriesCategory(View):
    """_ExportAccessoriesCategory_
    Returns an Excel file with filtered records by categories of stockroom accessories from the database
    """

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_ The function is used to return a list of categories

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to stockroom accessories list_
        """

        cat_acc = cache.get("cat_acc")
        if not cat_acc:
            cat_acc = CategoryAcc.objects.all()
            cache.set("cat_acc", cat_acc, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(menu_categories=cat_acc)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
        """extracts filtered records by categories of stockroom accessories from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_

        Other parameters:
            resource (StockAccResource): _dict of stockroom accessories for export into an xlsx file_
        """

        queryset = StockAcc.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        )
        resource = StockAccResource()
        dataset = resource.export(queryset, *args, **kwargs)
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f'Accessories_in_stockroom_{datetime.today().strftime("%Y_%m_%d")}',
                ext="xlsx",
            )
        )
        return response


class ExportConsumptionAccessories(View):
    """_ExportConsumptionAccessories_
    Returns an Excel file with all records of consumption of stockroom accessories from the database
    """

    def get(self, *args, **kwargs):
        """
        extracts all records of consumption of stockroom accessories from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_

        Other parameters:
            resource (AccessoriesConsumptionResource): _dict of accessories for export into an xlsx file_
        """
        resource = AccessoriesConsumptionResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f'Consumption_consumables_{datetime.today().strftime("%Y_%m_%d")}',
                ext="xlsx",
            )
        )
        return response


class ExportConsumptionAccessoriesCategory(View):
    """_ExportConsumptionAccessoriesCategory_
    Returns an Excel file with filtered records by categories of consumption of stockroom accessories from the database
    """

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_ The function is used to return a list of categories

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to stockroom accessories list_
        """

        cat_acc = cache.get("cat_acc")
        if not cat_acc:
            cat_acc = CategoryAcc.objects.all()
            cache.set("cat_acc", cat_acc, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(menu_categories=cat_acc)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
        """
        extracts filtered records by categories of consumption of stockroom accessories from the database and converts them into an xlsx file

        Returns:
            response (HttpResponse): _returns xlsx file_

        Other parameters:
            resource (AccessoriesConsumptionResource): _dict of accessories for export into an xlsx file_
        """

        queryset = (
            HistoryAcc.objects.filter(categories__slug=self.kwargs["category_slug"])
            .order_by("stock_model")
            .distinct("stock_model")
        )
        resource = AccessoriesConsumptionResource()
        dataset = resource.export(queryset, *args, **kwargs)
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f'Consumption_consumables_{datetime.today().strftime("%Y_%m_%d")}',
                ext="xlsx",
            )
        )
        return response


# History
class HistoryAccView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_HistoryAccView_
    Returns a list of all records of history of stockroom accessories from the database

    Other parameters:
        paginate_by (int): _number of records per page_
        template_name (str): _name of the template_
        model (HistoryAcc): _model of the HistoryAcc_
    """

    permission_required = "stockroom.view_historyacc"
    paginate_by = DataMixin.paginate
    template_name = "stock/history_acc_list.html"
    model = HistoryAcc

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_ The function is used to return a list of categories

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to stockroom accessories list, list of categories_
        """

        cat_acc = cache.get("cat_acc")
        if not cat_acc:
            cat_acc = CategoryAcc.objects.all()
            cache.set("cat_acc", cat_acc, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="История комплектующих",
            searchlink="stockroom:history_acc_search",
            menu_categories=cat_acc,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_returns queryset_

        Returns:
            object_list (HistoryAcc): _returns queryset_
        """

        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = HistoryAcc.objects.filter(
            Q(stock_model__icontains=query)
            | Q(device__icontains=query)
            | Q(categories__name__icontains=query)
            | Q(status__icontains=query)
            | Q(dateInstall__icontains=query)
            | Q(user__icontains=query)
        )
        return object_list


class HistoryAccCategoriesView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_HistoryAccCategoriesView_
    Returns a list of with filtered records by categories of history of stockroom accessories from the database

    Other parameters:
        paginate_by (int): _number of records per page_
        template_name (str): _name of the template_
        model (HistoryAcc): _model of the HistoryAcc_
    """

    permission_required = "stockroom.view_historyacc"
    paginate_by = DataMixin.paginate
    template_name = "stock/history_acc_list.html"
    model = HistoryAcc

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_ The function is used to return a list of categories

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to history of stockroom accessories list_
        """

        cat_acc = cache.get("cat_acc")
        if not cat_acc:
            cat_acc = CategoryAcc.objects.all()
            cache.set("cat_acc", cat_acc, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="История комплектующих",
            searchlink="stockroom:history_acc_search",
            menu_categories=cat_acc,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_returns queryset_

        Returns:
            object_list (HistoryAcc): _returns queryset_
        """

        query = self.request.GET.get("q")
        if not query:
            query = ""

        object_list = HistoryAcc.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        )
        return object_list


class HistoryConsumptionAccView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_HistoryConsumptionAccView_
    Returns a list of with all records of consumption of stockroom accessories from the database

    Other parameters:
        paginate_by (int): _number of records per page_
        template_name (str): _name of the template_
        model (HistoryAcc): _model of the HistoryAcc_
    """

    permission_required = "stockroom.view_history"
    paginate_by = DataMixin.paginate
    template_name = "stock/history_consumption_acc_list.html"
    model = HistoryAcc

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_ The function is used to return a list of categories

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to consumption of stockroom accessories list_
        """

        cat_acc = cache.get("cat_acc")
        if not cat_acc:
            cat_acc = CategoryAcc.objects.all()
            cache.set("cat_acc", cat_acc, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Расход комплектующих по годам",
            searchlink="stockroom:history_consumption_acc_search",
            menu_categories=cat_acc,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_returns queryset_

        Returns:
            object_list (HistoryAcc): _returns queryset_
        """

        query = self.request.GET.get("q")
        if not query:
            query = ""
        object_list = (
            HistoryAcc.objects.filter(
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


class HistoryAccConsumptionCategoriesView(
    LoginRequiredMixin, PermissionRequiredMixin, DataMixin, generic.ListView
):
    """_HistoryAccConsumptionCategoriesView_
    Returns a list of with filtered records by categories of consumption of stockroom accessories from the database

    Other parameters:
        paginate_by (int): _number of records per page_
        template_name (str): _name of the template_
        model (HistoryAcc): _model of the HistoryAcc_
    """

    permission_required = "stockroom.view_historyacc"
    paginate_by = DataMixin.paginate
    template_name = "stock/history_consumption_acc_list.html"
    model = HistoryAcc

    def get_context_data(self, *, object_list=None, **kwargs):
        """_returns context_ The function is used to return a list of categories

        Returns:
            context (object[dict[str, str],list[str]]): _returns title, link to consumption of stockroom accessories list_
        """

        cat_acc = cache.get("cat_acc")
        if not cat_acc:
            cat_acc = CategoryAcc.objects.all()
            cache.set("cat_acc", cat_acc, 300)
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Расход комплектующих по годам",
            searchlink="stockroom:history_consumption_acc_search",
            menu_categories=cat_acc,
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        """_returns queryset_

        Returns:
            object_list (HistoryAcc): _returns queryset_
        """

        object_list = (
            HistoryAcc.objects.filter(categories__slug=self.kwargs["category_slug"])
            .order_by("stock_model")
            .distinct("stock_model")
        )
        return object_list


# Methods
@require_POST
@login_required
@permission_required("stockroom.add_accessories_to_stock", raise_exception=True)
def stock_add_accessories(request, accessories_id):
    """
    adds accessories to the stockroom

    Args:
        request (request): _description_
        accessories_id (UUID): _id of the accessories_

    Returns:
        redirect (request): _stockroom:stock_acc_list_

    Other parameters:
        username (str): _username of the user model_
        accessories (Accessories | 404): _accessories model instance_
        stock (AccStock): _stock model_
        form (StockAddForm): _form for adding accessories to the stock_
    """
    username = request.user.username
    accessories = get_object_or_404(Accessories, id=accessories_id)
    stock = AccStock
    form = StockAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        stock.add_to_stock(
            model_id=accessories.id,
            quantity=cd["quantity"],
            number_rack=cd["number_rack"],
            number_shelf=cd["number_shelf"],
            username=username,
        )
        messages.add_message(
            request,
            level=messages.SUCCESS,
            message=f"Комплектующее {accessories.name} в количестве {str(cd['quantity'])} шт."
            f" успешно добавлен на склад",
            extra_tags="Успешно добавлен",
        )
    else:
        messages.add_message(
            request,
            level=messages.ERROR,
            message=f"Не удалось добавить {accessories.name} на склад",
            extra_tags="Ошибка формы",
        )
    return redirect("stockroom:stock_acc_list")


@login_required
@permission_required("stockroom.remove_accessories_from_stock", raise_exception=True)
def stock_remove_accessories(request, accessories_id):
    """
    remove accessories from the stockroom

    Args:
        request (request): _description_
        accessories_id (UUID): _id of the accessories_

    Returns:
        redirect (request): _stockroom:stock_acc_list_

    Other parameters:
        username (str): _username of the user model_
        accessories (Accessories | 404): _accessories model instance_
        stock (AccStock): _stock model_
        form (remove_from_stock): _form for removing accessories to the stock_
    """

    username = request.user.username
    accessories = get_object_or_404(Accessories, id=accessories_id)
    stock = AccStock
    stock.remove_from_stock(
        model_id=accessories.id,
        username=username,
    )
    messages.add_message(
        request,
        level=messages.SUCCESS,
        message=f"{accessories.name} успешно удален со склада",
        extra_tags="Успешно удален",
    )
    return redirect("stockroom:stock_acc_list")


@require_POST
@login_required
@permission_required("stockroom.add_accessories_to_device", raise_exception=True)
def device_add_accessories(request, accessories_id):
    """
    adds accessories to the device

    Args:
        request (request): _description_
        accessories_id (UUID): _id of the accessories_

    Returns:
        redirect (request): _stockroom:stock_acc_list_

    Other parameters:
        username (str): _username of the user model_
        get_device_id (UUID): _id of the device_
        accessories (Accessories | 404): _accessories model instance_
        stock (AccStock): _stock model_
        form (ConsumableInstallForm): _form for adding accessories to the device_
    """

    username = request.user.username
    get_device_id = request.session["get_device_id"]
    stock = AccStock
    accessories = get_object_or_404(Accessories, id=accessories_id)
    form = ConsumableInstallForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        if accessories.quantity == 0:
            messages.add_message(
                request,
                level=messages.WARNING,
                message=f"Комплектующее {accessories.name} закончилось на складе.",
                extra_tags="Нет расходника",
            )
        else:
            stock.add_to_device(
                model_id=accessories.id,
                device=get_device_id,
                quantity=cd["quantity"],
                note=cd["note"],
                username=username,
            )
            messages.add_message(
                request,
                level=messages.SUCCESS,
                message=f"Комплектующее {accessories.name} в количестве {str(cd['quantity'])} шт."
                f" успешно списан со склада",
                extra_tags="Успешное списание",
            )
    else:
        messages.add_message(
            request,
            level=messages.ERROR,
            message=f"Не удалось списать {accessories.name} со склада",
            extra_tags="Ошибка формы",
        )
    return redirect("stockroom:stock_acc_list")
