import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from .test_login import auto_login_user


# index
@pytest.mark.django_db
def test_url_exists_at_desired_location(auto_login_user):
    client, user = auto_login_user()
    links = [
        '/api/home/',
        '/api/csrf/',
        '/api/session/',
        '/api/whoami/'
    ]
    for link in links:
        url = link
        response = client.get(url)
        assert response.status_code == 200


@pytest.mark.django_db
def test_urls(auto_login_user):
    client, user = auto_login_user()
    links = [
        {'link': 'core:index', 'template': 'index.html'}
    ]
    for each in links:
        url = reverse(each.get('link'))
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, each.get('template'))
