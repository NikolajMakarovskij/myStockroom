import pytest
from ..forms import printerForm ,Manufacturer, Workplace
from ..models import Categories
from consumables.models import Consumables, Categories as con_cat


@pytest.mark.django_db
def test_printer_form_valid():
    """Тест на валидность формы"""
    Categories.objects.create(name="printer_category")
    Manufacturer.objects.create(name="epson")
    Workplace.objects.create(name="printer_workplace")
    Consumables.objects.create(
        name="T7741",
        categories=con_cat.objects.create(
            name="Картриджы",
            slug="cartridges"
        )
    ) 
    Consumables.objects.create(
        name="T7742",
        categories=con_cat.objects.create(
            name="Фотовал",
            slug="fotowall"
        )
    ) 
    Consumables.objects.create(
        name="T7743",
        categories=con_cat.objects.create(
            name="Тонер",
            slug="slug"
        )
    ) 
    Consumables.objects.create(
        name="T7744",
        categories=con_cat.objects.create(
            name="Фотобарабан",
            slug="drumm"
        )
    ) 
    form_data = {
        "name": "printer_name", 
        "categories": Categories.objects.get(name="printer_category"),
        "manufacturer": Manufacturer.objects.get(name="epson"),
        "serial": "some_serial",
        "invent": "some_number_124",
        "usbPort": "some_ports",
        "lanPort": "some_ports",
        "tray1": "A4",
        "tray2": "A4",
        "tray3": "A4",
        "traySide": "A4",
        "workplace": Workplace.objects.get(name="printer_workplace"),
        "cartridge": Consumables.objects.get(name="T7741"),
        "fotoval": Consumables.objects.get(name="T7742"),
        "toner": Consumables.objects.get(name="T7743"),
        "fotodrumm": Consumables.objects.get(name="T7744"),
        "score": "0",
        "note": "some_note"
    }
    form = printerForm(data=form_data)
    assert form.is_valid() is True


@pytest.mark.django_db
def test_printer_form_score_invalid():
    """Тест на правильность данных в поле количества"""
    err_mes = "Введите целое число."
    form_data = {
        "name": "my_consumable",
        "score": "qwerty",
    }
    form = printerForm(data=form_data)
    assert form.is_valid() is False
    assert [err_mes] == form.errors['score']