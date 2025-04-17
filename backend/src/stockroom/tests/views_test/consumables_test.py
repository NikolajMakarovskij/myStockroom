import pytest
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from accounting.models import Accounting
from consumables.models import Categories, Consumables
from core.tests.login_test import auto_login_user  # noqa: F401
from counterparty.models import Manufacturer

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
    def testing_stock_consumables_list(self, auto_login_user):  # noqa: F811
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


class HistoryStockViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(
            User.objects.get_or_create(
                username="user", is_superuser=True, is_staff=True
            )[0]
        )

    @classmethod
    def setUpTestData(cls):
        number_in_history = 149
        Consumables.objects.create(name="check_consumable")
        for history_num in range(number_in_history):
            History.objects.create(  # type: ignore[misc]
                stock_model="Christian %s" % history_num,
                stock_model_id=Consumables.objects.filter(name="check_consumable")
                .get()
                .id,
            )
        assert History.objects.count() == 149

    def test_context_data_in_consumption_list(self):
        links = [
            "stockroom:history_consumption_list",
            "stockroom:history_consumption_search",
        ]
        context_data = [
            {"data_key": "title", "data_value": "Расход расходников по годам"},
            {
                "data_key": "searchlink",
                "data_value": "stockroom:history_consumption_search",
            },
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get("data_key") in resp.context)
                self.assertTrue(
                    resp.context[each.get("data_key")] == each.get("data_value")  # type: ignore[index]
                )

    def test_pagination_is_ten_in_consumption(self):
        links = [
            "stockroom:history_consumption_list",
            "stockroom:history_consumption_search",
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)


class HistoryCategoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(
            User.objects.get_or_create(
                username="user", is_superuser=True, is_staff=True
            )[0]
        )

    @classmethod
    def setUpTestData(cls):
        number_in_stock = 149
        StockCat.objects.create(name="some_category", slug="some_category")
        Consumables.objects.create(name="check_consumable")
        for stocks_num in range(number_in_stock):
            History.objects.create(  # type: ignore[misc]
                stock_model="Christian %s" % stocks_num,
                categories=StockCat.objects.get(slug="some_category"),
                stock_model_id=Consumables.objects.filter(name="check_consumable")
                .get()
                .id,
            )
        assert History.objects.count() == 149
        assert StockCat.objects.count() == 1

    def test_context_data_in_consumption_category(self):
        context_data = [
            {"data_key": "title", "data_value": "Расход расходников по годам"},
            {
                "data_key": "searchlink",
                "data_value": "stockroom:history_consumption_search",
            },
        ]
        resp = self.client.get(
            reverse(
                "stockroom:history_consumption_category",
                kwargs={"category_slug": StockCat.objects.get(slug="some_category")},
            )
        )
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get("data_key") in resp.context)
            self.assertTrue(
                resp.context[each.get("data_key")] == each.get("data_value")  # type: ignore[index]
            )

    def test_pagination_is_ten_in_consumption(self):
        resp = self.client.get(
            reverse(
                "stockroom:history_consumption_category",
                kwargs={"category_slug": StockCat.objects.get(slug="some_category")},
            )
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("is_paginated" in resp.context)
        self.assertTrue(resp.context["is_paginated"] is True)
