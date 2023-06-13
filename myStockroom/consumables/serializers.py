from rest_framework import serializers
from .models import *


class CategoriesModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'
        extra_kwargs = {
            'id':{'read_only': True}
        }

class ConsumablesModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consumables
        fields = '__all__'
        extra_kwargs = {
            'id':{'read_only': True}
        }

class Acc_catModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Acc_cat
        fields = '__all__'
        extra_kwargs = {
            'id':{'read_only': True}
        }

class AccessoriesModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accessories
        fields = '__all__'
        extra_kwargs = {
            'id':{'read_only': True}
        }