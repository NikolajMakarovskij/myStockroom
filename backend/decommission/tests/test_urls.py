import pytest
from pytest_django.asserts import assertTemplateUsed
from core.tests.test_login import auto_login_user
from django.urls import reverse
from decommission.models import CategoryDec


# list and create
@pytest.mark.django_db
def test_list_url_exists_at_desired_location(auto_login_user):
    client, user = auto_login_user()
    links = [
        '/decommission/decom/',
        '/decommission/decom/search',
        '/decommission/decom/history/',
        '/decommission/decom/history/search',
        '/decommission/disposal/',
        '/decommission/disposal/search',
        '/decommission/disposal/history/',
        '/decommission/disposal/history/search',
    ]
    for link in links:
        url = link
        response = client.get(url)
        assert response.status_code == 200


@pytest.mark.django_db
def test_list_uses_correct_url_nad_template(auto_login_user):
    client, user = auto_login_user()
    links = [
        {'link': 'decommission:decom_list', 'template': 'decom/decom_list.html'},
        {'link': 'decommission:decom_search', 'template': 'decom/decom_list.html'},
        {'link': 'decommission:history_dec_list', 'template': 'decom/history_decom_list.html'},
        {'link': 'decommission:history_decom_search', 'template': 'decom/history_decom_list.html'},
        {'link': 'decommission:disp_list', 'template': 'decom/disp_list.html'},
        {'link': 'decommission:disp_search', 'template': 'decom/disp_list.html'},
        {'link': 'decommission:history_dis_list', 'template': 'decom/history_disp_list.html'},
        {'link': 'decommission:history_dis_search', 'template': 'decom/history_disp_list.html'},
    ]
    for each in links:
        url = reverse(each.get('link'))
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, each.get('template'))


# category
@pytest.mark.django_db
def test_stockroom_category_url(auto_login_user):
    client, user = auto_login_user()
    links = [
        {'link': 'decommission:decom_category', 'template': 'decom/decom_list.html'},
        {'link': 'decommission:history_dec_category', 'template': 'decom/history_decom_list.html'},
        {'link': 'decommission:disp_category', 'template': 'decom/disp_list.html'},
        {'link': 'decommission:history_dis_category', 'template': 'decom/history_disp_list.html'},
    ]
    CategoryDec.objects.create(name="some_category", slug="some_category")
    for each in links:
        url = reverse(each.get('link'), kwargs={"category_slug": CategoryDec.objects.get(slug="some_category")})
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, each.get('template'))
