from datetime import datetime

from django.core.cache import cache
from django.http import HttpResponse
from django.views import View
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.devices import CategoryDev, HistoryDev, StockDev
from ..resources import StockDevResource
from ..serializers.devices import (
    HistoryDeviceModelSerializer,
    StockDevCatSerializer,
    StockDevListSerializer,
)
from ..serializers.stock import (
    AddHistoryDeviceSerializer,
    AddToStockSerializer,
    MoveDeviceSerializer,
    RemoveFromStockSerializer,
)
from ..stock.stock import DevStock


# Devices
class StockDevCatListRestView(viewsets.ModelViewSet[CategoryDev]):
    """_StockDevCatListRestView_ returns categories in JSON format.

    Other parameters:
        queryset (CategoryDev):
        serializer_class (StockDevCatSerializer):
    """

    queryset = CategoryDev.objects.all()
    serializer_class = StockDevCatSerializer

    def list(self, request):
        """_list_ returns categories data in JSON format.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """

        queryset = CategoryDev.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class StockDevListRestView(viewsets.ModelViewSet[StockDev]):
    """_StockDevListRestView_ returns devices listed in the stockroom with extended fields data in JSON format.

    Other parameters:
        queryset (StockDev):
        serializer_class (StockDevListSerializer):
    """

    queryset = StockDev.objects.all()
    serializer_class = StockDevListSerializer

    def list(self, request):
        """_list_ returns devices listed in the stockroom with extended fields data in JSON format.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """

        queryset = StockDev.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


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
                filename=f"Devices_in_stockroom_{datetime.today().strftime('%Y_%m_%d')}",
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
        context = super().get_context_data(**kwargs)  # type: ignore[misc]
        c_def = self.get_user_context(menu_categories=cat_dev)  # type: ignore[attr-defined]
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
                filename=f"Devices_in_stockroom_{datetime.today().strftime('%Y_%m_%d')}",
                ext="xlsx",
            )
        )
        return response


# History
class HistoryDevListRestView(viewsets.ModelViewSet[HistoryDev]):
    """_HistoryDevListRestView_ returns the history of all devices in the stockroom in JSON format.

    Other parameters:
        queryset (HistoryDev):
        serializer_class (HistoryDeviceModelSerializer):
    """

    queryset = HistoryDev.objects.all()
    serializer_class = HistoryDeviceModelSerializer
    # permission_classes = [permissions.AllowAny]

    def list(self, request):
        """_list_ returns devices history data in JSON format.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """

        queryset = HistoryDev.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class HistoryDevFilterListRestView(generics.ListAPIView[HistoryDev]):
    """_HistoryDevFilterListRestView_ returns the history of all devices in the stockroom filtered by stock_model_id in JSON format.

    Other parameters:
        queryset (HistoryDev):
        serializer_class (HistoryDeviceModelSerializer):
    """

    queryset = HistoryDev.objects.all()
    serializer_class = HistoryDeviceModelSerializer
    # permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """_get_queryset_ returns list of all the history for the accessories as determined by the stock_model_id portion of the URL."""

        stock_model_id = self.kwargs["stock_model_id"]
        return HistoryDev.objects.filter(stock_model_id=stock_model_id)


class HistoryDevStatusFilterListRestView(generics.ListAPIView[HistoryDev]):
    """_HistoryDevStatusFilterListRestView_ returns the history of all devices in the stockroom filtered by status in JSON format.

    Other parameters:
        queryset (HistoryDev):
        serializer_class (HistoryDeviceModelSerializer):
    """

    queryset = HistoryDev.objects.all()
    serializer_class = HistoryDeviceModelSerializer
    # permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """_get_queryset_ returns list of all the history for the devices as determined by the status portion of the URL."""

        status = self.kwargs["status"]
        return HistoryDev.objects.filter(status=status)


# post methods
class AddToStockDeviceView(APIView, DevStock):
    """_AddToStockAccessoriesView_ adds the device to the stockroom.

    Other parameters:
        queryset (StockDev):
    """

    queryset = StockDev.objects.all()
    # @permission_required("stockroom.add_consumables_to_stock", raise_exception=True)

    def post(self, request, formant=None):
        """_post_ adds the device to the stockroom.

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
            self.add_to_stock_device(
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


class RemoveFromStockDeviceView(APIView, DevStock):
    """_RemoveFromStockAccessoriesView_ removes the device from the stockroom.

    Other parameters:
        queryset (StockDev):
    """

    queryset = StockDev.objects.all()
    # @permission_required("stockroom.remove_consumables_from_stock", raise_exception=True)

    def post(self, request, formant=None):
        """_post_ removes the device from the stockroom.

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
            self.remove_device_from_stock(model_id=model_id, username=username)
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


class MoveDeviceView(APIView, DevStock):
    """_MoveDeviceView_ moves the device to another workplace.

    Other parameters:
        queryset (StockDev):
    """

    queryset = StockDev.objects.all()
    # @permission_required("stockroom.move_device", raise_exception=True)

    def post(self, request, formant=None):
        """_post_ moves the device to another workplace.

        Args:
            request (_type_):
            formant (_type_, optional):

        Returns:
            Response (JSON):
        """

        serializer = MoveDeviceSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        model_id = serializer.validated_data["model_id"]
        workplace_id = serializer.validated_data["workplace_id"]
        note = serializer.data["note"]
        username = serializer.validated_data["username"]

        try:
            self.move_device(
                model_id=model_id,
                workplace_id=workplace_id,
                note=note,
                username=username,
            )
            return Response(
                {
                    "model_id": model_id,
                    "workplace_id": workplace_id,
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


class AddHistoryToDeviceView(APIView, DevStock):
    """_AddHistoryToDeviceView_ adds the history of the device.

    Other parameters:
        queryset (StockDev):
    """

    queryset = StockDev.objects.all()

    def post(self, request, formant=None):
        """_post_ adds the history of the device.

        Args:
            request (_type_):
            formant (_type_, optional):

        Returns:
            Response (JSON):
        """

        serializer = AddHistoryDeviceSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        model_id = serializer.validated_data["model_id"]
        quantity = 0
        status_choice = serializer.validated_data["status_choice"]
        note = serializer.validated_data["note"]
        username = serializer.validated_data["username"]

        try:
            self.create_history_device(
                model_id=model_id,
                quantity=quantity,
                status_choice=status_choice,
                note=note,
                username=username,
            )
            return Response(
                {
                    "model_id": model_id,
                    "status_choice": status_choice,
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
