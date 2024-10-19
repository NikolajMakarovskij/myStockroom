import pytest
from django.db.utils import IntegrityError
from workplace.models import Workplace

from ..models import Departament, Employee, Post


@pytest.mark.django_db
def test_departament_create():
    """Тестирует создание записи в базе данных для модели Departament приложения Employee"""
    Departament.objects.create(name="name_departament")
    departament = Departament.objects.get(name="name_departament")
    assert Departament.objects.count() == 1
    assert departament.name == "name_departament"
    assert departament.__str__() == "name_departament"


@pytest.mark.django_db
def test_post_create():
    """Тестирует создание записи в базе данных для модели Post приложения Employee"""
    Departament.objects.create(name="my_departament")
    Post.objects.create(
        name="my_post_name",
        departament=Departament.objects.get(name="my_departament"),
    )
    post = Post.objects.get(name="my_post_name")
    assert Post.objects.count() == 1
    assert post.name == "my_post_name"
    assert post.departament.name == "my_departament"  # type: ignore[union-attr]
    assert post.__str__() == "my_post_name"


@pytest.mark.django_db
def test_employee_create():
    """Тестирует создание записи в базе данных для модели Employee"""
    Departament.objects.create(name="my_departament")
    Post.objects.create(
        name="employee_post", departament=Departament.objects.get(name="my_departament")
    )
    Workplace.objects.create(
        name="my_workplace",
    )
    Employee.objects.create(
        name="employee_name",
        surname="employee_surname",
        last_name="employee_last_name",
        workplace=Workplace.objects.get(name="my_workplace"),
        post=Post.objects.get(name="employee_post"),
        employeeEmail="admin@admin.com",
    )
    employee = Employee.objects.get(name="employee_name")
    assert Employee.objects.count() == 1
    assert employee.name == "employee_name"
    assert employee.surname == "employee_surname"
    assert employee.last_name == "employee_last_name"
    assert employee.workplace.name == "my_workplace"  # type: ignore[union-attr]
    assert employee.post.name == "employee_post"  # type: ignore[union-attr]
    assert employee.post.departament.name == "my_departament"  # type: ignore[union-attr]
    assert employee.employeeEmail == "admin@admin.com"
    assert employee.__str__() == "employee_name"


@pytest.mark.django_db
def test_email_unique():
    """Тестирует наличие дублирования в поле employeeEmail"""
    with pytest.raises(IntegrityError):
        Employee.objects.create(name="my_category_1", employeeEmail="admin@admin.com")

        assert Employee.objects.create(
            name="my_category_2", employeeEmail="admin@admin.com"
        )
