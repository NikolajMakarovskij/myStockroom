import datetime

import pytest
from counterparty.models import Manufacturer
from decommission.models import CategoryDec, CategoryDis, Decommission, Disposal
from device.models import Device
from django.db.utils import IntegrityError


# Decommission
@pytest.mark.django_db
def test_category_decom_create():
    """Is testing the creation of a record in the database for the CategoryDec model of the Decommission application"""
    CategoryDec.objects.create(name="my_category_name", slug="my_category_slug")
    category = CategoryDec.objects.get(name="my_category_name")
    assert CategoryDec.objects.count() == 1
    assert category.name == "my_category_name"
    assert category.slug == "my_category_slug"
    assert category.__str__() == "my_category_name"


@pytest.mark.django_db
def test_category_dev_unique_slug():
    """Tests for duplication in the slug field in CategoryDec"""
    with pytest.raises(IntegrityError):
        CategoryDec.objects.create(name="my_category_1", slug="my_category")

        assert CategoryDec.objects.create(name="my_category_2", slug="my_category")


@pytest.mark.django_db
def test_decommission_dev_create():
    """Tests the creation of a record in the database for the Devices model"""
    CategoryDec.objects.create(name="my_category", slug="my_category")
    Manufacturer.objects.create(
        name="name_manufacturer",
    )
    Device.objects.create(
        name="my_device",
        manufacturer=Manufacturer.objects.get(name="name_manufacturer"),
        quantity=10,
    )
    Decommission.objects.create(
        stock_model=Device.objects.get(name="my_device"),
        categories=CategoryDec.objects.get(name="my_category"),
        date=datetime.date.today(),
    )
    decom = Decommission.objects.get(stock_model__name="my_device")
    assert Decommission.objects.count() == 1
    assert decom.stock_model.name == "my_device"
    assert decom.stock_model.manufacturer.name == "name_manufacturer"  # type: ignore[union-attr]
    assert decom.stock_model.quantity == 10
    assert decom.categories.name == "my_category"  # type: ignore[union-attr]
    assert decom.date == datetime.date.today()


# Disposal
@pytest.mark.django_db
def test_category_disp_create():
    """Is testing the creation of a record in the database for the CategoryDis model of the Disposal application"""
    CategoryDis.objects.create(name="my_category_name", slug="my_category_slug")
    category = CategoryDis.objects.get(name="my_category_name")
    assert CategoryDis.objects.count() == 1
    assert category.name == "my_category_name"
    assert category.slug == "my_category_slug"
    assert category.__str__() == "my_category_name"


@pytest.mark.django_db
def test_category_disp_unique_slug():
    """Tests for duplication in the slug field in CategoryDis"""
    with pytest.raises(IntegrityError):
        CategoryDis.objects.create(name="my_category_1", slug="my_category")

        assert CategoryDis.objects.create(name="my_category_2", slug="my_category")


@pytest.mark.django_db
def test_disposal_dev_create():
    """Tests the creation of a record in the database for the Devices model"""
    CategoryDis.objects.create(name="my_category", slug="my_category")
    Manufacturer.objects.create(
        name="name_manufacturer",
    )
    Device.objects.create(
        name="my_device",
        manufacturer=Manufacturer.objects.get(name="name_manufacturer"),
        quantity=10,
    )
    Disposal.objects.create(
        stock_model=Device.objects.get(name="my_device"),
        categories=CategoryDis.objects.get(name="my_category"),
        date=datetime.date.today(),
    )
    decom = Disposal.objects.get(stock_model__name="my_device")
    assert Disposal.objects.count() == 1
    assert decom.stock_model.name == "my_device"
    assert decom.stock_model.manufacturer.name == "name_manufacturer"  # type: ignore[union-attr]
    assert decom.stock_model.quantity == 10
    assert decom.categories.name == "my_category"  # type: ignore[union-attr]
    assert decom.date == datetime.date.today()
    assert decom.date == datetime.date.today()
