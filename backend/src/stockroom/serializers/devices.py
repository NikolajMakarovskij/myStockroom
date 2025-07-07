from rest_framework import serializers

from device.serializers import DeviceListSerializer

from ..models.devices import CategoryDev, HistoryDev, StockDev


class StockDevCatSerializer(serializers.ModelSerializer[CategoryDev]):
    """_StockDevCatSerializer_ Serialize Categories Model to JSON"""

    class Meta:
        """_Class returns JSON of Categories model_

        Returns:
            model (CategoryDev):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = CategoryDev
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class StockDevListSerializer(serializers.ModelSerializer[StockDev]):
    """_StockDevListSerializer_ Serialize StockDev Model with extended fields JSON

    Other parameters:
        categories (CategoryDev): _serialize Categories model_
        stock_model (Device): _serialize Accessories model_
    """

    categories = StockDevCatSerializer(read_only=True)
    stock_model = DeviceListSerializer(read_only=True)

    class Meta:
        """_Class returns JSON of StockDev model_

        Returns:
            model (StockDev):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = StockDev
        fields = [
            "stock_model",
            "dateAddToStock",
            "dateInstall",
            "rack",
            "shelf",
            "categories",
        ]
        extra_kwargs = {
            "stock_model": {"read_only": True},
            "dateAddToStock": {"read_only": True},
            "dateInstall": {"read_only": True},
            "rack": {"read_only": True},
            "shelf": {"read_only": True},
            "categories": {"read_only": True},
        }


class HistoryDeviceModelSerializer(serializers.ModelSerializer[HistoryDev]):
    """_HistoryDevModelSerializer_ Serialize HistoryDev Model with extended fields JSON

    Other parameters:
        categories (CategoryDev): _serialize Categories model_
    """

    categories = StockDevCatSerializer(read_only=True)

    class Meta:
        """_Class returns JSON of HistoryDev model_

        Returns:
            model (HistoryDev):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = HistoryDev
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "stock_model": {"read_only": True},
            "stock_model_id": {"read_only": True},
            "device": {"read_only": True},
            "deviceId": {"read_only": True},
            "categories": {"read_only": True},
            "quantity": {"read_only": True},
            "dateInstall": {"read_only": True},
            "user": {"read_only": True},
            "status": {"read_only": True},
            "note": {"read_only": True},
        }
