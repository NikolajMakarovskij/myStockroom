from rest_framework import serializers

from workplace.serializers import WorkplaceListSerializer

from .models import Departament, Employee, Post


class DepartamentSerializer(serializers.ModelSerializer[Departament]):
    queryset = Departament.objects.all()

    class Meta:
        model = Departament
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class PostSerializer(serializers.ModelSerializer[Post]):
    queryset = Post.objects.all()

    class Meta:
        model = Post
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class PostListSerializer(serializers.ModelSerializer[Post]):
    queryset = Post.objects.all()
    departament = DepartamentSerializer(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class EmployeeSerializer(serializers.ModelSerializer[Employee]):
    queryset = Employee.objects.all()

    class Meta:
        model = Employee
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class EmployeeListSerializer(serializers.ModelSerializer[Employee]):
    queryset = Employee.objects.all()
    post = PostListSerializer(read_only=True)
    workplace = WorkplaceListSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}
