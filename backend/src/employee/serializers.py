from rest_framework import serializers
from workplace.serializers import WorkplaceListSerializer
from .models import Post, Employee, Departament


class DepartamentSerializer(serializers.ModelSerializer):
    queryset = Departament.objects.all()

    class Meta:
        model = Departament
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class PostSerializer(serializers.ModelSerializer):
    queryset = Post.objects.all()

    class Meta:
        model = Post
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class PostListSerializer(serializers.ModelSerializer):
    queryset = Post.objects.all()
    departament = DepartamentSerializer(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class EmployeeSerializer(serializers.ModelSerializer):
    queryset = Employee.objects.all()

    class Meta:
        model = Employee
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class EmployeeListSerializer(serializers.ModelSerializer):
    queryset = Post.objects.all()
    post = PostListSerializer(read_only=True)
    workplace = WorkplaceListSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}
