import pytest
from ..forms import manufacturerForm


@pytest.mark.django_db
def test_manufacturer_form_valid():
    """Тест на валидность формы"""
    form_data = {
        "name": "manufacturer_name",
        "country": "manufacturer_country",
        "production": "manufacturer_production",
    }
    form = manufacturerForm(data=form_data)
    assert form.is_valid() is True