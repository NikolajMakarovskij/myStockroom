from unittest import mock

import pytest
from django.core.files import File

from counterparty.models import Manufacturer

from ..forms import OSForm, SoftwareForm


@pytest.mark.django_db
def test_software_form_valid():
    """Тест на валидность формы"""
    Manufacturer.objects.create(name="soft_manufacturer")

    form_data = {
        "name": "my_software_name",
        "manufacturer": Manufacturer.objects.get(name="soft_manufacturer"),
        "version": "12.rwg5",
        "bitDepth": "x64",
        "licenseKeyText": "Key_354ygar",
        "licenseKeyImg": mock.MagicMock(spec=File, name="serial_Img"),
        "licenseKeyFile": mock.MagicMock(spec=File, name="serial_Img"),
    }
    form = SoftwareForm(data=form_data)
    assert form.is_valid() is True


@pytest.mark.django_db
def test_software_form_name_invalid():
    """Тест на наличие названия"""
    err_name = "Обязательное поле."
    form_data = {
        "name": "",
    }
    form = SoftwareForm(data=form_data)
    assert form.is_valid() is False
    assert [err_name] == form.errors["name"]


@pytest.mark.django_db
def test_OS_form_valid():
    """Тест на валидность формы"""
    Manufacturer.objects.create(name="soft_manufacturer")

    form_data = {
        "name": "my_software_name",
        "manufacturer": Manufacturer.objects.get(name="soft_manufacturer"),
        "version": "12.rwg5",
        "bitDepth": "x64",
        "licenseKeyText": "Key_354ygar",
    }
    form = OSForm(data=form_data)
    assert form.is_valid() is True


@pytest.mark.django_db
def test_OS_form_name_invalid():
    """Тест на наличие названия"""
    err_name = "Обязательное поле."
    form_data = {
        "name": "",
    }
    form = OSForm(data=form_data)
    assert form.is_valid() is False
    assert [err_name] == form.errors["name"]
