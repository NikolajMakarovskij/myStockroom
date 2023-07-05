import pytest
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse


# index
@pytest.mark.django_db
def test_url_exists_at_desired_location(client):
    links = ['', '/references/', '/references/search']
    for link in links:
        url = link
        response = client.get(url)
        assert response.status_code == 200


@pytest.mark.django_db
def test_urls(client):
    links = [
        {'link': 'catalog:index', 'template': 'index.html'},
        {'link': 'catalog:references_list', 'template': 'catalog/references.html'},
        {'link': 'catalog:references_search', 'template': 'catalog/references.html'},
    ]
    for each in links:
        url = reverse(each.get('link'))
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, each.get('template'))
