from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from ..models import Accounting, Categories
from core.utils import DataMixin


# Расходники
class AccountingViewTest(TestCase, DataMixin):
    number_of_consumables = 149

    def setUp(self):
        self.client = Client()
        self.client.force_login(
            User.objects.get_or_create(
                username="user", is_superuser=True, is_staff=True
            )[0]
        )

    @classmethod
    def setUpTestData(cls):
        Categories.objects.create(name="some_category", slug="some_category")
        for consumables_num in range(cls.number_of_consumables):
            Accounting.objects.create(
                name="Christian %s" % consumables_num,
                categories=Categories.objects.get(slug="some_category"),
            )
        assert Accounting.objects.count() == 149

    def test_context_data_in_list(self):
        links = ["accounting:accounting_list", "accounting:accounting_search"]
        context_data = [
            {"data_key": "title", "data_value": "Баланс"},
            {"data_key": "searchlink", "data_value": "accounting:accounting_search"},
            {"data_key": "add", "data_value": "accounting:new-accounting"},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get("data_key") in resp.context)
                self.assertTrue(
                    resp.context[each.get("data_key")] == each.get("data_value")  # type: ignore[index]
                )

    def test_context_data_in_detail(self):
        context_data = [
            {"data_key": "title", "data_value": "Расходник"},
            {"data_key": "add", "data_value": "accounting:new-accounting"},
            {"data_key": "update", "data_value": "accounting:accounting-update"},
            {"data_key": "delete", "data_value": "accounting:accounting-delete"},
        ]
        Accounting.objects.create(
            name="Christian_detail",
        )
        model = Accounting.objects.get(
            name="Christian_detail",
        )
        resp = self.client.get(
            reverse("accounting:accounting-detail", kwargs={"pk": model.pk})
        )
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get("data_key") in resp.context)
            self.assertTrue(
                resp.context[each.get("data_key")] == each.get("data_value")  # type: ignore[index]
            )

    def test_pagination_is_paginate(self):
        links = ["accounting:accounting_list", "accounting:accounting_search"]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(len(resp.context["accounting_list"]) == self.paginate)

    def test_lists_all_accounting(self):
        links = ["accounting:accounting_list", "accounting:accounting_search"]
        for link in links:
            resp = self.client.get(
                reverse(link)
                + f"?page={self.number_of_consumables // self.paginate + 1}"
            )
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(
                len(resp.context["accounting_list"])
                == self.number_of_consumables
                - (self.number_of_consumables // self.paginate) * self.paginate
            )


class AccountingCategoryViewTest(TestCase, DataMixin):
    number_of_consumables = 149

    def setUp(self):
        self.client = Client()
        self.client.force_login(
            User.objects.get_or_create(
                username="user", is_superuser=True, is_staff=True
            )[0]
        )

    @classmethod
    def setUpTestData(cls):
        Categories.objects.create(name="some_category", slug="some_category")
        for consumables_num in range(cls.number_of_consumables):
            Accounting.objects.create(
                name="Christian %s" % consumables_num,
                categories=Categories.objects.get(slug="some_category"),
            )
        assert Accounting.objects.count() == 149
        assert Categories.objects.count() == 1

    def test_context_data_in_category(self):
        context_data = [
            {"data_key": "title", "data_value": "Баланс"},
            {"data_key": "searchlink", "data_value": "accounting:accounting_search"},
            {"data_key": "add", "data_value": "accounting:new-accounting"},
        ]
        resp = self.client.get(
            reverse(
                "accounting:category",
                kwargs={"category_slug": Categories.objects.get(slug="some_category")},
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
                "accounting:category",
                kwargs={"category_slug": Categories.objects.get(slug="some_category")},
            )
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("is_paginated" in resp.context)
        self.assertTrue(resp.context["is_paginated"] is True)
        self.assertTrue(len(resp.context["accounting_list"]) == self.paginate)

    def test_lists_all_categories(self):
        resp = self.client.get(
            reverse(
                "accounting:category",
                kwargs={"category_slug": Categories.objects.get(slug="some_category")},
            )
            + f"?page={self.number_of_consumables // self.paginate + 1}"
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("is_paginated" in resp.context)
        self.assertTrue(resp.context["is_paginated"] is True)
        self.assertTrue(
            len(resp.context["accounting_list"])
            == self.number_of_consumables
            - (self.number_of_consumables // self.paginate) * self.paginate
        )


# Комплектующие
class CategoriesViewTest(TestCase, DataMixin):
    number_of_accessories = 149

    def setUp(self):
        self.client = Client()
        self.client.force_login(
            User.objects.get_or_create(
                username="user", is_superuser=True, is_staff=True
            )[0]
        )

    @classmethod
    def setUpTestData(cls):
        for accessories_num in range(cls.number_of_accessories):
            Categories.objects.create(
                name="Christian %s" % accessories_num,
                slug="Christian %s" % accessories_num,
            )
        assert Categories.objects.count() == 149

    def test_context_data_in_list(self):
        links = ["accounting:categories_list", "accounting:categories_search"]
        context_data = [
            {"data_key": "title", "data_value": "Категории"},
            {"data_key": "searchlink", "data_value": "accounting:categories_search"},
            {"data_key": "add", "data_value": "accounting:new-categories"},
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
        links = ["accounting:categories_list", "accounting:categories_search"]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(len(resp.context["categories_list"]) == self.paginate)

    def test_lists_all_accessories(self):
        links = ["accounting:categories_list", "accounting:categories_search"]
        for link in links:
            resp = self.client.get(
                reverse(link)
                + f"?page={self.number_of_accessories // self.paginate + 1}"
            )
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(
                len(resp.context["categories_list"])
                == self.number_of_accessories
                - (self.number_of_accessories // self.paginate) * self.paginate
            )
