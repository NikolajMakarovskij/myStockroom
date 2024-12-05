from rest_framework import serializers

from .models import Device, DeviceCat


class DeviceCatModelSerializer(serializers.ModelSerializer):
    """_CategoriesModelSerializer_ Serialize the model of device categories to JSON"""

    class Meta:
        """_Class returns JSON of device categories model_

        Returns:
            model (DeviceCat):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = DeviceCat
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class DeviceModelSerializer(serializers.ModelSerializer):
    """_ConsumablesModelSerializer_ Serialize the model of device to JSON"""

    class Meta:
        """_Class returns JSON of device model_

        Returns:
            model (Device):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Device
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}
