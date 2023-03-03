import pytest
from ..forms import consumablesForm, Categories, Manufacturer

@pytest.mark.django_db
def test_consumable_form_valid():
    """Тест на валидность формы"""
    Categories.objects.create(name="my_category")
    Manufacturer.objects.create(name="My_manufacturer")

    form_data = {
        'name': "my_consumable",
        'categories': Categories.objects.get(name="my_category"),
        'description': "some_description",
        'note': "some_name",
        'manufacturer': Manufacturer.objects.get(name="My_manufacturer"),
        'buhCode': "000753",
        'score': "0",
        'serial': "some_serial123",
        'invent': "some_invent123",
    }
    form = consumablesForm(data=form_data)
    assert form.is_valid() is True

@pytest.mark.django_db
def test_consumable_form_code_invalid():
    """Тест на наличие бухгалтерского кода"""
    Categories.objects.create(name="my_category")
    Manufacturer.objects.create(name="My_manufacturer")
    err_mes = "Обязательное поле."

    form_data = {
        'name': "my_consumable",
        'buhCode': "",
    }
    form = consumablesForm(data=form_data)
    assert form.is_valid() is False
    assert [err_mes] == form.errors['buhCode']

@pytest.mark.django_db
def test_consumable_form_score_invalid():
    """Тест на правильность данных в поле количества"""
    Categories.objects.create(name="my_category")
    Manufacturer.objects.create(name="My_manufacturer")
    err_mes = "Введите целое число."

    form_data = {
        "name": "my_consumable",
        "score": "qwerty",
    }
    form = consumablesForm(data=form_data)
    assert form.is_valid() is False
    assert [err_mes] == form.errors['score']