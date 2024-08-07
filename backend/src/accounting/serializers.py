from rest_framework import serializers

from .models import Accounting, Categories


class CategoriesModelSerializer(serializers.ModelSerializer):
    """_CategoriesModelSerializer_ Serialize Categories Model to JSON

    Args:
        ModelSerializer (ModelSerializer): _description_
    """
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


class AccountingModelSerializer(serializers.ModelSerializer):
    """_AccountingModelSerializer_ Serialize Accounting Model to JSON

    Args:
        ModelSerializer (ModelSerializer): _description_
    """
    class Meta:
        """_Class returns JSON of Accounting model_

        Returns:
            model (Accounting):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """
        model = Accounting
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}
