from rest_framework import serializers
from .models import *

class RoomSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=15)
    building = serializers.CharField(max_length=25)
    floor = serializers.CharField(max_length=25)

    def create(self, validated_data):
        return Room.objects.create(**validated_data)

class RoomModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'
        extra_kwargs = {
            'id':{'read_only': True}
        }

class WorkplaceModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workplace
        fields = '__all__'
        extra_kwargs = {
            'id':{'read_only': True}
        }