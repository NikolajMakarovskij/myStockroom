from rest_framework import serializers

from consumables.models import Consumables

from .models.consumables import History, StockCat, Stockroom


class StockConSerializer(serializers.ModelSerializer):
    """_StockConSerializer_ Serialize consumables model to JSON

    Other parameters:
        device (StringRelatedField): _returns device_
        consumable (StringRelatedField): _returns consumables_

    """

    device: serializers.StringRelatedField = serializers.StringRelatedField(many=True)
    consumable: serializers.StringRelatedField = serializers.StringRelatedField(
        many=True
    )

    class Meta:
        """_Class returns JSON of consumables model_

        Returns:
            model (Consumables):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Consumables
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class StockCatModelSerializer(serializers.ModelSerializer):
    """_StockCatModelSerializer_ Serialize stockroom consumables categories model to JSON"""

    class Meta:
        """_Class returns JSON of stockroom consumables categories model_

        Returns:
            model (Categories):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = StockCat
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class StockModelSerializer(serializers.ModelSerializer):
    """_StockConSerializer_ Serialize stockroom consumables model to JSON

    Other parameters:
        categories  (StringRelatedField): _returns categories _
        stock_model (StringRelatedField): _returns consumables_

    """

    categories = StockCatModelSerializer()
    stock_model = StockConSerializer()

    class Meta:
        """_Class returns JSON of stockroom consumables model_

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
        extra_kwargs = {"id": {"read_only": True}}


class HistoryModelSerializer(serializers.ModelSerializer):
    """_HistoryModelSerializer_ Serialize history consumables model to JSON"""

    class Meta:
        """_Class returns JSON of stockroom history consumables model_

        Returns:
            model (History):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = History
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}
