import pytest

from core.tests.login_test import auto_login_user  # noqa: F401


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
        "/api/stockroom/stock_dev_list/",
        "/api/stockroom/stock_dev_cat_list/",
        "/api/stockroom/history_dev_list/",
    ]
    post_links = [
        "/api/stockroom/add_to_stock_consumable/",
        "/api/stockroom/add_to_device_consumable/",
        "/api/stockroom/remove_from_stock_consumable/",
        "/api/stockroom/add_to_stock_accessories/",
        "/api/stockroom/add_to_device_accessories/",
        "/api/stockroom/remove_from_stock_accessories/",
        "/api/stockroom/add_to_stock_device/",
        "/api/stockroom/remove_from_stock_device/",
        "/api/stockroom/move_device/",
        "/api/stockroom/add_device_history/",
    ]
    for link in links:
        url = link
        response = client.get(url)
        assert response.status_code == 200

    for link in post_links:
        url = link
        response = client.get(url)
        assert response.status_code == 405
