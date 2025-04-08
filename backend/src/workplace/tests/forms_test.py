import pytest

from ..forms import RoomForm, WorkplaceForm
from ..models import Room


@pytest.mark.django_db
def test_room_form_valid():
    """Тест на валидность формы"""
    form_data = {
        "name": "room_name",
        "floor": "room_floor",
        "building": "room_building",
    }
    form = RoomForm(data=form_data)
    assert form.is_valid() is True


@pytest.mark.django_db
def test_room_form_name_invalid():
    """Тест на наличие названия"""
    err_name = "Обязательное поле."
    form_data = {
        "name": "",
    }
    form = WorkplaceForm(data=form_data)
    assert form.is_valid() is False
    assert [err_name] == form.errors["name"]


@pytest.mark.django_db
def test_workplace_form_valid():
    """Тест на валидность формы"""
    Room.objects.create(name="my_room")

    form_data = {
        "name": "my_consumable",
        "room": Room.objects.get(name="my_room"),
    }
    form = WorkplaceForm(data=form_data)
    assert form.is_valid() is True


@pytest.mark.django_db
def test_workplace_form_name_invalid():
    """Тест на наличие названия"""
    err_name = "Обязательное поле."
    form_data = {
        "name": "",
    }
    form = WorkplaceForm(data=form_data)
    assert form.is_valid() is False
    assert [err_name] == form.errors["name"]
