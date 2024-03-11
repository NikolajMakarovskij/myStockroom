from rest_framework import serializers
#from device.serializers import DeviceListSerializer
from accounting.serializers import AccountingModelSerializer
from counterparty.serializers import ManufacturerSerializer
from .models import Categories, Consumables, AccCat, Accessories


class CategoriesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }


class ConsumablesModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consumables
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }


class ConsumablesListSerializer(serializers.ModelSerializer):
    queryset = Consumables.objects.all()
    device = serializers.StringRelatedField(many=True, read_only=True)
    consumable = AccountingModelSerializer(many=True, read_only=True)
    categories = CategoriesModelSerializer(read_only=True)
    manufacturer = ManufacturerSerializer(read_only=True)

    class Meta:
        model = Consumables
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }


class AccCatModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccCat
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }


class AccessoriesListModelSerializer(serializers.ModelSerializer):
    queryset = Accessories.objects.all()
    device = serializers.StringRelatedField(many=True, read_only=True)
    accessories = AccountingModelSerializer(many=True, read_only=True)
    categories = AccCatModelSerializer(read_only=True)
    manufacturer = ManufacturerSerializer(read_only=True)

    class Meta:
        model = Accessories
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }


class AccessoriesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }