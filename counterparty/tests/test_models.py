from django.db.utils import IntegrityError
import pytest  
from myStockroom.wsgi import *
from ..models import Manufacturer

@pytest.mark.django_db  
def test_manufacturer_create():
    """Тестирует создание записи в базе данных для модели Manufacturer приложения Counterparties"""
    manufacturer = Manufacturer.objects.create(
        name = "name_manufacturer",
        country = "country",
        production = "production_country"
    ) 

    assert manufacturer.name == "name_manufacturer"
    assert manufacturer.country == "country"
    assert manufacturer.production == "production_country"