from rest_framework import serializers

from .models import AccCat, Accessories, Categories, Consumables


class CategoriesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class ConsumablesModelSerializer(serializers.ModelSerializer):
    device: serializers.StringRelatedField = serializers.StringRelatedField(many=True)
    consumable: serializers.StringRelatedField = serializers.StringRelatedField(many=True)

    class Meta:
        model = Consumables
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class AccCatModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccCat
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class AccessoriesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}
