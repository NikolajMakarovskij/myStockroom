from rest_framework import serializers
from .models import *


class Device_catModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device_cat
        fields = '__all__'
        extra_kwargs = {
            'id':{'read_only': True}
        }

class DeviceModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = '__all__'
        extra_kwargs = {
            'id':{'read_only': True}
        }