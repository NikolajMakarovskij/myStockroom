from datetime import datetime

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from consumables.models import Accessories

from ..models.accessories import CategoryAcc, HistoryAcc, StockAcc
from ..resources import AccessoriesConsumptionResource, StockAccResource
from ..serializers.accessories import (
    HistoryAccModelSerializer,
    StockAccCatSerializer,
    StockAccListSerializer,
)
from ..serializers.stock import (
    AddToDeviceSerializer,
    AddToStockSerializer,
    RemoveFromStockSerializer,
)
from ..stock.stock import AccStock


# accessories
class StockAccCatListRestView(viewsets.ModelViewSet[CategoryAcc]):
    queryset = CategoryAcc.objects.all()
    serializer_class = StockAccCatSerializer
    # permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = CategoryAcc.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class StockAccListRestView(viewsets.ModelViewSet[StockAcc]):
    queryset = StockAcc.objects.all()
    serializer_class = StockAccListSerializer
    # permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = StockAcc.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


# History
class HistoryAccListRestView(viewsets.ModelViewSet[HistoryAcc]):
    queryset = HistoryAcc.objects.all()
    serializer_class = HistoryAccModelSerializer
    # permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = HistoryAcc.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class HistoryAccFilterListRestView(generics.ListAPIView[HistoryAcc]):
    queryset = HistoryAcc.objects.all()
    serializer_class = HistoryAccModelSerializer
    # permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        This view should return a list of all the history for
        the consumable as determined by the stock_model_id portion of the URL.
        """

        stock_model = self.kwargs["stock_model_id"]
        return HistoryAcc.objects.filter(stock_model_id=stock_model)


class HistoryAccDeviceFilterListRestView(generics.ListAPIView[HistoryAcc]):
    queryset = HistoryAcc.objects.all()
    serializer_class = HistoryAccModelSerializer
    # permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        This view should return a list of all the history for
        the consumable as determined by the stock_model_id portion of the URL.
        """

        device = self.kwargs["deviceId"]
        return HistoryAcc.objects.filter(deviceId=device)


class ConsumptionAccRestView(APIView):
    queryset = Accessories.objects.all()

    def get(self, request, format=None):
        """_API list consumption_

        Args:
            request (_type_): _description_
            format (_type_, optional): _description_. Defaults to None.

        Returns:
            _JSON_: _list consumption_
        """
        cur_year = datetime.now()
        history = HistoryAcc.objects.all()
        consumables = Accessories.objects.all()
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


# post methods
class AddToStockAccessoriesView(APIView, AccStock):
    queryset = StockAcc.objects.all()
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


class AddToDeviceAccessoriesView(APIView, AccStock):
    queryset = StockAcc.objects.all()
    # @permission_required("stockroom.add_consumables_to_device", raise_exception=True)

    def post(self, request, formant=None):
        serializer = AddToDeviceSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        model_id = serializer.validated_data["model_id"]
        device = serializer.validated_data["device"]
        quantity = serializer.validated_data["quantity"]
        note = serializer.validated_data["note"]
        username = serializer.validated_data["username"]

        consumable = get_object_or_404(Accessories, id=model_id)

        if consumable.quantity < quantity:
            return Response(
                {"error": {"message": "Не достаточно комплектующих на складе."}},
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


class RemoveFromStockAccessoriesView(APIView, AccStock):
    queryset = StockAcc.objects.all()
    # @permission_required("stockroom.remove_consumables_from_stock", raise_exception=True)

    def post(self, request, formant=None):
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


# exports
class ExportStockAccessories(View):
    def get(self, *args, **kwargs):
        resource = StockAccResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f"Accessories_in_stockroom_{datetime.today().strftime('%Y_%m_%d')}",
                ext="xlsx",
            )
        )
        return response


class ExportStockAccessoriesCategory(View):
    def get_context_data(self, *, object_list=None, **kwargs):
        cat_acc = cache.get("cat_acc")
        if not cat_acc:
            cat_acc = CategoryAcc.objects.all()
            cache.set("cat_acc", cat_acc, 300)
        context = super().get_context_data(**kwargs)  # type: ignore[misc]
        c_def = self.get_user_context(menu_categories=cat_acc)  # type: ignore[attr-defined]
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
        queryset = StockAcc.objects.filter(
            categories__slug=self.kwargs["category_slug"]
        )
        resource = StockAccResource()
        dataset = resource.export(queryset, *args, **kwargs)
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f"Accessories_in_stockroom_{datetime.today().strftime('%Y_%m_%d')}",
                ext="xlsx",
            )
        )
        return response


class ExportConsumptionAccessories(View):
    def get(self, *args, **kwargs):
        resource = AccessoriesConsumptionResource()
        dataset = resource.export()
        response = HttpResponse(dataset.xlsx, content_type="xlsx")
        response["Content-Disposition"] = (
            "attachment; filename={filename}.{ext}".format(
                filename=f"Consumption_consumables_{datetime.today().strftime('%Y_%m_%d')}",
                ext="xlsx",
            )
        )
        return response


class ExportConsumptionAccessoriesCategory(View):
    def get_context_data(self, *, object_list=None, **kwargs):
        cat_acc = cache.get("cat_acc")
        if not cat_acc:
            cat_acc = CategoryAcc.objects.all()
            cache.set("cat_acc", cat_acc, 300)
        context = super().get_context_data(**kwargs)  # type: ignore[misc]
        c_def = self.get_user_context(menu_categories=cat_acc)  # type: ignore[attr-defined]
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get(self, queryset=None, *args, **kwargs):
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
                filename=f"Consumption_consumables_{datetime.today().strftime('%Y_%m_%d')}",
                ext="xlsx",
            )
        )
        return response
