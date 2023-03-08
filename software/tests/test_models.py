from django.db.utils import IntegrityError
import pytest  
from myStockroom.wsgi import *
from ..models import Software, Os
from counterparty.models import Manufacturer


@pytest.mark.django_db  
def test_software_create():
    """Тестирует создание записи в базе данных для модели Software"""
    Manufacturer.objects.create(name="soft_manufacturer")
    soft = Software.objects.create(
        name = "my_software_name",
        manufacturer = Manufacturer.objects.get(name="soft_manufacturer"),
        version = "12.rwg5",
        bitDepth = "x64",
        licenseKeyText = "Key_354ygar",
    )

    assert soft.name == "my_software_name"
    assert soft.manufacturer.name == "soft_manufacturer"
    assert soft.version == "12.rwg5"
    assert soft.bitDepth == "x64"
    assert soft.licenseKeyText == "Key_354ygar"

@pytest.mark.django_db  
def test_OS_create():
    """Тестирует создание записи в базе данных для модели OS"""
    Manufacturer.objects.create(name="soft_manufacturer")
    OS = Os.objects.create(
        name = "my_OS_name",
        manufacturer = Manufacturer.objects.get(name="soft_manufacturer"),
        version = "12.rwg5",
        bitDepth = "x64",
        licenseKeyText = "Key_354ygar",
    )

    assert OS.name == "my_OS_name"
    assert OS.manufacturer.name == "soft_manufacturer"
    assert OS.version == "12.rwg5"
    assert OS.bitDepth == "x64"
    assert OS.licenseKeyText == "Key_354ygar"