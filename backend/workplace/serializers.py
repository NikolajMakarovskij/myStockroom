from rest_framework import serializers
from .models import *


class RoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }


class WorkplaceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplace
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }
