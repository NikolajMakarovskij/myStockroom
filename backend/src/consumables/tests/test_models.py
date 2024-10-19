import pytest
from counterparty.models import Manufacturer
from django.db.utils import IntegrityError

from ..models import AccCat, Accessories, Categories, Consumables


# Расходники
@pytest.mark.django_db
def test_category_create():
    """Тестирует создание записи в базе данных для модели Categories приложения Consumables"""
    Categories.objects.create(name="my_category_name", slug="my_category_slug")
    category = Categories.objects.get(name="my_category_name")
    assert Categories.objects.count() == 1
    assert category.name == "my_category_name"
    assert category.slug == "my_category_slug"
    assert category.__str__() == "my_category_name"
    # assert category.get_absolute_url() == reverse('consumables:category', kwargs={'category_slug': category.slug})


@pytest.mark.django_db
def test_category_unique_slug():
    """Тестирует наличие дублирования в поле slug"""
    with pytest.raises(IntegrityError):
        Categories.objects.create(name="my_category_1", slug="my_category")

        assert Categories.objects.create(name="my_category_2", slug="my_category")


@pytest.mark.django_db
def test_consumable_create():
    """Тестирует создание записи в базе данных для модели Consumables"""
    Categories.objects.create(name="my_category", slug="my_category")
    Manufacturer.objects.create(
        name="name_manufacturer", country="country", production="production_country"
    )
    Consumables.objects.create(
        name="my_consumable",
        categories=Categories.objects.get(name="my_category"),
        manufacturer=Manufacturer.objects.get(name="name_manufacturer"),
        serial="123",
        invent="321",
        quantity="2",
        description="my_description",
        note="my_note",
    )
    consumable = Consumables.objects.get(name="my_consumable")
    assert Consumables.objects.count() == 1
    assert consumable.name == "my_consumable"
    assert consumable.categories.name == "my_category"
    assert consumable.categories.slug == "my_category"
    assert consumable.manufacturer.name == "name_manufacturer"
    assert consumable.manufacturer.country == "country"
    assert consumable.manufacturer.production == "production_country"
    assert consumable.serial == "123"
    assert consumable.invent == "321"
    assert consumable.quantity == 2
    assert consumable.description == "my_description"
    assert consumable.note == "my_note"
    assert consumable.__str__() == "my_consumable"


# Комплектующие
@pytest.mark.django_db
def test_acc_cat_create():
    """Тестирует создание записи в базе данных для модели Acc_cat приложения Consumables"""
    AccCat.objects.create(name="my_category_name", slug="my_category_slug")
    category = AccCat.objects.get(name="my_category_name")
    assert AccCat.objects.count() == 1
    assert category.name == "my_category_name"
    assert category.slug == "my_category_slug"
    assert category.__str__() == "my_category_name"


# assert category.get_absolute_url() == reverse('consumables:category_accessories',
#                                              kwargs={'category_slug': category.slug})


@pytest.mark.django_db
def test_acc_cat_unique_slug():
    """Тестирует наличие дублирования в поле slug"""
    with pytest.raises(IntegrityError):
        AccCat.objects.create(name="my_category_1", slug="my_category")

        assert AccCat.objects.create(name="my_category_2", slug="my_category")


@pytest.mark.django_db
def test_accessories_create():
    """Тестирует создание записи в базе данных для модели Accessories"""
    AccCat.objects.create(name="my_category", slug="my_category")
    Manufacturer.objects.create(
        name="name_manufacturer", country="country", production="production_country"
    )
    Accessories.objects.create(
        name="my_consumable",
        categories=AccCat.objects.get(name="my_category"),
        manufacturer=Manufacturer.objects.get(name="name_manufacturer"),
        serial="123",
        invent="321",
        quantity="2",
        description="my_description",
        note="my_note",
    )
    accessories = Accessories.objects.get(name="my_consumable")
    assert Accessories.objects.count() == 1
    assert accessories.name == "my_consumable"
    assert accessories.categories.name == "my_category"
    assert accessories.categories.slug == "my_category"
    assert accessories.manufacturer.name == "name_manufacturer"
    assert accessories.manufacturer.country == "country"
    assert accessories.manufacturer.production == "production_country"
    assert accessories.serial == "123"
    assert accessories.invent == "321"
    assert accessories.quantity == 2
    assert accessories.description == "my_description"
    assert accessories.note == "my_note"
    assert accessories.__str__() == "my_consumable"
    assert accessories.__str__() == "my_consumable"
