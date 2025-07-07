from datetime import datetime

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from consumables.models import Consumables

from ..models.consumables import History, StockCat, Stockroom
from ..resources import ConsumableConsumptionResource, StockConResource
from ..serializers.consumables import (
    HistoryModelSerializer,
    StockConCatSerializer,
    StockConListSerializer,
)
from ..serializers.stock import (
    AddToDeviceSerializer,
    AddToStockSerializer,
    RemoveFromStockSerializer,
)
from ..stock.stock import ConStock


class StockConCatListRestView(viewsets.ModelViewSet[StockCat]):
    """_StockConCatListRestView_ returns categories in JSON format.

    Other parameters:
        queryset (StockCat):
        serializer_class (StockConCatSerializer):
    """

    queryset = StockCat.objects.all()
    serializer_class = StockConCatSerializer
    # permission_classes = [permissions.AllowAny]

    def list(self, request):
        """_list_ returns categories data in JSON format.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """

        queryset = StockCat.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class StockConListRestView(viewsets.ModelViewSet[Stockroom]):
    """_StockConListRestView_ returns consumables listed in the stockroom with extended fields data in JSON format.

    Other parameters:
        queryset (Stockroom):
        serializer_class (StockConListSerializer):
    """

    queryset = Stockroom.objects.all()
    serializer_class = StockConListSerializer
    # permission_classes = [permissions.AllowAny]

    def list(self, request):
        """_list_ returns consumables listed in the stockroom list with extended fields in JSON format.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """

        queryset = Stockroom.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


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
                filename=f"Consumables_in_stockroom_{datetime.today().strftime('%Y_%m_%d')}",
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
        context = super().get_context_data(**kwargs)  # type: ignore[misc]
        c_def = self.get_user_context(menu_categories=stock_cat)  # type: ignore[attr-defined]
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
                filename=f"Consumables_in_stockroom_{datetime.today().strftime('%Y_%m_%d')}",
                ext="xlsx",
            )
        )
        return response


# History
class HistoryConListRestView(viewsets.ModelViewSet[History]):
    """_HistoryConListRestView_ returns all history of consumables fields in JSON format.

    Other parameters:
        queryset (History):
        serializer_class (HistoryModelSerializer):
    """

    queryset = History.objects.all()
    serializer_class = HistoryModelSerializer
    # permission_classes = [permissions.AllowAny]

    def list(self, request):
        """_list_ returns all history of consumables fields in JSON format.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """

        queryset = History.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class HistoryConFilterListRestView(generics.ListAPIView[History]):
    """_HistoryConFilterListRestView_ returns history of consumables fields filtered by stock_model_id in JSON format.

    Other parameters:
        queryset (History):
        serializer_class (HistoryModelSerializer):
    """

    queryset = History.objects.all()
    serializer_class = HistoryModelSerializer
    # permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """_get_queryset_ returns list of all the history for the consumable as determined by the stock_model_id portion of the URL."""

        stock_model = self.kwargs["stock_model_id"]
        return History.objects.filter(stock_model_id=stock_model)


class HistoryConDeviceFilterListRestView(generics.ListAPIView[History]):
    """_HistoryConDeviceFilterListRestView_ returns history of consumables with extended fields filtered by deviceId in JSON format.

    Other parameters:
        queryset (History):
        serializer_class (HistoryModelSerializer):
    """

    queryset = History.objects.all()
    serializer_class = HistoryModelSerializer
    # permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """_get_queryset_ returns list of all the history for the consumable as determined by the deviceId portion of the URL."""

        device = self.kwargs["deviceId"]
        return History.objects.filter(deviceId=device)


class ConsumptionRestView(APIView):
    """_ConsumptionRestView_ returns the consumption of consumables in JSON format."""

    queryset = Consumables.objects.all()

    def get(self, request, formant=None):
        """_get_ Returns list consumption in JSON format

        Args:
            request (_type_):
            formant (_type_, optional):

        Returns:
            Response (JSON): _list consumption_
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
                filename=f"Consumption_consumables_{datetime.today().strftime('%Y_%m_%d')}",
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
        context = super().get_context_data(**kwargs)  # type: ignore[misc]
        c_def = self.get_user_context(menu_categories=stock_cat)  # type: ignore[attr-defined]
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
                filename=f"Consumption_consumables_{datetime.today().strftime('%Y_%m_%d')}",
                ext="xlsx",
            )
        )
        return response


# post methods
class AddToStockConsumableView(APIView, ConStock):
    """_AddToStockConsumableView_ adds the consumables to the stockroom.

    Other parameters:
        queryset (Stockroom):
    """

    queryset = Stockroom.objects.all()
    # @permission_required("stockroom.add_consumables_to_stock", raise_exception=True)

    def post(self, request, formant=None):
        """_post_ adds the consumables to the stockroom.

        Args:
            request (_type_):
            formant (_type_, optional):

        Returns:
            Response (JSON):
        """

        serializer = AddToStockSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        model_id = serializer.validated_data["model_id"]
        quantity = serializer.validated_data["quantity"]
        number_rack = serializer.validated_data["number_rack"]
        number_shelf = serializer.validated_data["number_shelf"]
        username = serializer.validated_data["username"]

        try:
            self.add_to_stock(
                model_id=model_id,
                quantity=quantity,
                number_rack=number_rack,
                number_shelf=number_shelf,
                username=username,
            )
            return Response(
                {
                    "model_id": model_id,
                    "quantity": quantity,
                    "number_rack": number_rack,
                    "number_shelf": number_shelf,
                    "username": username,
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )


class AddToDeviceConsumableView(APIView, ConStock):
    """_AddToDeviceConsumableView_ adds the consumables to the device.

    Other parameters:
        queryset (Stockroom):
    """

    queryset = Stockroom.objects.all()
    # @permission_required("stockroom.add_consumables_to_device", raise_exception=True)

    def post(self, request, formant=None):
        """_post_ adds the consumables to the device.

        Args:
            request (_type_):
            formant (_type_, optional):

        Returns:
            Response (JSON):
        """

        serializer = AddToDeviceSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        model_id = serializer.validated_data["model_id"]
        device = serializer.validated_data["device"]
        quantity = serializer.validated_data["quantity"]
        note = serializer.validated_data["note"]
        username = serializer.validated_data["username"]

        consumable = get_object_or_404(Consumables, id=model_id)

        if consumable.quantity < quantity:
            return Response(
                {"error": {"message": "Не достаточно расходников на складе."}},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            self.add_to_device(
                model_id=model_id,
                device=device,
                quantity=quantity,
                note=note,
                username=username,
            )
            return Response(
                {
                    "model_id": model_id,
                    "device": device,
                    "quantity": quantity,
                    "note": note,
                    "username": username,
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )


class RemoveFromStockConsumableView(APIView, ConStock):
    """_RemoveFromStockConsumableView_ removes the consumables from the stockroom.

    Other parameters:
        queryset (Stockroom):
    """

    queryset = Stockroom.objects.all()
    # @permission_required("stockroom.remove_consumables_from_stock", raise_exception=True)

    def post(self, request, formant=None):
        """_post_ removes the consumables from the stockroom.

        Args:
            request (_type_):
            formant (_type_, optional):

        Returns:
            Response (JSON):
        """

        serializer = RemoveFromStockSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        model_id = serializer.validated_data["model_id"]
        username = serializer.validated_data["username"]

        try:
            self.remove_from_stock(model_id=model_id, username=username)
            return Response(
                {
                    "model_id": model_id,
                    "username": username,
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )
