from rest_framework import serializers

from .models import AccCat, Accessories, Categories, Consumables


class CategoriesModelSerializer(serializers.ModelSerializer):
    """_CategoriesModelSerializer_ Serialize consumables categories model to JSON
    """
    class Meta:
        """_Class returns JSON of consumables categories model_

        Returns:
            model (Categories):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """
        model = Categories
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class ConsumablesModelSerializer(serializers.ModelSerializer):
    """_ConsumablesModelSerializer_ Serialize consumables model to JSON

        Other parameters:
            device (StringRelatedField): _returns device_
            consumable (StringRelatedField): _returns consumables_
    """
    device: serializers.StringRelatedField = serializers.StringRelatedField(many=True)
    consumable: serializers.StringRelatedField = serializers.StringRelatedField(many=True)

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


class AccCatModelSerializer(serializers.ModelSerializer):
    """_AccCatModelSerializer_ Serialize accessories categories model to JSON
    """
    class Meta:
        """_Class returns JSON of accessories categories model_

        Returns:
            model (AccCat):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """
        model = AccCat
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class AccessoriesModelSerializer(serializers.ModelSerializer):
    """_AccessoriesModelSerializer_ Serialize accessories model to JSON
    """
    class Meta:
        """_Class returns JSON of accessories model_

        Returns:
            model (Accessories):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """
        model = Accessories
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}
