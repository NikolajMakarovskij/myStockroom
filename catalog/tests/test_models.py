import pytest  
from myStockroom.wsgi import *
from ..models import References

@pytest.mark.django_db  
def test_references_create():
    # Create dummy data 
    references = References.objects.create(
        name = "my_reference_name",
        linkname = "my_reference_link"
    ) 
    # Assert the dummy data saved as expected
    assert references.name == "my_reference_name"
    assert references.linkname == "my_reference_link"
