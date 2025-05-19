from rest_framework import serializers

from device.serializers import DeviceListSerializer

from .models import CategoryDec, CategoryDis, Decommission, Disposal
from .tasks import DecomTasks


class DecommissionCatSerializer(serializers.ModelSerializer[CategoryDec]):
    """_DecommissionCatSerializer_ Serialize Categories Model to JSON"""

    class Meta:
        """_Class returns JSON of Categories model_

        Returns:
            model (Categories):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = CategoryDec
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class DecommissionListSerializer(serializers.ModelSerializer[Decommission]):
    """_DecommissionListSerializer_ Serialize Decommission Model with extended fields JSON

    Other parameters:
        stock_model (Device): _serialize Device model_
        categories (Categories): _serialize Categories model_
    """

    categories = DecommissionCatSerializer(read_only=True)
    stock_model = DeviceListSerializer(read_only=True)

    class Meta:
        """_Class returns JSON of Decommission model_

        Returns:
            model (Decommission):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Decommission
        fields = [
            "stock_model",
            "date",
            "categories",
        ]
        extra_kwargs = {
            "stock_model": {"read_only": True},
            "date": {"read_only": True},
            "categories": {"read_only": True},
        }


class DisposalCatSerializer(serializers.ModelSerializer[CategoryDis]):
    """_DisposalCatSerializer_ Serialize Categories Model to JSON"""

    class Meta:
        """_Class returns JSON of Categories model_

        Returns:
            model (Categories):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = CategoryDis
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class DisposalListSerializer(serializers.ModelSerializer[Disposal]):
    """_DisposalListSerializer_ Serialize Disposal Model with extended fields JSON

    Other parameters:
        stock_model (Device): _serialize Device model_
        categories (Categories): _serialize Categories model_
    """

    categories = DisposalCatSerializer(read_only=True)
    stock_model = DeviceListSerializer(read_only=True)

    class Meta:
        """_Class returns JSON of Disposal model_

        Returns:
            model (Disposal):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Disposal
        fields = [
            "stock_model",
            "date",
            "categories",
        ]
        extra_kwargs = {
            "stock_model": {"read_only": True},
            "date": {"read_only": True},
            "categories": {"read_only": True},
        }


class DecommissionTasksSerializer(serializers.Serializer[DecomTasks]):
    """_DecommissionTasksSerializer_ Serialize fields for adding a device to a decommission or disposal tasks.

    Other parameters:
        device_id (UUID): _serialize Device id field_
        username (str): _serialize username field_
    """

    device_id = serializers.UUIDField(required=True)
    username = serializers.CharField(required=True)
