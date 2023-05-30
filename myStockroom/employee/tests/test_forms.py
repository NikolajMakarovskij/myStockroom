import pytest
from ..forms import employeeForm ,departamentForm, postForm, Post, Departament
from workplace.models import Workplace


@pytest.mark.django_db
def test_departament_form_valid():
    """Тест на валидность формы"""

    form_data = {
        "name": "departament_name",  
    }
    form = departamentForm(data=form_data)
    assert form.is_valid() is True

@pytest.mark.django_db
def test_departament_form_name_invalid():
    """Тест на наличие названия"""
    err_name = "Обязательное поле."
    form_data = {
        'name': "",
    }
    form = departamentForm(data=form_data)
    assert form.is_valid() is False
    assert [err_name] == form.errors['name']

@pytest.mark.django_db
def test_post_form_valid():
    """Тест на валидность формы"""
    Departament.objects.create(name="dep_name")
    form_data = {
        "name": "departament_name",
        "departament": Departament.objects.get(name="dep_name")  
    }
    form = postForm(data=form_data)
    assert form.is_valid() is True

@pytest.mark.django_db
def test_post_form_name_invalid():
    """Тест на наличие названия"""
    err_name = "Обязательное поле."
    form_data = {
        'name': "",
    }
    form = postForm(data=form_data)
    assert form.is_valid() is False
    assert [err_name] == form.errors['name']

@pytest.mark.django_db
def test_employee_form_valid():
    """Тест на валидность формы"""
    Post.objects.create(name = "employee_post")
    Workplace.objects.create(name = "my_workplace")

    form_data = {
        "name": "employee_name",  
        "sername": "employee_sername",
        "family": "employee_family",  
        "workplace": Workplace.objects.get(name="my_workplace"),
        "post": Post.objects.get(name = "employee_post"),
        "employeeEmail": "admin@admin.com",
    }
    form = employeeForm(data=form_data)
    assert form.is_valid() is True

@pytest.mark.django_db
def test_employee_form_name_invalid():
    """Тест на наличие названия"""
    err_name = "Обязательное поле."
    form_data = {
        'name': "",
    }
    form = employeeForm(data=form_data)
    assert form.is_valid() is False
    assert [err_name] == form.errors['name']

@pytest.mark.django_db
def test_employye_form_email_invalid():
    """Тест на проверку адреса электронной почты"""
    err_mes = "Введите правильный адрес электронной почты."
    form_data = {
        "name": "my_consumable",
        "employeeEmail": "123adb",
    }
    form = employeeForm(data=form_data)
    assert form.is_valid() is False
    assert [err_mes] == form.errors['employeeEmail']