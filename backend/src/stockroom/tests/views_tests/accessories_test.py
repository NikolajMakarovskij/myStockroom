from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from consumables.models import Accessories
from stockroom.models.accessories import CategoryAcc, HistoryAcc, StockAcc


# Accessories
class StockAccViewTest(TestCase):
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
        for stocks_num in range(number_in_stock):
            cons = Accessories.objects.create(name="Christian %s" % stocks_num)
            StockAcc.objects.create(stock_model=cons)
        assert Accessories.objects.count() == 149

    def test_context_data_in_list(self):
        links = ["stockroom:stock_acc_list", "stockroom:stock_acc_search"]
        context_data = [
            {"data_key": "title", "data_value": "Склад комплектующих"},
            {"data_key": "searchlink", "data_value": "stockroom:stock_acc_search"},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get("data_key") in resp.context)
                self.assertTrue(
                    resp.context[each.get("data_key")] == each.get("data_value")  # type: ignore[index]
                )

    def test_pagination_is_ten(self):
        links = ["stockroom:stock_acc_list", "stockroom:stock_acc_search"]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(len(resp.context["stockacc_list"]) == 20)

    def test_lists_all_stockroom(self):
        links = ["stockroom:stock_acc_list", "stockroom:stock_acc_search"]
        for link in links:
            resp = self.client.get(reverse(link) + "?page=8")
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(len(resp.context["stockacc_list"]) == 9)


class StockroomAccCategoryViewTest(TestCase):
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
        CategoryAcc.objects.create(name="some_category", slug="some_category")
        for stocks_num in range(number_in_stock):
            cons = Accessories.objects.create(name="Christian %s" % stocks_num)
            StockAcc.objects.create(
                stock_model=cons,
                categories=CategoryAcc.objects.get(slug="some_category"),
            )
        assert StockAcc.objects.count() == 149
        assert CategoryAcc.objects.count() == 1

    def test_context_data_in_category(self):
        context_data = [
            {"data_key": "title", "data_value": "Склад комплектующих"},
            {"data_key": "searchlink", "data_value": "stockroom:stock_acc_search"},
        ]
        resp = self.client.get(
            reverse(
                "stockroom:accessories_category",
                kwargs={"category_slug": CategoryAcc.objects.get(slug="some_category")},
            )
        )
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get("data_key") in resp.context)
            self.assertTrue(
                resp.context[each.get("data_key")] == each.get("data_value")  # type: ignore[index]
            )

    def test_pagination_is_ten(self):
        resp = self.client.get(
            reverse(
                "stockroom:accessories_category",
                kwargs={"category_slug": CategoryAcc.objects.get(slug="some_category")},
            )
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("is_paginated" in resp.context)
        self.assertTrue(resp.context["is_paginated"] is True)
        self.assertTrue(len(resp.context["stockacc_list"]) == 20)

    def test_lists_all_stockroom_consumables(self):
        resp = self.client.get(
            reverse(
                "stockroom:accessories_category",
                kwargs={"category_slug": CategoryAcc.objects.get(slug="some_category")},
            )
            + "?page=8"
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("is_paginated" in resp.context)
        self.assertTrue(resp.context["is_paginated"] is True)
        self.assertTrue(len(resp.context["stockacc_list"]) == 9)


class HistoryAccStockViewTest(TestCase):
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
        Accessories.objects.create(name="check_consumable")
        for history_num in range(number_in_history):
            HistoryAcc.objects.create(  # type: ignore[misc]
                stock_model="Christian %s" % history_num,
                stock_model_id=Accessories.objects.filter(name="check_consumable")
                .get()
                .id,
            )
        assert HistoryAcc.objects.count() == 149

    def test_context_data_in_history_list(self):
        links = ["stockroom:history_acc_list", "stockroom:history_acc_search"]
        context_data = [
            {"data_key": "title", "data_value": "История комплектующих"},
            {"data_key": "searchlink", "data_value": "stockroom:history_acc_search"},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get("data_key") in resp.context)
                self.assertTrue(
                    resp.context[each.get("data_key")] == each.get("data_value")  # type: ignore[index]
                )

    def test_context_data_in_consumption_list(self):
        links = [
            "stockroom:history_consumption_acc_list",
            "stockroom:history_consumption_acc_search",
        ]
        context_data = [
            {"data_key": "title", "data_value": "Расход комплектующих по годам"},
            {
                "data_key": "searchlink",
                "data_value": "stockroom:history_consumption_acc_search",
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

    def test_pagination_is_ten_in_history_list(self):
        links = ["stockroom:history_acc_list", "stockroom:history_acc_search"]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(len(resp.context["historyacc_list"]) == 20)

    def test_pagination_is_ten_in_consumption_list(self):
        links = [
            "stockroom:history_consumption_acc_list",
            "stockroom:history_consumption_acc_search",
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)

    def test_lists_all_stockroom_in_history_list(self):
        links = ["stockroom:history_acc_list", "stockroom:history_acc_search"]
        for link in links:
            resp = self.client.get(reverse(link) + "?page=8")
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(len(resp.context["historyacc_list"]) == 9)


class HistoryAccCategoryViewTest(TestCase):
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
        CategoryAcc.objects.create(name="some_category", slug="some_category")
        Accessories.objects.create(name="check_consumable")
        for stocks_num in range(number_in_stock):
            HistoryAcc.objects.create(  # type: ignore[misc]
                stock_model="Christian %s" % stocks_num,
                categories=CategoryAcc.objects.get(slug="some_category"),
                stock_model_id=Accessories.objects.filter(name="check_consumable")
                .get()
                .id,
            )
        assert HistoryAcc.objects.count() == 149
        assert CategoryAcc.objects.count() == 1

    def test_context_data_in_history_category(self):
        context_data = [
            {"data_key": "title", "data_value": "История комплектующих"},
            {"data_key": "searchlink", "data_value": "stockroom:history_acc_search"},
        ]
        resp = self.client.get(
            reverse(
                "stockroom:history_acc_category",
                kwargs={"category_slug": CategoryAcc.objects.get(slug="some_category")},
            )
        )
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get("data_key") in resp.context)
            self.assertTrue(
                resp.context[each.get("data_key")] == each.get("data_value")  # type: ignore[index]
            )

    def test_context_data_in_consumption_category(self):
        context_data = [
            {"data_key": "title", "data_value": "Расход комплектующих по годам"},
            {
                "data_key": "searchlink",
                "data_value": "stockroom:history_consumption_acc_search",
            },
        ]
        resp = self.client.get(
            reverse(
                "stockroom:history_acc_consumption_category",
                kwargs={"category_slug": CategoryAcc.objects.get(slug="some_category")},
            )
        )
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get("data_key") in resp.context)
            self.assertTrue(
                resp.context[each.get("data_key")] == each.get("data_value")  # type: ignore[index]
            )

    def test_pagination_is_ten_in_history(self):
        resp = self.client.get(
            reverse(
                "stockroom:history_acc_category",
                kwargs={"category_slug": CategoryAcc.objects.get(slug="some_category")},
            )
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("is_paginated" in resp.context)
        self.assertTrue(resp.context["is_paginated"] is True)
        self.assertTrue(len(resp.context["historyacc_list"]) == 20)

    def test_pagination_is_ten_in_consumption(self):
        resp = self.client.get(
            reverse(
                "stockroom:history_acc_consumption_category",
                kwargs={"category_slug": CategoryAcc.objects.get(slug="some_category")},
            )
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("is_paginated" in resp.context)
        self.assertTrue(resp.context["is_paginated"] is True)

    def test_lists_all_stockroom_history_acc_consumables(self):
        resp = self.client.get(
            reverse(
                "stockroom:history_acc_category",
                kwargs={"category_slug": CategoryAcc.objects.get(slug="some_category")},
            )
            + "?page=8"
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("is_paginated" in resp.context)
        self.assertTrue(resp.context["is_paginated"] is True)
        self.assertTrue(len(resp.context["historyacc_list"]) == 9)
