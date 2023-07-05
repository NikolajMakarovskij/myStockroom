import pytest
import warnings
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from ..models import Categories, Consumables, Accessories, AccCat


# Расходники
# list and create
@pytest.mark.django_db
def test_list_url_exists_at_desired_location(client):
    warnings.filterwarnings(action="ignore")
    links = ['/consumables/', '/consumables/consumables/', '/consumables/consumables/search',
             '/consumables/accessories/', '/consumables/accessories/search']
    for link in links:
        url = link
        response = client.get(url)
        assert response.status_code == 200


@pytest.mark.django_db
def test_list_uses_correct_url_nad_template(client):
    warnings.filterwarnings(action="ignore")
    links = [
        {'link': 'consumables:consumables_index', 'template': 'consumables/consumables_index.html'},
        {'link': 'consumables:consumables_list', 'template': 'consumables/consumables_list.html'},
        {'link': 'consumables:consumables_search', 'template': 'consumables/consumables_list.html'},
        {'link': 'consumables:new-consumables', 'template': 'Forms/add.html'},
        {'link': 'consumables:accessories_list', 'template': 'consumables/accessories_list.html'},
        {'link': 'consumables:accessories_search', 'template': 'consumables/accessories_list.html'},
        {'link': 'consumables:new-accessories', 'template': 'Forms/add.html'},
    ]
    for each in links:
        url = reverse(each.get('link'))
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, each.get('template'))


# detail_update_delete
@pytest.mark.django_db
def test_details_url(client):
    warnings.filterwarnings(action="ignore")
    links = [
        {'model': Consumables, 'link': 'consumables:consumables-detail',
         'template': 'consumables/consumables_detail.html'},
        {'model': Consumables, 'link': 'consumables:consumables-update', 'template': 'Forms/add.html'},
        {'model': Consumables, 'link': 'consumables:consumables-delete', 'template': 'Forms/delete.html'},
        {'model': Accessories, 'link': 'consumables:accessories-detail',
         'template': 'consumables/accessories_detail.html'},
        {'model': Accessories, 'link': 'consumables:accessories-update', 'template': 'Forms/add.html'},
        {'model': Accessories, 'link': 'consumables:accessories-delete', 'template': 'Forms/delete.html'},
    ]
    for each in links:
        model = each.get('model').objects.create(name="some_model")
        url = reverse(each.get('link'), kwargs={"pk": model.pk})
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, each.get('template'))


# category
@pytest.mark.django_db
def test_consumable_category_url(client):
    warnings.filterwarnings(action="ignore")
    Categories.objects.create(name="some_category", slug="some_category")
    url = reverse('consumables:category', kwargs={"category_slug": Categories.objects.get(slug="some_category")})
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, 'consumables/consumables_list.html')


# category
@pytest.mark.django_db
def test_consumable_category_url(client):
    warnings.filterwarnings(action="ignore")
    AccCat.objects.create(name="some_category", slug="some_category")
    url = reverse('consumables:category_accessories',
                  kwargs={"category_slug": AccCat.objects.get(slug="some_category")})
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, 'consumables/accessories_list.html')
