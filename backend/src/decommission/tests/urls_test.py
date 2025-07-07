import pytest

from core.tests.login_test import auto_login_user  # noqa: F401


# list and create
@pytest.mark.django_db
def test_list_url_exists_at_desired_location(auto_login_user):  # noqa: F811
    client, user = auto_login_user()
    links = [
        "/api/decommission/decommission_list/",
        "/api/decommission/decommission_cat_list/",
        "/api/decommission/disposal_list/",
        "/api/decommission/disposal_cat_list/",
    ]
    post_links = [
        "/api/decommission/add_to_decommission/",
        "/api/decommission/remove_from_decommission/",
        "/api/decommission/add_to_disposal/",
        "/api/decommission/remove_from_disposal/",
    ]
    for link in links:
        url = link
        response = client.get(url)
        assert response.status_code == 200

    for link in post_links:
        url = link
        response = client.get(url)
        assert response.status_code == 405
