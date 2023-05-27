from django.db.utils import IntegrityError
from django.urls import reverse
import pytest  
from myStockroom.wsgi import *
from ..models import Printer, Printer_cat, Consumables
from workplace.models import Workplace
from counterparty.models import Manufacturer

@pytest.mark.django_db  
def test_printer_category_create():
    """Тестирует создание записи в базе данных для модели Categories приложения Printer"""
    Printer_cat.objects.create(
        name = "my_category_name",
        slug = "my_category_slug"
    )
    category = Printer_cat.objects.get(name = "my_category_name")
    assert Printer_cat.objects.count() == 1
    assert category.name == "my_category_name"
    assert category.slug == "my_category_slug"
    assert category.__str__() == "my_category_name"
    assert category.get_absolute_url() == reverse('printer:category',kwargs={'category_slug': category.slug})

@pytest.mark.django_db  
def test_printer_category_unique_slug():
    """Тестирует наличие дублирования в поле slug приложение Printer"""
    with pytest.raises(IntegrityError):
        Printer_cat.objects.create(
            name = "my_category_1",
            slug = "my_category"
        )

        assert  (Printer_cat.objects.create(
            name = "my_category_2",
            slug = "my_category"
        )
        )
    
@pytest.mark.django_db  
def test_printer_create():
    """Тестирует создание записи в базе данных для модели Printer"""
    Printer_cat.objects.create(name="printer_category")
    Manufacturer.objects.create(name="epson")
    Workplace.objects.create(name = "printer_workplace")
    Consumables.objects.create(name = "cartridge") 
    Printer.objects.create(  
        name = "printer_name", 
        categories = Printer_cat.objects.get(name="printer_category"),
        manufacturer = Manufacturer.objects.get(name="epson"),
        serial = "some_serial",
        invent = "some_number_124",
        usbPort = "some_ports",
        lanPort = "some_ports",
        workplace = Workplace.objects.get(name="printer_workplace"),
        consumable = Consumables.objects.get(name = "cartridge"),
        score = 0,
        note = "some_note"
    )  
    printer = Printer.objects.get(name = "printer_name") 
    assert Printer.objects.count() == 1
    assert printer.name == "printer_name"
    assert printer.categories.name == "printer_category"
    assert printer.manufacturer.name == "epson"
    assert printer.serial == "some_serial"
    assert printer.invent == "some_number_124"
    assert printer.usbPort == "some_ports"
    assert printer.lanPort == "some_ports"
    assert printer.tray1 == "A4"
    assert printer.tray2 == "A3"
    assert printer.tray3 == "Отсутствует"
    assert printer.traySide == "A4"
    assert printer.workplace.name == "printer_workplace"
    assert printer.consumable.name == "cartridge"
    assert printer.score == 0
    assert printer.note == "some_note"
    assert printer.__str__() == "printer_name"
    assert printer.get_absolute_url() == reverse('printer:printer-detail', kwargs={'pk': printer.pk})

