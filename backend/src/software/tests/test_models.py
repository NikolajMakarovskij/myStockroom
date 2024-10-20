import pytest
from counterparty.models import Manufacturer

from ..models import Os, Software


@pytest.mark.django_db
def test_software_create():
    """Тестирует создание записи в базе данных для модели Software"""
    Manufacturer.objects.create(name="soft_manufacturer")
    Software.objects.create(
        name="my_software_name",
        manufacturer=Manufacturer.objects.get(name="soft_manufacturer"),
        version="12.rwg5",
        bitDepth="x64",
        licenseKeyText="Key_354ygar",
    )
    soft = Software.objects.get(name="my_software_name")
    assert Software.objects.count() == 1
    assert soft.name == "my_software_name"
    assert soft.manufacturer.name == "soft_manufacturer"
    assert soft.version == "12.rwg5"
    assert soft.bitDepth == "x64"
    assert soft.licenseKeyText == "Key_354ygar"
    assert soft.__str__() == "my_software_name"


@pytest.mark.django_db
def test_os_create():
    """Тестирует создание записи в базе данных для модели OS"""
    Manufacturer.objects.create(name="soft_manufacturer")
    Os.objects.create(
        name="my_OS_name",
        manufacturer=Manufacturer.objects.get(name="soft_manufacturer"),
        version="12.rwg5",
        bitDepth="x64",
        licenseKeyText="Key_354ygar",
    )
    os_vars = Os.objects.get(name="my_OS_name")
    assert Os.objects.count() == 1
    assert os_vars.name == "my_OS_name"
    assert os_vars.manufacturer.name == "soft_manufacturer"
    assert os_vars.version == "12.rwg5"
    assert os_vars.bitDepth == "x64"
    assert os_vars.licenseKeyText == "Key_354ygar"
    assert os_vars.__str__() == "my_OS_name"
    assert os_vars.__str__() == "my_OS_name"
