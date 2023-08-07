import pytest
from ..forms import ConsumablesForm, Categories, Manufacturer, AccessoriesForm, AccCat
from django.core.files import File
from unittest import mock


# Расходники
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
        'cost': "32.23",
        'serial': "some_serial123",
        'invent': "some_invent123",
        'serialImg': mock.MagicMock(spec=File, name='serial_Img'),
        'inventImg': mock.MagicMock(spec=File, name='invent_Img'),
    }
    form = ConsumablesForm(data=form_data)
    assert form.is_valid() is True


@pytest.mark.django_db
def test_consumable_form_name_invalid():
    """Тест на наличие названия"""
    err_name = "Обязательное поле."
    form_data = {
        'name': "",
    }
    form = ConsumablesForm(data=form_data)
    assert form.is_valid() is False
    assert [err_name] == form.errors['name']


@pytest.mark.django_db
def test_consumable_form_code_invalid():
    """Тест на наличие бухгалтерского кода"""
    err_mes = "Введите число."
    form_data = {
        'name': "my_consumable",
        'cost': "qwerty",
    }
    form = ConsumablesForm(data=form_data)
    assert form.is_valid() is False
    assert [err_mes] == form.errors['cost']


# Комплектующие
@pytest.mark.django_db
def test_accessories_form_valid():
    """Тест на валидность формы"""
    AccCat.objects.create(name="my_category")
    Manufacturer.objects.create(name="My_manufacturer")

    form_data = {
        'name': "my_consumable",
        'categories': AccCat.objects.get(name="my_category"),
        'description': "some_description",
        'note': "some_name",
        'manufacturer': Manufacturer.objects.get(name="My_manufacturer"),
        'buhCode': "000753",
        'cost': "32.23",
        'serial': "some_serial123",
        'invent': "some_invent123",
        'serialImg': mock.MagicMock(spec=File, name='serial_Img'),
        'inventImg': mock.MagicMock(spec=File, name='invent_Img'),
    }
    form = AccessoriesForm(data=form_data)
    assert form.is_valid() is True


@pytest.mark.django_db
def test_accessories_form_name_invalid():
    """Тест на наличие названия"""
    err_name = "Обязательное поле."
    form_data = {
        'name': "",
    }
    form = AccessoriesForm(data=form_data)
    assert form.is_valid() is False
    assert [err_name] == form.errors['name']


@pytest.mark.django_db
def test_accessories_form_code_invalid():
    """Тест на наличие бухгалтерского кода"""
    err_mes = "Введите число."
    form_data = {
        'name': "my_consumable",
        'cost': "qwerty",
    }
    form = AccessoriesForm(data=form_data)
    assert form.is_valid() is False
    assert [err_mes] == form.errors['cost']
