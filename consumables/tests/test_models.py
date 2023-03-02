import pytest  
from myStockroom.wsgi import *
from ..models import Consumables, Categories

@pytest.mark.django_db  
def test_consumable_create():
    # Create dummy data 
    category = Categories.objects.create(
        name = "my_category_name",
        slug = "my_category_slug"
    ) 
    consumable = Consumables.objects.create(  
        name = "my_consumable",  
        categories = category,  
        serial = "123",
        invent = "321",
        buhCode = "code",
        score = "0",
        description = "my_description",
        note = "my_note",
    )  
    # Assert the dummy data saved as expected
    assert category.name == "my_category"
    assert category.slug == "my_category"
    assert consumable.name == "my_consumable"
    assert consumable.categories.name == "my_category"
    assert consumable.categories.slug == "my_category"  
    assert consumable.serial == "123"
    assert consumable.invent == "321"
    assert consumable.buhCode == "code"
    assert consumable.score == "0"
    assert consumable.description == "my_description"
    assert consumable.note == "my_note"






