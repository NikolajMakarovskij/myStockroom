from rest_framework import serializers

from device.serializers import DeviceListSerializer

from .models import CategoryDec, CategoryDis, Decommission, Disposal
from .tasks import DecomTasks


class DecommissionCatSerializer(serializers.ModelSerializer[CategoryDec]):
    class Meta:
        model = CategoryDec
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class DecommissionListSerializer(serializers.ModelSerializer[Decommission]):
    queryset = Decommission.objects.all()
    categories = DecommissionCatSerializer(read_only=True)
    stock_model = DeviceListSerializer(read_only=True)

    class Meta:
        model = Decommission
        fields = [
            "stock_model",
            "date",
            "categories",
        ]
        extra_kwargs = {
            "stock_model": {"read_only": True},
            "date": {"read_only": True},
            "categories": {"read_only": True},
        }


class DisposalCatSerializer(serializers.ModelSerializer[CategoryDis]):
    class Meta:
        model = CategoryDis
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class DisposalListSerializer(serializers.ModelSerializer[Disposal]):
    queryset = Disposal.objects.all()
    categories = DisposalCatSerializer(read_only=True)
    stock_model = DeviceListSerializer(read_only=True)

    class Meta:
        model = Disposal
        fields = [
            "stock_model",
            "date",
            "categories",
        ]
        extra_kwargs = {
            "stock_model": {"read_only": True},
            "date": {"read_only": True},
            "categories": {"read_only": True},
        }


class DecommissionTasksSerializer(serializers.Serializer[DecomTasks]):
    device_id = serializers.UUIDField(required=True)
    username = serializers.CharField(required=True)
