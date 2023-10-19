import datetime

import pytest

from stockroom.models.consumables import History, Stockroom, StockCat
from stockroom.stock.stock import ConStock
from stockroom.tests.test_stock.test_stock import add_consumables_in_devices, create_consumable, create_session


@pytest.mark.django_db
def test_stock_no_category():
    """Checks the operation of the add_category method of the Stock class"""
    from consumables.models import Consumables
    Consumables.objects.create(name="my_consumable")
    consumable = Consumables.objects.get(name="my_consumable")
    consumable_id = consumable.id
    ConStock.add_category(consumable_id)

    assert StockCat.objects.count() == 0


@pytest.mark.django_db
def test_stock_add_category():
    """Checks the operation of the add_category method of the Stock class"""
    consumable = create_consumable()
    consumable_id = consumable.id
    ConStock.add_category(consumable_id)
    test_category = StockCat.objects.get(name='my_category')

    assert StockCat.objects.count() == 1
    assert test_category.name == 'my_category'
    assert test_category.slug == 'my_category'


@pytest.mark.django_db
def test_stock_create_history():
    """Checks the operation of the add_history method of the Stock class"""
    consumable = create_consumable()
    consumable_id = consumable.id
    device_id = None
    quantity = 1
    username = 'admin'
    status_choice = 'Приход'
    note = 'Примечание'
    ConStock.create_history(consumable_id, device_id, quantity, username, note, status_choice)
    test_history = History.objects.get(stock_model='my_consumable')

    assert History.objects.count() == 1
    assert test_history.categories.name == 'my_category'
    assert test_history.categories.slug == 'my_category'
    assert test_history.stock_model == 'my_consumable'
    assert test_history.quantity == 1
    assert test_history.dateInstall == datetime.date.today()
    assert test_history.user == 'admin'
    assert test_history.status == 'Приход'
    assert test_history.note == 'Примечание'


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
    ConStock.add_to_stock(model_id=consumable.id, quantity=quantity, number_rack=number_rack,
                               number_shelf=number_shelf, username=username)
    test_get_stock = Stockroom.objects.get(stock_model__name='my_consumable')
    test_get_history = History.objects.get(stock_model='my_consumable')

    assert Stockroom.objects.count() == 1
    assert History.objects.count() == 1
    assert test_get_stock.categories.name == 'my_category'
    assert test_get_stock.categories.slug == 'my_category'
    assert test_get_stock.stock_model.name == 'my_consumable'
    assert test_get_stock.stock_model.quantity == 5
    assert test_get_stock.rack == 3
    assert test_get_stock.shelf == 13
    assert test_get_stock.dateAddToStock == datetime.date.today()
    assert test_get_history.stock_model == 'my_consumable'
    assert test_get_history.categories.name == 'my_category'
    assert test_get_history.categories.slug == 'my_category'
    assert test_get_history.dateInstall == datetime.date.today()
    assert test_get_history.quantity == 5
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
    ConStock.add_to_stock(model_id=consumable.id, quantity=quantity, number_rack=number_rack,
                               number_shelf=number_shelf, username=username)
    test_get_stock = Stockroom.objects.get(stock_model__name='my_consumable')
    test_get_history = History.objects.get(stock_model='my_consumable')

    assert Stockroom.objects.count() == 1
    assert History.objects.count() == 1
    assert test_get_stock.categories is None
    assert test_get_stock.stock_model.name == 'my_consumable'
    assert test_get_stock.stock_model.quantity == 5
    assert test_get_stock.rack == 3
    assert test_get_stock.shelf == 13
    assert test_get_stock.dateAddToStock == datetime.date.today()
    assert test_get_history.stock_model == 'my_consumable'
    assert test_get_history.categories is None
    assert test_get_history.dateInstall == datetime.date.today()
    assert test_get_history.quantity == 5
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
    ConStock.add_to_stock(model_id=consumable.id, quantity=quantity, number_rack=number_rack,
                               number_shelf=number_shelf, username=username)
    ConStock.add_to_stock(model_id=consumable.id, quantity=quantity, number_rack=2,
                               number_shelf=2,
                               username=username)
    test_get_stock = Stockroom.objects.get(stock_model__name='my_consumable')

    assert Stockroom.objects.count() == 1
    assert History.objects.count() == 2
    assert test_get_stock.stock_model.quantity == 10
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
    ConStock.add_to_stock(model_id=consumable.id, quantity=quantity, number_rack=number_rack,
                               number_shelf=number_shelf, username=username)
    ConStock.remove_from_stock(model_id=consumable.id, quantity=0, username=username)
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
    Device.objects.create(name='device')
    device = Device.objects.get(name='device')
    device.consumable.set([consumable.id])
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    ConStock.add_to_stock(model_id=consumable.id, quantity=quantity, number_rack=number_rack,
                               number_shelf=number_shelf, username=username)
    ConStock.add_to_device(model_id=consumable.id, device=device.id, quantity=1, note='note',
                                username=username)
    test_get_stock = Stockroom.objects.get(stock_model__name='my_consumable')
    test_history = History.objects.get(status='Расход')

    assert Stockroom.objects.count() == 1
    assert History.objects.count() == 2
    assert Device.objects.count() == 1
    assert test_get_stock.stock_model.quantity == 4
    assert test_get_stock.rack == 3
    assert test_get_stock.shelf == 13
    assert test_history.status == 'Расход'
    assert test_history.note == 'note'
    #TODO check note in device
