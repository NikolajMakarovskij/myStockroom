import uuid
import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.fixture
def auto_login_user(db, client):
    def make_auto_login(user=None):
        client.force_login(User.objects.get_or_create(username='user')[0])
        return client, user

    return make_auto_login


@pytest.mark.django_db
def test_view_unauthorized(auto_login_user):
    client, user = auto_login_user()
    url = reverse('catalog:index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_view_as_admin(admin_client):
    url = reverse('catalog:index')
    response = admin_client.get(url)
    assert response.status_code == 200


