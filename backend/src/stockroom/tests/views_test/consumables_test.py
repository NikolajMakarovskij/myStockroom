from datetime import datetime

import pytest

from accounting.models import Accounting
from consumables.models import Categories, Consumables
from core.tests.login_test import auto_login_user  # noqa: F401
from counterparty.models import Manufacturer
from device.models import Device

from ...models.consumables import History, StockCat, Stockroom


# Consumables
class TestStockConsumablesCategoriesEndpoints:
    endpoint = "/api/stockroom/stock_con_cat_list/"

    @pytest.mark.django_db
    def testing_stock_consumables_list(self, auto_login_user):  # noqa: F811
        StockCat.objects.bulk_create(
            [
                StockCat(name="category_01", slug="category_01"),
                StockCat(name="category_02", slug="category_02"),
                StockCat(name="category_03", slug="category_03"),
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


class TestStockConsumablesEndpoints:
    endpoint = "/api/stockroom/stock_con_list/"

    @pytest.mark.django_db
    def testing_stock_consumables_list(self, auto_login_user):  # noqa: F811
        Categories.objects.get_or_create(name="category_01", slug="category_01")
        Manufacturer.objects.get_or_create(name="manufacturer")
        cat = Categories.objects.get(name="category_01")
        man = Manufacturer.objects.get(name="manufacturer")
        Consumables.objects.bulk_create(
            [
                Consumables(name="01", categories=cat, manufacturer=man, quantity=1),
                Consumables(name="02"),
                Consumables(name="03"),
            ]
        )
        Accounting.objects.get_or_create(
            name="category_01",
            quantity=2,
            consumable=Consumables.objects.get(name="01"),
        )
        StockCat.objects.get_or_create(name="some_category", slug="some_category")
        Stockroom.objects.bulk_create(
            [
                Stockroom(
                    stock_model=Consumables.objects.get(name="01"),
                    categories=StockCat.objects.get(name="some_category"),
                    dateAddToStock="2022-03-03",
                    dateInstall="2022-03-04",
                    rack=1,
                    shelf=2,
                ),
                Stockroom(stock_model=Consumables.objects.get(name="02")),
                Stockroom(stock_model=Consumables.objects.get(name="03")),
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
        assert data[0]["stock_model"]["difference"] == -1
        assert data[0]["categories"]["name"] == "some_category"
        assert data[0]["categories"]["slug"] == "some_category"
        assert data[0]["dateAddToStock"] == "2022-03-03"
        assert data[0]["dateInstall"] == "2022-03-04"
        assert data[0]["rack"] == 1
        assert data[0]["shelf"] == 2
        assert data[1]["stock_model"]["name"] == "02"
        assert data[2]["stock_model"]["name"] == "03"


class TestHistoryConsumablesEndpoints:
    endpoint = "/api/stockroom/history_con_list/"

    @pytest.mark.django_db
    def testing_history_consumables_list(self, auto_login_user):  # noqa: F811
        StockCat.objects.get_or_create(name="some_category", slug="some_category")
        History.objects.bulk_create(
            [
                History(
                    stock_model="category_01",
                    categories=StockCat.objects.get(name="some_category"),
                ),
                History(stock_model="category_02"),
                History(stock_model="category_03"),
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
    def testing_history_filtered_consumables_list(self, auto_login_user):  # noqa: F811
        StockCat.objects.get_or_create(name="some_category", slug="some_category")
        Consumables.objects.bulk_create(
            [
                Consumables(name="some_consumable_01"),
                Consumables(name="some_consumable_02"),
                Consumables(name="some_consumable_03"),
            ]
        )
        consumable = Consumables.objects.all()
        History.objects.bulk_create(
            [
                History(  # type: ignore[misc]
                    stock_model=consumable[0].name,
                    stock_model_id=consumable[0].id,
                    categories=StockCat.objects.get(name="some_category"),
                ),
                History(  # type: ignore[misc]
                    stock_model=consumable[1].name,
                    stock_model_id=consumable[1].id,
                ),
                History(  # type: ignore[misc]
                    stock_model=consumable[2].name,
                    stock_model_id=consumable[2].id,
                ),
            ]
        )
        client, user = auto_login_user()
        url = f"{self.endpoint}filter/{consumable[0].id}/"
        response = client.get(url)
        data = response.data
        assert response.status_code == 200
        assert len(data) == 1
        assert data[0]["stock_model"] == "some_consumable_01"


class TestConsumptionConsumablesEndpoints:
    endpoint = "/api/stockroom/consumption_con_list/"

    @pytest.mark.django_db
    def testing_consumption_consumables_list(self, auto_login_user):  # noqa: F811
        current_date = datetime.now()
        Categories.objects.get_or_create(name="some_category", slug="some_category")
        Consumables.objects.get_or_create(
            name="some_consumable",
            categories=Categories.objects.get(name="some_category"),
        )
        Device.objects.get_or_create(
            name="some_device",
        )
        Device.objects.get(
            name="some_device",
        ).consumable.add(Consumables.objects.get(name="some_consumable"))
        consumable = Consumables.objects.get(name="some_consumable")
        device = Device.objects.get(name="some_device")
        History.objects.bulk_create(
            [
                History(  # type: ignore[misc]
                    stock_model=consumable.name,
                    stock_model_id=consumable.id,
                    device=device.name,
                    deviceId=device.id,
                    quantity=4,
                    dateInstall=f"{(current_date.strftime('%Y-%m-%d'))}",
                    status="Расход",
                ),
                History(  # type: ignore[misc]
                    stock_model=consumable.name,
                    stock_model_id=consumable.id,
                    device=device.name,
                    deviceId=device.id,
                    quantity=4,
                    dateInstall=f"{int(current_date.strftime('%Y')) - 1}-{current_date.strftime('%m-%d')}",
                    status="Расход",
                ),
                History(  # type: ignore[misc]
                    stock_model=consumable.name,
                    stock_model_id=consumable.id,
                    device=device.name,
                    deviceId=device.id,
                    quantity=4,
                    dateInstall=f"{int(current_date.strftime('%Y')) - 2}-{current_date.strftime('%m-%d')}",
                    status="Расход",
                ),
            ]
        )
        client, user = auto_login_user()
        response = client.get(self.endpoint)
        data = response.data
        assert response.status_code == 200
        assert len(data) == 1
        assert data[0]["name"] == "some_consumable"
        assert data[0]["categories"]["name"] == "some_category"
        assert data[0]["categories"]["slug"] == "some_category"
        assert data[0]["device_name"] == "some_device"
        assert data[0]["device_count"] == 1
        assert data[0]["quantity_all"] == 12
        assert data[0]["quantity_last_year"] == 4
        assert data[0]["quantity_current_year"] == 4
        assert data[0]["quantity"] == 0
        assert data[0]["requirement"] == 12
