import pytest

from consumables.models import Categories as ConCat

from ..forms import Consumables, Device, Employee, SignatureForm


@pytest.mark.django_db
def test_signature_form_valid():
    """Тест на валидность формы"""
    Employee.objects.create(name="some_employee_1")
    Employee.objects.create(name="some_employee_2")
    Device.objects.create(name="Acer C27")
    Consumables.objects.create(
        name="T7741",
        categories=ConCat.objects.create(
            name="Накопители",
            slug="storages"
        )
    )
    form_data = {
        "name": "signature_name",
        "periodOpen": "2018-9-12",
        "periodClose": "2022-3-31",
        "employeeRegister": Employee.objects.get(name="some_employee_1"),
        "employeeStorage": Employee.objects.get(name="some_employee_2"),
        "workstation": Device.objects.get(name="Acer C27"),
        "storage": Consumables.objects.get(name="T7741")
    }
    form = SignatureForm(data=form_data)
    assert form.is_valid() is True


@pytest.mark.django_db
def test_signature_form_date_open_incorrect():
    """Тест на формат ввода даты"""
    err_mes = "Введите правильную дату."
    form_data = {
        "name": "my_consumable",
        "periodOpen": "12-12-2018",
    }
    form = SignatureForm(data=form_data)
    assert form.is_valid() is False
    assert [err_mes] == form.errors['periodOpen']


@pytest.mark.django_db
def test_signature_form_date_close_incorrect():
    """Тест на формат ввода даты"""
    err_mes = "Введите правильную дату."
    form_data = {
        "name": "my_consumable",
        "periodClose": "2022-13-42",
    }
    form = SignatureForm(data=form_data)
    assert form.is_valid() is False
    assert [err_mes] == form.errors['periodClose']
