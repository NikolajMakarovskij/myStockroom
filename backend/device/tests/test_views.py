from ..models import Device, DeviceCat
from counterparty.models import Manufacturer
from workplace.models import Workplace, Room
from stockroom.models.devices import StockDev
from decommission.models import Decommission, Disposal
import json
import pytest
from core.tests.test_login import auto_login_user  # noqa: F401


class TestDeviceEndpoints:
    endpoint = "/api/device/device/"

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
        response = client.get("/api/device/device_list/")
        data = json.loads(response.content)
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
        data = json.loads(response.content)
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
        get_response = client.get("/api/device/device_list/")
        data = json.loads(get_response.content)
        assert response.status_code == 200
        assert data[0]["name"] == "04"
        assert data[0]["categories"]["name"] == "category_01"
        assert data[0]["categories"]["slug"] == "category_01"
        assert data[0]["manufacturer"]["name"] == "manufacturer"

    @pytest.mark.django_db
    def test_retrieve(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Device.objects.get_or_create(name="10")
        test_dev = Device.objects.get(name="10")
        url = f"{self.endpoint}{test_dev.id}/"

        response = client.get(url)

        assert response.status_code == 200
        assert json.loads(response.content)["name"] == "10"

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
        response = client.get("/api/device/device_list/")
        data = json.loads(response.content)
        assert data[0]["accounting"] == "Н"

    @pytest.mark.django_db
    def test_in_stock(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Device.objects.get_or_create(name="10")
        device = Device.objects.get(name="10")
        StockDev.objects.create(stock_model=device)
        response = client.get("/api/device/device_list/")
        data = json.loads(response.content)
        assert data[0]["accounting"] == "Б"

    @pytest.mark.django_db
    def test_in_decommission(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Device.objects.get_or_create(name="10")
        device = Device.objects.get(name="10")
        Decommission.objects.create(stock_model=device)
        response = client.get("/api/device/device_list/")
        data = json.loads(response.content)
        assert data[0]["accounting"] == "С"

    @pytest.mark.django_db
    def test_in_disposal(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Device.objects.get_or_create(name="10")
        device = Device.objects.get(name="10")
        Disposal.objects.create(stock_model=device)
        response = client.get("/api/device/device_list/")
        data = json.loads(response.content)
        assert data[0]["accounting"] == "У"


class TestCategoryEndpoints:
    endpoint = "/api/device/device_cat/"

    @pytest.mark.django_db
    def test_categories_list(self, auto_login_user):  # noqa: F811
        (DeviceCat.objects.get_or_create(name="category_01", slug="category_01"),)
        (DeviceCat.objects.get_or_create(name="category_02", slug="category_02"),)
        (DeviceCat.objects.get_or_create(name="category_03", slug="category_03"),)
        client, user = auto_login_user()
        response = client.get(self.endpoint)
        data = json.loads(response.content)
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
        data = json.loads(get_response.content)
        assert response.status_code == 200
        assert data[0]["name"] == "04"
        assert data[0]["slug"] == "04"

    @pytest.mark.django_db
    def test_retrieve(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        DeviceCat.objects.get_or_create(name="10", slug="10")
        test_cat = DeviceCat.objects.get(name="10")
        url = f"{self.endpoint}{test_cat.id}/"

        response = client.get(url)

        assert response.status_code == 200
        assert json.loads(response.content)["name"] == "10"
        assert json.loads(response.content)["slug"] == "10"

    @pytest.mark.django_db
    def test_delete(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        DeviceCat.objects.get_or_create(name="10")
        test_cat = DeviceCat.objects.get(name="10")
        url = f"{self.endpoint}{test_cat.id}/"

        response = client.delete(url)

        assert response.status_code == 204
        assert DeviceCat.objects.all().count() == 0
