import pytest
from decommission.decom import Decom
from decommission.models import CategoryDec, CategoryDis
from device.models import Device, DeviceCat
from django.conf import settings
from django.contrib.auth.models import User


def create_session(client):
    """Creates a user and a session"""
    User.objects.create_superuser("admin", "foo@foo.com", "admin")
    client.login(username="admin", password="admin")
    session = client.session
    session[settings.DECOM_SESSION_ID] = "6fk7mglhnq7f3avej9rmlshjyrokal3l"
    session.save()
    return client


def create_devices() -> Device:
    """Service function. Creates a category and device"""

    if Device.objects.filter(name="my_consumable").aexists():
        DeviceCat.objects.create(name="my_category", slug="my_category")
        Device.objects.create(
            name="my_consumable", categories=DeviceCat.objects.get(name="my_category")
        )
        get_device = Device.objects.get(name="my_consumable")
    else:
        get_device = Device.objects.get(name="my_consumable")
    return get_device


# Decommission
@pytest.mark.django_db
def test_decom_no_category():
    """Checks the operation of the add_category_decom method of the Decom class"""

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
    test_category = CategoryDec.objects.get(name="my_category")

    assert CategoryDec.objects.count() == 1
    assert test_category.name == "my_category"
    assert test_category.slug == "my_category"


# Disposal
@pytest.mark.django_db
def test_disp_no_category():
    """Checks the operation of the add_category_disp method of the Decom class"""

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
    test_category = CategoryDis.objects.get(name="my_category")

    assert CategoryDis.objects.count() == 1
    assert test_category.name == "my_category"
    assert test_category.slug == "my_category"
