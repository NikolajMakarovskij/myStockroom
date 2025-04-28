from rest_framework import serializers

from consumables.serializers import AccessoriesListModelSerializer

from ..models.accessories import CategoryAcc, HistoryAcc, StockAcc


class StockAccCatSerializer(serializers.ModelSerializer[CategoryAcc]):
    class Meta:
        model = CategoryAcc
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class StockAccListSerializer(serializers.ModelSerializer[StockAcc]):
    queryset = StockAcc.objects.all()
    categories = StockAccCatSerializer(read_only=True)
    stock_model = AccessoriesListModelSerializer(read_only=True)

    class Meta:
        model = StockAcc
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


class HistoryAccModelSerializer(serializers.ModelSerializer[HistoryAcc]):
    categories = StockAccCatSerializer(read_only=True)

    class Meta:
        model = HistoryAcc
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
