import datetime
import pytest
from stockroom.models import History, Stockroom, StockAcc, HistoryAcc, HistoryDev, StockDev
from stockroom.tasks import StockTasks
from stockroom.tests.test_stock import (
    add_consumables_in_devices, create_consumable, create_session, create_devices, create_accessories
)


# Consumables
@pytest.mark.django_db
def test_stock_add_consumable(client):
    """Checks the operation of the add_consumable method of the Stock class"""
    create_session(client)
    consumable = create_consumable()
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    add_consumables_in_devices(consumable, accessories=None)
    StockTasks.add_consumable(consumable=consumable.id, quantity=quantity, number_rack=number_rack,
                              number_shelf=number_shelf, username=username)
    test_get_stock = Stockroom.objects.get(consumables__name='my_consumable')
    test_get_history = History.objects.get(consumable='my_consumable')

    assert Stockroom.objects.count() == 1
    assert History.objects.count() == 1
    assert test_get_stock.categories.name == 'my_category'
    assert test_get_stock.categories.slug == 'my_category'
    assert test_get_stock.consumables.name == 'my_consumable'
    assert test_get_stock.consumables.score == 5
    assert test_get_stock.rack == 3
    assert test_get_stock.shelf == 13
    assert test_get_stock.dateAddToStock == datetime.date.today()
    assert test_get_history.consumable == 'my_consumable'
    assert test_get_history.categories.name == 'my_category'
    assert test_get_history.categories.slug == 'my_category'
    assert test_get_history.dateInstall == datetime.date.today()
    assert test_get_history.score == 5
    assert test_get_history.user == 'admin'
    assert test_get_history.status == 'Приход'


@pytest.mark.django_db
def test_stock_add_consumable_not_category(client):
    """Checks the operation of the add_consumable method of the Stock class"""
    create_session(client)
    from consumables.models import Consumables
    Consumables.objects.create(name="my_consumable")
    consumable = Consumables.objects.get(name="my_consumable")
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    add_consumables_in_devices(consumable, accessories=None)
    StockTasks.add_consumable(consumable=consumable.id, quantity=quantity, number_rack=number_rack,
                              number_shelf=number_shelf, username=username)
    test_get_stock = Stockroom.objects.get(consumables__name='my_consumable')
    test_get_history = History.objects.get(consumable='my_consumable')

    assert Stockroom.objects.count() == 1
    assert History.objects.count() == 1
    assert test_get_stock.categories is None
    assert test_get_stock.consumables.name == 'my_consumable'
    assert test_get_stock.consumables.score == 5
    assert test_get_stock.rack == 3
    assert test_get_stock.shelf == 13
    assert test_get_stock.dateAddToStock == datetime.date.today()
    assert test_get_history.consumable == 'my_consumable'
    assert test_get_history.categories is None
    assert test_get_history.dateInstall == datetime.date.today()
    assert test_get_history.score == 5
    assert test_get_history.user == 'admin'
    assert test_get_history.status == 'Приход'


@pytest.mark.django_db
def test_stock_update_consumable(client):
    """Checks the operation of the add_consumable method of the Stock class"""
    create_session(client)
    consumable = create_consumable()
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    add_consumables_in_devices(consumable, accessories=None)
    StockTasks.add_consumable(consumable=consumable.id, quantity=quantity, number_rack=number_rack,
                              number_shelf=number_shelf, username=username)
    StockTasks.add_consumable(consumable=consumable.id, quantity=quantity, number_rack=2,
                              number_shelf=2,
                              username=username)
    test_get_stock = Stockroom.objects.get(consumables__name='my_consumable')

    assert Stockroom.objects.count() == 1
    assert History.objects.count() == 2
    assert test_get_stock.consumables.score == 10
    assert test_get_stock.rack == 3
    assert test_get_stock.shelf == 13


@pytest.mark.django_db
def test_stock_remove_consumable(client):
    """Checks the operation of the add_consumable method of the Stock class"""
    create_session(client)
    consumable = create_consumable()
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    add_consumables_in_devices(consumable, accessories=None)
    StockTasks.add_consumable(consumable=consumable.id, quantity=quantity, number_rack=number_rack,
                              number_shelf=number_shelf, username=username)
    StockTasks.remove_consumable(consumable=consumable.id, quantity=0, username=username)
    test_history = History.objects.get(status='Удаление')

    assert Stockroom.objects.count() == 0
    assert History.objects.count() == 2
    assert test_history.status == 'Удаление'


@pytest.mark.django_db
def test_stock_device_add_consumable(client):
    """Checks the operation of the add_consumable method of the Stock class"""
    from device.models import Device
    create_session(client)
    consumable = create_consumable()
    Device.objects.create(name='device', consumable=consumable)
    device = Device.objects.get(name='device').id
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    add_consumables_in_devices(consumable, accessories=None)
    StockTasks.add_consumable(consumable=consumable.id, quantity=quantity, number_rack=number_rack,
                              number_shelf=number_shelf, username=username)
    StockTasks.device_add_consumable(consumable=consumable.id, device=device, quantity=1,
                                     username=username)
    test_get_stock = Stockroom.objects.get(consumables__name='my_consumable')
    test_history = History.objects.get(status='Расход')

    assert Stockroom.objects.count() == 1
    assert History.objects.count() == 2
    assert test_get_stock.consumables.score == 4
    assert test_get_stock.rack == 3
    assert test_get_stock.shelf == 13
    assert test_history.status == 'Расход'


# Accessories
@pytest.mark.django_db
def test_stock_add_accessories(client):
    """Checks the operation of the add_consumable method of the Stock class"""
    create_session(client)
    accessories = create_accessories()
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    add_consumables_in_devices(consumable=None, accessories=accessories)
    StockTasks.add_accessories(accessories=accessories.id, quantity=quantity, number_rack=number_rack,
                               number_shelf=number_shelf, username=username)
    test_get_stock = StockAcc.objects.get(accessories__name='my_consumable')
    test_get_history = HistoryAcc.objects.get(accessories='my_consumable')

    assert StockAcc.objects.count() == 1
    assert HistoryAcc.objects.count() == 1
    assert test_get_stock.categories.name == 'my_category'
    assert test_get_stock.categories.slug == 'my_category'
    assert test_get_stock.accessories.name == 'my_consumable'
    assert test_get_stock.accessories.score == 5
    assert test_get_stock.rack == 3
    assert test_get_stock.shelf == 13
    assert test_get_stock.dateAddToStock == datetime.date.today()
    assert test_get_history.accessories == 'my_consumable'
    assert test_get_history.categories.name == 'my_category'
    assert test_get_history.categories.slug == 'my_category'
    assert test_get_history.dateInstall == datetime.date.today()
    assert test_get_history.score == 5
    assert test_get_history.user == 'admin'
    assert test_get_history.status == 'Приход'


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
    username = 'admin'
    add_consumables_in_devices(consumable=None, accessories=accessories)
    StockTasks.add_accessories(accessories=accessories.id, quantity=quantity, number_rack=number_rack,
                               number_shelf=number_shelf, username=username)
    test_get_stock = StockAcc.objects.get(accessories__name='my_consumable')
    test_get_history = HistoryAcc.objects.get(accessories='my_consumable')

    assert StockAcc.objects.count() == 1
    assert HistoryAcc.objects.count() == 1
    assert test_get_stock.categories is None
    assert test_get_stock.accessories.name == 'my_consumable'
    assert test_get_stock.accessories.score == 5
    assert test_get_stock.rack == 3
    assert test_get_stock.shelf == 13
    assert test_get_stock.dateAddToStock == datetime.date.today()
    assert test_get_history.accessories == 'my_consumable'
    assert test_get_history.categories is None
    assert test_get_history.dateInstall == datetime.date.today()
    assert test_get_history.score == 5
    assert test_get_history.user == 'admin'
    assert test_get_history.status == 'Приход'


@pytest.mark.django_db
def test_stock_acc_update_accessories(client):
    """Checks the operation of the add_consumable method of the Stock class"""
    create_session(client)
    accessories = create_accessories()
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    add_consumables_in_devices(consumable=None, accessories=accessories)
    StockTasks.add_accessories(accessories=accessories.id, quantity=quantity, number_rack=number_rack,
                               number_shelf=number_shelf, username=username)
    StockTasks.add_accessories(accessories=accessories.id, quantity=quantity, number_rack=2, number_shelf=2,
                               username=username)
    test_get_stock = StockAcc.objects.get(accessories__name='my_consumable')

    assert StockAcc.objects.count() == 1
    assert HistoryAcc.objects.count() == 2
    assert test_get_stock.accessories.score == 10
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
    username = 'admin'
    add_consumables_in_devices(consumable=None, accessories=accessories)
    StockTasks.add_accessories(accessories=accessories.id, quantity=quantity, number_rack=number_rack,
                               number_shelf=number_shelf, username=username)
    StockTasks.remove_accessories(accessories=accessories.id, quantity=0, username=username)
    test_history = HistoryAcc.objects.get(status='Удаление')

    assert StockAcc.objects.count() == 0
    assert HistoryAcc.objects.count() == 2
    assert test_history.status == 'Удаление'


@pytest.mark.django_db
def test_stock_device_acc_add_accessories(client):
    """Checks the operation of the device_add_accessories method of the Stock class"""
    from device.models import Device
    create_session(client)
    accessories = create_accessories()
    Device.objects.create(name='device', accessories=accessories)
    device = Device.objects.get(name='device').id
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    add_consumables_in_devices(consumable=None, accessories=accessories)
    StockTasks.add_accessories(accessories=accessories.id, quantity=quantity, number_rack=number_rack,
                               number_shelf=number_shelf, username=username)
    StockTasks.device_add_accessories(accessories=accessories.id, device=device,
                                      quantity=1, username=username)
    test_get_stock = StockAcc.objects.get(accessories__name='my_consumable')
    test_history = HistoryAcc.objects.get(status='Расход')

    assert StockAcc.objects.count() == 1
    assert HistoryAcc.objects.count() == 2
    assert test_get_stock.accessories.score == 4
    assert test_get_stock.rack == 3
    assert test_get_stock.shelf == 13
    assert test_history.status == 'Расход'


# Devices
@pytest.mark.django_db
def test_stock_add_devices(client):
    """Checks the operation of the add_consumable method of the Stock class"""
    create_session(client)
    devices = create_devices()
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    StockTasks.add_device(device_id=devices.id, quantity=quantity, number_rack=number_rack,
                          number_shelf=number_shelf, username=username)
    test_get_stock = StockDev.objects.get(devices__name='my_consumable')
    test_get_history = HistoryDev.objects.get(devices='my_consumable')

    assert StockDev.objects.count() == 1
    assert HistoryDev.objects.count() == 1
    assert test_get_stock.categories.name == 'my_category'
    assert test_get_stock.categories.slug == 'my_category'
    assert test_get_stock.devices.name == 'my_consumable'
    assert test_get_stock.devices.score == 5
    assert test_get_stock.rack == 3
    assert test_get_stock.shelf == 13
    assert test_get_stock.dateAddToStock == datetime.date.today()
    assert test_get_history.devices == 'my_consumable'
    assert test_get_history.categories.name == 'my_category'
    assert test_get_history.categories.slug == 'my_category'
    assert test_get_history.dateInstall == datetime.date.today()
    assert test_get_history.score == 5
    assert test_get_history.user == 'admin'
    assert test_get_history.status == 'Приход'


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
    username = 'admin'
    StockTasks.add_device(device_id=devices.id, quantity=quantity, number_rack=number_rack,
                          number_shelf=number_shelf, username=username)
    test_get_stock = StockDev.objects.get(devices__name='my_consumable')
    test_get_history = HistoryDev.objects.get(devices='my_consumable')

    assert StockDev.objects.count() == 1
    assert HistoryDev.objects.count() == 1
    assert test_get_stock.categories is None
    assert test_get_stock.devices.name == 'my_consumable'
    assert test_get_stock.devices.score == 5
    assert test_get_stock.rack == 3
    assert test_get_stock.shelf == 13
    assert test_get_stock.dateAddToStock == datetime.date.today()
    assert test_get_history.devices == 'my_consumable'
    assert test_get_history.categories is None
    assert test_get_history.dateInstall == datetime.date.today()
    assert test_get_history.score == 5
    assert test_get_history.user == 'admin'
    assert test_get_history.status == 'Приход'


@pytest.mark.django_db
def test_stock_dev_update_device(client):
    """Checks the operation of the add_consumable method of the Stock class"""
    create_session(client)
    devices = create_devices()
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    StockTasks.add_device(device_id=devices.id, quantity=quantity, number_rack=number_rack,
                          number_shelf=number_shelf, username=username)
    StockTasks.add_device(device_id=devices.id, quantity=quantity, number_rack=2, number_shelf=2,
                          username=username)
    test_get_stock = StockDev.objects.get(devices__name='my_consumable')

    assert StockDev.objects.count() == 1
    assert HistoryDev.objects.count() == 2
    assert test_get_stock.devices.score == 10
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
    username = 'admin'
    status_choice = "Удаление"
    StockTasks.add_device(device_id=devices.id, quantity=quantity, number_rack=number_rack,
                          number_shelf=number_shelf, username=username)
    StockTasks.remove_device(device_id=devices.id, quantity=0, username=username, status_choice=status_choice)
    test_history = HistoryDev.objects.get(status='Удаление')

    assert StockDev.objects.count() == 0
    assert HistoryDev.objects.count() == 2
    assert test_history.status == 'Удаление'


@pytest.mark.django_db
def test_stock_move_device(client):
    """Checks the operation of the remove_accessories method of the Stock class"""
    create_session(client)
    from workplace.models import Workplace
    workplace = Workplace.objects.create(name="pc-004-r")
    devices = create_devices()
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    StockTasks.add_device(device_id=devices.id, quantity=quantity, number_rack=number_rack,
                          number_shelf=number_shelf, username=username)
    StockTasks.move_device(device_id=devices.id, workplace=workplace, username=username)
    test_history = HistoryDev.objects.get(status='Перемещение на рабочее место pc-004-r')
    test_stock = StockDev.objects.get(devices__name='my_consumable')

    assert StockDev.objects.count() == 1
    assert HistoryDev.objects.count() == 2
    assert test_stock.devices.workplace.name == 'pc-004-r'
    assert test_history.status == 'Перемещение на рабочее место pc-004-r'
