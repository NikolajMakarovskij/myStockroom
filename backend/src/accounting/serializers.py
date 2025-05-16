from rest_framework import serializers

from .models import Accounting, Categories


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


class AccountingModelSerializer(serializers.ModelSerializer[Accounting]):
    """_AccountingModelSerializer_ Serialize Accounting Model to JSON"""

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


class AccountingListModelSerializer(serializers.ModelSerializer[Accounting]):
    """_AccountingListModelSerializer_ Serialize Accounting Model with extended fields JSON

    Other parameters:
        categories (Categories): _serialize Categories model_
        costAll (float): _serialize costAll field_
    """

    categories = CategoriesModelSerializer(read_only=True)
    costAll = serializers.SerializerMethodField("get_cost_all")

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

    def get_cost_all(self, obj=Meta.model):
        """_summary_

        Args:
            obj (_type_, optional): _description_. Defaults to Meta.model.

        Returns:
            cost_all (float): _returns cost all consumables or accessories for record in database_
        """

        cost_all = obj.cost * obj.quantity
        return float("{:.2f}".format(cost_all))
