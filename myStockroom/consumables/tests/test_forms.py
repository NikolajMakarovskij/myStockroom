import pytest
from ..forms import consumablesForm, Categories, Manufacturer, Consumables
from django.core.files import File
from unittest import mock

@pytest.mark.django_db
def test_consumable_form_valid():
    """Тест на валидность формы"""
    Categories.objects.create(name="my_category")
    Manufacturer.objects.create(name="My_manufacturer")

    form_data = {
        'name': "my_consumable",
        'categories': Categories.objects.get(name="my_category"),
        'description': "some_description",
        'note': "some_name",
        'manufacturer': Manufacturer.objects.get(name="My_manufacturer"),
        'buhCode': "000753",
        'score': "0",
        'serial': "some_serial123",
        'invent': "some_invent123",
        'serialImg': mock.MagicMock(spec=File, name='serial_Img'),
        'inventImg': mock.MagicMock(spec=File, name='invent_Img'),
    }
    form = consumablesForm(data=form_data)
    assert form.is_valid() is True
    

@pytest.mark.django_db
def test_consumable_form_name_invalid():
    """Тест на наличие названия"""
    err_name = "Обязательное поле."
    form_data = {
        'name': "",
    }
    form = consumablesForm(data=form_data)
    assert form.is_valid() is False
    assert [err_name] == form.errors['name']

@pytest.mark.django_db
def test_consumable_form_code_invalid():
    """Тест на наличие бухгалтерского кода"""
    err_mes = "Обязательное поле."
    form_data = {
        'name': "my_consumable",
        'buhCode': "",
    }
    form = consumablesForm(data=form_data)
    assert form.is_valid() is False
    assert [err_mes] == form.errors['buhCode']

@pytest.mark.django_db
def test_consumable_form_score_invalid():
    """Тест на правильность данных в поле количества"""
    err_mes = "Введите целое число."
    form_data = {
        "name": "my_consumable",
        "score": "qwerty",
    }
    form = consumablesForm(data=form_data)
    assert form.is_valid() is False
    assert [err_mes] == form.errors['score']

