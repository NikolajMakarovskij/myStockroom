import datetime
import pytest
from django.conf import settings
from django.contrib.auth.models import User
from ..models import StockCat, History, CategoryAcc, HistoryAcc, CategoryDev, HistoryDev
from ..stock import Stock


def create_session(client):
    """Creates a user and a session"""
    User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
    client.login(username='admin', password='admin')
    session = client.session
    session[settings.STOCK_SESSION_ID] = '6fk7mglhnq7f3avej9rmlshjyrokal3l'
    session.save()
    return client


def create_consumable() -> dict:
    """Service function. Creates a category and a consumable"""
    from consumables.models import Categories, Consumables
    if Consumables.objects.filter(name='my_consumable').aexists():
        Categories.objects.create(name='my_category', slug='my_category')
        Consumables.objects.create(name='my_consumable', categories=Categories.objects.get(name='my_category'))
        get_consumable = Consumables.objects.get(name='my_consumable')
    else:
        get_consumable = Consumables.objects.get(name='my_consumable')
    return get_consumable


def create_accessories() -> dict:
    """Service function. Creates a category and accessories"""
    from consumables.models import AccCat, Accessories
    if Accessories.objects.filter(name='my_consumable').aexists():
        AccCat.objects.create(name='my_category', slug='my_category')
        Accessories.objects.create(name='my_consumable', categories=AccCat.objects.get(name='my_category'))
        get_accessories = Accessories.objects.get(name='my_consumable')
    else:
        get_accessories = Accessories.objects.get(name='my_consumable')
    return get_accessories


def create_devices() -> dict:
    """Service function. Creates a category and accessories"""
    from device.models import DeviceCat, Device
    if Device.objects.filter(name='my_consumable').aexists():
        DeviceCat.objects.create(name='my_category', slug='my_category')
        Device.objects.create(name='my_consumable', categories=DeviceCat.objects.get(name='my_category'))
        get_device = Device.objects.get(name='my_consumable')
    else:
        get_device = Device.objects.get(name='my_consumable')
    return get_device


def add_consumables_in_devices(consumable: dict, accessories: dict) -> dict:
    """Service function. Creates a category, consumable and accessories. Return devices"""
    from device.models import Device
    Device.objects.bulk_create([
        Device(name='device 1', consumable=consumable, accessories=accessories),
        Device(name='device 2', consumable=consumable, accessories=accessories),
        Device(name='device 3', consumable=consumable, accessories=accessories),
    ])
    get_devices = Device.objects.all()
    return get_devices


# Consumables
@pytest.mark.django_db
def test_stock_no_category():
    """Checks the operation of the add_category method of the Stock class"""
    from consumables.models import Consumables
    Consumables.objects.create(name="my_consumable")
    consumable = Consumables.objects.get(name="my_consumable")
    consumable_id = consumable.id
    Stock.add_category(consumable_id)

    assert StockCat.objects.count() == 0


@pytest.mark.django_db
def test_stock_add_category():
    """Checks the operation of the add_category method of the Stock class"""
    consumable = create_consumable()
    consumable_id = consumable.id
    Stock.add_category(consumable_id)
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
    Stock.create_history(consumable_id, device_id, quantity, username, status_choice)
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
    """Checks the operation of the get_device method of the Stock class in the absence of feedback"""
    consumable = create_consumable()
    consumable_id = consumable.id
    test_device = Stock.get_device(consumable_id)
    assert test_device == 'Нет'


@pytest.mark.django_db
def test_stock_get_device():
    """Checks the operation of the get_device method of the Stock class"""
    from device.models import Device
    consumable = create_consumable()
    Device.objects.create(name='device', consumable=consumable)
    consumable_id = consumable.id
    test_device = Stock.get_device(consumable_id)

    assert Device.objects.count() == 1
    assert test_device == 'device'


@pytest.mark.django_db
def test_stock_get_devices():
    """Checks the operation of the get_device method with multiple connections of the Stock class"""
    from device.models import Device
    consumable = create_consumable()
    add_consumables_in_devices(consumable, accessories=None)

    consumable_id = consumable.id
    test_printer = Stock.get_device(consumable_id)

    assert Device.objects.count() == 3
    assert test_printer == 'device 1, device 2, device 3'


# Accessories
@pytest.mark.django_db
def test_stock_acc_no_category():
    """Checks the operation of the add_category_acc method of the Stock class"""
    from consumables.models import Accessories
    Accessories.objects.create(name="my_consumable")
    accessories = Accessories.objects.get(name="my_consumable")
    accessories_id = accessories.id
    Stock.add_category_acc(accessories_id)

    assert CategoryAcc.objects.count() == 0


@pytest.mark.django_db
def test_stock_acc_add_category():
    """Checks the operation of the add_category method of the Stock class"""
    accessories = create_accessories()
    accessories_id = accessories.id
    Stock.add_category_acc(accessories_id)
    test_category = CategoryAcc.objects.get(name='my_category')

    assert CategoryAcc.objects.count() == 1
    assert test_category.name == 'my_category'
    assert test_category.slug == 'my_category'


@pytest.mark.django_db
def test_stock_acc_create_history():
    """Checks the operation of the add_history method of the Stock class"""
    accessories = create_accessories()
    accessories_id = accessories.id
    device_id = None
    quantity = 1
    username = 'admin'
    status_choice = 'Приход'
    Stock.create_history_acc(accessories_id, device_id, quantity, username, status_choice)
    test_history = HistoryAcc.objects.get(accessories='my_consumable')

    assert HistoryAcc.objects.count() == 1
    assert test_history.categories.name == 'my_category'
    assert test_history.categories.slug == 'my_category'
    assert test_history.accessories == 'my_consumable'
    assert test_history.score == 1
    assert test_history.dateInstall == datetime.date.today()
    assert test_history.user == 'admin'
    assert test_history.status == 'Приход'


@pytest.mark.django_db
def test_stock_acc_if_not_device():
    """Checks the operation of the get_device method of the Stock class in the absence of feedback"""
    accessories = create_accessories()
    accessories_id = accessories.id
    test_device = Stock.get_device_acc(accessories_id)
    assert test_device == 'Нет'


@pytest.mark.django_db
def test_stock_acc_get_device():
    """Checks the operation of the get_device method of the Stock class"""
    from device.models import Device
    accessories = create_accessories()
    Device.objects.create(name='device', accessories=accessories)
    accessories_id = accessories.id
    test_device = Stock.get_device_acc(accessories_id)

    assert Device.objects.count() == 1
    assert test_device == 'device'


@pytest.mark.django_db
def test_stock_acc_get_devices():
    """Checks the operation of the get_device method with multiple connections of the Stock class"""
    from device.models import Device
    accessories = create_accessories()
    add_consumables_in_devices(consumable=None, accessories=accessories)

    accessories_id = accessories.id
    test_printer = Stock.get_device_acc(accessories_id)

    assert Device.objects.count() == 3
    assert test_printer == 'device 1, device 2, device 3'


# Devices
@pytest.mark.django_db
def test_stock_dev_no_category():
    """Checks the operation of the add_category_dev method of the Stock class"""
    from device.models import Device
    Device.objects.create(name="my_consumable")
    device = Device.objects.get(name="my_consumable")
    device_id = device.id
    Stock.add_category_dev(device_id)

    assert CategoryDev.objects.count() == 0


@pytest.mark.django_db
def test_stock_dev_add_category():
    """Checks the operation of the add_category_dev method of the Stock class"""
    device = create_devices()
    device_id = device.id
    Stock.add_category_dev(device_id)
    test_category = CategoryDev.objects.get(name='my_category')

    assert CategoryDev.objects.count() == 1
    assert test_category.name == 'my_category'
    assert test_category.slug == 'my_category'


@pytest.mark.django_db
def test_stock_dev_create_history():
    """Checks the operation of the add_history method of the Stock class"""
    devices = create_devices()
    devices_id = devices.id
    quantity = 1
    username = 'admin'
    status_choice = 'Приход'
    Stock.create_history_dev(devices_id, quantity, username, status_choice)
    test_history = HistoryDev.objects.get(devices='my_consumable')

    assert HistoryDev.objects.count() == 1
    assert test_history.categories.name == 'my_category'
    assert test_history.categories.slug == 'my_category'
    assert test_history.devices == 'my_consumable'
    assert test_history.score == 1
    assert test_history.dateInstall == datetime.date.today()
    assert test_history.user == 'admin'
    assert test_history.status == 'Приход'
