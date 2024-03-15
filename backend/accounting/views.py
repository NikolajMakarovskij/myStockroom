from rest_framework import viewsets
from rest_framework.response import Response
from .models import Accounting, Categories
from .serializers import AccountingModelSerializer, CategoriesModelSerializer, AccountingListModelSerializer


class AccountingListRestView(viewsets.ModelViewSet):
    queryset = Accounting.objects.all()
    serializer_class = AccountingListModelSerializer

    def list(self, request):
        queryset = Accounting.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class AccountingRestView( viewsets.ModelViewSet):
    queryset = Accounting.objects.all()
    serializer_class = AccountingModelSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)

    def update(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)


class CategoriesRestView(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesModelSerializer

    def list(self, request):
        queryset = Categories.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)

    def update(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)
