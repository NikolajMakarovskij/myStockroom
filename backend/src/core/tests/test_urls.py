import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from core.tests.test_login import auto_login_user  # noqa F401


# index
@pytest.mark.django_db
def test_url_exists_at_desired_location(auto_login_user): # noqa F811
    """_Tests that the url exists at the desired location_

    Args:
        auto_login_user (_type_): _description_
    """
    client, user = auto_login_user()
    links = ['/home/']
    for link in links:
        url = link
        response = client.get(url)
        assert response.status_code == 200


@pytest.mark.django_db
def test_urls(auto_login_user): # noqa F811
    """_summary_: Tests routing in the core application

    Args:
        auto_login_user (_type_): _description_
    """
    client, user = auto_login_user()
    links = [
        {'link': 'core:index', 'template': 'index.html'}
    ]
    for each in links:
        url = reverse(each.get('link'))
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, each.get('template'))
