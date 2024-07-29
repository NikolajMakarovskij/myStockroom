from rest_framework import serializers

from .models import Accounting, Categories


class CategoriesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class AccountingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounting
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}
