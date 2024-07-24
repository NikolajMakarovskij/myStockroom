from rest_framework import serializers
from .models import Manufacturer


class ManufacturerSerializer(serializers.ModelSerializer):
    queryset = Manufacturer.objects.all()

    class Meta:
        model = Manufacturer
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }

