from rest_framework import serializers
from .models import Categories, Accounting


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


class AccountingListModelSerializer(serializers.ModelSerializer):
    categories = CategoriesModelSerializer(read_only=True)
    costAll = serializers.SerializerMethodField("get_cost_all")

    class Meta:
        model = Accounting
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}

    def get_cost_all(self, obj=Meta.model):
        cost_all = obj.cost * obj.quantity
        return float("{:.2f}".format(cost_all))
