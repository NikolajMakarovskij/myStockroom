import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from core.tests.login_test import auto_login_user  # noqa F401

from ..models import Manufacturer


# list and create
@pytest.mark.django_db
def test_list_url_exists_at_desired_location(auto_login_user):  # noqa F811
    client, user = auto_login_user()
    links = [
        "/counterparty/",
        "/counterparty/manufacturer/",
        "/counterparty/manufacturer/search",
    ]
    for link in links:
        url = link
        response = client.get(url)
        assert response.status_code == 200


@pytest.mark.django_db
def test_list_uses_correct_url_nad_template(auto_login_user):  # noqa F811
    client, user = auto_login_user()
    links = [
        {
            "link": "counterparty:counterparty",
            "template": "counterparty/counterparty.html",
        },
        {
            "link": "counterparty:manufacturer_list",
            "template": "counterparty/manufacturer_list.html",
        },
        {"link": "counterparty:new-manufacturer", "template": "Forms/add.html"},
    ]
    for each in links:
        url = reverse(each.get("link"))
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, each.get("template"))


# detail_update_delete
@pytest.mark.django_db
def test_details_url(auto_login_user):  # noqa F811
    client, user = auto_login_user()
    links = [
        {
            "model": Manufacturer,
            "link": "counterparty:manufacturer-detail",
            "template": "counterparty/manufacturer_detail.html",
        },
        {
            "model": Manufacturer,
            "link": "counterparty:manufacturer-update",
            "template": "Forms/add.html",
        },
        {
            "model": Manufacturer,
            "link": "counterparty:manufacturer-delete",
            "template": "Forms/delete.html",
        },
    ]
    for each in links:
        model = each.get("model").objects.create(name="some_model")  # type: ignore[attr-defined]
        url = reverse(each.get("link"), kwargs={"pk": model.pk})  # type: ignore[arg-type]
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, each.get("template"))  # type: ignore[arg-type]
