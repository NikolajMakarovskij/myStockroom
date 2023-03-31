import pytest, datetime
from django.conf import settings
from ..stock import Stock
from ..models import *
from django.contrib.auth.models import User


def create_session(client):
    """Создает пользователя и сессию"""
    User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
    client.login(username='admin', password='admin')
    session = client.session
    session[settings.STOCK_SESSION_ID] = '6fk7mglhnq7f3avej9rmlshjyrokal3l'
    session.save()
    response = client.get(('/')) 
    return client

def create_consumable():
    """Служебная функция. Создает категорию и расходник"""
    from consumables.models import Categories, Consumables
    if Consumables.objects.filter(name='my_consumable').aexists():
        Categories.objects.create(name='my_category', slug='my_category')
        Consumables.objects.create(name='my_consumable',categories = Categories.objects.get(name='my_category'))
        get_consumable = Consumables.objects.get(name='my_consumable')
    else:
        get_consumable = Consumables.objects.get(name='my_consumable')
    return get_consumable

def add_consumables_in_printers(consumable):
    """Служебная функция. Создает категорию и расходник"""
    from printer.models import Printer
    Printer.objects.bulk_create([
        Printer(name='printer 1', consumable = consumable),
        Printer(name='printer 2', consumable = consumable),
        Printer(name='printer 3', consumable = consumable),
    ])
    get_printers = Printer.objects.all()
    return get_printers

@pytest.mark.django_db
def test_stock_no_category():
    """Проверяет работу метода add_category класса Stock"""
    from consumables.models import Consumables
    Consumables.objects.create(name="my_consumable")
    consumable = Consumables.objects.get(name="my_consumable")
    consumable_id = consumable.id
    test_category = Stock.add_category(consumable_id)

    assert Stock_cat.objects.count() == 0


@pytest.mark.django_db
def test_stock_add_category():
    """Проверяет работу метода add_category класса Stock"""
    consumable = create_consumable()
    consumable_id = consumable.id
    test_category = Stock.add_category(consumable_id)

    assert Stock_cat.objects.count() == 1
    assert test_category.name == 'my_category'
    assert test_category.slug == 'my_category'

@pytest.mark.django_db
def test_stock_create_history():
    """Проверяет работу метода add_history класса Stock"""
    consumable = create_consumable()
    consumable_id = consumable.id
    quantity = 1
    username = 'admin'
    status_choise = 'Приход'
    test_history = Stock.create_history(consumable_id, quantity, username, status_choise)

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
    test_printer = Stock.get_device(consumable_id)
    assert test_printer == 'Нет'

@pytest.mark.django_db
def test_stock_get_device():
    """Проверяет работу метода get_device класса Stock"""
    from printer.models import Printer
    consumable = create_consumable()
    Printer.objects.create(name='printer', consumable = consumable)
    consumable_id = consumable.id
    test_printer = Stock.get_device(consumable_id)

    assert Printer.objects.count() == 1
    assert test_printer == 'printer'

@pytest.mark.django_db
def test_stock_get_device_ups():
    """Проверяет работу метода get_device класса Stock"""
    from ups.models import Ups
    consumable = create_consumable()
    Ups.objects.create(name='ups', accumulator = consumable)
    consumable_id = consumable.id
    test_printer = Stock.get_device(consumable_id)

    assert Ups.objects.count() == 1
    assert test_printer == 'ups'

@pytest.mark.django_db
def test_stock_get_device_cassette():
    """Проверяет работу метода get_device класса Stock"""
    from ups.models import Cassette
    consumable = create_consumable()
    Cassette.objects.create(name='cassette', accumulator = consumable)
    consumable_id = consumable.id
    test_printer = Stock.get_device(consumable_id)

    assert Cassette.objects.count() == 1
    assert test_printer == 'cassette'

@pytest.mark.django_db
def test_stock_get_device_cassette_and_ups():
    """Проверяет работу метода get_device класса Stock"""
    from ups.models import Cassette, Ups
    consumable = create_consumable()
    Cassette.objects.create(name='cassette', accumulator = consumable)
    Ups.objects.create(name='ups', accumulator = consumable)
    consumable_id = consumable.id
    test_printer = Stock.get_device(consumable_id)

    assert Cassette.objects.count() == 1
    assert Ups.objects.count() == 1
    assert test_printer == 'ups, cassette'

@pytest.mark.django_db
def test_stock_get_devices():
    """Проверяет работу метода get_device при нескольких связях класса Stock"""
    from printer.models import Printer
    consumable = create_consumable()
    add_consumables_in_printers(consumable)

    consumable_id = consumable.id
    test_printer = Stock.get_device(consumable_id)

    assert Printer.objects.count() == 3
    assert test_printer == 'printer 1, printer 2, printer 3'


@pytest.mark.django_db
def test_stock_add_consumable(client):
    """Проверяет работу метода add_consumable класса Stock"""
    create_session(client)
    consumable = create_consumable()
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    add_consumables_in_printers(consumable)
    Stock.add_consumable(self = Stock(client), consumable = consumable, quantity = quantity, number_rack = number_rack, number_shelf = number_shelf, username = username)
    test_get_stock = Stockroom.objects.get(consumables__name='my_consumable')
    test_get_history = History.objects.get(consumable='my_consumable')

    assert Stockroom.objects.count() == 1
    assert History.objects.count() == 1
    assert test_get_stock.categories.name == 'my_category'
    assert test_get_stock.categories.slug == 'my_category'
    assert test_get_stock.consumables.name == 'my_consumable'
    assert test_get_stock.device == 'printer 1, printer 2, printer 3'
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
    add_consumables_in_printers(consumable)
    Stock.add_consumable(self = Stock(client), consumable = consumable, quantity = quantity, number_rack = number_rack, number_shelf = number_shelf, username = username)
    test_get_stock = Stockroom.objects.get(consumables__name='my_consumable')
    test_get_history = History.objects.get(consumable='my_consumable')

    assert Stockroom.objects.count() == 1
    assert History.objects.count() == 1
    assert test_get_stock.categories == None
    assert test_get_stock.consumables.name == 'my_consumable'
    assert test_get_stock.device == 'printer 1, printer 2, printer 3'
    assert test_get_stock.consumables.score == 5
    assert test_get_stock.rack == 3
    assert test_get_stock.shelf == 13
    assert test_get_stock.dateAddToStock == datetime.date.today()
    assert test_get_history.consumable == 'my_consumable'
    assert test_get_history.categories == None
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
    add_consumables_in_printers(consumable)
    Stock.add_consumable(self = Stock(client), consumable = consumable, quantity = quantity, number_rack = number_rack, number_shelf = number_shelf, username = username)
    Stock.add_consumable(self = Stock(client), consumable = consumable, quantity = quantity, number_rack = 2, number_shelf = 2, username = username)
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
    add_consumables_in_printers(consumable)
    Stock.add_consumable(self = Stock(client), consumable = consumable, quantity = quantity, number_rack = number_rack, number_shelf = number_shelf, username = username)
    Stock.remove_consumable(self = Stock(client), consumable = consumable, quantity=0, username=username)
    test_history = History.objects.get(status='Удаление')

    assert Stockroom.objects.count() == 0
    assert History.objects.count() == 2
    assert test_history.status == 'Удаление'

@pytest.mark.django_db
def test_stock_device_add_consumable(client):
    """Проверяет работу метода add_consumable класса Stock"""
    create_session(client)
    consumable = create_consumable()
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    add_consumables_in_printers(consumable)
    Stock.add_consumable(self = Stock(client), consumable = consumable, quantity = quantity, number_rack = number_rack, number_shelf = number_shelf, username = username)
    Stock.device_add_consumable(self = Stock(client), consumable = consumable, quantity=1, username=username)
    test_get_stock = Stockroom.objects.get(consumables__name='my_consumable')
    test_history = History.objects.get(status='Расход')

    assert Stockroom.objects.count() == 1
    assert History.objects.count() == 2
    assert test_get_stock.consumables.score == -1
    assert test_get_stock.rack == 3
    assert test_get_stock.shelf == 13
    assert test_history.status == 'Расход'

