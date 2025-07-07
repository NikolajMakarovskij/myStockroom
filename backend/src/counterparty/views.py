from rest_framework import viewsets
from rest_framework.response import Response

from .models import Manufacturer
from .serializers import ManufacturerSerializer


class ManufacturerRestView(viewsets.ViewSet):
    """_ManufacturerRestView_ returns manufacturer data in JSON format.

    Other parameters:
        queryset (Manufacturer):
        serializer_class (ManufacturerSerializer):
    """

    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

    def list(self, request):
        """_list_ returns manufacturer list in JSON format.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """

        queryset = Manufacturer.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """_create_ adds a new manufacturer to the database.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        """_retrieve_ returns a specific manufacturer in JSON format.

        Args:
            request (_type_):
            pk (UUID | None, optional):

        Returns:
            data (JSON):
        """

        queryset = Manufacturer.objects.all()
        manufacturer = queryset.get(pk=pk)
        serializer = self.serializer_class(manufacturer)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """_update_ updates a manufacturer in the database.

        Args:
            request (_type_):
            pk (UUID | None, optional):

        Returns:
            data (JSON):
            errors (JSON):
        """

        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        """_destroy_ deletes a manufacturer from the database.

        Args:
            request (_type_):
            pk (UUID | None, optional):

        Returns:
            status (204):
        """

        project = self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)
