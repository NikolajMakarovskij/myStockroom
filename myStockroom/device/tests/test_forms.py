from unittest import mock
from django.core.files import File
import pytest
from workplace.models import Workplace
from ..forms import DeviceForm, Manufacturer
from ..models import DeviceCat
from consumables.models import Consumables, Categories as ConCat


@pytest.mark.django_db
def test_device_form_valid():
    """Тест на валидность формы приложения Device"""
    DeviceCat.objects.create(name="device_category")
    Manufacturer.objects.create(name="epson")
    Workplace.objects.create(name="device_workplace")
    Consumables.objects.create(
        name="T7741",
        categories=ConCat.objects.create(
            name="Картриджы",
            slug="cartridges"
        )
    )
    form_data = {
        "name": "device_name",
        "categories": DeviceCat.objects.get(name="device_category"),
        "manufacturer": Manufacturer.objects.get(name="epson"),
        "serial": "some_serial",
        "invent": "some_number_124",
        'serialImg': mock.MagicMock(spec=File, name='serial_Img'),
        'inventImg': mock.MagicMock(spec=File, name='invent_Img'),
        "description": "some_description",
        "workplace": Workplace.objects.get(name="device_workplace"),
        "consumable": Consumables.objects.get(name="T7741"),
        "note": "some_note"
    }
    form = DeviceForm(data=form_data)
    assert form.is_valid() is True
