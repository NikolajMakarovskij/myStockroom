# Devices
import pytest

from core.tests.login_test import auto_login_user  # noqa: F401
from counterparty.models import Manufacturer
from device.models import Device, DeviceCat
from workplace.models import Workplace

from ...models.devices import CategoryDev, HistoryDev, StockDev


class TestStockDeviceCategoriesEndpoints:
    endpoint = "/api/stockroom/stock_dev_cat_list/"

    @pytest.mark.django_db
    def testing_stock_device_cat_list(self, auto_login_user):  # noqa: F811
        CategoryDev.objects.bulk_create(
            [
                CategoryDev(name="category_01", slug="category_01"),
                CategoryDev(name="category_02", slug="category_02"),
                CategoryDev(name="category_03", slug="category_03"),
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


class TestStockDeviceEndpoints:
    endpoint = "/api/stockroom/stock_dev_list/"

    @pytest.mark.django_db
    def testing_stock_device_list(self, auto_login_user):  # noqa: F811
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
        CategoryDev.objects.get_or_create(name="some_category", slug="some_category")
        StockDev.objects.bulk_create(
            [
                StockDev(
                    stock_model=Device.objects.get(name="01"),
                    categories=CategoryDev.objects.get(name="some_category"),
                    dateAddToStock="2022-03-03",
                    dateInstall="2022-03-04",
                    rack=1,
                    shelf=2,
                ),
                StockDev(stock_model=Device.objects.get(name="02")),
                StockDev(stock_model=Device.objects.get(name="03")),
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
        assert data[0]["dateAddToStock"] == "2022-03-03"
        assert data[0]["dateInstall"] == "2022-03-04"
        assert data[0]["rack"] == 1
        assert data[0]["shelf"] == 2
        assert data[1]["stock_model"]["name"] == "02"
        assert data[2]["stock_model"]["name"] == "03"


class TestHistoryDeviceEndpoints:
    endpoint = "/api/stockroom/history_dev_list/"

    @pytest.mark.django_db
    def testing_history_device_list(self, auto_login_user):  # noqa: F811
        CategoryDev.objects.get_or_create(name="some_category", slug="some_category")
        HistoryDev.objects.bulk_create(
            [
                HistoryDev(
                    stock_model="category_01",
                    categories=CategoryDev.objects.get(name="some_category"),
                ),
                HistoryDev(stock_model="category_02"),
                HistoryDev(stock_model="category_03"),
            ]
        )
        client, user = auto_login_user()
        response = client.get(self.endpoint)
        data = response.data
        assert response.status_code == 200
        assert len(data) == 3
        assert data[0]["stock_model"] == "category_01"
        assert data[0]["categories"]["name"] == "some_category"
        assert data[0]["categories"]["slug"] == "some_category"
        assert data[1]["stock_model"] == "category_02"
        assert data[2]["stock_model"] == "category_03"

    @pytest.mark.django_db
    def testing_history_filtered_device_list(self, auto_login_user):  # noqa: F811
        CategoryDev.objects.get_or_create(name="some_category", slug="some_category")
        Device.objects.bulk_create(
            [
                Device(name="some_device_01"),
                Device(name="some_device_02"),
                Device(name="some_device_03"),
            ]
        )
        HistoryDev.objects.bulk_create(
            [
                HistoryDev(  # type: ignore[misc]
                    stock_model=Device.objects.get(name="some_device_01").name,
                    stock_model_id=Device.objects.get(name="some_device_01").id,
                    categories=CategoryDev.objects.get(name="some_category"),
                ),
                HistoryDev(  # type: ignore[misc]
                    stock_model=Device.objects.get(name="some_device_02").name,
                    stock_model_id=Device.objects.get(name="some_device_02").id,
                ),
                HistoryDev(  # type: ignore[misc]
                    stock_model=Device.objects.get(name="some_device_02").name,
                    stock_model_id=Device.objects.get(name="some_device_02").id,
                ),
            ]
        )
        client, user = auto_login_user()
        device1 = Device.objects.get(name="some_device_01")
        url = f"{self.endpoint}filter/{device1.id}/"
        response = client.get(url)
        data = response.data
        assert response.status_code == 200
        assert len(data) == 1
        assert data[0]["stock_model"] == "some_device_01"

    @pytest.mark.django_db
    def testing_history_status_filtered_device_list(self, auto_login_user):  # noqa: F811
        CategoryDev.objects.get_or_create(name="some_category", slug="some_category")
        Device.objects.bulk_create(
            [
                Device(name="some_device_01"),
                Device(name="some_device_02"),
                Device(name="some_device_03"),
            ]
        )
        device_1 = Device.objects.filter(name="some_device_01")[0]
        device_2 = Device.objects.filter(name="some_device_02")[0]
        device_3 = Device.objects.filter(name="some_device_03")[0]
        HistoryDev.objects.bulk_create(
            [
                HistoryDev(  # type: ignore[misc]
                    stock_model=device_1.name,
                    stock_model_id=device_1.id,
                    categories=CategoryDev.objects.get(name="some_category"),
                    status="some_status",
                ),
                HistoryDev(  # type: ignore[misc]
                    stock_model=device_2.name,
                    stock_model_id=device_2.id,
                ),
                HistoryDev(  # type: ignore[misc]
                    stock_model=device_3.name,
                    stock_model_id=device_3.id,
                ),
            ]
        )
        client, user = auto_login_user()
        url = f"{self.endpoint}status/filter/some_status/"
        response = client.get(url)
        data = response.data
        assert response.status_code == 200
        assert len(data) == 1
        assert data[0]["stock_model"] == "some_device_01"
        assert data[0]["status"] == "some_status"


class TestAddToStockDeviceEndpoints:
    endpoint = "/api/stockroom/add_to_stock_device/"

    @pytest.mark.django_db
    def test_add_to_stock_device(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Device.objects.get_or_create(name="some_device")
        device = Device.objects.get(name="some_device")
        expected_json = {
            "model_id": device.id,
            "quantity": 1,
            "number_rack": 1,
            "number_shelf": 1,
            "username": "username",
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 201

        stock = StockDev.objects.get(stock_model=device.id)
        history = HistoryDev.objects.get(stock_model="some_device")

        assert StockDev.objects.count() == 1
        assert HistoryDev.objects.count() == 1
        assert stock.stock_model.name == "some_device"
        assert stock.stock_model.quantity == 1
        assert stock.rack == 1
        assert stock.shelf == 1
        assert history.user == "username"
        assert history.quantity == 1
        assert history.status == "Приход"
        assert history.note == ""

    @pytest.mark.django_db
    def test_no_valid(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        expected_json = {
            "model_id": "",
            "quantity": "",
            "number_rack": "",
            "number_shelf": "",
            "username": "",
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_bad_request(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        expected_json = {
            "model_id": "2c426393-51b3-4434-a90d-34e6ea1dfb01",
            "quantity": 1,
            "number_rack": 1,
            "number_shelf": 1,
            "username": "data",
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 400
        assert response.data["error"] == "Device matching query does not exist."


class TestMoveDeviceEndpoints:
    endpoint = "/api/stockroom/move_device/"

    @pytest.mark.django_db
    def test_move_device(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Device.objects.get_or_create(name="some_consumable")
        Workplace.objects.get_or_create(name="some_workplace")
        device = Device.objects.get(name="some_consumable")
        workplace = Workplace.objects.get(name="some_workplace")
        StockDev.objects.get_or_create(stock_model=device)
        expected_json = {
            "model_id": device.id,
            "workplace_id": workplace.id,
            "note": "some_note",
            "username": "username",
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 201

        history = HistoryDev.objects.get(stock_model="some_consumable")

        assert StockDev.objects.count() == 1
        assert HistoryDev.objects.count() == 1
        assert history.user == "username"
        assert history.quantity == 1
        assert history.status == "Перемещение на рабочее место some_workplace"
        assert history.note == "some_note"

    @pytest.mark.django_db
    def test_no_valid(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        expected_json = {
            "model_id": "",
            "workplace_id": "",
            "note": "",
            "username": "",
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_bad_request_device(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Workplace.objects.get_or_create(name="some_consumable")
        workplace = Workplace.objects.get(name="some_consumable")
        expected_json = {
            "model_id": "2c426393-51b3-4434-a90d-34e6ea1dfb01",
            "workplace_id": workplace.id,
            "note": "some_note",
            "username": "username",
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 400
        assert response.data["error"] == "Device matching query does not exist."

    @pytest.mark.django_db
    def test_bad_request_workplace(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Device.objects.get_or_create(name="some_consumable")
        device = Device.objects.get(name="some_consumable")
        expected_json = {
            "model_id": device.id,
            "workplace_id": "2c426393-51b3-4434-a90d-34e6ea1dfb01",
            "note": "some_note",
            "username": "username",
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 400
        assert response.data["error"] == "Workplace matching query does not exist."


class TestAddToDeviceHistoryEndpoints:
    endpoint = "/api/stockroom/add_device_history/"

    @pytest.mark.django_db
    def test_add_to_device_history(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Device.objects.get_or_create(name="some_device")
        device = Device.objects.get(name="some_device")
        StockDev.objects.get_or_create(stock_model=device)
        expected_json = {
            "model_id": device.id,
            "status_choice": "some_status",
            "note": "some_note",
            "username": "username",
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        print(response.data)
        assert response.status_code == 201

        history = HistoryDev.objects.get(stock_model="some_device")

        assert StockDev.objects.count() == 1
        assert HistoryDev.objects.count() == 1
        assert history.user == "username"
        assert history.quantity == 0
        assert history.status == "some_status"
        assert history.note == "some_note"

    @pytest.mark.django_db
    def test_no_valid(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        expected_json = {
            "model_id": "",
            "workplace_id": "",
            "note": "",
            "username": "",
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_bad_request(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        expected_json = {
            "model_id": "2c426393-51b3-4434-a90d-34e6ea1dfb01",
            "status_choice": "some_status",
            "note": "some_note",
            "username": "username",
        }

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 400
        assert response.data["error"] == "Device matching query does not exist."


class TestRemoveFromStockDeviceEndpoints:
    endpoint = "/api/stockroom/remove_from_stock_device/"

    @pytest.mark.django_db
    def test_remove_from_stock_device(self, auto_login_user):  # noqa: F811
        client, user = auto_login_user()
        Device.objects.get_or_create(name="some_device")
        device = Device.objects.get(name="some_device")
        StockDev.objects.get_or_create(stock_model=device)
        expected_json = {"model_id": device.id, "username": "username"}

        response = client.post(self.endpoint, data=expected_json, format="json")
        assert response.status_code == 201

        history = HistoryDev.objects.get(stock_model="some_device")

        assert StockDev.objects.count() == 0
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
