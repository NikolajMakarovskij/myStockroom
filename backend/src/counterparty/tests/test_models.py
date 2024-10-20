import pytest

from ..models import Manufacturer


@pytest.mark.django_db
def test_manufacturer_create():
    """Тестирует создание записи в базе данных для модели Manufacturer приложения Counterparties"""
    Manufacturer.objects.create(
        name="name_manufacturer", country="country", production="production_country"
    )
    manufacturer = Manufacturer.objects.get(name="name_manufacturer")
    assert Manufacturer.objects.count() == 1
    assert manufacturer.name == "name_manufacturer"
    assert manufacturer.country == "country"
    assert manufacturer.production == "production_country"
    assert manufacturer.__str__() == "name_manufacturer"
