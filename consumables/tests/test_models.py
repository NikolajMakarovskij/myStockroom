from django.db.utils import IntegrityError
import pytest  
from myStockroom.wsgi import *
from ..models import Consumables, Categories

@pytest.mark.django_db  
def test_category_create():

    category = Categories.objects.create(
        name = "my_category_name",
        slug = "my_category_slug"
    )

    assert category.name == "my_category_name"
    assert category.slug == "my_category_slug"

@pytest.mark.django_db  
def test_category_unique_slug():

    with pytest.raises(IntegrityError):
        Categories.objects.create(
            name = "my_category_1",
            slug = "my_category"
        )

        assert  (Categories.objects.create(
            name = "my_category_2",
            slug = "my_category"
        )
        )
    

@pytest.mark.django_db  
def test_consumable_create():

    category = Categories.objects.create(
        name = "my_category",
        slug = "my_category"
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

    assert consumable.name == "my_consumable"
    assert consumable.categories.name == "my_category"
    assert consumable.categories.slug == "my_category"  
    assert consumable.serial == "123"
    assert consumable.invent == "321"
    assert consumable.buhCode == "code"
    assert consumable.score == "0"
    assert consumable.description == "my_description"
    assert consumable.note == "my_note"






