import pytest
from ..forms import ManufacturerForm


@pytest.mark.django_db
def test_manufacturer_form_valid():
    """Тест на валидность формы"""
    form_data = {
        "name": "manufacturer_name",
        "country": "manufacturer_country",
        "production": "manufacturer_production",
    }
    form = ManufacturerForm(data=form_data)
    assert form.is_valid() is True


@pytest.mark.django_db
def test_manufacturer_form_name_invalid():
    """Тест на наличие названия"""
    err_mes = "Обязательное поле."
    form_data = {
        'name': "",
    }
    form = ManufacturerForm(data=form_data)
    assert form.is_valid() is False
    assert [err_mes] == form.errors['name']
