import pytest  
from myStockroom.wsgi import *
from ..models import Consumables, Cassette, Ups
from counterparty.models import Manufacturer
from django.urls import reverse


@pytest.mark.django_db  
def test_cassette_create():
    """Тестирует создание записи в базе данных для модели Cassette"""
    Manufacturer.objects.create(name="epson")
    Consumables.objects.create(name = "accumulator") 
    Cassette.objects.create(  
        name = "cassette_name", 
        manufacturer = Manufacturer.objects.get(name="epson"),
        serial = "some_serial",
        invent = "some_number_124",
        power = "150W",
        voltage = "12V",
        current = "7A",
        accumulator = Consumables.objects.get(name = "accumulator"),
        score = 0,
    )
    cassette = Cassette.objects.get(name = "cassette_name")
    assert Cassette.objects.count() == 1
    assert cassette.name == "cassette_name"
    assert cassette.manufacturer.name == "epson"
    assert cassette.serial == "some_serial"
    assert cassette.invent == "some_number_124"
    assert cassette.power == "150W"
    assert cassette.voltage == "12V"
    assert cassette.current == "7A"
    assert cassette.accumulator.name == "accumulator"
    assert cassette.score == 0
    assert cassette.__str__() == "cassette_name"
    assert cassette.get_absolute_url() == reverse('ups:cassette-detail',kwargs={'pk': cassette.pk})


@pytest.mark.django_db  
def test_ups_create():
    """Тестирует создание записи в базе данных для модели UPS"""
    Manufacturer.objects.create(name="epson")
    Consumables.objects.create(name = "accumulator")
    Cassette.objects.create(
        name="some_cassette",
        manufacturer=Manufacturer.objects.get(name="epson"),
        accumulator=Consumables.objects.get(name = "accumulator")
    )
     
    Ups.objects.create(  
        name = "cassette_name", 
        manufacturer = Manufacturer.objects.get(name="epson"),
        serial = "some_serial",
        invent = "some_number_124",
        power = "150W",
        voltage = "12V",
        current = "7A",
        accumulator = Consumables.objects.get(name = "accumulator"),
        cassette = Cassette.objects.get(name="some_cassette"),
        score = 0,
    )  
    ups = Ups.objects.get(name = "cassette_name")
    assert Ups.objects.count() == 1
    assert ups.name == "cassette_name"
    assert ups.manufacturer.name == "epson"
    assert ups.serial == "some_serial"
    assert ups.invent == "some_number_124"
    assert ups.power == "150W"
    assert ups.voltage == "12V"
    assert ups.current == "7A"
    assert ups.accumulator.name == "accumulator"
    assert ups.cassette.name == "some_cassette"
    assert ups.cassette.accumulator.name == "accumulator"
    assert ups.cassette.manufacturer.name == "epson"
    assert ups.score == 0
    assert ups.__str__() == "cassette_name"
    assert ups.get_absolute_url() == reverse('ups:ups-detail',kwargs={'pk': ups.pk})