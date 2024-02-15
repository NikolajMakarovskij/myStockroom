import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from core.tests.test_login import auto_login_user
from ..models import Workplace, Room


# list and create
@pytest.mark.django_db
def test_list_url_exists_at_desired_location(auto_login_user):
    client, user = auto_login_user()
    links = [
        '/api/workplace/workplace/',
        '/api/workplace/workplace_list/',
        '/api/workplace/room/'
    ]
    for link in links:
        url = link
        response = client.get(url)
        assert response.status_code == 200

