import pytest

from core.tests.login_test import auto_login_user  # noqa: F401
from counterparty.models import Manufacturer
from decommission.models import Decommission, Disposal
from stockroom.models.devices import StockDev
from workplace.models import Room, Workplace

from ..models import Device, DeviceCat


class TestDeviceEndpoints:
    endpoint = "/api/devices/device_crud/"

    @pytest.mark.django_db
    def test_device_list(self, auto_login_user):  # noqa: F811
        DeviceCat.objects.get_or_create(name="category_01", slug="category_01")
        Manufacturer.objects.get_or_create(name="manufacturer")
        Room.objects.get_or_create(name="01", building="01")
        room = Room.objects.get(name="01")
        Workplace.objects.get_or_create(name="01", room=room)
        Workplace.objects.get_or_create(name="02", room=room)
        Workplace.objects.get_or_create(name="03", room=room)
        workplace_1 = Workplace.objects.get(name="01")
        workplace_2 = Workplace.objects.get(name="02")
        workplace_3 = Workplace.objects.get(name="03")
        cat = DeviceCat.objects.get(name="category_01")
        man = Manufacturer.objects.get(name="manufacturer")
        Device.objects.bulk_create(
            [
                Device(
                    name="01", categories=cat, manufacturer=man, workplace=workplace_1
                ),
                Device(name="02", workplace=workplace_2),
                Device(name="03", workplace=workplace_3),
            ]
        )
        client, user = auto_login_user()
        response = client.get("/api/devices/device_list/")
        data = response.data
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]["name"] == "01"
        assert data[0]["categories"]["name"] == "category_01"
        assert data[0]["categories"]["slug"] == "category_01"
        assert data[0]["manufacturer"]["name"] == "manufacturer"
        assert data[1]["name"] == "02"
        assert data[2]["name"] == "03"

    @pytest.mark.django_db
    def test_device_list_2(self, auto_login_user):  # noqa: F811
        Room.objects.get_or_create(name="01", building="01")
        room = Room.objects.get(name="01")
        Workplace.objects.get_or_create(name="01", room=room)
        Workplace.objects.get_or_create(name="02", room=room)
        Workplace.objects.get_or_create(name="03", room=room)
        workplace_1 = Workplace.objects.get(name="01")
        workplace_2 = Workplace.objects.get(name="02")
        workplace_3 = Workplace.objects.get(name="03")
        Device.objects.bulk_create(
            [
                Device(name="01", workplace=workplace_1),
                Device(name="02", workplace=workplace_2),
                Device(name="03", workplace=workplace_3),
            ]
        )
        client, user = auto_login_user()
        response = client.get(self.endpoint)
        data = response.data
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]["name"] == "01"
        assert data[1]["name"] == "02"
        assert data[2]["name"] == "03"

    @pytest.mark.django_db
    def test_create(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        DeviceCat.objects.get_or_create(name="category_01", slug="category_01")
        Manufacturer.objects.get_or_create(name="manufacturer")
        cat = DeviceCat.objects.get(name="category_01")
        man = Manufacturer.objects.get(name="manufacturer")
        expected_json = {"name": "04", "categories": cat.id, "manufacturer": man.id}

        response = client.post(self.endpoint, data=expected_json, format="json")
        get_response = client.get("/api/devices/device_list/")
        data = get_response.data
        assert response.status_code == 200
        assert data[0]["name"] == "04"
        assert data[0]["categories"]["name"] == "category_01"
        assert data[0]["categories"]["slug"] == "category_01"
        assert data[0]["manufacturer"]["name"] == "manufacturer"

    @pytest.mark.django_db
    def test_create_no_valid(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        expected_json = {"name": "", "categories": "", "manufacturer": ""}

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_retrieve(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Device.objects.get_or_create(name="10")
        test_dev = Device.objects.get(name="10")
        url = f"{self.endpoint}{test_dev.id}/"

        response = client.get(url)

        assert response.status_code == 200
        assert response.data["name"] == "10"

    @pytest.mark.django_db
    def test_update(self, auto_login_user):  # noqa F811
        client, user = auto_login_user()
        Device.objects.get_or_create(name="10")
        test = Device.objects.get(name="10")
        expected_json = {
            "name": "test",
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
        Device.objects.get_or_create(name="10")
        test = Device.objects.get(name="10")
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
        Device.objects.get_or_create(name="10")
        test_dev = Device.objects.get(name="10")
        url = f"{self.endpoint}{test_dev.id}/"

        response = client.delete(url)

        assert response.status_code == 204
        assert Device.objects.all().count() == 0

    @pytest.mark.django_db
    def test_no_accounting(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Device.objects.get_or_create(name="10")
        response = client.get("/api/devices/device_list/")
        data = response.data
        assert data[0]["accounting"] == "Н"

    @pytest.mark.django_db
    def test_in_stock(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Device.objects.get_or_create(name="10")
        device = Device.objects.get(name="10")
        StockDev.objects.create(stock_model=device)
        response = client.get("/api/devices/device_list/")
        data = response.data
        assert data[0]["accounting"] == "Б"

    @pytest.mark.django_db
    def test_in_decommission(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Device.objects.get_or_create(name="10")
        device = Device.objects.get(name="10")
        Decommission.objects.create(stock_model=device)
        response = client.get("/api/devices/device_list/")
        data = response.data
        assert data[0]["accounting"] == "С"

    @pytest.mark.django_db
    def test_in_disposal(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Device.objects.get_or_create(name="10")
        device = Device.objects.get(name="10")
        Disposal.objects.create(stock_model=device)
        response = client.get("/api/devices/device_list/")
        data = response.data
        assert data[0]["accounting"] == "У"


class TestCategoryEndpoints:
    endpoint = "/api/devices/device_cat/"

    @pytest.mark.django_db
    def test_categories_list(self, auto_login_user):  # noqa: F811
        (DeviceCat.objects.get_or_create(name="category_01", slug="category_01"),)
        (DeviceCat.objects.get_or_create(name="category_02", slug="category_02"),)
        (DeviceCat.objects.get_or_create(name="category_03", slug="category_03"),)
        client, user = auto_login_user()
        response = client.get(self.endpoint)
        data = response.data
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]["name"] == "category_01"
        assert data[0]["slug"] == "category_01"
        assert data[1]["name"] == "category_02"
        assert data[1]["slug"] == "category_02"
        assert data[2]["name"] == "category_03"
        assert data[2]["slug"] == "category_03"

    @pytest.mark.django_db
    def test_create(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        expected_json = {
            "name": "04",
            "slug": "04",
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        get_response = client.get(self.endpoint)
        data = get_response.data
        assert response.status_code == 200
        assert data[0]["name"] == "04"
        assert data[0]["slug"] == "04"

    @pytest.mark.django_db
    def test_create_no_valid(self, auto_login_user):  # noqa F811
        client, user = auto_login_user()
        expected_json = {
            "name": "",
            "slug": "",
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_retrieve(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        DeviceCat.objects.get_or_create(name="10", slug="10")
        test_cat = DeviceCat.objects.get(name="10")
        url = f"{self.endpoint}{test_cat.id}/"

        response = client.get(url)

        assert response.status_code == 200
        assert response.data["name"] == "10"
        assert response.data["slug"] == "10"

    @pytest.mark.django_db
    def test_update(self, auto_login_user):  # noqa F811
        client, user = auto_login_user()
        DeviceCat.objects.get_or_create(name="category_01", slug="category_01")
        test_cat = DeviceCat.objects.get(name="category_01")
        expected_json = {
            "name": "test",
            "slug": "test",
        }
        url = f"{self.endpoint}{test_cat.id}/"
        response = client.put(
            url, data=expected_json, format="json", content_type="application/json"
        )

        get_response = client.get(f"{self.endpoint}{test_cat.id}/")
        data = get_response.data
        print(response)
        assert response.status_code == 200
        assert data["name"] == "test"
        assert data["slug"] == "test"

    @pytest.mark.django_db
    def test_update_no_valid(self, auto_login_user):  # noqa F811
        client, user = auto_login_user()
        DeviceCat.objects.get_or_create(name="category_01", slug="category_01")
        test_cat = DeviceCat.objects.get(name="category_01")
        expected_json = {
            "name": "",
            "slug": "",
        }
        url = f"{self.endpoint}{test_cat.id}/"
        response = client.put(
            url, data=expected_json, format="json", content_type="application/json"
        )
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_delete(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        DeviceCat.objects.get_or_create(name="10")
        test_cat = DeviceCat.objects.get(name="10")
        url = f"{self.endpoint}{test_cat.id}/"

        response = client.delete(url)

        assert response.status_code == 204
        assert DeviceCat.objects.all().count() == 0
