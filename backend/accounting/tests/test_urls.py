import pytest
from core.tests.test_login import auto_login_user  # noqa F401


# Accounting
@pytest.mark.django_db
def test_list_url_exists_at_desired_location(auto_login_user):  # noqa F811
    client, user = auto_login_user()
    links = [
        "/api/accounting/accounting/",
        "/api/accounting/accounting_list/",
        "/api/accounting/accounting_category/",
    ]
    for link in links:
        url = link
        response = client.get(url)
        assert response.status_code == 200
