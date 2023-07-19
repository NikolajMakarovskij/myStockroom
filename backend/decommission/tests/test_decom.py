import datetime
import pytest
from django.conf import settings
from django.contrib.auth.models import User
from decommission.models import Decommission, CategoryDec, HistoryDec, Disposal, CategoryDis, HistoryDis
from decommission.decom import Decom
from stockroom.models import StockDev, HistoryDev
from stockroom.stock import Stock


def create_session(client):
    """Creates a user and a session"""
    User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
    client.login(username='admin', password='admin')
    session = client.session
    session[settings.DECOM_SESSION_ID] = '6fk7mglhnq7f3avej9rmlshjyrokal3l'
    session.save()
    return client


def create_devices() -> dict:
    """Service function. Creates a category and device"""
    from device.models import DeviceCat, Device
    if Device.objects.filter(name='my_consumable').aexists():
        DeviceCat.objects.create(name='my_category', slug='my_category')
        Device.objects.create(name='my_consumable', categories=DeviceCat.objects.get(name='my_category'))
        get_device = Device.objects.get(name='my_consumable')
    else:
        get_device = Device.objects.get(name='my_consumable')
    return get_device


# Decommission
@pytest.mark.django_db
def test_decom_no_category():
    """Checks the operation of the add_category_decom method of the Decom class"""
    from device.models import Device
    Device.objects.create(name="my_consumable")
    device = Device.objects.get(name="my_consumable")
    device_id = device.id
    Decom.add_category_decom(device_id)

    assert CategoryDec.objects.count() == 0


@pytest.mark.django_db
def test_decom_add_category():
    """Checks the operation of the add_category_decom method of the Decom class"""
    device = create_devices()
    device_id = device.id
    Decom.add_category_decom(device_id)
    test_category = CategoryDec.objects.get(name='my_category')

    assert CategoryDec.objects.count() == 1
    assert test_category.name == 'my_category'
    assert test_category.slug == 'my_category'


@pytest.mark.django_db
def test_decom_create_history():
    """Checks the operation of the add_history method of the Stock class"""
    devices = create_devices()
    devices_id = devices.id
    username = 'admin'
    Decom.create_history_decom(devices_id, username)
    test_history = HistoryDec.objects.get(devices='my_consumable')

    assert HistoryDec.objects.count() == 1
    assert test_history.categories.name == 'my_category'
    assert test_history.categories.slug == 'my_category'
    assert test_history.devices == 'my_consumable'
    assert test_history.date == datetime.date.today()
    assert test_history.user == 'admin'


@pytest.mark.django_db
def test_decom_add_devices(client):
    """Checks the operation of the add_device method of the Decom class"""
    create_session(client)
    devices = create_devices()
    quantity = 1
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    Stock.add_device(self=Stock(client), device=devices, quantity=quantity, number_rack=number_rack,
                     number_shelf=number_shelf, username=username)
    Decom.add_device_decom(self=Decom(client), device=devices, username=username, status_choice="В список на списание")
    test_get_decom = Decommission.objects.get(devices__name='my_consumable')
    test_get_history_decom = HistoryDec.objects.get(devices='my_consumable')
    test_get_history_stock = HistoryDev.objects.get(status="В список на списание")

    assert StockDev.objects.count() == 0
    assert Decommission.objects.count() == 1
    assert CategoryDec.objects.count() == 1
    assert HistoryDec.objects.count() == 1
    assert HistoryDev.objects.count() == 2
    assert test_get_decom.categories.name == 'my_category'
    assert test_get_decom.categories.slug == 'my_category'
    assert test_get_decom.devices.name == 'my_consumable'
    assert test_get_decom.devices.score == 1
    assert test_get_decom.date == datetime.date.today()
    assert test_get_history_decom.devices == 'my_consumable'
    assert test_get_history_decom.categories.name == 'my_category'
    assert test_get_history_decom.categories.slug == 'my_category'
    assert test_get_history_decom.date == datetime.date.today()
    assert test_get_history_decom.user == 'admin'
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
    username = 'admin'
    Stock.add_device(self=Stock(client), device=devices, quantity=quantity, number_rack=number_rack,
                     number_shelf=number_shelf, username=username)
    Decom.add_device_decom(self=Decom(client), device=devices, username=username, status_choice="В список на списание")
    test_get_decom = Decommission.objects.get(devices__name='my_consumable')
    test_get_history_decom = HistoryDec.objects.get(devices='my_consumable')
    test_get_history_stock = HistoryDev.objects.get(status="В список на списание")

    assert StockDev.objects.count() == 0
    assert Decommission.objects.count() == 1
    assert HistoryDec.objects.count() == 1
    assert HistoryDev.objects.count() == 2
    assert test_get_decom.categories is None
    assert test_get_decom.devices.name == 'my_consumable'
    assert test_get_decom.devices.score == 1
    assert test_get_decom.date == datetime.date.today()
    assert test_get_history_decom.devices == 'my_consumable'
    assert test_get_history_decom.categories is None
    assert test_get_history_decom.date == datetime.date.today()
    assert test_get_history_decom.user == 'admin'
    assert test_get_history_stock.status == "В список на списание"


@pytest.mark.django_db
def test_stock_dev_remove_device(client):
    """Checks the operation of the remove_decom method of the Decom class"""
    create_session(client)
    devices = create_devices()
    quantity = 1
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    Stock.add_device(self=Stock(client), device=devices, quantity=quantity, number_rack=number_rack,
                     number_shelf=number_shelf, username=username)
    Decom.add_device_decom(self=Decom(client), device=devices, username=username, status_choice="В список на списание")
    Decom.remove_decom(self=Decom(client), device=devices, username=username, status_choice="Удаление")
    test_history = HistoryDev.objects.get(status='Удаление')

    assert StockDev.objects.count() == 0
    assert Decommission.objects.count() == 0
    assert HistoryDev.objects.count() == 3
    assert test_history.status == 'Удаление'


# Disposal
@pytest.mark.django_db
def test_disp_no_category():
    """Checks the operation of the add_category_disp method of the Decom class"""
    from device.models import Device
    Device.objects.create(name="my_consumable")
    device = Device.objects.get(name="my_consumable")
    device_id = device.id
    Decom.add_category_disp(device_id)

    assert CategoryDis.objects.count() == 0


@pytest.mark.django_db
def test_disp_add_category():
    """Checks the operation of the add_category_disp method of the Decom class"""
    device = create_devices()
    device_id = device.id
    Decom.add_category_disp(device_id)
    test_category = CategoryDis.objects.get(name='my_category')

    assert CategoryDis.objects.count() == 1
    assert test_category.name == 'my_category'
    assert test_category.slug == 'my_category'


@pytest.mark.django_db
def test_disp_create_history():
    """Checks the operation of the create_history_disp method of the Decom class"""
    devices = create_devices()
    devices_id = devices.id
    username = 'admin'
    Decom.create_history_disp(devices_id, username)
    test_history = HistoryDis.objects.get(devices='my_consumable')

    assert HistoryDis.objects.count() == 1
    assert test_history.categories.name == 'my_category'
    assert test_history.categories.slug == 'my_category'
    assert test_history.devices == 'my_consumable'
    assert test_history.date == datetime.date.today()
    assert test_history.user == 'admin'


@pytest.mark.django_db
def test_disp_add_devices(client):
    """Checks the operation of the add_device_disp method of the Decom class"""
    create_session(client)
    devices = create_devices()
    quantity = 1
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    Stock.add_device(self=Stock(client), device=devices, quantity=quantity, number_rack=number_rack,
                     number_shelf=number_shelf, username=username)
    Decom.add_device_decom(self=Decom(client), device=devices, username=username, status_choice="В список на списание")
    Decom.add_device_disp(self=Decom(client), device=devices, username=username, status_choice="В список на утилизацию")
    test_get_disp = Disposal.objects.get(devices__name='my_consumable')
    test_get_history_disp = HistoryDis.objects.get(devices='my_consumable')
    test_get_history_stock = HistoryDev.objects.get(status="В список на утилизацию")

    assert StockDev.objects.count() == 0
    assert Decommission.objects.count() == 0
    assert Disposal.objects.count() == 1
    assert CategoryDis.objects.count() == 1
    assert HistoryDis.objects.count() == 1
    assert HistoryDev.objects.count() == 3
    assert test_get_disp.categories.name == 'my_category'
    assert test_get_disp.categories.slug == 'my_category'
    assert test_get_disp.devices.name == 'my_consumable'
    assert test_get_disp.devices.score == 1
    assert test_get_disp.date == datetime.date.today()
    assert test_get_history_disp.devices == 'my_consumable'
    assert test_get_history_disp.categories.name == 'my_category'
    assert test_get_history_disp.categories.slug == 'my_category'
    assert test_get_history_disp.date == datetime.date.today()
    assert test_get_history_disp.user == 'admin'
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
    username = 'admin'
    Stock.add_device(self=Stock(client), device=devices, quantity=quantity, number_rack=number_rack,
                     number_shelf=number_shelf, username=username)
    Decom.add_device_decom(self=Decom(client), device=devices, username=username, status_choice="В список на списание")
    Decom.add_device_disp(self=Decom(client), device=devices, username=username, status_choice="В список на утилизацию")
    test_get_disp = Disposal.objects.get(devices__name='my_consumable')
    test_get_history_disp = HistoryDis.objects.get(devices='my_consumable')
    test_get_history_stock = HistoryDev.objects.get(status="В список на утилизацию")

    assert StockDev.objects.count() == 0
    assert Decommission.objects.count() == 0
    assert Disposal.objects.count() == 1
    assert HistoryDis.objects.count() == 1
    assert HistoryDev.objects.count() == 3
    assert test_get_disp.categories is None
    assert test_get_disp.devices.name == 'my_consumable'
    assert test_get_disp.devices.score == 1
    assert test_get_disp.date == datetime.date.today()
    assert test_get_history_disp.devices == 'my_consumable'
    assert test_get_history_disp.categories is None
    assert test_get_history_disp.date == datetime.date.today()
    assert test_get_history_disp.user == 'admin'
    assert test_get_history_stock.status == "В список на утилизацию"


@pytest.mark.django_db
def test_disp_remove_device(client):
    """Checks the operation of the remove_disp method of the Decom class"""
    create_session(client)
    devices = create_devices()
    quantity = 1
    number_rack = 3
    number_shelf = 13
    username = 'admin'
    Stock.add_device(self=Stock(client), device=devices, quantity=quantity, number_rack=number_rack,
                     number_shelf=number_shelf, username=username)
    Decom.add_device_decom(self=Decom(client), device=devices, username=username, status_choice="В список на списание")
    Decom.add_device_disp(self=Decom(client), device=devices, username=username, status_choice="В список на утилизацию")
    Decom.remove_disp(self=Decom(client), device=devices, username=username, status_choice="Удаление")
    test_history = HistoryDev.objects.get(status='Удаление')

    assert StockDev.objects.count() == 0
    assert Decommission.objects.count() == 0
    assert Disposal.objects.count() == 0
    assert HistoryDev.objects.count() == 4
    assert test_history.status == 'Удаление'