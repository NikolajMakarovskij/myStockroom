from device.models import Device
from device.serializers import DeviceListSerializer
from rest_framework import serializers

from ..models.devices import CategoryDev, StockDev


class StockDevSerializer(serializers.ModelSerializer):
    device: serializers.StringRelatedField = serializers.StringRelatedField(many=True)
    consumable: serializers.StringRelatedField = serializers.StringRelatedField(
        many=True
    )

    class Meta:
        model = Device
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class StockDevCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryDev
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class StockDevListSerializer(serializers.ModelSerializer):
    queryset = Device.objects.all()
    categories = StockDevCatSerializer(read_only=True)
    stock_model = DeviceListSerializer(read_only=True)

    class Meta:
        model = StockDev
        fields = [
            "stock_model",
            "dateAddToStock",
            "dateInstall",
            "rack",
            "shelf",
            "categories",
        ]
        extra_kwargs = {"id": {"read_only": True}}
