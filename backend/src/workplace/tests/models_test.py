import pytest

from ..models import Room, Workplace


@pytest.mark.django_db
def test_room_create():
    """Тестирует создание записи в базе данных для модели Room приложения Workplace"""
    Room.objects.create(name="name_room", building="name_building", floor="name_floor")
    room = Room.objects.get(name="name_room")
    assert Room.objects.count() == 1
    assert room.name == "name_room"
    assert room.building == "name_building"
    assert room.floor == "name_floor"
    assert room.__str__() == "name_room"


@pytest.mark.django_db
def test_workplace_create():
    """Тестирует создание записи в базе данных для модели Workplace"""
    Room.objects.create(name="my_room")
    Workplace.objects.create(
        name="my_workplace_name",
        room=Room.objects.get(name="my_room"),
    )
    wp = Workplace.objects.get(name="my_workplace_name")
    assert Workplace.objects.count() == 1
    assert wp.name == "my_workplace_name"
    assert wp.room.name == "my_room"  # type: ignore[union-attr]
    assert wp.__str__() == "my_workplace_name"
