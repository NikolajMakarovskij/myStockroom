from rest_framework import serializers

from .models import Device, DeviceCat


class DeviceCatModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceCat
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }


class DeviceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }
