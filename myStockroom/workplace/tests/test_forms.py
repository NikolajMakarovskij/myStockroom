import pytest
from ..forms import workplaceForm, roomForm, Room


@pytest.mark.django_db
def test_room_form_valid():
    """Тест на валидность формы"""
    form_data = {
        "name": "room_name",
        "floor": "room_floor",
        "building": "room_building",
    }
    form = roomForm(data=form_data)
    assert form.is_valid() is True

@pytest.mark.django_db
def test_room_form_name_invalid():
    """Тест на наличие названия"""
    err_name = "Обязательное поле."
    form_data = {
        'name': "",
    }
    form = workplaceForm(data=form_data)
    assert form.is_valid() is False
    assert [err_name] == form.errors['name']

@pytest.mark.django_db
def test_workplace_form_valid():
    """Тест на валидность формы"""
    Room.objects.create(name="my_room")

    form_data = {
        'name': "my_consumable",
        'room': Room.objects.get(name="my_room"),
    }
    form = workplaceForm(data=form_data)
    assert form.is_valid() is True

@pytest.mark.django_db
def test_workplace_form_name_invalid():
    """Тест на наличие названия"""
    err_name = "Обязательное поле."
    form_data = {
        'name': "",
    }
    form = workplaceForm(data=form_data)
    assert form.is_valid() is False
    assert [err_name] == form.errors['name']