import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from core.tests.test_login import auto_login_user
from ..models import Categories, Accounting


# Accounting
# list and create
@pytest.mark.django_db
def test_list_url_exists_at_desired_location(auto_login_user):
    client, user = auto_login_user()
    links = ['/accounting/', '/accounting/accounting/', '/accounting/accounting/search',
             '/accounting/categories/', '/accounting/categories/search']
    for link in links:
        url = link
        response = client.get(url)
        assert response.status_code == 200


@pytest.mark.django_db
def test_list_uses_correct_url_nad_template(auto_login_user):
    client, user = auto_login_user()
    links = [
        {'link': 'accounting:accounting_index', 'template': 'accounting/accounting_index.html'},
        {'link': 'accounting:accounting_list', 'template': 'accounting/accounting_list.html'},
        {'link': 'accounting:accounting_search', 'template': 'accounting/accounting_list.html'},
        {'link': 'accounting:new-accounting', 'template': 'Forms/add.html'},
        {'link': 'accounting:categories_list', 'template': 'accounting/categories_list.html'},
        {'link': 'accounting:categories_search', 'template': 'accounting/categories_list.html'},
        {'link': 'accounting:new-categories', 'template': 'Forms/add.html'},
    ]
    for each in links:
        url = reverse(each.get('link'))
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, each.get('template'))


# detail_update_delete
@pytest.mark.django_db
def test_details_url(auto_login_user):
    client, user = auto_login_user()
    links = [
        {'model': Accounting, 'link': 'accounting:accounting-detail',
            'template': 'accounting/accounting_detail.html'},
        {'model': Accounting, 'link': 'accounting:accounting-update', 'template': 'Forms/add.html'},
        {'model': Accounting, 'link': 'accounting:accounting-delete', 'template': 'Forms/delete.html'},
    ]
    for each in links:

        model = each.get('model').objects.create(name="some_model")
        url = reverse(each.get('link'), kwargs={"pk": model.pk})
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, each.get('template'))


# category
@pytest.mark.django_db
def test_consumable_category_url(auto_login_user):
    client, user = auto_login_user()
    Categories.objects.create(name="some_category")
    url = reverse('accounting:category', kwargs={"category_slug": Categories.objects.get(slug="some_category")})
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, 'accounting/accounting_list.html')
