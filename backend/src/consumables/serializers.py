# from device.serializers import DeviceListSerializer
from rest_framework import serializers

from accounting.serializers import AccountingModelSerializer
from counterparty.serializers import ManufacturerSerializer
from device.models import Device

from .models import AccCat, Accessories, Categories, Consumables


class CategoriesModelSerializer(serializers.ModelSerializer[Categories]):
    """_CategoriesModelSerializer_ Serialize Categories Model to JSON"""

    class Meta:
        """_Class returns JSON of Categories model_

        Returns:
            model (Categories):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Categories
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class ConsumablesModelSerializer(serializers.ModelSerializer[Consumables]):
    """_ConsumablesModelSerializer_ Serialize Consumables Model to JSON"""

    class Meta:
        """_Class returns JSON of Consumables model_

        Returns:
            model (Consumables):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Consumables
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class ConsumablesListSerializer(serializers.ModelSerializer[Consumables]):
    """_ConsumablesListSerializer_ Serialize Accounting Model with extended fields JSON

    Other parameters:
        device (Device): _serialize Device model_
        consumable (Accounting): _serialize Accounting model_
        categories (Categories): _serialize Categories model_
        manufacturer (Manufacturer): _serialize Manufacturer model_
        difference (float): _serialize difference field_
    """

    device: serializers.StringRelatedField[Device] = serializers.StringRelatedField(
        many=True, read_only=True
    )
    consumable = AccountingModelSerializer(many=True, read_only=True)
    categories = CategoriesModelSerializer(read_only=True)
    manufacturer = ManufacturerSerializer(read_only=True)
    difference = serializers.SerializerMethodField("get_difference")

    class Meta:
        """_Class returns JSON of Consumables model_

        Returns:
            model (Consumables):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Consumables
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}

    def get_difference(self, obj=Meta.model):
        """_difference_ Calculate the difference between the quantity of consumables and the amount of consumables in the Accounting

        Args:
            obj (_type_, optional): _description_. Defaults to Meta.model.

        Returns:
            difference (int): _returns difference of quantity_
        """

        difference = 0
        quantity_all = 0
        for each in obj.consumable.all():
            quantity_all += each.quantity
        difference = int(obj.quantity) - int(quantity_all)
        return difference


class AccCatModelSerializer(serializers.ModelSerializer[AccCat]):
    """_AccCatModelSerializer_ Serialize Accessories Categories Model to JSON"""

    class Meta:
        """_Class returns JSON of AccCat model_

        Returns:
            model (AccCat):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = AccCat
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class AccessoriesModelSerializer(serializers.ModelSerializer[Accessories]):
    """_AccessoriesModelSerializer_ Serialize Accessories Model to JSON"""

    class Meta:
        """_Class returns JSON of Accessories model_

        Returns:
            model (Accessories):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Accessories
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class AccessoriesListModelSerializer(serializers.ModelSerializer[Accessories]):
    """_AccessoriesListModelSerializer_ Serialize Accessories Model with extended fields JSON

    Other parameters:
        device (Device): _serialize Device model_
        accessories (Accounting): _serialize Accounting model_
        categories (AccCat): _serialize Accessories Categories model_
        manufacturer (Manufacturer): _serialize Manufacturer model_
        difference (float): _serialize difference field_
    """

    device: serializers.StringRelatedField[Device] = serializers.StringRelatedField(
        many=True, read_only=True
    )
    accessories = AccountingModelSerializer(many=True, read_only=True)
    categories = AccCatModelSerializer(read_only=True)
    manufacturer = ManufacturerSerializer(read_only=True)
    difference = serializers.SerializerMethodField("get_difference")

    class Meta:
        """_Class returns JSON of Accessories model_

        Returns:
            model (Accessories):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Accessories
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}

    def get_difference(self, obj=Meta.model):
        """_difference_ Calculate the difference between the quantity of accessories and the amount of accessories in the Accounting

        Args:
            obj (_type_, optional): _description_. Defaults to Meta.model.

        Returns:
            difference (int): _returns difference of quantity_
        """

        difference = 0
        quantity_all = 0
        for each in obj.accessories.all():
            quantity_all += each.quantity
        difference = int(obj.quantity) - int(quantity_all)
        return difference
