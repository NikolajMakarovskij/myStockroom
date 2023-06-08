from unittest import mock
from django.core.files import File
import pytest
from ..forms import deviceForm ,Manufacturer, Workplace
from ..models import Device_cat
from consumables.models import Consumables, Categories as con_cat


@pytest.mark.django_db
def test_device_form_valid():
    """Тест на валидность формы приложения Device"""
    Device_cat.objects.create(name="device_category")
    Manufacturer.objects.create(name="epson")
    Workplace.objects.create(name="device_workplace")
    Consumables.objects.create(
            name="T7741",
            categories=con_cat.objects.create(
                name="Картриджы",
                slug="cartridges"
            )
        ) 
    form_data = {
        "name": "device_name", 
        "categories": Device_cat.objects.get(name="device_category"),
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
    form = deviceForm(data=form_data)
    assert form.is_valid() is True
