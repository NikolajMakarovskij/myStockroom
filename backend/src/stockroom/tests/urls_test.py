import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from core.tests.login_test import auto_login_user  # noqa: F401
from stockroom.models.consumables import StockCat


# list and create
@pytest.mark.django_db
def test_list_url_exists_at_desired_location(auto_login_user):  # noqa: F811
    client, user = auto_login_user()
    links = [
        "/api/stockroom/",
        "/api/stockroom/stock_con_list/",
        "/api/stockroom/stock_con_cat_list/",
        "/api/stockroom/history_con_list/",
        "/api/stockroom/consumption_con_list/",
        "/api/stockroom/stock_acc_list/",
        "/api/stockroom/stock_acc_cat_list/",
        "/api/stockroom/history_acc_list/",
        "/api/stockroom/consumption_acc_list/",
        "/api/stockroom/devices/",
        "/api/stockroom/devices/search",
        "/api/stockroom/devices/history/",
        "/api/stockroom/devices/history/search",
    ]
    post_links = [
        "/api/stockroom/add_to_stock_consumable/",
        "/api/stockroom/add_to_device_consumable/",
        "/api/stockroom/remove_from_stock_consumable/",
        "/api/stockroom/add_to_stock_accessories/",
        "/api/stockroom/add_to_device_accessories/",
        "/api/stockroom/remove_from_stock_accessories/",
    ]
    for link in links:
        url = link
        response = client.get(url)
        assert response.status_code == 200

    for link in post_links:
        url = link
        response = client.get(url)
        assert response.status_code == 405


@pytest.mark.django_db
def test_list_uses_correct_url_nad_template(auto_login_user):  # noqa: F811
    client, user = auto_login_user()
    links = [
        {"link": "stockroom:stock_index", "template": "stock/stock_index.html"},
        {"link": "stockroom:stock_dev_list", "template": "stock/stock_dev_list.html"},
        {"link": "stockroom:stock_dev_search", "template": "stock/stock_dev_list.html"},
        {
            "link": "stockroom:history_dev_list",
            "template": "stock/history_dev_list.html",
        },
        {
            "link": "stockroom:history_dev_search",
            "template": "stock/history_dev_list.html",
        },
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
        {"link": "stockroom:devices_category", "template": "stock/stock_dev_list.html"},
        {
            "link": "stockroom:history_dev_category",
            "template": "stock/history_dev_list.html",
        },
    ]
    StockCat.objects.create(name="some_category", slug="some_category")
    for each in links:
        url = reverse(
            each.get("link"),
            kwargs={"category_slug": StockCat.objects.get(slug="some_category")},
        )
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, each.get("template"))
