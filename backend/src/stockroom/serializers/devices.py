from rest_framework import serializers

from device.serializers import DeviceListSerializer

from ..models.devices import CategoryDev, StockDev


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
        extra_kwargs = {"id": {"read_only": True}}
