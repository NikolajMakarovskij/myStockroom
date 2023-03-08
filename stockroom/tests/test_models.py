from django.db.utils import IntegrityError
import pytest  
from myStockroom.wsgi import *
from ..models import Stockroom, Consumables, Categories, History
from counterparty.models import Manufacturer


@pytest.mark.django_db  
def test_category_create():
    """Тестирует создание записи в базе данных для модели Categories приложения Stockroom"""
    category = Categories.objects.create(
        name = "my_category_name",
        slug = "my_category_slug"
    )

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
def test_stockroom_create():
    """Тестирует создание записи в базе данных для модели Consumables"""
    Categories.objects.create(name = "my_category",slug = "my_category")
    Manufacturer.objects.create(name = "name_manufacturer",) 
    Consumables.objects.create(
        name="my_consumable",
        manufacturer = Manufacturer.objects.get(name = "name_manufacturer"), 
        score=10
    )
    stockroom = Stockroom.objects.create(  
        consumables= Consumables.objects.get(name="my_consumable", score=10),  
        categories = Categories.objects.get(name="my_category"),
        dateAddToStock = "2022-12-25",
        dateInstall = "2023-03-03",
        rack = 6,
        shelf = 15
    )  

    assert stockroom.consumables.name == "my_consumable"
    assert stockroom.consumables.manufacturer.name == "name_manufacturer"
    assert stockroom.consumables.score == 10
    assert stockroom.categories.name == "my_category"
    assert stockroom.dateAddToStock == "2022-12-25"
    assert stockroom.dateInstall == "2023-03-03"
    assert stockroom.rack == 6
    assert stockroom.shelf == 15


