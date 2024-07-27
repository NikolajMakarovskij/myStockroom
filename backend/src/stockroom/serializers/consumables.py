from rest_framework import serializers

from consumables.models import Consumables

from ..models.consumables import History, StockCat, Stockroom


class StockConSerializer(serializers.ModelSerializer):
    device: serializers.StringRelatedField = serializers.StringRelatedField(many=True)
    consumable: serializers.StringRelatedField = serializers.StringRelatedField(many=True)

    class Meta:
        model = Consumables
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class StockCatModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockCat
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class StockModelSerializer(serializers.ModelSerializer):
    categories = StockCatModelSerializer()
    stock_model = StockConSerializer()

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
        extra_kwargs = {"id": {"read_only": True}}


class HistoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}
