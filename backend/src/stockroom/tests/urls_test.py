import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from core.tests.login_test import auto_login_user  # noqa F401
from stockroom.models.consumables import StockCat


# list and create
@pytest.mark.django_db
def test_list_url_exists_at_desired_location(auto_login_user):  # noqa F811
    client, user = auto_login_user()
    links = [
        "/stockroom/",
        "/stockroom/stockroom/",
        "/stockroom/stockroom/search",
        "/stockroom/history/consumption/",
        "/stockroom/history/consumption/search",
        "/stockroom/history/",
        "/stockroom/history/search",
        "/stockroom/accessories/",
        "/stockroom/accessories/search",
        "/stockroom/accessories/history/",
        "/stockroom/accessories/history/search",
        "/stockroom/accessories/consumption/",
        "/stockroom/accessories/consumption/search",
        "/stockroom/devices/",
        "/stockroom/devices/search",
        "/stockroom/devices/history/",
        "/stockroom/devices/history/search",
    ]
    for link in links:
        url = link
        response = client.get(url)
        assert response.status_code == 200


@pytest.mark.django_db
def test_list_uses_correct_url_nad_template(auto_login_user):  # noqa F811
    client, user = auto_login_user()
    links = [
        {"link": "stockroom:stock_index", "template": "stock/stock_index.html"},
        {"link": "stockroom:stock_list", "template": "stock/stock_list.html"},
        {"link": "stockroom:stock_search", "template": "stock/stock_list.html"},
        {"link": "stockroom:history_list", "template": "stock/history_list.html"},
        {"link": "stockroom:history_search", "template": "stock/history_list.html"},
        {
            "link": "stockroom:history_consumption_list",
            "template": "stock/history_consumption_list.html",
        },
        {
            "link": "stockroom:history_consumption_search",
            "template": "stock/history_consumption_list.html",
        },
        {"link": "stockroom:stock_acc_list", "template": "stock/stock_acc_list.html"},
        {"link": "stockroom:stock_acc_search", "template": "stock/stock_acc_list.html"},
        {
            "link": "stockroom:history_acc_list",
            "template": "stock/history_acc_list.html",
        },
        {
            "link": "stockroom:history_acc_search",
            "template": "stock/history_acc_list.html",
        },
        {
            "link": "stockroom:history_consumption_acc_list",
            "template": "stock/history_consumption_acc_list.html",
        },
        {
            "link": "stockroom:history_consumption_acc_list",
            "template": "stock/history_consumption_acc_list.html",
        },
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
def test_stockroom_category_url(auto_login_user):  # noqa F811
    client, user = auto_login_user()
    links = [
        {"link": "stockroom:category", "template": "stock/stock_list.html"},
        {"link": "stockroom:history_category", "template": "stock/history_list.html"},
        {
            "link": "stockroom:history_consumption_category",
            "template": "stock/history_consumption_list.html",
        },
        {
            "link": "stockroom:accessories_category",
            "template": "stock/stock_acc_list.html",
        },
        {
            "link": "stockroom:history_acc_category",
            "template": "stock/history_acc_list.html",
        },
        {
            "link": "stockroom:history_acc_consumption_category",
            "template": "stock/history_consumption_acc_list.html",
        },
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
