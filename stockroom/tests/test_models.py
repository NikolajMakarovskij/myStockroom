from django.db.utils import IntegrityError
import pytest  
from ..models import Stockroom, Consumables, Stock_cat, History
from counterparty.models import Manufacturer


@pytest.mark.django_db  
def test_category_create():
    """Тестирует создание записи в базе данных для модели Categories приложения Stockroom"""
    category = Stock_cat.objects.create(
        name = "my_category_name",
        slug = "my_category_slug"
    )
    assert Stock_cat.objects.count() == 1
    assert category.name == "my_category_name"
    assert category.slug == "my_category_slug"

@pytest.mark.django_db  
def test_category_unique_slug():
    """Тестирует наличие дублирования в поле slug"""
    with pytest.raises(IntegrityError):
        Stock_cat.objects.create(
            name = "my_category_1",
            slug = "my_category"
        )

        assert  (Stock_cat.objects.create(
            name = "my_category_2",
            slug = "my_category"
        )
        )
    

@pytest.mark.django_db  
def test_stockroom_create():
    """Тестирует создание записи в базе данных для модели Consumables"""
    Stock_cat.objects.create(name = "my_category",slug = "my_category")
    Manufacturer.objects.create(name = "name_manufacturer",) 
    Consumables.objects.create(
        name="my_consumable",
        manufacturer = Manufacturer.objects.get(name = "name_manufacturer"), 
        score=10
    )
    stockroom = Stockroom.objects.create(  
        consumables= Consumables.objects.get(name="my_consumable", score=10),  
        categories = Stock_cat.objects.get(name="my_category"),
        dateAddToStock = "2022-12-25",
        dateInstall = "2023-03-03",
        rack = 6,
        shelf = 15,
        device = 'epson'
    )  
    assert Stockroom.objects.count() == 1
    assert stockroom.consumables.name == "my_consumable"
    assert stockroom.consumables.manufacturer.name == "name_manufacturer"
    assert stockroom.consumables.score == 10
    assert stockroom.categories.name == "my_category"
    assert stockroom.dateAddToStock == "2022-12-25"
    assert stockroom.dateInstall == "2023-03-03"
    assert stockroom.rack == 6
    assert stockroom.shelf == 15
    assert stockroom.device == 'epson'

@pytest.mark.django_db  
def test_hysrory_create():
    """Тестирует создание записи в базе данных для модели Consumables"""
    Stock_cat.objects.create(name = "my_category",slug = "my_category")
    history = History.objects.create(  
        consumable = "my_consumable",  
        consumableId = "name_manufacturer",
        categories = Stock_cat.objects.get(name="my_category"),
        score = "1",
        dateInstall = "2022-09-01",
        user = "admin"
    )  
    assert History.objects.count() == 1
    assert history.consumable == "my_consumable"
    assert history.consumableId == "name_manufacturer"
    assert history.categories.name == "my_category"
    assert history.score == "1"
    assert history.dateInstall == "2022-09-01"
    assert history.user == "admin"




