from rest_framework import serializers

from consumables.serializers import ConsumablesListSerializer

from ..models.consumables import History, StockCat, Stockroom


class StockConCatSerializer(serializers.ModelSerializer[StockCat]):
    """_StockConCatSerializer_ Serialize Categories Model to JSON"""

    class Meta:
        """_Class returns JSON of Categories model_

        Returns:
            model (StockCat):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = StockCat
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class StockConListSerializer(serializers.ModelSerializer[Stockroom]):
    """_StockAccListSerializer_ Serialize StockAcc Model with extended fields JSON

    Other parameters:
        categories (StockCat): _serialize Categories model_
        stock_model (Consumables): _serialize Consumables model_
    """

    categories = StockConCatSerializer(read_only=True)
    stock_model = ConsumablesListSerializer(read_only=True)

    class Meta:
        """_Class returns JSON of StockAcc model_

        Returns:
            model (Stockroom):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Stockroom
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


class HistoryModelSerializer(serializers.ModelSerializer[History]):
    """_HistoryModelSerializer_ Serialize History Model with extended fields JSON

    Other parameters:
        categories (StockCat): _serialize Categories model_
    """

    categories = StockConCatSerializer(read_only=True)

    class Meta:
        """_Class returns JSON of History model_

        Returns:
            model (History):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = History
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
