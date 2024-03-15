import pytest
from django.db.utils import IntegrityError
from django.urls import reverse

from consumables.models import Accessories, Consumables

from ..models import Accounting, Categories


@pytest.mark.django_db
def test_category_create():
    """Тестирует создание записи в базе данных для модели Categories приложения Accounting"""
    Categories.objects.create(
        name="my_category_name",
        slug="my_category_name",
    )
    category = Categories.objects.get(name="my_category_name")
    assert Categories.objects.count() == 1
    assert category.name == "my_category_name"
    assert category.slug == "my_category_name"
    assert category.__str__() == 'my_category_name'
    assert category.get_absolute_url() == reverse('accounting:categories-detail',
                                                  kwargs={'pk': category.pk})

@pytest.mark.django_db
def test_category_unique_slug():
    """Тестирует наличие дублирования в поле slug"""
    with pytest.raises(IntegrityError):
        Categories.objects.create(
            name="my_category",
        )

        assert Categories.objects.create(
            name="my_category",
        )


@pytest.mark.django_db
def test_accounting_create():
    """Тестирует создание записи в базе данных для модели Consumables"""
    Categories.objects.create(name="my_category", slug="my_category")
    Consumables.objects.create(name="my_consumable")
    Accessories.objects.create(name="my_accessories")
    Accounting.objects.create(
        name="my_accounting",
        categories=Categories.objects.get(name="my_category"),
        account="123",
        consumable=Consumables.objects.get(name="my_consumable"),
        accessories=Accessories.objects.get(name="my_accessories"),
        quantity="3",
        note="some_name",
        code="000753",
        cost="35.23",
    )
    accounting = Accounting.objects.get(name="my_accounting")
    assert Accounting.objects.count() == 1
    assert accounting.name == "my_accounting"
    assert accounting.categories.name == "my_category"  # type: ignore[union-attr]
    assert accounting.categories.slug == "my_category"  # type: ignore[union-attr]
    assert accounting.consumable.name == "my_consumable"  # type: ignore[union-attr]
    assert accounting.accessories.name == "my_accessories"  # type: ignore[union-attr]
    assert accounting.account == 123
    assert accounting.code == "000753"
    assert accounting.quantity == 3
    assert accounting.cost == 35.23
    assert accounting.get_cost_all() == 105.69
    assert accounting.note == "some_name"
    assert accounting.__str__() == "my_accounting"
    assert accounting.get_absolute_url() == reverse(
        "accounting:accounting-detail", kwargs={"pk": accounting.pk}
    )
