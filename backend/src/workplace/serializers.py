from rest_framework import serializers

from .models import Room, Workplace


class WorkplaceSerializer(serializers.ModelSerializer[Workplace]):
    """_WorkplaceSerializer_ Serialize workplace model to JSON for CRUD views

    Other parameters:
        queryset (Workplace): _returns workplace queryset_
    """

    queryset = Workplace.objects.all()

    def display_value(self, instance):
        """_display_value_

        Args:
            instance (str): _description_

        Returns:
            instance__name (str): _description_
        """
        return "%s" % instance.name

    class Meta:
        """_Class returns JSON of workplace model_

        Returns:
            model (Workplace):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Workplace
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class RoomModelSerializer(serializers.ModelSerializer[Room]):
    """_RoomModelSerializer_ Serialize room model to JSON for list views

    Other parameters:
        queryset (Room): _returns room queryset_
        workplace (WorkplaceSerializer): _many=True, read_only=True, returns room queryset_
    """

    queryset = Room.objects.all()
    workplace = WorkplaceSerializer(many=True, read_only=True)

    class Meta:
        """_Class returns JSON of room model_

        Returns:
            model (Room):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Room
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class RoomSerializer(serializers.ModelSerializer[Room]):
    """_RoomSerializer_ Serialize room model to JSON for CRUD views

    Other parameters:
        queryset (Room): _returns room queryset_
    """

    queryset = Room.objects.all()

    class Meta:
        """_Class returns JSON of room model_

        Returns:
            model (Room):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Room
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class WorkplaceModelSerializer(serializers.ModelSerializer[Workplace]):
    """_WorkplaceSerializer_ Serialize workplace model to JSON for list views

    Other parameters:
        queryset (Workplace): _returns workplace queryset_
        room (RoomSerializer): _ read_only=True, returns room queryset_
    """

    queryset = Workplace.objects.all()
    room = RoomSerializer(read_only=True)

    class Meta:
        """_Class returns JSON of workplace model_

        Returns:
            model (Workplace):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Workplace
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}
