import pytest
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@pytest.fixture
def auto_login_user(db, client):
    def make_auto_login(user=None):
        client.force_login(
            User.objects.get_or_create(
                username="user", is_superuser=True, is_staff=True
            )[0]
        )
        return client, user

    return make_auto_login


# DRF
@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def get_or_create_token(db, create_user):
    user = create_user()
    token, _ = Token.objects.get_or_create(user=user)
    return token


@pytest.fixture
def api_client_with_credentials(db, create_user, api_client):
    user = create_user()
    api_client.force_authenticate(user=user)
    yield api_client
    api_client.force_authenticate(user=None)


"""
@pytest.mark.django_db
@pytest.mark.parametrize(
   'email, password, status_code', [
       (None, None, 400),
       (None, 'strong_pass', 400),
       ('user@example.com', None, 400),
       ('user@example.com', 'invalid_pass', 400),
       ('user@example.com', 'strong_pass', 201),
   ]
)
def test_login_data_validation(
   email, password, status_code, api_client
):
   url = reverse('login')
   data = {
       'email': email,
       'password': password
   }
   response = api_client.post(url, data=data)
   assert response.status_code == status_code

"""
