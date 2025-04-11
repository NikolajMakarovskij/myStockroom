import datetime

import pytest

from decommission.models import CategoryDec, CategoryDis, Decommission, Disposal
from decommission.tasks import DecomTasks
from decommission.tests.decom_test import create_devices, create_session
from stockroom.models.devices import HistoryDev, StockDev
from stockroom.stock.stock import DevStock


# Decommission
@pytest.mark.django_db
def test_decom_add_devices(client):
    """Checks the operation of the add_device method of the Decom class"""
    create_session(client)
    devices = create_devices()
    quantity = 1
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
    DecomTasks.add_device_decom(
        device_id=devices.id, username=username, status_choice="В список на списание"
    )
    test_get_decom = Decommission.objects.get(stock_model__name="my_consumable")
    test_get_history_stock = HistoryDev.objects.get(status="В список на списание")

    assert StockDev.objects.count() == 0
    assert Decommission.objects.count() == 1
    assert CategoryDec.objects.count() == 1
    assert HistoryDev.objects.count() == 2
    assert test_get_decom.categories.name == "my_category"  # type: ignore[union-attr]
    assert test_get_decom.categories.slug == "my_category"  # type: ignore[union-attr]
    assert test_get_decom.stock_model.name == "my_consumable"
    assert test_get_decom.stock_model.quantity == 1
    assert test_get_decom.date == datetime.date.today()
    assert test_get_history_stock.status == "В список на списание"


@pytest.mark.django_db
def test_decom_add_device_not_category(client):
    """Checks the operation of the add_device_decom method of the Decom class"""
    create_session(client)
    from device.models import Device

    Device.objects.create(name="my_consumable")
    devices = Device.objects.get(name="my_consumable")
    quantity = 1
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
    DecomTasks.add_device_decom(
        device_id=devices.id, username=username, status_choice="В список на списание"
    )
    test_get_decom = Decommission.objects.get(stock_model__name="my_consumable")
    test_get_history_stock = HistoryDev.objects.get(status="В список на списание")

    assert StockDev.objects.count() == 0
    assert Decommission.objects.count() == 1
    assert HistoryDev.objects.count() == 2
    assert test_get_decom.categories is None
    assert test_get_decom.stock_model.name == "my_consumable"
    assert test_get_decom.stock_model.quantity == 1
    assert test_get_decom.date == datetime.date.today()
    assert test_get_history_stock.status == "В список на списание"


@pytest.mark.django_db
def test_stock_dev_remove_device(client):
    """Checks the operation of the remove_decom method of the Decom class"""
    create_session(client)
    devices = create_devices()
    quantity = 1
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
    DecomTasks.add_device_decom(
        device_id=devices.id, username=username, status_choice="В список на списание"
    )
    DecomTasks.remove_decom(
        device_id=devices.id, username=username, status_choice="Удаление"
    )
    test_history = HistoryDev.objects.get(status="Удаление")

    assert StockDev.objects.count() == 0
    assert Decommission.objects.count() == 0
    assert HistoryDev.objects.count() == 3
    assert test_history.status == "Удаление"


# Disposal
@pytest.mark.django_db
def test_disp_add_devices(client):
    """Checks the operation of the add_device_disp method of the Decom class"""
    create_session(client)
    devices = create_devices()
    quantity = 1
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
    DecomTasks.add_device_decom(
        device_id=devices.id, username=username, status_choice="В список на списание"
    )
    DecomTasks.add_device_disp(
        device_id=devices.id, username=username, status_choice="В список на утилизацию"
    )
    test_get_disp = Disposal.objects.get(stock_model__name="my_consumable")
    test_get_history_stock = HistoryDev.objects.get(status="В список на утилизацию")

    assert StockDev.objects.count() == 0
    assert Decommission.objects.count() == 0
    assert Disposal.objects.count() == 1
    assert CategoryDis.objects.count() == 1
    assert HistoryDev.objects.count() == 3
    assert test_get_disp.categories.name == "my_category"  # type: ignore[union-attr]
    assert test_get_disp.categories.slug == "my_category"  # type: ignore[union-attr]
    assert test_get_disp.stock_model.name == "my_consumable"
    assert test_get_disp.stock_model.quantity == 1
    assert test_get_disp.date == datetime.date.today()
    assert test_get_history_stock.status == "В список на утилизацию"


@pytest.mark.django_db
def test_disp_add_device_not_category(client):
    """Checks the operation of the add_device_disp method of the Decom class"""
    create_session(client)
    from device.models import Device

    Device.objects.create(name="my_consumable")
    devices = Device.objects.get(name="my_consumable")
    quantity = 1
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
    DecomTasks.add_device_decom(
        device_id=devices.id, username=username, status_choice="В список на списание"
    )
    DecomTasks.add_device_disp(
        device_id=devices.id, username=username, status_choice="В список на утилизацию"
    )
    test_get_disp = Disposal.objects.get(stock_model__name="my_consumable")
    test_get_history_stock = HistoryDev.objects.get(status="В список на утилизацию")

    assert StockDev.objects.count() == 0
    assert Decommission.objects.count() == 0
    assert Disposal.objects.count() == 1
    assert HistoryDev.objects.count() == 3
    assert test_get_disp.categories is None
    assert test_get_disp.stock_model.name == "my_consumable"
    assert test_get_disp.stock_model.quantity == 1
    assert test_get_disp.date == datetime.date.today()
    assert test_get_history_stock.status == "В список на утилизацию"


@pytest.mark.django_db
def test_disp_remove_device(client):
    """Checks the operation of the remove_disp method of the Decom class"""
    create_session(client)
    devices = create_devices()
    quantity = 1
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
    DecomTasks.add_device_decom(
        device_id=devices.id, username=username, status_choice="В список на списание"
    )
    DecomTasks.add_device_disp(
        device_id=devices.id, username=username, status_choice="В список на утилизацию"
    )
    DecomTasks.remove_disp(
        device_id=devices.id, username=username, status_choice="Удаление"
    )
    test_history = HistoryDev.objects.get(status="Удаление")

    assert StockDev.objects.count() == 0
    assert Decommission.objects.count() == 0
    assert Disposal.objects.count() == 0
    assert HistoryDev.objects.count() == 4
    assert test_history.status == "Удаление"
