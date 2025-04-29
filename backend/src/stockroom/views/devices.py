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
    queryset = CategoryDev.objects.all()
    serializer_class = StockDevCatSerializer

    def list(self, request):
        queryset = CategoryDev.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class StockDevListRestView(viewsets.ModelViewSet[StockDev]):
    queryset = StockDev.objects.all()
    serializer_class = StockDevListSerializer

    def list(self, request):
        queryset = StockDev.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


# History
class HistoryDevListRestView(viewsets.ModelViewSet[HistoryDev]):
    queryset = HistoryDev.objects.all()
    serializer_class = HistoryDeviceModelSerializer
    # permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = HistoryDev.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class HistoryDevFilterListRestView(generics.ListAPIView[HistoryDev]):
    queryset = HistoryDev.objects.all()
    serializer_class = HistoryDeviceModelSerializer
    # permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        This view should return a list of all the history for
        the devices as determined by the stock_model_id portion of the URL.
        """

        stock_model = self.kwargs["stock_model_id"]
        return HistoryDev.objects.filter(stock_model_id=stock_model)


# post methods
class AddToStockDeviceView(APIView, DevStock):
    queryset = StockDev.objects.all()
    # @permission_required("stockroom.add_consumables_to_stock", raise_exception=True)

    def post(self, request, formant=None):
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
    queryset = StockDev.objects.all()
    # @permission_required("stockroom.remove_consumables_from_stock", raise_exception=True)

    def post(self, request, formant=None):
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
    queryset = StockDev.objects.all()
    # @permission_required("stockroom.move_device", raise_exception=True)

    def post(self, request, formant=None):
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
    queryset = StockDev.objects.all()

    def post(self, request, formant=None):
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


class ExportStockDevice(View):
    def get(self, *args, **kwargs):
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
    def get_context_data(self, *, object_list=None, **kwargs):
        cat_dev = cache.get("cat_dev")
        if not cat_dev:
            cat_dev = CategoryDev.objects.all()
            cache.set("cat_dev", cat_dev, 300)
        context = super().get_context_data(**kwargs)  # type: ignore[misc]
        c_def = self.get_user_context(menu_categories=cat_dev)  # type: ignore[attr-defined]
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
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
