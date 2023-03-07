from django.db.utils import IntegrityError
import pytest  
from myStockroom.wsgi import *
from ..models import Employee, Departament, Post
from workplace.models import Workplace



@pytest.mark.django_db  
def test_departament_create():
    """Тестирует создание записи в базе данных для модели Departament приложения Employee"""
    departament = Departament.objects.create(
        name = "name_departament",
    ) 

    assert departament.name == "name_departament"

@pytest.mark.django_db  
def test_post_create():
    """Тестирует создание записи в базе данных для модели Post приложения Employee"""
    Departament.objects.create(name="my_departament") 
    post = Post.objects.create(
        name = "my_post_name",
        departament = Departament.objects.get(name="my_departament"),
    )

    assert post.name == "my_post_name"
    assert post.departament.name == "my_departament"
    
@pytest.mark.django_db  
def test_employee_create():
    """Тестирует создание записи в базе данных для модели Employee"""
    Departament.objects.create(name="my_departament")
    Post.objects.create(
        name = "employee_post",
        departament = Departament.objects.get(name="my_departament")
    )
    Workplace.objects.create(
        name = "my_workplace",
    ) 
    employee = Employee.objects.create(  
        name = "employee_name",  
        sername = "employee_sername",
        family = "employee_family",  
        workplace = Workplace.objects.get(name="my_workplace"),
        post = Post.objects.get(name = "employee_post"),
        employeeEmail = "admin@admin.com",
    )  

    assert employee.name == "employee_name"
    assert employee.sername == "employee_sername"
    assert employee.family == "employee_family" 
    assert employee.workplace.name == "my_workplace"
    assert employee.post.name == "employee_post"
    assert employee.post.departament.name == "my_departament"
    assert employee.employeeEmail == "admin@admin.com"

@pytest.mark.django_db  
def test_email_unique():
    """Тестирует наличие дублирования в поле employeeEmail"""
    with pytest.raises(IntegrityError):
        Employee.objects.create(
            name = "my_category_1",
            employeeEmail = "admin@admin.com"
        )

        assert  (Employee.objects.create(
            name = "my_category_2",
            employeeEmail = "admin@admin.com"
        )
        )