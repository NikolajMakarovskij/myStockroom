import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.fixture
def auto_login_user(db, client):
    """_auto_login_user_ Auxiliary function for authorization

    Args:
        db (db):
        client (client):

    Returns:
        make_auto_login (func):
    """

    def make_auto_login(user=None):
        """_make_auto_login_ Autologin

        Args:
            user (user, optional): _description_.

        Returns:
            user (user): _user of db_
            client (client): _description_
        """
        client.force_login(
            User.objects.get_or_create(
                username="user", is_superuser=True, is_staff=True
            )[0]
        )
        return client, user

    return make_auto_login


@pytest.mark.django_db
def test_view_unauthorized(auto_login_user):
    """_test_view_unauthorized_ Testing unauthorized access

    Args:
        auto_login_user (_type_): _description_
    """
    client, user = auto_login_user()
    url = reverse("core:index")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_view_as_admin(admin_client):
    """_test_view_as_admin_ Testing admin access

    Args:
        admin_client (_type_): _description_
    """
    url = reverse("core:index")
    response = admin_client.get(url)
    assert response.status_code == 200
