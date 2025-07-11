import pytest

from core.tests.login_test import auto_login_user  # noqa: F401


# list and create
@pytest.mark.django_db
def test_list_url_exists_at_desired_location(auto_login_user):  # noqa: F811
    client, user = auto_login_user()
    links = [
        "/api/employee/employee/",
        "/api/employee/post/",
        "/api/employee/departament/",
        "/api/employee/post_list/",
        "/api/employee/employee_list/",
    ]
    for link in links:
        url = link
        response = client.get(url)
        assert response.status_code == 200
