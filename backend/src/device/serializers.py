from rest_framework import serializers

from consumables.serializers import (
    AccessoriesListModelSerializer,
    ConsumablesListSerializer,
)
from counterparty.serializers import ManufacturerSerializer
from workplace.serializers import WorkplaceListSerializer

from .models import Device, DeviceCat


class DeviceCatModelSerializer(serializers.ModelSerializer[DeviceCat]):
    """_DeviceCatModelSerializer_ Serialize Categories Model to JSON"""

    class Meta:
        """_Class returns JSON of Categories model_

        Returns:
            model (DeviceCat):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = DeviceCat
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class DeviceSerializer(serializers.ModelSerializer[Device]):
    """_DeviceSerializer_ Serialize Device Model to JSON"""

    class Meta:
        """_Class returns JSON of Device model_

        Returns:
            model (Device):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Device
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class DeviceListSerializer(serializers.ModelSerializer[Device]):
    """_ConsumablesListSerializer_ Serialize Accounting Model with extended fields JSON

    Other parameters:
        workplace (workplace): _serialize Workplace model_
        categories (Categories): _serialize Categories model_
        manufacturer (Manufacturer): _serialize Manufacturer model_
        consumable (Consumables): _serialize Consumables model_
        accessories (Accessories): _serialize Accessories model_
        accounting (str): _serialize accounting field_
    """

    workplace = WorkplaceListSerializer(read_only=True)
    categories = DeviceCatModelSerializer(read_only=True)
    manufacturer = ManufacturerSerializer(read_only=True)
    consumable = ConsumablesListSerializer(many=True, read_only=True)
    accessories = AccessoriesListModelSerializer(many=True, read_only=True)
    accounting = serializers.SerializerMethodField("get_accounting")

    class Meta:
        """_Class returns JSON of Device model with extended fields_

        Returns:
            model (Device):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Device
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}

    def get_accounting(self, obj=Meta.model):
        """_get_accounting_ Checks which of the lists the device is in and returns the list pointer.

        Args:
            obj (Device): _returns object from Device model_

        Returns:
            accounting (str): _returns the pointer of the list to which the device is added_
        """

        from decommission.models import Decommission, Disposal
        from stockroom.models.devices import StockDev

        if not StockDev.objects.filter(stock_model=obj.id):
            if not Decommission.objects.filter(stock_model=obj.id):
                if not Disposal.objects.filter(stock_model=obj.id):
                    account = "Н"
                else:
                    account = "У"
            else:
                account = "С"
        else:
            account = "Б"

        return account
