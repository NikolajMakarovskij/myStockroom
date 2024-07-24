import datetime

import pytest

from stockroom.models.devices import CategoryDev, HistoryDev, StockDev
from stockroom.stock.stock import DevStock
from stockroom.tests.stock_tests.stock_test import create_devices, create_session


@pytest.mark.django_db
def test_stock_dev_no_category():
    """Checks the operation of the add_category_dev method of the Stock class"""
    from device.models import Device

    Device.objects.create(name="my_consumable")
    device = Device.objects.get(name="my_consumable")
    device_id = device.id
    DevStock.add_category(device_id)

    assert CategoryDev.objects.count() == 0


@pytest.mark.django_db
def test_stock_dev_add_category():
    """Checks the operation of the add_category_dev method of the Stock class"""
    device = create_devices()
    device_id = device.id
    DevStock.add_category(device_id)
    test_category = CategoryDev.objects.get(name="my_category")

    assert CategoryDev.objects.count() == 1
    assert test_category.name == "my_category"
    assert test_category.slug == "my_category"


@pytest.mark.django_db
def test_stock_dev_create_history():
    """Checks the operation of the add_history method of the Stock class"""
    devices = create_devices()
    devices_id = devices.id
    quantity = 1
    username = "admin"
    status_choice = "Приход"
    note = "some history"
    DevStock.create_history_device(devices_id, quantity, username, status_choice, note)
    test_history = HistoryDev.objects.get(stock_model="my_consumable")

    assert HistoryDev.objects.count() == 1
    assert test_history.categories.name == "my_category"  # type: ignore[union-attr]
    assert test_history.categories.slug == "my_category"  # type: ignore[union-attr]
    assert test_history.stock_model == "my_consumable"
    assert test_history.quantity == 1
    assert test_history.dateInstall == datetime.date.today()
    assert test_history.user == "admin"
    assert test_history.status == "Приход"
    assert test_history.note == "some history"


@pytest.mark.django_db
def test_stock_add_devices(client):
    """Checks the operation of the add_consumable method of the Stock class"""
    create_session(client)
    devices = create_devices()
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = "admin"
    DevStock.add_to_stock_device(
        model_id=devices.id,
        quantity=quantity,
        number_rack=number_rack,
        number_shelf=number_shelf,
        username=username,
    )
    test_get_stock = StockDev.objects.get(stock_model__name="my_consumable")
    test_get_history = HistoryDev.objects.get(stock_model="my_consumable")

    assert StockDev.objects.count() == 1
    assert HistoryDev.objects.count() == 1
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
def test_stock_dev_add_device_not_category(client):
    """Checks the operation of the add_consumable method of the Stock class"""
    create_session(client)
    from device.models import Device

    Device.objects.create(name="my_consumable")
    devices = Device.objects.get(name="my_consumable")
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = "admin"
    DevStock.add_to_stock_device(
        model_id=devices.id,
        quantity=quantity,
        number_rack=number_rack,
        number_shelf=number_shelf,
        username=username,
    )
    test_get_stock = StockDev.objects.get(stock_model__name="my_consumable")
    test_get_history = HistoryDev.objects.get(stock_model="my_consumable")

    assert StockDev.objects.count() == 1
    assert HistoryDev.objects.count() == 1
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
def test_stock_dev_update_device(client):
    """Checks the operation of the add_consumable method of the Stock class"""
    create_session(client)
    devices = create_devices()
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = "admin"
    DevStock.add_to_stock_device(
        model_id=devices.id,
        quantity=quantity,
        number_rack=number_rack,
        number_shelf=number_shelf,
        username=username,
    )
    DevStock.add_to_stock_device(
        model_id=devices.id,
        quantity=quantity,
        number_rack=2,
        number_shelf=2,
        username=username,
    )
    test_get_stock = StockDev.objects.get(stock_model__name="my_consumable")

    assert StockDev.objects.count() == 1
    assert HistoryDev.objects.count() == 2
    assert test_get_stock.stock_model.quantity == 10
    assert test_get_stock.rack == 3
    assert test_get_stock.shelf == 13


@pytest.mark.django_db
def test_stock_dev_remove_device(client):
    """Checks the operation of the remove_accessories method of the Stock class"""
    create_session(client)
    devices = create_devices()
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = "admin"
    DevStock.add_to_stock_device(
        model_id=devices.id,
        quantity=quantity,
        number_rack=number_rack,
        number_shelf=number_shelf,
        username=username,
    )
    DevStock.remove_device_from_stock(
        model_id=devices.id, quantity=0, username=username
    )
    test_history = HistoryDev.objects.get(status="Удаление")

    assert StockDev.objects.count() == 0
    assert HistoryDev.objects.count() == 2
    assert test_history.status == "Удаление"


@pytest.mark.django_db
def test_stock_move_device(client):
    """Checks the operation of the remove_accessories method of the Stock class"""
    create_session(client)
    from workplace.models import Workplace

    Workplace.objects.create(name="pc-004-r")
    workplace = Workplace.objects.get(name="pc-004-r")
    devices = create_devices()
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = "admin"
    DevStock.add_to_stock_device(
        model_id=devices.id,
        quantity=quantity,
        number_rack=number_rack,
        number_shelf=number_shelf,
        username=username,
    )
    DevStock.move_device(
        model_id=devices.id, workplace_id=workplace.id, username=username
    )
    test_history = HistoryDev.objects.get(
        status="Перемещение на рабочее место pc-004-r"
    )
    test_stock = StockDev.objects.get(stock_model__name="my_consumable")

    assert StockDev.objects.count() == 1
    assert HistoryDev.objects.count() == 2
    assert test_stock.stock_model.workplace.name == "pc-004-r"  # type: ignore[union-attr]
    assert test_history.status == "Перемещение на рабочее место pc-004-r"
