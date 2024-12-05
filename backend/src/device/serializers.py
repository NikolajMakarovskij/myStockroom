from rest_framework import serializers

from consumables.serializers import (
    AccessoriesListModelSerializer,
    ConsumablesListSerializer,
)
from counterparty.serializers import ManufacturerSerializer
from workplace.serializers import WorkplaceListSerializer

from .models import Device, DeviceCat


class DeviceCatModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceCat
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class DeviceListSerializer(serializers.ModelSerializer):
    queryset = Device.objects.all()
    workplace = WorkplaceListSerializer(read_only=True)
    categories = DeviceCatModelSerializer(read_only=True)
    manufacturer = ManufacturerSerializer(read_only=True)
    consumable = ConsumablesListSerializer(many=True, read_only=True)
    accessories = AccessoriesListModelSerializer(many=True, read_only=True)
    accounting = serializers.SerializerMethodField("get_accounting")

    def get_queryset(self):
        categories = self.request.categories
        return Device.objects.filter(categories=categories)

    class Meta:
        model = Device
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}

    def get_accounting(self, obj=Meta.model):
        from decommission.models import Decommission, Disposal

        if not StockDev.objects.filter(stock_model=obj.id):
            if not Decommission.objects.filter(stock_model=obj.id):
                if not Disposal.objects.filter(stock_model=obj.id):
                    account = "Н"
                else:
                    account = "У"
            else:
                account = "С"
        else:
            account = "Б"

        return account
