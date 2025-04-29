from rest_framework import serializers

from device.serializers import DeviceListSerializer

from ..models.devices import CategoryDev, HistoryDev, StockDev


class StockDevCatSerializer(serializers.ModelSerializer[CategoryDev]):
    class Meta:
        model = CategoryDev
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class StockDevListSerializer(serializers.ModelSerializer[StockDev]):
    queryset = StockDev.objects.all()
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
        extra_kwargs = {
            "stock_model": {"read_only": True},
            "dateAddToStock": {"read_only": True},
            "dateInstall": {"read_only": True},
            "rack": {"read_only": True},
            "shelf": {"read_only": True},
            "categories": {"read_only": True},
        }


class HistoryDeviceModelSerializer(serializers.ModelSerializer[HistoryDev]):
    categories = StockDevCatSerializer(read_only=True)

    class Meta:
        model = HistoryDev
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
