import pytest

from core.tests.login_test import auto_login_user  # noqa: F401

from ..models import Manufacturer

pytestmark = pytest.mark.django_db


class TestManufacturerEndpoints:
    endpoint = "/api/counterparty/manufacturer/"

    @pytest.mark.django_db
    def test_list(self, auto_login_user):  # noqa: F811
        Manufacturer.objects.bulk_create(
            [
                Manufacturer(name="01", country="Китай", production="Китай"),
                Manufacturer(name="02"),
                Manufacturer(name="03"),
            ]
        )
        client, user = auto_login_user()
        response = client.get(self.endpoint)
        data = response.data
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]["name"] == "01"
        assert data[0]["country"] == "Китай"
        assert data[0]["production"] == "Китай"
        assert data[1]["name"] == "02"
        assert data[2]["name"] == "03"

    @pytest.mark.django_db
    def test_create(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        expected_json = {"name": "04", "country": "Китай", "production": "Китай"}

        response = client.post(self.endpoint, data=expected_json, format="json")
        get_response = client.get(self.endpoint)
        data = get_response.data
        assert response.status_code == 200
        assert data[0]["name"] == "04"
        assert data[0]["country"] == "Китай"
        assert data[0]["production"] == "Китай"

    @pytest.mark.django_db
    def test_create_no_valid(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        expected_json = {"name": "", "country": "", "production": ""}

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_retrieve(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Manufacturer.objects.get_or_create(
            name="10", country="Китай", production="Китай"
        )
        test_manufacturer = Manufacturer.objects.get(name="10")
        url = f"{self.endpoint}{test_manufacturer.id}/"

        response = client.get(url)

        assert response.status_code == 200
        assert response.data["name"] == "10"
        assert response.data["country"] == "Китай"
        assert response.data["production"] == "Китай"

    @pytest.mark.django_db
    def test_update(self, auto_login_user):  # noqa F811
        client, user = auto_login_user()
        Manufacturer.objects.get_or_create(name="10")
        test = Manufacturer.objects.get(name="10")
        expected_json = {
            "name": "test",
            "country": "Китай",
            "production": "Китай",
        }
        url = f"{self.endpoint}{test.id}/"
        response = client.put(
            url, data=expected_json, format="json", content_type="application/json"
        )

        get_response = client.get(f"{self.endpoint}{test.id}/")
        data = get_response.data
        assert response.status_code == 200
        assert data["name"] == "test"

    @pytest.mark.django_db
    def test_update_no_valid(self, auto_login_user):  # noqa F811
        client, user = auto_login_user()
        Manufacturer.objects.get_or_create(name="10")
        test = Manufacturer.objects.get(name="10")
        expected_json = {
            "name": "",
        }
        url = f"{self.endpoint}{test.id}/"
        response = client.put(
            url, data=expected_json, format="json", content_type="application/json"
        )
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_delete(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Manufacturer.objects.get_or_create(
            name="10", country="Китай", production="Китай"
        )
        test_manufacturer = Manufacturer.objects.get(name="10")
        url = f"{self.endpoint}{test_manufacturer.id}/"

        response = client.delete(url)

        assert response.status_code == 204
        assert Manufacturer.objects.all().count() == 0
