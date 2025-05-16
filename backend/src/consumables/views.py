from rest_framework import viewsets
from rest_framework.response import Response

from .models import AccCat, Accessories, Categories, Consumables
from .serializers import (
    AccCatModelSerializer,
    AccessoriesListModelSerializer,
    AccessoriesModelSerializer,
    CategoriesModelSerializer,
    ConsumablesListSerializer,
    ConsumablesModelSerializer,
)


# Consumables
class ConsumablesListRestView(viewsets.ModelViewSet[Consumables]):
    """_ConsumablesListRestView_ returns consumables with extended fields data in JSON format.

    Other parameters:
        queryset (Consumables):
        serializer_class (ConsumablesListSerializer):
    """

    queryset = Consumables.objects.all()
    serializer_class = ConsumablesListSerializer

    def list(self, request):
        """_list_ returns consumables list with extended fields in JSON format.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """

        queryset = Consumables.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class ConsumablesRestView(viewsets.ModelViewSet[Consumables]):
    """_ConsumablesRestView_ returns consumables in JSON format.

    Other parameters:
        queryset (Consumables):
        serializer_class (ConsumablesModelSerializer):
    """

    queryset = Consumables.objects.all()
    serializer_class = ConsumablesModelSerializer

    def create(self, request):
        """_create_ adds consumables to the database.

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
        """_retrieve_ returns consumables data in JSON format.

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
        """_update_ updates consumables in the database.

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
        """_destroy_ deletes consumables from the database.

        Args:
            request (_type_):
            pk (UUID | None, optional):

        Returns:
            status (204):
        """

        project = self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)


class CategoriesRestView(viewsets.ModelViewSet[Categories]):
    """_CategoriesRestView_ returns categories in JSON format.

    Other parameters:
        queryset (Categories):
        serializer_class (CategoriesModelSerializer):
    """

    queryset = Categories.objects.all()
    serializer_class = CategoriesModelSerializer

    def list(self, request):
        """_list_ returns categories data in JSON format.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """

        queryset = Categories.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """_create_ adds categories to the database.

        Args:
            request (_type_):

        Returns:
            data (JSON):
            error (JSON):
        """

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        """_retrieve_ returns categories data in JSON format.

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
        """_update_ updates categories in the database.

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
        """_destroy_ deletes categories from the database.

        Args:
            request (_type_):
            pk (UUID | None, optional):

        Returns:
            status (204):
        """

        project = self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)


# Accessories
class AccessoriesListRestView(viewsets.ModelViewSet[Accessories]):
    """_AccessoriesListRestView_ returns accessories list with extended fields data in JSON format.

    Other parameters:
        queryset (Accessories):
        serializer_class (AccessoriesListModelSerializer):
    """

    queryset = Accessories.objects.all()
    serializer_class = AccessoriesListModelSerializer

    def list(self, request):
        """_list_ returns accessories list with extended fields data in JSON format.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """

        queryset = Accessories.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class AccessoriesRestView(viewsets.ModelViewSet[Accessories]):
    """_AccessoriesRestView_ returns accessories in JSON format.

    Other parameters:
        queryset (Accessories):
        serializer_class (AccessoriesModelSerializer):
    """

    queryset = Accessories.objects.all()
    serializer_class = AccessoriesModelSerializer

    def create(self, request):
        """_create_ adds accessories to the database.

        Args:
            request (_type_):
        Returns:
            data (JSON):
            error (JSON):
        """

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        """_retrieve_ returns accessories data in JSON format.

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
        """_update_ updates accessories in the database.

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
        """_destroy_ deletes accessories from the database.

        Args:
            request (_type_):
            pk (UUID | None, optional):

        Returns:
            status (204):
        """

        project = self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)


class AccCatRestView(viewsets.ModelViewSet[AccCat]):
    """_AccCatRestView_ returns accessories categories in JSON format.

    Other parameters:
        queryset (AccCat):
        serializer_class (AccCatModelSerializer):
    """

    queryset = AccCat.objects.all()
    serializer_class = AccCatModelSerializer

    def list(self, request):
        """_list_ returns accessories categories in JSON format.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """

        queryset = AccCat.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """_create_ adds accessories categories to the database.

        Args:
            request (_type_):

        Returns:
            data (JSON):
            error (JSON):
        """

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        """_retrieve_ returns accessories categories data in JSON format.

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
        """_update_ updates accessories categories in the database.

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
        """_destroy_ deletes accessories categories from the database.

        Args:
            request (_type_):
            pk (UUID | None, optional):

        Returns:
            status (204):
        """

        project = self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)
