from rest_framework import serializers

from .models import Room, Workplace


class WorkplaceSerializer(serializers.ModelSerializer[Workplace]):
    queryset = Workplace.objects.all()

    class Meta:
        model = Workplace
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class RoomModelSerializer(serializers.ModelSerializer[Room]):
    queryset = Room.objects.all()
    workplace = WorkplaceSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class RoomSerializer(serializers.ModelSerializer[Room]):
    queryset = Room.objects.all()

    class Meta:
        model = Room
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class WorkplaceListSerializer(serializers.ModelSerializer[Workplace]):
    queryset = Workplace.objects.all()
    room = RoomSerializer(read_only=True)

    class Meta:
        model = Workplace
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}
