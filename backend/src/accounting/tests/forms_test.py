import pytest

from consumables.models import Accessories, Consumables

from ..forms import AccountingForm, CategoriesForm
from ..models import Categories


# Accounting
@pytest.mark.django_db
def test_accounting_form_valid():
    """_Form validation test_

    Returns:
        AccountingForm (func): _form.is_valid() is True_
    """
    Categories.objects.create(name="my_category", slug="my_category")
    Consumables.objects.create(name="my_consumable")
    Accessories.objects.create(name="my_accessories")

    form_data = {
        "name": "my_consumable",
        "categories": Categories.objects.get(name="my_category"),
        "account": "123",
        "consumable": Consumables.objects.get(name="my_consumable"),
        "accessories": Accessories.objects.get(name="my_accessories"),
        "quantity": "3",
        "note": "some_name",
        "code": "000753",
        "cost": "32.23",
    }
    form = AccountingForm(data=form_data)
    assert form.is_valid() is True


@pytest.mark.django_db
def test_accounting_form_name_invalid():
    """_Test for the presence of a name_

    Returns:
        AccountingForm (func): _form.is_valid() is False_
        err_name (str): _form.errors["name"]_
    """
    err_name = "Обязательное поле."
    form_data = {
        "name": "",
    }
    form = AccountingForm(data=form_data)
    assert form.is_valid() is False
    assert [err_name] == form.errors["name"]


@pytest.mark.django_db
def test_accounting_form_cost_invalid():
    """_Test for entering a number in the cost field_

    Returns:
        AccountingForm (func): _form.is_valid() is False_
        err_mes (str): _form.errors["cost"]_
    """
    err_mes = "Введите число."
    form_data = {
        "name": "my_consumable",
        "cost": "qwerty",
    }
    form = AccountingForm(data=form_data)
    assert form.is_valid() is False
    assert [err_mes] == form.errors["cost"]


@pytest.mark.django_db
def test_accounting_form_account_invalid():
    """_Test for entering a number in the account field_

    Returns:
        AccountingForm (func): _form.is_valid() is False_
        err_mes (str): _form.errors["account"]_
    """
    err_mes = "Введите целое число."
    form_data = {
        "name": "my_consumable",
        "account": "qwerty",
    }
    form = AccountingForm(data=form_data)
    assert form.is_valid() is False
    assert [err_mes] == form.errors["account"]


@pytest.mark.django_db
def test_accounting_form_quantity_invalid():
    """_Test for entering a number in the quantity field_

    Returns:
        AccountingForm (func): _form.is_valid() is False_
        err_mes (str): _form.errors["quantity"]_
    """
    err_mes = "Введите целое число."
    form_data = {
        "name": "my_consumable",
        "quantity": "qwerty",
    }
    form = AccountingForm(data=form_data)
    assert form.is_valid() is False
    assert [err_mes] == form.errors["quantity"]


# Categories
@pytest.mark.django_db
def test_categories_form_valid():
    """Тест на валидность формы"""

    form_data = {"name": "my_consumable", "slug": "my_consumable"}
    form = CategoriesForm(data=form_data)
    assert form.is_valid() is True
