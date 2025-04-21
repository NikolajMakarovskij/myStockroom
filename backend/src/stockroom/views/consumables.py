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
from rest_framework.response import Response
from rest_framework.views import APIView

from consumables.models import Consumables
from core.utils import DataMixin
from stockroom.serializers.consumables import (
    HistoryModelSerializer,
    StockConCatSerializer,
    StockConListSerializer,
)
from stockroom.stock.stock import ConStock

from ..forms import ConsumableInstallForm, StockAddForm
from ..models.consumables import History, StockCat, Stockroom
from ..resources import ConsumableConsumptionResource, StockConResource


class StockConCatListRestView(DataMixin, viewsets.ModelViewSet[StockCat]):
    queryset = StockCat.objects.all()
    serializer_class = StockConCatSerializer
    # permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = StockCat.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class StockConListRestView(DataMixin, viewsets.ModelViewSet[Stockroom]):
    queryset = Stockroom.objects.all()
    serializer_class = StockConListSerializer
    # permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = Stockroom.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class ExportStockConsumable(View):
    def get(self, *args, **kwargs):
        resource = StockConResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f"Consumables_in_stockroom_{datetime.today().strftime('%Y_%m_%d')}",
                ext="xlsx",
            )
        )
        return response


class ExportStockConsumableCategory(View):
    def get_context_data(self, *, object_list=None, **kwargs):
        stock_cat = cache.get("stock_cat")
        if not stock_cat:
            stock_cat = StockCat.objects.all()
            cache.set("stock_cat", stock_cat, 300)
        context = super().get_context_data(**kwargs)  # type: ignore[misc]
        c_def = self.get_user_context(menu_categories=stock_cat)  # type: ignore[attr-defined]
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
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
                filename=f"Consumables_in_stockroom_{datetime.today().strftime('%Y_%m_%d')}",
                ext="xlsx",
            )
        )
        return response


# History
class HistoryConListRestView(DataMixin, viewsets.ModelViewSet[History]):
    queryset = History.objects.all()
    serializer_class = HistoryModelSerializer
    # permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = History.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class ConsumptionRestView(APIView):
    queryset = Consumables.objects.all()

    def get(self, request, format=None):
        """_API list consumption_

        Args:
            request (_type_): _description_
            format (_type_, optional): _description_. Defaults to None.

        Returns:
            _JSON_: _list consumption_
        """
        cur_year = datetime.now()
        history = History.objects.all()
        consumables = Consumables.objects.all()
        responses = []
        for consumable in consumables:
            device_count = 0
            device_name = ""
            quantity = consumable.quantity
            if consumable.device.exists():
                device_name = ", ".join(
                    [
                        device.name
                        for device in consumable.device.all()
                        .order_by("name")
                        .distinct("name")
                    ]
                )
                device_count = consumable.device.count()

            unit_history_all = history.filter(
                status="Расход", stock_model_id=consumable.id
            )
            unit_history_last_year = history.filter(
                status="Расход",
                stock_model_id=consumable.id,
                dateInstall__gte=f"{int(cur_year.strftime('%Y')) - 1}-01-01",
                dateInstall__lte=f"{int(cur_year.strftime('%Y')) - 1}-12-31",
            )
            unit_history_current_year = history.filter(
                status="Расход",
                stock_model_id=consumable.id,
                dateInstall__gte=f"{cur_year.strftime('%Y')}-01-01",
                dateInstall__lte=f"{cur_year.strftime('%Y')}-12-31",
            )
            quantity_all = 0
            quantity_last_year = 0
            quantity_current_year = 0
            for unit in unit_history_all:
                quantity_all += unit.quantity
            for unit in unit_history_last_year:
                quantity_last_year += unit.quantity
            for unit in unit_history_current_year:
                quantity_current_year += unit.quantity
            if quantity <= 2 * quantity_last_year:
                requirement = abs(
                    2 * quantity_last_year - quantity + quantity_current_year
                )
            else:
                requirement = 0
            responses.append(
                {
                    "stock_model_id": consumable.id,
                    "name": consumable.name,
                    "categories": {
                        "id": consumable.categories.id,  # type: ignore[union-attr]
                        "name": consumable.categories.name,  # type: ignore[union-attr]
                        "slug": consumable.categories.slug,  # type: ignore[union-attr]
                    },
                    "device_name": device_name,
                    "device_count": device_count,
                    "quantity_all": quantity_all,
                    "quantity_last_year": quantity_last_year,
                    "quantity_current_year": quantity_current_year,
                    "quantity": quantity,
                    "requirement": requirement,
                }
            )
        return Response(responses)


class HistoryConsumptionView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DataMixin,
    generic.ListView,  # type: ignore[type-arg]
):
    permission_required = "stockroom.view_history"
    template_name = "stock/history_consumption_list.html"
    paginate_by = DataMixin.paginate
    model = History

    def get_context_data(self, *, object_list=None, **kwargs):
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
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DataMixin,
    generic.ListView,  # type: ignore[type-arg]
):
    permission_required = "stockroom.view_history"
    template_name = "stock/history_consumption_list.html"
    paginate_by = DataMixin.paginate
    model = History

    def get_context_data(self, *, object_list=None, **kwargs):
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
        object_list = (
            History.objects.filter(categories__slug=self.kwargs["category_slug"])
            .order_by("stock_model")
            .distinct("stock_model")
        )
        return object_list


class ExportConsumptionConsumable(View):
    def get(self, *args, **kwargs):
        resource = ConsumableConsumptionResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f"Consumption_consumables_{datetime.today().strftime('%Y_%m_%d')}",
                ext="xlsx",
            )
        )
        return response


class ExportConsumptionConsumableCategory(View):
    def get_context_data(self, *, object_list=None, **kwargs):
        stock_cat = cache.get("stock_cat")
        if not stock_cat:
            stock_cat = StockCat.objects.all()
            cache.set("stock_cat", stock_cat, 300)
        context = super().get_context_data(**kwargs)  # type: ignore[misc]
        c_def = self.get_user_context(menu_categories=stock_cat)  # type: ignore[attr-defined]
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
        queryset = History.objects.filter(categories__slug=self.kwargs["category_slug"])
        resource = ConsumableConsumptionResource()
        dataset = resource.export(queryset, *args, **kwargs)
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f"Consumption_consumables_{datetime.today().strftime('%Y_%m_%d')}",
                ext="xlsx",
            )
        )
        return response


# Methods
@require_POST
@login_required
@permission_required("stockroom.add_consumables_to_stock", raise_exception=True)
def stock_add_consumable(request, consumable_id):
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
