import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from core.tests.login_test import auto_login_user  # noqa: F401
from decommission.models import CategoryDec


# list and create
@pytest.mark.django_db
def test_list_url_exists_at_desired_location(auto_login_user):  # noqa: F811
    client, user = auto_login_user()
    links = [
        "/decommission/decom/",
        "/decommission/decom/search",
        "/decommission/disposal/",
        "/decommission/disposal/search",
    ]
    for link in links:
        url = link
        response = client.get(url)
        assert response.status_code == 200


@pytest.mark.django_db
def test_list_uses_correct_url_nad_template(auto_login_user):  # noqa: F811
    client, user = auto_login_user()
    links = [
        {"link": "decommission:decom_list", "template": "decom/decom_list.html"},
        {"link": "decommission:decom_search", "template": "decom/decom_list.html"},
        {"link": "decommission:disp_list", "template": "decom/disp_list.html"},
        {"link": "decommission:disp_search", "template": "decom/disp_list.html"},
    ]
    for each in links:
        url = reverse(each.get("link"))
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, each.get("template"))


# category
@pytest.mark.django_db
def test_stockroom_category_url(auto_login_user):  # noqa: F811
    client, user = auto_login_user()
    links = [
        {"link": "decommission:decom_category", "template": "decom/decom_list.html"},
        {"link": "decommission:disp_category", "template": "decom/disp_list.html"},
    ]
    CategoryDec.objects.create(name="some_category", slug="some_category")
    for each in links:
        url = reverse(
            each.get("link"),
            kwargs={"category_slug": CategoryDec.objects.get(slug="some_category")},
        )
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, each.get("template"))
