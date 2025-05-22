from rest_framework import viewsets
from rest_framework.response import Response

from .models import Room, Workplace
from .serializers import (
    RoomModelSerializer,
    RoomSerializer,
    WorkplaceListSerializer,
    WorkplaceSerializer,
)


# Workplace
class WorkplaceListRestView(viewsets.ModelViewSet[Workplace]):
    """_WorkplaceListRestView_ returns workplace with extended fields data in JSON format.

    Other parameters:
        queryset (Workplace):
        serializer_class (WorkplaceListSerializer:
    """

    queryset = Workplace.objects.all()
    serializer_class = WorkplaceListSerializer

    def list(self, request):
        """_list_ returns workplace list with extended fields in JSON format.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """

        queryset = Workplace.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class WorkplaceRestView(viewsets.ModelViewSet[Workplace]):
    """_WorkplaceRestView_ returns workplace in JSON format.

    Other parameters:
        queryset (Workplace):
        serializer_class (WorkplaceSerializer):
    """

    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer

    def create(self, request):
        """_create_ adds workplace to the database.

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
        """_retrieve_ returns workplace data in JSON format.

        Args:
            request (_type_):
            pk (UUID | None, optional):

        Returns:
            data (JSON):
        """

        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """_update_ updates workplace in the database.

        Args:
            request (_type_):
            pk (UUID | None, optional):

        Returns:
            data (JSON):
            error (JSON):
        """

        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        """_destroy_ deletes workplace from the database.

        Args:
            request (_type_):
            pk (UUID | None, optional):

        Returns:
            status (204):
        """

        project = self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)


# Room
class RoomListRestView(viewsets.ModelViewSet[Room]):
    """_RoomListRestView_ returns room with extended fields data in JSON format.

    Other parameters:
        queryset (Room):
        serializer_class (RoomModelSerializer):
    """

    queryset = Room.objects.all()
    serializer_class = RoomModelSerializer

    def list(self, request):
        """_list_ returns room list with extended fields in JSON format.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """

        queryset = Room.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class RoomRestView(viewsets.ViewSet):
    """_RoomRestView_ returns room in JSON format.

    Other parameters:
        queryset (Room):
        serializer_class (RoomSerializer):
    """

    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def list(self, request):
        """_list_ returns room list in JSON format.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """

        queryset = Room.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """_create_ adds room to the database.

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
        """_retrieve_ returns room data in JSON format.

        Args:
            request (_type_):
            pk (UUID | None, optional):

        Returns:
            data (JSON):
        """

        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """_update_ updates room in the database.

        Args:
            request (_type_):
            pk (UUID | None, optional):

        Returns:
            data (JSON):
            error (JSON):
        """

        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        """_destroy_ deletes room from the database.

        Args:
            request (_type_):
            pk (UUID | None, optional):

        Returns:
            status (204):
        """

        project = self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)
