from rest_framework import serializers

from consumables.serializers import ConsumablesListSerializer

from ..models.consumables import History, StockCat, Stockroom
from ..stock.stock import ConStock


class StockConCatSerializer(serializers.ModelSerializer[StockCat]):
    class Meta:
        model = StockCat
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class StockConListSerializer(serializers.ModelSerializer[Stockroom]):
    queryset = Stockroom.objects.all()
    categories = StockConCatSerializer(read_only=True)
    stock_model = ConsumablesListSerializer(read_only=True)

    class Meta:
        model = Stockroom
        fields = [
            "stock_model",
            "dateAddToStock",
            "dateInstall",
            "rack",
            "shelf",
            "categories",
        ]
        extra_kwargs = {
            "stock_model": {"read_only": True},
            "dateAddToStock": {"read_only": True},
            "dateInstall": {"read_only": True},
            "rack": {"read_only": True},
            "shelf": {"read_only": True},
            "categories": {"read_only": True},
        }


class HistoryModelSerializer(serializers.ModelSerializer[History]):
    categories = StockConCatSerializer(read_only=True)

    class Meta:
        model = History
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "stock_model": {"read_only": True},
            "stock_model_id": {"read_only": True},
            "device": {"read_only": True},
            "deviceId": {"read_only": True},
            "categories": {"read_only": True},
            "quantity": {"read_only": True},
            "dateInstall": {"read_only": True},
            "user": {"read_only": True},
            "status": {"read_only": True},
            "note": {"read_only": True},
        }


class AddToStockSerializer(serializers.Serializer[ConStock]):
    model_id = serializers.UUIDField(required=True)
    quantity = serializers.IntegerField(required=True)
    number_rack = serializers.IntegerField(required=True)
    number_shelf = serializers.IntegerField(required=True)
    username = serializers.CharField(required=True)


class AddToDeviceSerializer(serializers.Serializer[ConStock]):
    model_id = serializers.UUIDField(required=True)
    device = serializers.UUIDField(required=True)
    quantity = serializers.IntegerField(required=True)
    note = serializers.CharField(required=True)
    username = serializers.CharField(required=True)


class RemoveFromStockSerializer(serializers.Serializer[ConStock]):
    model_id = serializers.UUIDField(required=True)
    username = serializers.CharField(required=True)
