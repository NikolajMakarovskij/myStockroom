from rest_framework import viewsets
from rest_framework.response import Response

from .models import Accounting, Categories
from .serializers import (
    AccountingListModelSerializer,
    AccountingModelSerializer,
    CategoriesModelSerializer,
)


class AccountingListRestView(viewsets.ModelViewSet[Accounting]):
    """_AccountingRestView_ returns accounting with extended fields data in JSON format.

    Other parameters:
        queryset (Accounting):
        serializer_class (AccountingModelSerializer):
    """

    queryset = Accounting.objects.all()
    serializer_class = AccountingListModelSerializer

    def list(self, request):
        """_list_ returns accounting list with extended fields data in JSON format.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """
        queryset = Accounting.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class AccountingRestView(viewsets.ModelViewSet[Accounting]):
    """_AccountingRestView_ returns accounting data in JSON format.

    Other parameters:
        queryset (Accounting):
        serializer_class (AccountingModelSerializer):
    """

    queryset = Accounting.objects.all()
    serializer_class = AccountingModelSerializer

    def list(self, request):
        """_list_ returns accounting data in JSON format.

        Args:
            request (_type_):

        Returns:
            data (JSON):
        """

        queryset = Accounting.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """_create_ creates new accounting data in JSON format.

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
        """_retrieve_ retrieves accounting data in JSON format.

        Args:
            request (_type_):
            pk (UUID | None, optional): Defaults to None.

        Returns:
            data (JSON):
        """

        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """_update_ updates accounting data in JSON format.

        Args:
            request (_type_):
            pk (UUID | None, optional): Defaults to None.

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
        """_destroy_ deletes accounting data in JSON format.

        Args:
            request (_type_):
            pk (UUID | None, optional): Defaults to None.

        Returns:
            data (JSON):
        """

        project = self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)


class CategoriesRestView(viewsets.ModelViewSet[Categories]):
    """_CategoriesRestView_ returns categories data in JSON format.

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
        """_create_ creates new categories data in JSON format.

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
        """_retrieve_ retrieves categories data in JSON format.

        Args:
            request (_type_):
            pk (UUID | None, optional): Defaults to None.

        Returns:
            data (JSON):
        """

        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """_update_ updates categories data in JSON format.

        Args:
            request (_type_):
            pk (UUID | None, optional): Defaults to None.

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
        """_destroy_ deletes categories data in JSON format.

        Args:
            request (_type_):
            pk (UUID | None, optional): Defaults to None.

        Returns:
            data (JSON):
            error (JSON):
        """

        project = self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)
