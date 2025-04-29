from rest_framework import serializers

from ..stock.stock import AccStock, ConStock, DevStock


class AddToStockSerializer(serializers.Serializer[ConStock | AccStock | DevStock]):
    model_id = serializers.UUIDField(required=True)
    quantity = serializers.IntegerField(required=True)
    number_rack = serializers.IntegerField(required=True)
    number_shelf = serializers.IntegerField(required=True)
    username = serializers.CharField(required=True)


class AddToDeviceSerializer(serializers.Serializer[ConStock | AccStock]):
    model_id = serializers.UUIDField(required=True)
    device = serializers.UUIDField(required=True)
    quantity = serializers.IntegerField(required=True)
    note = serializers.CharField(required=False)
    username = serializers.CharField(required=True)


class RemoveFromStockSerializer(serializers.Serializer[ConStock | AccStock | DevStock]):
    model_id = serializers.UUIDField(required=True)
    username = serializers.CharField(required=True)


class MoveDeviceSerializer(serializers.Serializer[DevStock]):
    model_id = serializers.UUIDField(required=True)
    workplace_id = serializers.UUIDField(required=True)
    note = serializers.CharField(required=False)
    username = serializers.CharField(required=True)


class AddHistoryDeviceSerializer(serializers.Serializer[DevStock]):
    model_id = serializers.UUIDField(required=True)
    status_choice = serializers.CharField(required=True)
    note = serializers.CharField(required=False)
    username = serializers.CharField(required=True)
