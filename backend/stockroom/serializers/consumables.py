from rest_framework import serializers

from ..models.consumables import Stockroom, StockCat, History


class StockCatModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockCat
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }


class StockModelSerializer(serializers.ModelSerializer):
    stock_model = ConsumablesModelSerializer(many=True, read_only=True)

    class Meta:
        model = Stockroom
        fields = ['stock_model']
        extra_kwargs = {
            'id': {'read_only': True}
        }


class HistoryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = History
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }