from rest_framework import serializers

from consumables.serializers import AccessoriesListModelSerializer

from ..models.accessories import CategoryAcc, HistoryAcc, StockAcc


class StockAccCatSerializer(serializers.ModelSerializer[CategoryAcc]):
    """_StockAccCatSerializer_ Serialize Categories Model to JSON"""

    class Meta:
        """_Class returns JSON of Categories model_

        Returns:
            model (CategoryAcc):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = CategoryAcc
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class StockAccListSerializer(serializers.ModelSerializer[StockAcc]):
    """_StockAccListSerializer_ Serialize StockAcc Model with extended fields JSON

    Other parameters:
        categories (CategoryAcc): _serialize Categories model_
        stock_model (Accessories): _serialize Accessories model_
    """

    categories = StockAccCatSerializer(read_only=True)
    stock_model = AccessoriesListModelSerializer(read_only=True)

    class Meta:
        """_Class returns JSON of StockAcc model_

        Returns:
            model (StockAcc):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = StockAcc
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


class HistoryAccModelSerializer(serializers.ModelSerializer[HistoryAcc]):
    """_HistoryAccModelSerializer_ Serialize HistoryAcc Model with extended fields JSON

    Other parameters:
        categories (CategoryAcc): _serialize Categories model_
    """

    categories = StockAccCatSerializer(read_only=True)

    class Meta:
        """_Class returns JSON of HistoryAcc model_

        Returns:
            model (HistoryAcc):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = HistoryAcc
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
