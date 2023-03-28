import datetime, pytest
from urllib import request
from ..stock import Stock
from ..models import *



def create_consumable():
    """Служебная функция"""
    from consumables.models import Categories, Consumables
    Categories.objects.create(name='my_category', slug='my_category')
    Consumables.objects.create(name='my_consumable',categories = Categories.objects.get(name='my_category'))
    get_consumable = Consumables.objects.get(name='my_consumable')
    return get_consumable

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
def test_stock_get_devices():
    """Проверяет работу метода get_device при нескольких связях класса Stock"""
    from printer.models import Printer
    consumable = create_consumable()
    Printer.objects.bulk_create([
        Printer(name='printer 1', consumable = consumable),
        Printer(name='printer 2', consumable = consumable),
        Printer(name='printer 3', consumable = consumable),
    ])

    consumable_id = consumable.id
    test_printer = Stock.get_device(consumable_id)

    assert Printer.objects.count() == 3
    assert test_printer == 'printer 1, printer 2, printer 3'

@pytest.mark.django_db 
def test_stock_add_consumable():
    """Проверяет работу метода add_consumable класса Stock"""
    from printer.models import Printer
    consumable = create_consumable()
    quantity = 5
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    Printer.objects.bulk_create([
        Printer(name='printer 1', consumable = consumable),
        Printer(name='printer 2', consumable = consumable),
        Printer(name='printer 3', consumable = consumable),
    ])
    Stock.add_consumable(self = Stock(request), consumable = consumable, quantity = quantity, number_rack = number_rack, number_shelf = number_shelf, username = username)
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