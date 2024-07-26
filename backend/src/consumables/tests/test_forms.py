from unittest import mock

import pytest
from django.core.files import File

from ..forms import AccCat, AccessoriesForm, Categories, ConsumablesForm, Manufacturer


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
