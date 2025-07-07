from rest_framework import serializers

from workplace.serializers import WorkplaceListSerializer

from .models import Departament, Employee, Post


class DepartamentSerializer(serializers.ModelSerializer[Departament]):
    """_DepartamentSerializer_ Serialize Departament Model to JSON"""

    class Meta:
        """_Class returns JSON of Departament model_

        Returns:
            model (Departament):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Departament
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class PostSerializer(serializers.ModelSerializer[Post]):
    """_PostSerializer_ Serialize Post Model to JSON"""

    class Meta:
        """_Class returns JSON of Post model_

        Returns:
            model (Post):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Post
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class PostListSerializer(serializers.ModelSerializer[Post]):
    """_PostListSerializer_ Serialize Post Model with extended fields JSON

    Other parameters:
        departament (DepartamentSerializer): _serialize Departament model_
    """

    departament = DepartamentSerializer(read_only=True)

    class Meta:
        """_Class returns JSON of Post model with extended fields_

        Returns:
            model (Post):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Post
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class EmployeeSerializer(serializers.ModelSerializer[Employee]):
    """_EmployeeSerializer_ Serialize Employee Model to JSON"""

    class Meta:
        """_Class returns JSON of Employee model_

        Returns:
            model (Employee):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Employee
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class EmployeeListSerializer(serializers.ModelSerializer[Employee]):
    """_EmployeeListSerializer_ Serialize Employee Model with extended fields JSON

    Other parameters:
        post (PostListSerializer): _serialize Post model with extended fields_
        workplace (WorkplaceListSerializer): _serialize Workplace model with extended fields_
    """

    post = PostListSerializer(read_only=True)
    workplace = WorkplaceListSerializer(read_only=True)

    class Meta:
        """_Class returns JSON of Employee model with extended fields_

        Returns:
            model (Employee):
            fields (list[str]): _returns fields of model in form_
            extra_kwargs (dict[str,list[str]): _returns settings of fields_
        """

        model = Employee
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}
