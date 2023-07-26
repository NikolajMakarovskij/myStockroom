from django.db.utils import IntegrityError
from django.urls import reverse
import pytest

from consumables.models import Accessories
from ..models import Device, DeviceCat, Consumables
from workplace.models import Workplace
from counterparty.models import Manufacturer


@pytest.mark.django_db
def test_device_category_create():
    """Тестирует создание записи в базе данных для модели DeviceCat приложения Device"""
    DeviceCat.objects.create(
        name="my_category_name",
        slug="my_category_slug"
    )
    category = DeviceCat.objects.get(name="my_category_name")
    assert DeviceCat.objects.count() == 1
    assert category.name == "my_category_name"
    assert category.slug == "my_category_slug"
    assert category.__str__() == "my_category_name"
    assert category.get_absolute_url() == reverse('device:category', kwargs={'category_slug': category.slug})


@pytest.mark.django_db
def test_device_category_unique_slug():
    """Тестирует наличие дублирования в поле slug приложение Device"""
    with pytest.raises(IntegrityError):
        DeviceCat.objects.create(
            name="my_category_1",
            slug="my_category"
        )

        assert (DeviceCat.objects.create(
            name="my_category_2",
            slug="my_category"
        )
        )


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
        categories=DeviceCat.objects.get(name="device_category"),
        manufacturer=Manufacturer.objects.get(name="epson"),
        serial="some_serial",
        invent="some_number_124",
        description="some_description",
        workplace=Workplace.objects.get(name="device_workplace"),
        consumable=Consumables.objects.get(name="cartridge"),
        accessories=Accessories.objects.get(name="accessories"),
        quantity=0,
        note="some_note"
    )
    device = Device.objects.get(name="device_name")
    assert Device.objects.count() == 1
    assert device.name == "device_name"
    assert device.categories.name == "device_category"
    assert device.manufacturer.name == "epson"
    assert device.serial == "some_serial"
    assert device.invent == "some_number_124"
    assert device.description == "some_description"
    assert device.workplace.name == "device_workplace"
    assert device.consumable.name == "cartridge"
    assert device.accessories.name == "accessories"
    assert device.quantity == 0
    assert device.note == "some_note"
    assert device.__str__() == "device_name"
    assert device.get_absolute_url() == reverse('device:device-detail', kwargs={'pk': device.pk})
