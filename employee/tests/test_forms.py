import pytest
from ..forms import employeeForm ,Employee, Post
from workplace.models import Workplace

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