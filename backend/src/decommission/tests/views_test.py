from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from decommission.models import CategoryDec, CategoryDis, Decommission, Disposal
from device.models import Device
from core.utils import DataMixin


# Decommission
class DecommissionViewTest(TestCase, DataMixin):
    number_in_stock = 149

    def setUp(self):
        self.client = Client()
        self.client.force_login(
            User.objects.get_or_create(
                username="user", is_superuser=True, is_staff=True
            )[0]
        )

    @classmethod
    def setUpTestData(cls):
        for stocks_num in range(cls.number_in_stock):
            dev = Device.objects.create(name="Christian %s" % stocks_num)
            Decommission.objects.create(stock_model=dev)
        assert Decommission.objects.count() == 149

    def test_context_data_in_list(self):
        links = ["decommission:decom_list", "decommission:decom_search"]
        context_data = [
            {"data_key": "title", "data_value": "Списание устройств"},
            {"data_key": "searchlink", "data_value": "decommission:decom_search"},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get("data_key") in resp.context)
                self.assertTrue(
                    resp.context[each.get("data_key")] == each.get("data_value")  # type: ignore[index]
                )

    def test_pagination_is_paginate(self):
        links = ["decommission:decom_list", "decommission:decom_search"]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(len(resp.context["decommission_list"]) == self.paginate)

    def test_lists_all_decommission(self):
        links = ["decommission:decom_list", "decommission:decom_search"]
        for link in links:
            resp = self.client.get(
                reverse(link) + f"?page={self.number_in_stock // self.paginate + 1}"
            )
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(
                len(resp.context["decommission_list"])
                == self.number_in_stock
                - (self.number_in_stock // self.paginate) * self.paginate
            )


class DecommissionCategoryViewTest(TestCase, DataMixin):
    number_in_stock = 149

    def setUp(self):
        self.client = Client()
        self.client.force_login(
            User.objects.get_or_create(
                username="user", is_superuser=True, is_staff=True
            )[0]
        )

    @classmethod
    def setUpTestData(cls):
        CategoryDec.objects.create(name="some_category", slug="some_category")
        for stocks_num in range(cls.number_in_stock):
            dev = Device.objects.create(name="Christian %s" % stocks_num)
            Decommission.objects.create(
                stock_model=dev,
                categories=CategoryDec.objects.get(slug="some_category"),
            )
        assert Decommission.objects.count() == 149
        assert CategoryDec.objects.count() == 1

    def test_context_data_in_category(self):
        context_data = [
            {"data_key": "title", "data_value": "Списание устройств"},
            {"data_key": "searchlink", "data_value": "decommission:decom_search"},
        ]
        resp = self.client.get(
            reverse(
                "decommission:decom_category",
                kwargs={"category_slug": CategoryDec.objects.get(slug="some_category")},
            )
        )
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get("data_key") in resp.context)
            self.assertTrue(
                resp.context[each.get("data_key")] == each.get("data_value")  # type: ignore[index]
            )

    def test_pagination_is_paginate(self):
        resp = self.client.get(
            reverse(
                "decommission:decom_category",
                kwargs={"category_slug": CategoryDec.objects.get(slug="some_category")},
            )
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("is_paginated" in resp.context)
        self.assertTrue(resp.context["is_paginated"] is True)
        self.assertTrue(len(resp.context["decommission_list"]) == self.paginate)

    def test_lists_all_stockroom_consumables(self):
        resp = self.client.get(
            reverse(
                "decommission:decom_category",
                kwargs={"category_slug": CategoryDec.objects.get(slug="some_category")},
            )
            + f"?page={self.number_in_stock // self.paginate + 1}"
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("is_paginated" in resp.context)
        self.assertTrue(resp.context["is_paginated"] is True)
        self.assertTrue(
            len(resp.context["decommission_list"])
            == self.number_in_stock
            - (self.number_in_stock // self.paginate) * self.paginate
        )


# Disposal
class DisposalViewTest(TestCase, DataMixin):
    number_in_stock = 149

    def setUp(self):
        self.client = Client()
        self.client.force_login(
            User.objects.get_or_create(
                username="user", is_superuser=True, is_staff=True
            )[0]
        )

    @classmethod
    def setUpTestData(cls):
        for stocks_num in range(cls.number_in_stock):
            dev = Device.objects.create(name="Christian %s" % stocks_num)
            Disposal.objects.create(stock_model=dev)
        assert Disposal.objects.count() == 149

    def test_context_data_in_list(self):
        links = ["decommission:disp_list", "decommission:disp_search"]
        context_data = [
            {"data_key": "title", "data_value": "Утилизация устройств"},
            {"data_key": "searchlink", "data_value": "decommission:disp_search"},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get("data_key") in resp.context)
                self.assertTrue(
                    resp.context[each.get("data_key")] == each.get("data_value")  # type: ignore[index]
                )

    def test_pagination_is_paginate(self):
        links = ["decommission:disp_list", "decommission:disp_search"]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(len(resp.context["disposal_list"]) == self.paginate)

    def test_lists_all_disposal(self):
        links = ["decommission:disp_list", "decommission:disp_search"]
        for link in links:
            resp = self.client.get(
                reverse(link) + f"?page={self.number_in_stock // self.paginate + 1}"
            )
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(
                len(resp.context["disposal_list"])
                == self.number_in_stock
                - (self.number_in_stock // self.paginate) * self.paginate
            )


class DisposalCategoryViewTest(TestCase, DataMixin):
    number_in_stock = 149

    def setUp(self):
        self.client = Client()
        self.client.force_login(
            User.objects.get_or_create(
                username="user", is_superuser=True, is_staff=True
            )[0]
        )

    @classmethod
    def setUpTestData(cls):
        CategoryDis.objects.create(name="some_category", slug="some_category")
        for stocks_num in range(cls.number_in_stock):
            dev = Device.objects.create(name="Christian %s" % stocks_num)
            Disposal.objects.create(
                stock_model=dev,
                categories=CategoryDis.objects.get(slug="some_category"),
            )
        assert Disposal.objects.count() == 149
        assert CategoryDis.objects.count() == 1

    def test_context_data_in_category(self):
        context_data = [
            {"data_key": "title", "data_value": "Утилизация устройств"},
            {"data_key": "searchlink", "data_value": "decommission:disp_search"},
        ]
        resp = self.client.get(
            reverse(
                "decommission:disp_category",
                kwargs={"category_slug": CategoryDis.objects.get(slug="some_category")},
            )
        )
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get("data_key") in resp.context)
            self.assertTrue(
                resp.context[each.get("data_key")] == each.get("data_value")  # type: ignore[index]
            )

    def test_pagination_is_paginate(self):
        resp = self.client.get(
            reverse(
                "decommission:disp_category",
                kwargs={"category_slug": CategoryDis.objects.get(slug="some_category")},
            )
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("is_paginated" in resp.context)
        self.assertTrue(resp.context["is_paginated"] is True)
        self.assertTrue(len(resp.context["disposal_list"]) == self.paginate)

    def test_lists_all_disposal_categories(self):
        resp = self.client.get(
            reverse(
                "decommission:disp_category",
                kwargs={"category_slug": CategoryDis.objects.get(slug="some_category")},
            )
            + f"?page={self.number_in_stock // self.paginate + 1}"
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("is_paginated" in resp.context)
        self.assertTrue(resp.context["is_paginated"] is True)
        self.assertTrue(
            len(resp.context["disposal_list"])
            == self.number_in_stock
            - (self.number_in_stock // self.paginate) * self.paginate
        )
