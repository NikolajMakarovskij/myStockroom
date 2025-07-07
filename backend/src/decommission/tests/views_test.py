import pytest

from core.tests.login_test import auto_login_user  # noqa: F401
from counterparty.models import Manufacturer
from decommission.models import CategoryDec, CategoryDis, Decommission, Disposal
from device.models import Device, DeviceCat
from stockroom.models.devices import HistoryDev


# Decommission
class TestDecommissionCategoriesEndpoints:
    endpoint = "/api/decommission/decommission_cat_list/"

    @pytest.mark.django_db
    def testing_decommission_cat_list(self, auto_login_user):  # noqa: F811
        CategoryDec.objects.bulk_create(
            [
                CategoryDec(name="category_01", slug="category_01"),
                CategoryDec(name="category_02", slug="category_02"),
                CategoryDec(name="category_03", slug="category_03"),
            ]
        )
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


class TestDecommissionEndpoints:
    endpoint = "/api/decommission/decommission_list/"

    @pytest.mark.django_db
    def testing_decommission_list(self, auto_login_user):  # noqa: F811
        DeviceCat.objects.get_or_create(name="category_01", slug="category_01")
        Manufacturer.objects.get_or_create(name="manufacturer")
        cat = DeviceCat.objects.get(name="category_01")
        man = Manufacturer.objects.get(name="manufacturer")
        Device.objects.bulk_create(
            [
                Device(name="01", categories=cat, manufacturer=man, quantity=1),
                Device(name="02"),
                Device(name="03"),
            ]
        )
        CategoryDec.objects.get_or_create(name="some_category", slug="some_category")
        Decommission.objects.bulk_create(
            [
                Decommission(
                    stock_model=Device.objects.get(name="01"),
                    categories=CategoryDec.objects.get(name="some_category"),
                    date="2022-03-03",
                ),
                Decommission(stock_model=Device.objects.get(name="02")),
                Decommission(stock_model=Device.objects.get(name="03")),
            ]
        )
        client, user = auto_login_user()
        response = client.get(self.endpoint)
        data = response.data
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]["stock_model"]["name"] == "01"
        assert data[0]["stock_model"]["categories"]["name"] == "category_01"
        assert data[0]["stock_model"]["categories"]["slug"] == "category_01"
        assert data[0]["stock_model"]["manufacturer"]["name"] == "manufacturer"
        assert data[0]["categories"]["name"] == "some_category"
        assert data[0]["categories"]["slug"] == "some_category"
        assert data[0]["date"] == "2022-03-03"
        assert data[1]["stock_model"]["name"] == "02"
        assert data[2]["stock_model"]["name"] == "03"


class TestAddToDecommissionEndpoints:
    endpoint = "/api/decommission/add_to_decommission/"

    @pytest.mark.django_db
    def test_add_to_decommission(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Device.objects.get_or_create(name="some_device")
        device = Device.objects.get(name="some_device")
        device_id = device.id
        expected_json = {
            "device_id": device_id,
            "username": "username",
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 201

        decom = Decommission.objects.get(stock_model=device_id)
        history = HistoryDev.objects.get(stock_model="some_device")

        assert Decommission.objects.count() == 1
        assert HistoryDev.objects.count() == 1
        assert decom.stock_model.name == "some_device"
        assert history.user == "username"
        assert history.status == "Списание"
        assert history.note == ""

    @pytest.mark.django_db
    def test_no_valid(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        expected_json = {
            "device_id": "",
            "username": "",
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_bad_request(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        expected_json = {
            "device_id": "2c426393-51b3-4434-a90d-34e6ea1dfb01",
            "username": "data",
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 400
        assert response.data["error"] == "Device matching query does not exist."


class TestRemoveFromDecommissionEndpoints:
    endpoint = "/api/decommission/remove_from_decommission/"

    @pytest.mark.django_db
    def test_remove_from_decommission(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Device.objects.get_or_create(name="some_device")
        device = Device.objects.get(name="some_device")
        Decommission.objects.get_or_create(stock_model=device)
        expected_json = {"device_id": device.id, "username": "username"}

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 201

        history = HistoryDev.objects.get(stock_model="some_device")

        assert Decommission.objects.count() == 0
        assert HistoryDev.objects.count() == 1
        assert history.user == "username"
        assert history.quantity == 0
        assert history.status == "Удаление"
        assert history.note == ""

    @pytest.mark.django_db
    def test_no_valid(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        expected_json = {"device_id": "", "username": ""}

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 400


# Disposal
class TestDisposalCategoriesEndpoints:
    endpoint = "/api/decommission/disposal_cat_list/"

    @pytest.mark.django_db
    def testing_disposal_cat_list(self, auto_login_user):  # noqa: F811
        CategoryDis.objects.bulk_create(
            [
                CategoryDis(name="category_01", slug="category_01"),
                CategoryDis(name="category_02", slug="category_02"),
                CategoryDis(name="category_03", slug="category_03"),
            ]
        )
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


class TestDisposalEndpoints:
    endpoint = "/api/decommission/disposal_list/"

    @pytest.mark.django_db
    def testing_decommission_list(self, auto_login_user):  # noqa: F811
        DeviceCat.objects.get_or_create(name="category_01", slug="category_01")
        Manufacturer.objects.get_or_create(name="manufacturer")
        cat = DeviceCat.objects.get(name="category_01")
        man = Manufacturer.objects.get(name="manufacturer")
        Device.objects.bulk_create(
            [
                Device(name="01", categories=cat, manufacturer=man, quantity=1),
                Device(name="02"),
                Device(name="03"),
            ]
        )
        CategoryDis.objects.get_or_create(name="some_category", slug="some_category")
        Disposal.objects.bulk_create(
            [
                Disposal(
                    stock_model=Device.objects.get(name="01"),
                    categories=CategoryDis.objects.get(name="some_category"),
                    date="2022-03-03",
                ),
                Disposal(stock_model=Device.objects.get(name="02")),
                Disposal(stock_model=Device.objects.get(name="03")),
            ]
        )
        client, user = auto_login_user()
        response = client.get(self.endpoint)
        data = response.data
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]["stock_model"]["name"] == "01"
        assert data[0]["stock_model"]["categories"]["name"] == "category_01"
        assert data[0]["stock_model"]["categories"]["slug"] == "category_01"
        assert data[0]["stock_model"]["manufacturer"]["name"] == "manufacturer"
        assert data[0]["categories"]["name"] == "some_category"
        assert data[0]["categories"]["slug"] == "some_category"
        assert data[0]["date"] == "2022-03-03"
        assert data[1]["stock_model"]["name"] == "02"
        assert data[2]["stock_model"]["name"] == "03"


class TestAddToDisposalEndpoints:
    endpoint = "/api/decommission/add_to_disposal/"

    @pytest.mark.django_db
    def test_add_to_decommission(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Device.objects.get_or_create(name="some_device")
        device = Device.objects.get(name="some_device")
        device_id = device.id
        expected_json = {
            "device_id": device_id,
            "username": "username",
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 201

        disp = Disposal.objects.get(stock_model=device_id)
        history = HistoryDev.objects.get(stock_model="some_device")

        assert Disposal.objects.count() == 1
        assert HistoryDev.objects.count() == 1
        assert disp.stock_model.name == "some_device"
        assert history.user == "username"
        assert history.status == "Утилизация"
        assert history.note == ""

    @pytest.mark.django_db
    def test_no_valid(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        expected_json = {
            "device_id": "",
            "username": "",
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_bad_request(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        expected_json = {
            "device_id": "2c426393-51b3-4434-a90d-34e6ea1dfb01",
            "username": "data",
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 400
        assert response.data["error"] == "Device matching query does not exist."


class TestRemoveFromDisposalEndpoints:
    endpoint = "/api/decommission/remove_from_disposal/"

    @pytest.mark.django_db
    def test_remove_from_decommission(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Device.objects.get_or_create(name="some_device")
        device = Device.objects.get(name="some_device")
        Disposal.objects.get_or_create(stock_model=device)
        expected_json = {"device_id": device.id, "username": "username"}

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 201

        history = HistoryDev.objects.get(stock_model="some_device")

        assert Disposal.objects.count() == 0
        assert HistoryDev.objects.count() == 1
        assert history.user == "username"
        assert history.quantity == 0
        assert history.status == "Удаление"
        assert history.note == ""

    @pytest.mark.django_db
    def test_no_valid(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        expected_json = {"device_id": "", "username": ""}

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 400
