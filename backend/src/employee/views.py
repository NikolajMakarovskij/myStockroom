from rest_framework import viewsets
from rest_framework.response import Response

from .models import Departament, Employee, Post
from .serializers import (
    DepartamentSerializer,
    EmployeeListSerializer,
    EmployeeSerializer,
    PostListSerializer,
    PostSerializer,
)


# Сотрудники
class EmployeeListRestView(viewsets.ModelViewSet[Employee]):
    """_EmployeeListRestView_ returns employees with extended fields data in JSON format.

    Other parameters:
        queryset (Employee):
        serializer_class (EmployeeListSerializer):
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeListSerializer

    def list(self, request):
        """_list_ returns employees with extended fields data in JSON format.

        Args:
            request (_type_): _description_

        Returns:
            data (JSON):
        """

        queryset = Employee.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class EmployeeRestView(viewsets.ModelViewSet[Employee]):
    """_EmployeeRestView_ returns employees in JSON format.

    Other parameters:
        queryset (Employee):
        serializer_class (EmployeeSerializer):
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request):
        """_create_ adds a new employee to the database.

        Args:
            request (_type_): _description_

        Returns:
            data (JSON):
            errors (JSON):
        """

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        """_retrieve_ returns the specified employee in JSON format.

        Args:
            request (_type_): _description_
            pk (UUID | None, optional):

        Returns:
            data (JSON):
        """

        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """_update_ updates the employee in the database.

        Args:
            request (_type_): _description_
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
        """_destroy_ deletes the employee from the database.

        Args:
            request (_type_): _description_
            pk (UUID | None, optional):

        Returns:
            status (204)
        """

        project = self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)


# Должность
class PostListRestView(viewsets.ModelViewSet[Post]):
    """_PostListRestView_ returns positions with extended fields data in JSON format.

    Other parameters:
        queryset (Post):
        serializer_class (PostListSerializer):
    """

    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def list(self, request):
        """_list_ returns positions with extended fields data in JSON format.

        Args:
            request (_type_): _description_

        Returns:
            data (JSON):
        """

        queryset = Post.objects.all()  # Do not delete it. When inheriting from a class, it returns empty data in tests.
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class PostRestView(viewsets.ModelViewSet[Post]):
    """_PostRestView_ returns positions in JSON format.

    Other parameters:
        queryset (Post):
        serializer_class (PostSerializer):
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request):
        """_create_ adds post to the database.

        Args:
            request (_type_): _description_

        Returns:
            data (JSON):
            errors (JSON):
        """

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        """_retrieve_ returns posts data in JSON format.

        Args:
            request (_type_): _description_
            pk (UUID | None, optional):

        Returns:
            data (JSON):
            errors (JSON):
        """

        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """_update_ updates post in the database.

        Args:
            request (_type_): _description_
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
        """_destroy_ deletes the post from the database.

        Args:
            request (_type_): _description_
            pk (UUID | None, optional):

        Returns:
            status (204)
        """

        project = self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)


# Отдел
class DepartamentRestView(viewsets.ModelViewSet[Departament]):
    queryset = (
        Departament.objects.all()
    )  # Do not delete it. When inheriting from a class, it returns empty data in tests.
    """_DepartamentRestView_ returns departments in JSON format.

    Other parameters:
        serializer_class (DepartamentSerializer):
    """

    serializer_class = DepartamentSerializer

    def list(self, request):
        """_list_ returns departments with extended fields data in JSON format.

        Args:
            request (_type_): _description_

        Returns:
            data (JSON):
        """

        queryset = Departament.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """_create_ adds departments to the database.

        Args:
            request (_type_): _description_

        Returns:
            data (JSON):
            errors (JSON):
        """

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        """_retrieve_ returns departments data in JSON format.

        Args:
            request (_type_): _description_
            pk (UUID | None, optional):

        Returns:
            data (JSON):
            errors (JSON):
        """

        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """_update_ updates departments in the database.

        Args:
            request (_type_): _description_
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
        """_destroy_ deletes the departments from the database.

        Args:
            request (_type_): _description_
            pk (UUID | None, optional):

        Returns:
            status (204)
        """

        project = self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)
