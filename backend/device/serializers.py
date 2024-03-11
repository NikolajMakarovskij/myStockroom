from rest_framework import serializers
from workplace.serializers import WorkplaceListSerializer
from consumables.serializers import AccessoriesListModelSerializer, ConsumablesListSerializer
from .models import DeviceCat, Device


class DeviceCatModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceCat
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }


class DeviceListSerializer(serializers.ModelSerializer):
    queryset = Device.objects.all()
    workplace = WorkplaceListSerializer(read_only=True)
    categories = DeviceCatModelSerializer(read_only=True)
    consumables = ConsumablesListSerializer(many=True, read_only=True)
    accessories = AccessoriesListModelSerializer(many=True, read_only=True)

    def get_queryset(self):

        categories = self.request.categories
        return Device.objects.filter(categories=categories)

    class Meta:
        model = Device
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }