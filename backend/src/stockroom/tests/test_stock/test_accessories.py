import datetime

import pytest

from stockroom.models.accessories import CategoryAcc, HistoryAcc, StockAcc
from stockroom.stock.stock import AccStock
from stockroom.tests.test_stock.test_stock import (
    add_consumables_in_devices,
    create_accessories,
    create_session,
)


@pytest.mark.django_db
def test_stock_acc_no_category():
    """Checks the operation of the add_category_acc method of the Stock class"""
    from consumables.models import Accessories

    Accessories.objects.create(name="my_consumable")
    accessories = Accessories.objects.get(name="my_consumable")
    accessories_id = accessories.id
    AccStock.add_category(accessories_id)

    assert CategoryAcc.objects.count() == 0


@pytest.mark.django_db
def test_stock_acc_add_category():
    """Checks the operation of the add_category method of the Stock class"""
    accessories = create_accessories()
    accessories_id = accessories.id
    AccStock.add_category(accessories_id)
    test_category = CategoryAcc.objects.get(name="my_category")

    assert CategoryAcc.objects.count() == 1
    assert test_category.name == "my_category"
    assert test_category.slug == "my_category"


@pytest.mark.django_db
def test_stock_acc_create_history():
    """Checks the operation of the add_history method of the Stock class"""
    accessories = create_accessories()
    accessories_id = accessories.id
    device_id = None
    quantity = 1
    username = "admin"
    status_choice = "Приход"
    note = "Примечание"
    AccStock.create_history(
        accessories_id, device_id, quantity, username, note, status_choice
    )
    test_history = HistoryAcc.objects.get(stock_model="my_consumable")

    assert HistoryAcc.objects.count() == 1
    assert test_history.categories.name == "my_category"  # type: ignore[union-attr]
    assert test_history.categories.slug == "my_category"  # type: ignore[union-attr]
    assert test_history.stock_model == "my_consumable"
    assert test_history.quantity == 1
    assert test_history.dateInstall == datetime.date.today()
    assert test_history.user == "admin"
    assert test_history.status == "Приход"
    assert test_history.note == "Примечание"


@pytest.mark.django_db
def test_stock_add_accessories(client):
    """Checks the operation of the add_consumable method of the Stock class"""
    create_session(client)
    accessories = create_accessories()
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = "admin"
    add_consumables_in_devices(consumable=None, accessories=accessories)
    AccStock.add_to_stock(
        model_id=accessories.id,
        quantity=quantity,
        number_rack=number_rack,
        number_shelf=number_shelf,
        username=username,
    )
    test_get_stock = StockAcc.objects.get(stock_model__name="my_consumable")
    test_get_history = HistoryAcc.objects.get(stock_model="my_consumable")

    assert StockAcc.objects.count() == 1
    assert HistoryAcc.objects.count() == 1
    assert test_get_stock.categories.name == "my_category"  # type: ignore[union-attr]
    assert test_get_stock.categories.slug == "my_category"  # type: ignore[union-attr]
    assert test_get_stock.stock_model.name == "my_consumable"
    assert test_get_stock.stock_model.quantity == 5
    assert test_get_stock.rack == 3
    assert test_get_stock.shelf == 13
    assert test_get_stock.dateAddToStock == datetime.date.today()
    assert test_get_history.stock_model == "my_consumable"
    assert test_get_history.categories.name == "my_category"  # type: ignore[union-attr]
    assert test_get_history.categories.slug == "my_category"  # type: ignore[union-attr]
    assert test_get_history.dateInstall == datetime.date.today()
    assert test_get_history.quantity == 5
    assert test_get_history.user == "admin"
    assert test_get_history.status == "Приход"


@pytest.mark.django_db
def test_stock_acc_add_accessories_not_category(client):
    """Checks the operation of the add_consumable method of the Stock class"""
    create_session(client)
    from consumables.models import Accessories

    Accessories.objects.create(name="my_consumable")
    accessories = Accessories.objects.get(name="my_consumable")
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = "admin"
    add_consumables_in_devices(consumable=None, accessories=accessories)
    AccStock.add_to_stock(
        model_id=accessories.id,
        quantity=quantity,
        number_rack=number_rack,
        number_shelf=number_shelf,
        username=username,
    )
    test_get_stock = StockAcc.objects.get(stock_model__name="my_consumable")
    test_get_history = HistoryAcc.objects.get(stock_model="my_consumable")

    assert StockAcc.objects.count() == 1
    assert HistoryAcc.objects.count() == 1
    assert test_get_stock.categories is None
    assert test_get_stock.stock_model.name == "my_consumable"
    assert test_get_stock.stock_model.quantity == 5
    assert test_get_stock.rack == 3
    assert test_get_stock.shelf == 13
    assert test_get_stock.dateAddToStock == datetime.date.today()
    assert test_get_history.stock_model == "my_consumable"
    assert test_get_history.categories is None
    assert test_get_history.dateInstall == datetime.date.today()
    assert test_get_history.quantity == 5
    assert test_get_history.user == "admin"
    assert test_get_history.status == "Приход"


@pytest.mark.django_db
def test_stock_acc_update_accessories(client):
    """Checks the operation of the add_consumable method of the Stock class"""
    create_session(client)
    accessories = create_accessories()
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = "admin"
    add_consumables_in_devices(consumable=None, accessories=accessories)
    AccStock.add_to_stock(
        model_id=accessories.id,
        quantity=quantity,
        number_rack=number_rack,
        number_shelf=number_shelf,
        username=username,
    )
    AccStock.add_to_stock(
        model_id=accessories.id,
        quantity=quantity,
        number_rack=2,
        number_shelf=2,
        username=username,
    )
    test_get_stock = StockAcc.objects.get(stock_model__name="my_consumable")

    assert StockAcc.objects.count() == 1
    assert HistoryAcc.objects.count() == 2
    assert test_get_stock.stock_model.quantity == 10
    assert test_get_stock.rack == 3
    assert test_get_stock.shelf == 13


@pytest.mark.django_db
def test_stock_acc_remove_accessories(client):
    """Checks the operation of the remove_accessories method of the Stock class"""
    create_session(client)
    accessories = create_accessories()
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = "admin"
    add_consumables_in_devices(consumable=None, accessories=accessories)
    AccStock.add_to_stock(
        model_id=accessories.id,
        quantity=quantity,
        number_rack=number_rack,
        number_shelf=number_shelf,
        username=username,
    )
    AccStock.remove_from_stock(model_id=accessories.id, quantity=0, username=username)
    test_history = HistoryAcc.objects.get(status="Удаление")

    assert StockAcc.objects.count() == 0
    assert HistoryAcc.objects.count() == 2
    assert test_history.status == "Удаление"


@pytest.mark.django_db
def test_stock_device_acc_add_accessories(client):
    """Checks the operation of the device_add_accessories method of the Stock class"""
    from device.models import Device

    create_session(client)
    accessories = create_accessories()
    Device.objects.get_or_create(name="device")
    device = Device.objects.get(name="device")
    device.accessories.set([accessories.id])  # type: ignore[list-item]
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = "admin"
    AccStock.add_to_stock(
        model_id=accessories.id,
        quantity=quantity,
        number_rack=number_rack,
        number_shelf=number_shelf,
        username=username,
    )
    AccStock.add_to_device(
        model_id=accessories.id,
        device=device.id,
        quantity=1,
        note="note",
        username=username,
    )
    test_get_stock = StockAcc.objects.get(stock_model__name="my_consumable")
    test_history = HistoryAcc.objects.get(status="Расход")

    assert StockAcc.objects.count() == 1
    assert HistoryAcc.objects.count() == 2
    assert Device.objects.count() == 1
    assert test_get_stock.stock_model.quantity == 4
    # assert device.note == f"{datetime.date.today()} note"
    assert test_get_stock.rack == 3
    assert test_get_stock.shelf == 13
    assert test_history.status == "Расход"
    assert test_history.note == "note"
    # TODO check note in device
