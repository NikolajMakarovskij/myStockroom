import datetime
import pytest
from django.db.utils import IntegrityError
from django.urls import reverse

from counterparty.models import Manufacturer
from ..models import Stockroom, Consumables, StockCat, History


@pytest.mark.django_db
def test_category_create():
    """Тестирует создание записи в базе данных для модели Categories приложения Stockroom"""
    StockCat.objects.create(
        name="my_category_name",
        slug="my_category_slug"
    )
    category = StockCat.objects.get(name="my_category_name")
    assert StockCat.objects.count() == 1
    assert category.name == "my_category_name"
    assert category.slug == "my_category_slug"
    assert category.__str__() == 'my_category_name'
    assert category.get_absolute_url() == reverse('stockroom:category', kwargs={'category_slug': category.slug})


@pytest.mark.django_db
def test_category_unique_slug():
    """Тестирует наличие дублирования в поле slug"""
    with pytest.raises(IntegrityError):
        StockCat.objects.create(
            name="my_category_1",
            slug="my_category"
        )

        assert (StockCat.objects.create(
            name="my_category_2",
            slug="my_category"
        )
        )


@pytest.mark.django_db
def test_stockroom_create():
    """Тестирует создание записи в базе данных для модели Consumables"""
    StockCat.objects.create(name="my_category", slug="my_category")
    Manufacturer.objects.create(name="name_manufacturer", )
    Consumables.objects.create(
        name="my_consumable",
        manufacturer=Manufacturer.objects.get(name="name_manufacturer"),
        score=10
    )
    Stockroom.objects.create(
        consumables=Consumables.objects.get(name="my_consumable", score=10),
        categories=StockCat.objects.get(name="my_category"),
        dateAddToStock=datetime.date.today(),
        dateInstall=datetime.date.today(),
        rack=6,
        shelf=15,
        device='epson'
    )
    stockroom = Stockroom.objects.get(consumables__name="my_consumable")
    assert Stockroom.objects.count() == 1
    assert stockroom.consumables.name == "my_consumable"
    assert stockroom.consumables.manufacturer.name == "name_manufacturer"
    assert stockroom.consumables.score == 10
    assert stockroom.categories.name == "my_category"
    assert stockroom.dateAddToStock == datetime.date.today()
    assert stockroom.dateInstall == datetime.date.today()
    assert stockroom.rack == 6
    assert stockroom.shelf == 15
    assert stockroom.device == 'epson'


@pytest.mark.django_db
def test_history_create():
    """Тестирует создание записи в базе данных для модели Consumables"""
    StockCat.objects.create(name="my_category", slug="my_category")
    History.objects.create(
        consumable="my_consumable",
        consumableId="name_manufacturer",
        categories=StockCat.objects.get(name="my_category"),
        score=1,
        dateInstall=datetime.date.today(),
        user="admin"
    )
    history = History.objects.get(consumable="my_consumable")
    assert History.objects.count() == 1
    assert history.consumable == "my_consumable"
    assert history.consumableId == "name_manufacturer"
    assert history.categories.name == "my_category"
    assert history.score == 1
    assert history.dateInstall == datetime.date.today()
    assert history.user == "admin"
