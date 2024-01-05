from rest_framework import serializers
from workplace.serializers import WorkplaceListSerializer
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

    class Meta:
        model = Device
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }