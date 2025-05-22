from rest_framework import serializers

from .models import Room, Workplace


class WorkplaceSerializer(serializers.ModelSerializer[Workplace]):
    """_WorkplaceSerializer_ Serialize Workplace Model to JSON"""

    class Meta:
        """_Class returns JSON of Workplace model_

        Returns:
            model (Workplace):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Workplace
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class RoomModelSerializer(serializers.ModelSerializer[Room]):
    """_RoomModelSerializer_ Serialize Room Model with extended fields JSON

    Other parameters:
        workplace (Workplace): _serialize Workplace model_
    """

    workplace = WorkplaceSerializer(many=True, read_only=True)

    class Meta:
        """_Class returns JSON of Room model_

        Returns:
            model (Room):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Room
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class RoomSerializer(serializers.ModelSerializer[Room]):
    """_RoomSerializer_ Serialize Room Model to JSON"""

    class Meta:
        """_Class returns JSON of Room model_

        Returns:
            model (Room):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Room
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class WorkplaceListSerializer(serializers.ModelSerializer[Workplace]):
    """_WorkplaceListSerializer_ Serialize Room Model with extended fields JSON

    Other parameters:
        room (Room: _serialize Room model_
    """

    room = RoomSerializer(read_only=True)

    class Meta:
        """_Class returns JSON of Workplace model_

        Returns:
            model (Workplace):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Workplace
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}
