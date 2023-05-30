from unittest import mock
from django.core.files import File
import pytest
from ..forms import upsForm, cassetteForm, Manufacturer, Cassette
from consumables.models import Consumables, Categories as con_cat


@pytest.mark.django_db
def test_cassette_form_valid():
    """Тест на валидность формы"""
    Manufacturer.objects.create(name="epson")
    Consumables.objects.create(
        name="accumulator",
        categories=con_cat.objects.create(
            name="Аккумуляторы",
            slug="accumulators"
        )
    )
    form_data = {
        "name": "cassette_name", 
        "manufacturer": Manufacturer.objects.get(name="epson"),
        "serial": "some_serial",
        "invent": "some_number_124",
        "serialImg": mock.MagicMock(spec=File, name='serial_Img'),
        "inventImg": mock.MagicMock(spec=File, name='invent_Img'),
        "power": "150W",
        "voltage": "12V",
        "current": "7A",
        "accumulator": Consumables.objects.get(name = "accumulator"),
        "score": "0",
    }
    form = cassetteForm(data=form_data)
    assert form.is_valid() is True

@pytest.mark.django_db
def test_cassette_form_name_invalid():
    """Тест на наличие названия"""
    err_name = "Обязательное поле."
    form_data = {
        'name': "",
    }
    form = cassetteForm(data=form_data)
    assert form.is_valid() is False
    assert [err_name] == form.errors['name']

@pytest.mark.django_db
def test_cassete_form_score_invalid():
    """Тест на правильность данных в поле количества"""
    err_mes = "Введите целое число."
    form_data = {
        "name": "my_consumable",
        "score": "qwerty",
    }
    form = cassetteForm(data=form_data)
    assert form.is_valid() is False
    assert [err_mes] == form.errors['score']

@pytest.mark.django_db
def test_ups_form_valid():
    """Тест на валидность формы"""
    Manufacturer.objects.create(name="epson")
    Consumables.objects.create(
        name="accumulator",
        categories=con_cat.objects.create(
            name="Аккумуляторы",
            slug="accumulators"
        )
    )
    Cassette.objects.create(name="some_cassette", accumulator= Consumables.objects.get(name="accumulator"))
    form_data = {
        "name": "cassette_name", 
        "manufacturer": Manufacturer.objects.get(name="epson"),
        "serial": "some_serial",
        "invent": "some_number_124",
        "power": "150W",
        "voltage": "12V",
        "current": "7A",
        "accumulator": Consumables.objects.get(name = "accumulator"),
        "cassette": Cassette.objects.get(name="some_cassette"),
        "score": "0",
    }
    form = upsForm(data=form_data)
    assert form.is_valid() is True

@pytest.mark.django_db
def test_ups_form_name_invalid():
    """Тест на наличие названия"""
    err_name = "Обязательное поле."
    form_data = {
        'name': "",
    }
    form = upsForm(data=form_data)
    assert form.is_valid() is False
    assert [err_name] == form.errors['name']

@pytest.mark.django_db
def test_ups_form_score_invalid():
    """Тест на правильность данных в поле количества"""
    err_mes = "Введите целое число."
    form_data = {
        "name": "my_consumable",
        "score": "qwerty",
    }
    form = upsForm(data=form_data)
    assert form.is_valid() is False
    assert [err_mes] == form.errors['score']