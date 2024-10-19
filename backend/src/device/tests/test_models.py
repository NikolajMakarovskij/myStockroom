import pytest
from django.db.utils import IntegrityError

from consumables.models import Accessories
from counterparty.models import Manufacturer
from workplace.models import Workplace

from ..models import Consumables, Device, DeviceCat


@pytest.mark.django_db
def test_device_category_create():
    """Тестирует создание записи в базе данных для модели DeviceCat приложения Device"""
    DeviceCat.objects.create(name="my_category_name", slug="my_category_slug")
    category = DeviceCat.objects.get(name="my_category_name")
    assert DeviceCat.objects.count() == 1
    assert category.name == "my_category_name"
    assert category.slug == "my_category_slug"
    assert category.__str__() == "my_category_name"


@pytest.mark.django_db
def test_device_category_unique_slug():
    """Тестирует наличие дублирования в поле slug приложение Device"""
    with pytest.raises(IntegrityError):
        DeviceCat.objects.create(name="my_category_1", slug="my_category")

        assert DeviceCat.objects.create(name="my_category_2", slug="my_category")


@pytest.mark.django_db
def test_device_create():
    """Тестирует создание записи в базе данных для модели Device"""
    DeviceCat.objects.create(name="device_category")
    Manufacturer.objects.create(name="epson")
    Workplace.objects.create(name="device_workplace")
    Consumables.objects.create(name="cartridge")
    Accessories.objects.create(name="accessories")
    Device.objects.create(
        name="device_name",
        hostname="web.db",
        ip_address="10.10.10.10",
        login="db_user",
        pwd="123zxc",
        categories=DeviceCat.objects.get(name="device_category"),
        manufacturer=Manufacturer.objects.get(name="epson"),
        serial="some_serial",
        invent="some_number_124",
        description="some_description",
        workplace=Workplace.objects.get(name="device_workplace"),
        quantity=0,
        note="some_note",
    )

    device = Device.objects.get(name="device_name")
    device.consumable.set([Consumables.objects.get(name="cartridge").id])  # type: ignore[list-item]
    device.accessories.set([Accessories.objects.get(name="accessories").id])  # type: ignore[list-item]

    assert Device.objects.count() == 1
    assert device.name == "device_name"
    assert device.hostname == "web.db"
    assert device.ip_address == "10.10.10.10"
    assert device.login == "db_user"
    assert device.pwd == "123zxc"
    assert device.categories.name == "device_category"  # type: ignore[union-attr]
    assert device.manufacturer.name == "epson"  # type: ignore[union-attr]
    assert device.serial == "some_serial"
    assert device.invent == "some_number_124"
    assert device.description == "some_description"
    assert device.workplace.name == "device_workplace"  # type: ignore[union-attr]
    assert device.consumable.count() == 1
    assert device.accessories.count() == 1
    assert device.quantity == 0
    assert device.note == "some_note"
    assert device.__str__() == "device_name"
