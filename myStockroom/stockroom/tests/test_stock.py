import datetime
import pytest
from django.conf import settings
from django.contrib.auth.models import User

from ..models import StockCat, History, Stockroom
from ..stock import Stock


def create_session(client):
    """Создает пользователя и сессию"""
    User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
    client.login(username='admin', password='admin')
    session = client.session
    session[settings.STOCK_SESSION_ID] = '6fk7mglhnq7f3avej9rmlshjyrokal3l'
    session.save()
    return client


def create_consumable():
    """Служебная функция. Создает категорию и расходник"""
    from consumables.models import Categories, Consumables
    if Consumables.objects.filter(name='my_consumable').aexists():
        Categories.objects.create(name='my_category', slug='my_category')
        Consumables.objects.create(name='my_consumable', categories=Categories.objects.get(name='my_category'))
        get_consumable = Consumables.objects.get(name='my_consumable')
    else:
        get_consumable = Consumables.objects.get(name='my_consumable')
    return get_consumable


def add_consumables_in_devices(consumable):
    """Служебная функция. Создает категорию и расходник"""
    from device.models import Device
    Device.objects.bulk_create([
        Device(name='device 1', consumable=consumable),
        Device(name='device 2', consumable=consumable),
        Device(name='device 3', consumable=consumable),
    ])
    get_devices = Device.objects.all()
    return get_devices


@pytest.mark.django_db
def test_stock_no_category():
    """Проверяет работу метода add_category класса Stock"""
    from consumables.models import Consumables
    Consumables.objects.create(name="my_consumable")
    consumable = Consumables.objects.get(name="my_consumable")
    consumable_id = consumable.id
    Stock.add_category(consumable_id)

    assert StockCat.objects.count() == 0


@pytest.mark.django_db
def test_stock_add_category():
    """Проверяет работу метода add_category класса Stock"""
    consumable = create_consumable()
    consumable_id = consumable.id
    Stock.add_category(consumable_id)
    test_category = StockCat.objects.get(name='my_category')

    assert StockCat.objects.count() == 1
    assert test_category.name == 'my_category'
    assert test_category.slug == 'my_category'


@pytest.mark.django_db
def test_stock_create_history():
    """Проверяет работу метода add_history класса Stock"""
    consumable = create_consumable()
    consumable_id = consumable.id
    device_id = None
    quantity = 1
    username = 'admin'
    status_choise = 'Приход'
    Stock.create_history(consumable_id, device_id, quantity, username, status_choise)
    test_history = History.objects.get(consumable='my_consumable')

    assert History.objects.count() == 1
    assert test_history.categories.name == 'my_category'
    assert test_history.categories.slug == 'my_category'
    assert test_history.consumable == 'my_consumable'
    assert test_history.score == 1
    assert test_history.dateInstall == datetime.date.today()
    assert test_history.user == 'admin'
    assert test_history.status == 'Приход'


@pytest.mark.django_db
def test_stock_if_not_device():
    """Проверяет работу метода get_device класса Stock при отсутствии обратной связи"""
    consumable = create_consumable()
    consumable_id = consumable.id
    test_device = Stock.get_device(consumable_id)
    assert test_device == 'Нет'


@pytest.mark.django_db
def test_stock_get_device():
    """Проверяет работу метода get_device класса Stock"""
    from device.models import Device
    consumable = create_consumable()
    Device.objects.create(name='device', consumable=consumable)
    consumable_id = consumable.id
    test_device = Stock.get_device(consumable_id)

    assert Device.objects.count() == 1
    assert test_device == 'device'


@pytest.mark.django_db
def test_stock_get_devices():
    """Проверяет работу метода get_device при нескольких связях класса Stock"""
    from device.models import Device
    consumable = create_consumable()
    add_consumables_in_devices(consumable)

    consumable_id = consumable.id
    test_printer = Stock.get_device(consumable_id)

    assert Device.objects.count() == 3
    assert test_printer == 'device 1, device 2, device 3'


@pytest.mark.django_db
def test_stock_add_consumable(client):
    """Проверяет работу метода add_consumable класса Stock"""
    create_session(client)
    consumable = create_consumable()
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    add_consumables_in_devices(consumable)
    Stock.add_consumable(self=Stock(client), consumable=consumable, quantity=quantity, number_rack=number_rack,
                         number_shelf=number_shelf, username=username)
    test_get_stock = Stockroom.objects.get(consumables__name='my_consumable')
    test_get_history = History.objects.get(consumable='my_consumable')

    assert Stockroom.objects.count() == 1
    assert History.objects.count() == 1
    assert test_get_stock.categories.name == 'my_category'
    assert test_get_stock.categories.slug == 'my_category'
    assert test_get_stock.consumables.name == 'my_consumable'
    assert test_get_stock.device == 'device 1, device 2, device 3'
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
    """Проверяет работу метода add_consumable класса Stock"""
    create_session(client)
    from consumables.models import Consumables
    Consumables.objects.create(name="my_consumable")
    consumable = Consumables.objects.get(name="my_consumable")
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    add_consumables_in_devices(consumable)
    Stock.add_consumable(self=Stock(client), consumable=consumable, quantity=quantity, number_rack=number_rack,
                         number_shelf=number_shelf, username=username)
    test_get_stock = Stockroom.objects.get(consumables__name='my_consumable')
    test_get_history = History.objects.get(consumable='my_consumable')

    assert Stockroom.objects.count() == 1
    assert History.objects.count() == 1
    assert test_get_stock.categories is None
    assert test_get_stock.consumables.name == 'my_consumable'
    assert test_get_stock.device == 'device 1, device 2, device 3'
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
    """Проверяет работу метода add_consumable класса Stock"""
    create_session(client)
    consumable = create_consumable()
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    add_consumables_in_devices(consumable)
    Stock.add_consumable(self=Stock(client), consumable=consumable, quantity=quantity, number_rack=number_rack,
                         number_shelf=number_shelf, username=username)
    Stock.add_consumable(self=Stock(client), consumable=consumable, quantity=quantity, number_rack=2, number_shelf=2,
                         username=username)
    test_get_stock = Stockroom.objects.get(consumables__name='my_consumable')

    assert Stockroom.objects.count() == 1
    assert History.objects.count() == 2
    assert test_get_stock.consumables.score == 5
    assert test_get_stock.rack == 3
    assert test_get_stock.shelf == 13


@pytest.mark.django_db
def test_stock_remove_consumable(client):
    """Проверяет работу метода add_consumable класса Stock"""
    create_session(client)
    consumable = create_consumable()
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    add_consumables_in_devices(consumable)
    Stock.add_consumable(self=Stock(client), consumable=consumable, quantity=quantity, number_rack=number_rack,
                         number_shelf=number_shelf, username=username)
    Stock.remove_consumable(self=Stock(client), consumable=consumable, quantity=0, username=username)
    test_history = History.objects.get(status='Удаление')

    assert Stockroom.objects.count() == 0
    assert History.objects.count() == 2
    assert test_history.status == 'Удаление'


@pytest.mark.django_db
def test_stock_device_add_consumable(client):
    """Проверяет работу метода add_consumable класса Stock"""
    from device.models import Device
    create_session(client)
    consumable = create_consumable()
    Device.objects.create(name='device', consumable=consumable)
    device = Device.objects.get(name='device').id
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    add_consumables_in_devices(consumable)
    Stock.add_consumable(self=Stock(client), consumable=consumable, quantity=quantity, number_rack=number_rack,
                         number_shelf=number_shelf, username=username)
    Stock.device_add_consumable(self=Stock(client), consumable=consumable, device=device, quantity=1, username=username)
    test_get_stock = Stockroom.objects.get(consumables__name='my_consumable')
    test_history = History.objects.get(status='Расход')

    assert Stockroom.objects.count() == 1
    assert History.objects.count() == 2
    assert test_get_stock.consumables.score == -1
    assert test_get_stock.rack == 3
    assert test_get_stock.shelf == 13
    assert test_history.status == 'Расход'
