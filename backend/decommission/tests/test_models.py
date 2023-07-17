import datetime
import pytest
from django.db.utils import IntegrityError
from django.urls import reverse
from counterparty.models import Manufacturer
from device.models import Device
from decommission.models import Decommision, CategoryDec, HistoryDec, Disposal, CategoryDis, HistoryDis


# Decommission
@pytest.mark.django_db
def test_category_decom_create():
    """Is testing the creation of a record in the database for the CategoryDec model of the Decommission application"""
    CategoryDec.objects.create(
        name="my_category_name",
        slug="my_category_slug"
    )
    category = CategoryDec.objects.get(name="my_category_name")
    assert CategoryDec.objects.count() == 1
    assert category.name == "my_category_name"
    assert category.slug == "my_category_slug"
    assert category.__str__() == 'my_category_name'
    #assert category.get_absolute_url() == reverse(
    #    'decommission:decom_category', kwargs={'category_slug': category.slug})


@pytest.mark.django_db
def test_category_dev_unique_slug():
    """Tests for duplication in the slug field in CategoryDec"""
    with pytest.raises(IntegrityError):
        CategoryDec.objects.create(
            name="my_category_1",
            slug="my_category"
        )

        assert (CategoryDec.objects.create(
            name="my_category_2",
            slug="my_category"
        )
        )


@pytest.mark.django_db
def test_decommission_dev_create():
    """Tests the creation of a record in the database for the Devices model"""
    CategoryDec.objects.create(name="my_category", slug="my_category")
    Manufacturer.objects.create(name="name_manufacturer", )
    Device.objects.create(
        name="my_device",
        manufacturer=Manufacturer.objects.get(name="name_manufacturer"),
        score=10
    )
    Decommision.objects.create(
        devices=Device.objects.get(name="my_device"),
        categories=CategoryDec.objects.get(name="my_category"),
        date=datetime.date.today(),
    )
    decom = Decommision.objects.get(devices__name="my_device")
    assert Decommision.objects.count() == 1
    assert decom.devices.name == "my_device"
    assert decom.devices.manufacturer.name == "name_manufacturer"
    assert decom.devices.score == 10
    assert decom.categories.name == "my_category"
    assert decom.date == datetime.date.today()


@pytest.mark.django_db
def test_history_decom_create():
    """Tests the creation History of a record in the database for the Device model"""
    CategoryDec.objects.create(name="my_category", slug="my_category")
    HistoryDec.objects.create(
        devices="my_device",
        devicesId="name_manufacturer",
        categories=CategoryDec.objects.get(name="my_category"),
        date=datetime.date.today(),
        user="admin"
    )
    history = HistoryDec.objects.get(devices="my_device")
    assert HistoryDec.objects.count() == 1
    assert history.devices == "my_device"
    assert history.devicesId == "name_manufacturer"
    assert history.categories.name == "my_category"
    assert history.date == datetime.date.today()
    assert history.user == "admin"


# Disposal
@pytest.mark.django_db
def test_category_disp_create():
    """Is testing the creation of a record in the database for the CategoryDis model of the Disposal application"""
    CategoryDis.objects.create(
        name="my_category_name",
        slug="my_category_slug"
    )
    category = CategoryDis.objects.get(name="my_category_name")
    assert CategoryDis.objects.count() == 1
    assert category.name == "my_category_name"
    assert category.slug == "my_category_slug"
    assert category.__str__() == 'my_category_name'
    #assert category.get_absolute_url() == reverse(
    #    'decommission:disp_category', kwargs={'category_slug': category.slug})


@pytest.mark.django_db
def test_category_disp_unique_slug():
    """Tests for duplication in the slug field in CategoryDis"""
    with pytest.raises(IntegrityError):
        CategoryDis.objects.create(
            name="my_category_1",
            slug="my_category"
        )

        assert (CategoryDis.objects.create(
            name="my_category_2",
            slug="my_category"
        )
        )


@pytest.mark.django_db
def test_disposal_dev_create():
    """Tests the creation of a record in the database for the Devices model"""
    CategoryDis.objects.create(name="my_category", slug="my_category")
    Manufacturer.objects.create(name="name_manufacturer", )
    Device.objects.create(
        name="my_device",
        manufacturer=Manufacturer.objects.get(name="name_manufacturer"),
        score=10
    )
    Disposal.objects.create(
        devices=Device.objects.get(name="my_device"),
        categories=CategoryDis.objects.get(name="my_category"),
        date=datetime.date.today(),
    )
    decom = Disposal.objects.get(devices__name="my_device")
    assert Disposal.objects.count() == 1
    assert decom.devices.name == "my_device"
    assert decom.devices.manufacturer.name == "name_manufacturer"
    assert decom.devices.score == 10
    assert decom.categories.name == "my_category"
    assert decom.date == datetime.date.today()


@pytest.mark.django_db
def test_history_disposal_create():
    """Tests the creation History of a record in the database for the Device model"""
    CategoryDis.objects.create(name="my_category", slug="my_category")
    HistoryDis.objects.create(
        devices="my_device",
        devicesId="name_manufacturer",
        categories=CategoryDis.objects.get(name="my_category"),
        date=datetime.date.today(),
        user="admin"
    )
    history = HistoryDis.objects.get(devices="my_device")
    assert HistoryDis.objects.count() == 1
    assert history.devices == "my_device"
    assert history.devicesId == "name_manufacturer"
    assert history.categories.name == "my_category"
    assert history.date == datetime.date.today()
    assert history.user == "admin"
