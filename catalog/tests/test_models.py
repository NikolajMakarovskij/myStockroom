import pytest  
from myStockroom.wsgi import *
from ..models import References


@pytest.mark.django_db  
def test_references_create():

    References.objects.create(
        name = "my_reference_name",
        linkname = "my_reference_link"
    ) 
    references = References.objects.get(name = "my_reference_name")

    assert References.objects.count() == 1
    assert references.__str__() == "my_reference_name"
    assert references.name == "my_reference_name"
    assert references.linkname == "my_reference_link"
