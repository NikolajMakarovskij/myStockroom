from rest_framework import serializers

from .models import Manufacturer


class ManufacturerSerializer(serializers.ModelSerializer[Manufacturer]):
    """_ManufacturerSerializer_ Serialize Manufacturer Model to JSON"""

    class Meta:
        """_Class returns JSON of Manufacturer model_

        Returns:
            model (Manufacturer):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Manufacturer
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}
