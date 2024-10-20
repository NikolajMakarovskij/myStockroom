import datetime

import pytest
from django.db.utils import IntegrityError

from consumables.models import Accessories, Consumables
from counterparty.models import Manufacturer
from device.models import Device
from stockroom.models.accessories import CategoryAcc, HistoryAcc, StockAcc
from stockroom.models.consumables import History, StockCat, Stockroom
from stockroom.models.devices import CategoryDev, HistoryDev, StockDev


# Consumables
@pytest.mark.django_db
def test_category_create():
    """Is testing the creation of a record in the database for the Categories model of the Stockroom application"""
    StockCat.objects.create(name="my_category_name", slug="my_category_slug")
    category = StockCat.objects.get(name="my_category_name")
    assert StockCat.objects.count() == 1
    assert category.name == "my_category_name"
    assert category.slug == "my_category_slug"
    assert category.__str__() == "my_category_name"


@pytest.mark.django_db
def test_category_unique_slug():
    """Tests for duplication in the slug field"""
    with pytest.raises(IntegrityError):
        StockCat.objects.create(name="my_category_1", slug="my_category")

        assert StockCat.objects.create(name="my_category_2", slug="my_category")


@pytest.mark.django_db
def test_stockroom_create():
    """Tests the creation of a record in the database for the Consumables model"""
    StockCat.objects.create(name="my_category", slug="my_category")
    Manufacturer.objects.create(
        name="name_manufacturer",
    )
    Consumables.objects.create(
        name="my_consumable",
        manufacturer=Manufacturer.objects.get(name="name_manufacturer"),
        quantity=10,
    )
    Stockroom.objects.create(
        stock_model=Consumables.objects.get(name="my_consumable"),
        categories=StockCat.objects.get(name="my_category"),
        dateAddToStock=datetime.date.today(),
        dateInstall=datetime.date.today(),
        rack=6,
        shelf=15,
    )
    stockroom = Stockroom.objects.get(stock_model__name="my_consumable")
    assert Stockroom.objects.count() == 1
    assert stockroom.stock_model.name == "my_consumable"
    assert stockroom.stock_model.manufacturer.name == "name_manufacturer"  # type: ignore[union-attr]
    assert stockroom.stock_model.quantity == 10
    assert stockroom.categories.name == "my_category"  # type: ignore[union-attr]
    assert stockroom.dateAddToStock == datetime.date.today()
    assert stockroom.dateInstall == datetime.date.today()
    assert stockroom.rack == 6
    assert stockroom.shelf == 15


@pytest.mark.django_db
def test_history_create():
    """Tests the creation of a record in the database for the Consumables model"""
    StockCat.objects.create(name="my_category", slug="my_category")
    History.objects.create(
        stock_model="my_consumable",
        stock_model_id="name_manufacturer",
        device="my_device",
        deviceId="device_id",
        categories=StockCat.objects.get(name="my_category"),
        quantity=1,
        dateInstall=datetime.date.today(),
        user="admin",
    )
    history = History.objects.get(stock_model="my_consumable")
    assert History.objects.count() == 1
    assert history.stock_model == "my_consumable"
    assert history.stock_model_id == "name_manufacturer"
    assert history.device == "my_device"
    assert history.deviceId == "device_id"
    assert history.categories.name == "my_category"  # type: ignore[union-attr]
    assert history.quantity == 1
    assert history.dateInstall == datetime.date.today()
    assert history.user == "admin"


# Accessories
@pytest.mark.django_db
def test_category_acc_create():
    """Is testing the creation of a record in the database for the CategoryAcc model of the Stockroom application"""
    CategoryAcc.objects.create(name="my_category_name", slug="my_category_slug")
    category = CategoryAcc.objects.get(name="my_category_name")
    assert CategoryAcc.objects.count() == 1
    assert category.name == "my_category_name"
    assert category.slug == "my_category_slug"
    assert category.__str__() == "my_category_name"


@pytest.mark.django_db
def test_category_acc_unique_slug():
    """Tests for duplication in the slug field in CategoryAcc"""
    with pytest.raises(IntegrityError):
        CategoryAcc.objects.create(name="my_category_1", slug="my_category")

        assert CategoryAcc.objects.create(name="my_category_2", slug="my_category")


@pytest.mark.django_db
def test_stockroom_acc_create():
    """Tests the creation of a record in the database for the Accessories model"""
    CategoryAcc.objects.create(name="my_category", slug="my_category")
    Manufacturer.objects.create(
        name="name_manufacturer",
    )
    Accessories.objects.create(
        name="my_accessories",
        manufacturer=Manufacturer.objects.get(name="name_manufacturer"),
        quantity=10,
    )
    StockAcc.objects.create(
        stock_model=Accessories.objects.get(name="my_accessories"),
        categories=CategoryAcc.objects.get(name="my_category"),
        dateAddToStock=datetime.date.today(),
        dateInstall=datetime.date.today(),
        rack=6,
        shelf=15,
    )
    stockroom = StockAcc.objects.get(stock_model__name="my_accessories")
    assert StockAcc.objects.count() == 1
    assert stockroom.stock_model.name == "my_accessories"
    assert stockroom.stock_model.manufacturer.name == "name_manufacturer"  # type: ignore[union-attr]
    assert stockroom.stock_model.quantity == 10
    assert stockroom.categories.name == "my_category"  # type: ignore[union-attr]
    assert stockroom.dateAddToStock == datetime.date.today()
    assert stockroom.dateInstall == datetime.date.today()
    assert stockroom.rack == 6
    assert stockroom.shelf == 15


@pytest.mark.django_db
def test_history_acc_create():
    """Tests the creation History of a record in the database for the Accessories model"""
    CategoryAcc.objects.create(name="my_category", slug="my_category")
    HistoryAcc.objects.create(
        stock_model="my_accessories",
        stock_model_id="name_manufacturer",
        device="my_device",
        deviceId="device_id",
        categories=CategoryAcc.objects.get(name="my_category"),
        quantity=1,
        dateInstall=datetime.date.today(),
        user="admin",
    )
    history = HistoryAcc.objects.get(stock_model="my_accessories")
    assert HistoryAcc.objects.count() == 1
    assert history.stock_model == "my_accessories"
    assert history.stock_model_id == "name_manufacturer"
    assert history.device == "my_device"
    assert history.deviceId == "device_id"
    assert history.categories.name == "my_category"  # type: ignore[union-attr]
    assert history.quantity == 1
    assert history.dateInstall == datetime.date.today()
    assert history.user == "admin"


# Devices
@pytest.mark.django_db
def test_category_dev_create():
    """Is testing the creation of a record in the database for the CategoryDev model of the Stockroom application"""
    CategoryDev.objects.create(name="my_category_name", slug="my_category_slug")
    category = CategoryDev.objects.get(name="my_category_name")
    assert CategoryDev.objects.count() == 1
    assert category.name == "my_category_name"
    assert category.slug == "my_category_slug"
    assert category.__str__() == "my_category_name"


@pytest.mark.django_db
def test_category_dev_unique_slug():
    """Tests for duplication in the slug field in CategoryDev"""
    with pytest.raises(IntegrityError):
        CategoryDev.objects.create(name="my_category_1", slug="my_category")

        assert CategoryDev.objects.create(name="my_category_2", slug="my_category")


@pytest.mark.django_db
def test_stockroom_dev_create():
    """Tests the creation of a record in the database for the Devices model"""
    CategoryDev.objects.create(name="my_category", slug="my_category")
    Manufacturer.objects.create(
        name="name_manufacturer",
    )
    Device.objects.create(
        name="my_device",
        manufacturer=Manufacturer.objects.get(name="name_manufacturer"),
        quantity=10,
    )
    StockDev.objects.create(
        stock_model=Device.objects.get(name="my_device"),
        categories=CategoryDev.objects.get(name="my_category"),
        dateAddToStock=datetime.date.today(),
        dateInstall=datetime.date.today(),
        rack=6,
        shelf=15,
    )
    stockroom = StockDev.objects.get(stock_model__name="my_device")
    assert StockDev.objects.count() == 1
    assert stockroom.stock_model.name == "my_device"
    assert stockroom.stock_model.manufacturer.name == "name_manufacturer"  # type: ignore[union-attr]
    assert stockroom.stock_model.quantity == 10
    assert stockroom.categories.name == "my_category"  # type: ignore[union-attr]
    assert stockroom.dateAddToStock == datetime.date.today()
    assert stockroom.dateInstall == datetime.date.today()
    assert stockroom.rack == 6
    assert stockroom.shelf == 15


@pytest.mark.django_db
def test_history_dev_create():
    """Tests the creation History of a record in the database for the Device model"""
    CategoryDev.objects.create(name="my_category", slug="my_category")
    HistoryDev.objects.create(
        stock_model="my_device",
        stock_model_id="name_manufacturer",
        categories=CategoryDev.objects.get(name="my_category"),
        quantity=1,
        dateInstall=datetime.date.today(),
        user="admin",
    )
    history = HistoryDev.objects.get(stock_model="my_device")
    assert HistoryDev.objects.count() == 1
    assert history.stock_model == "my_device"
    assert history.stock_model_id == "name_manufacturer"
    assert history.categories.name == "my_category"  # type: ignore[union-attr]
    assert history.quantity == 1
    assert history.dateInstall == datetime.date.today()
    assert history.user == "admin"
