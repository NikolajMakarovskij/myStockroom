from django.db.utils import IntegrityError
import pytest  
from myStockroom.wsgi import *
from ..models import Workplace, Room



@pytest.mark.django_db  
def test_room_create():
    """Тестирует создание записи в базе данных для модели Room приложения Workplace"""
    room = Room.objects.create(
        name = "name_room",
        building = "name_building",
        floor = "name_floor"
    ) 
    assert Room.objects.count() == 1
    assert room.name == "name_room"
    assert room.building == "name_building"
    assert room.floor == "name_floor"

@pytest.mark.django_db  
def test_workplace_create():
    """Тестирует создание записи в базе данных для модели Workplace"""
    Room.objects.create(name="my_room") 
    post = Workplace.objects.create(
        name = "my_workplace_name",
        room = Room.objects.get(name="my_room"),
    )
    assert Workplace.objects.count() == 1
    assert post.name == "my_workplace_name"
    assert post.room.name == "my_room"
    
