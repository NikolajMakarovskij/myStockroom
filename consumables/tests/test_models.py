from django.db.utils import IntegrityError
import pytest
from myStockroom.wsgi import *
from ..models import Consumables, Categories
from counterparty.models import Manufacturer
from django.core.files import File
from unittest import mock


@pytest.mark.django_db  
def test_category_create():
    """Тестирует создание записи в базе данных для модели Categories приложения Consumables"""
    category = Categories.objects.create(
        name = "my_category_name",
        slug = "my_category_slug"
    )
    assert Categories.objects.count() == 1
    assert category.name == "my_category_name"
    assert category.slug == "my_category_slug"

@pytest.mark.django_db  
def test_category_unique_slug():
    """Тестирует наличие дублирования в поле slug"""
    with pytest.raises(IntegrityError):
        Categories.objects.create(
            name = "my_category_1",
            slug = "my_category"
        )

        assert  (Categories.objects.create(
            name = "my_category_2",
            slug = "my_category"
        )
        )

@pytest.mark.django_db  
def test_consumable_create():
    """Тестирует создание записи в базе данных для модели Consumables"""
    Categories.objects.create(
        name = "my_category",
        slug = "my_category"
    )
    Manufacturer.objects.create(
        name = "name_manufacturer",
        country = "country",
        production = "production_country"
    ) 
    consumable = Consumables.objects.create(  
        name = "my_consumable",  
        categories = Categories.objects.get(name="my_category"),
        manufacturer = Manufacturer.objects.get(name="name_manufacturer"),  
        serial = "123",
        invent = "321",
        buhCode = "code",
        score = "0",
        description = "my_description",
        note = "my_note",
    )  
    assert Consumables.objects.count() == 1
    assert consumable.name == "my_consumable"
    assert consumable.categories.name == "my_category"
    assert consumable.categories.slug == "my_category" 
    assert consumable.manufacturer.name == "name_manufacturer"
    assert consumable.manufacturer.country == "country"
    assert consumable.manufacturer.production == "production_country"
    assert consumable.serial == "123"
    assert consumable.invent == "321"
    assert consumable.buhCode == "code"
    assert consumable.score == "0"
    assert consumable.description == "my_description"
    assert consumable.note == "my_note"



