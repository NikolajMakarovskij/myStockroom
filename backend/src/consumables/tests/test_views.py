from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from ..models import AccCat, Accessories, Categories, Consumables


# Расходники
class ConsumablesViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(
            User.objects.get_or_create(
                username="user", is_superuser=True, is_staff=True
            )[0]
        )

    @classmethod
    def setUpTestData(cls):
        number_of_consumables = 149
        Categories.objects.create(name="some_category", slug="some_category")
        for consumables_num in range(number_of_consumables):
            Consumables.objects.create(
                name="Christian %s" % consumables_num,
                categories=Categories.objects.get(slug="some_category"),
            )
        assert Consumables.objects.count() == 149

    def test_context_data_in_list(self):
        links = ["consumables:consumables_list", "consumables:consumables_search"]
        context_data = [
            {"data_key": "title", "data_value": "Расходники"},
            {"data_key": "searchlink", "data_value": "consumables:consumables_search"},
            {"data_key": "add", "data_value": "consumables:new-consumables"},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get("data_key") in resp.context)
                self.assertTrue(
                    resp.context[each.get("data_key")] == each.get("data_value")
                )

    def test_context_data_in_detail(self):
        context_data = [
            {"data_key": "title", "data_value": "Расходник"},
            {"data_key": "add", "data_value": "consumables:new-consumables"},
            {"data_key": "update", "data_value": "consumables:consumables-update"},
            {"data_key": "delete", "data_value": "consumables:consumables-delete"},
        ]
        Consumables.objects.create(
            name="Christian_detail",
        )
        model = Consumables.objects.get(
            name="Christian_detail",
        )
        resp = self.client.get(
            reverse("consumables:consumables-detail", kwargs={"pk": model.pk})
        )
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get("data_key") in resp.context)
            self.assertTrue(
                resp.context[each.get("data_key")] == each.get("data_value")
            )

    def test_pagination_is_ten(self):
        links = ["consumables:consumables_list", "consumables:consumables_search"]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(len(resp.context["consumables_list"]) == 20)

    def test_lists_all_consumables(self):
        links = ["consumables:consumables_list", "consumables:consumables_search"]
        for link in links:
            resp = self.client.get(reverse(link) + "?page=8")
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(len(resp.context["consumables_list"]) == 9)


class ConsumablesCategoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(
            User.objects.get_or_create(
                username="user", is_superuser=True, is_staff=True
            )[0]
        )

    @classmethod
    def setUpTestData(cls):
        number_of_consumables = 149
        Categories.objects.create(name="some_category", slug="some_category")
        for consumables_num in range(number_of_consumables):
            Consumables.objects.create(
                name="Christian %s" % consumables_num,
                categories=Categories.objects.get(slug="some_category"),
            )
        assert Consumables.objects.count() == 149
        assert Categories.objects.count() == 1

    def test_context_data_in_category(self):
        context_data = [
            {"data_key": "title", "data_value": "Расходники"},
            {"data_key": "searchlink", "data_value": "consumables:consumables_search"},
            {"data_key": "add", "data_value": "consumables:new-consumables"},
        ]
        resp = self.client.get(
            reverse(
                "consumables:category",
                kwargs={"category_slug": Categories.objects.get(slug="some_category")},
            )
        )
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get("data_key") in resp.context)
            self.assertTrue(
                resp.context[each.get("data_key")] == each.get("data_value")
            )

    def test_pagination_is_ten(self):
        resp = self.client.get(
            reverse(
                "consumables:category",
                kwargs={"category_slug": Categories.objects.get(slug="some_category")},
            )
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("is_paginated" in resp.context)
        self.assertTrue(resp.context["is_paginated"] is True)
        self.assertTrue(len(resp.context["consumables_list"]) == 20)

    def test_lists_all_categories(self):
        resp = self.client.get(
            reverse(
                "consumables:category",
                kwargs={"category_slug": Categories.objects.get(slug="some_category")},
            )
            + "?page=8"
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("is_paginated" in resp.context)
        self.assertTrue(resp.context["is_paginated"] is True)
        self.assertTrue(len(resp.context["consumables_list"]) == 9)


# Комплектующие
class AccessoriesViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(
            User.objects.get_or_create(
                username="user", is_superuser=True, is_staff=True
            )[0]
        )

    @classmethod
    def setUpTestData(cls):
        number_of_accessories = 149
        AccCat.objects.create(name="some_category", slug="some_category")
        for accessories_num in range(number_of_accessories):
            Accessories.objects.create(
                name="Christian %s" % accessories_num,
                categories=AccCat.objects.get(slug="some_category"),
            )
        assert Accessories.objects.count() == 149

    def test_context_data_in_list(self):
        links = ["consumables:accessories_list", "consumables:accessories_search"]
        context_data = [
            {"data_key": "title", "data_value": "Комплектующие"},
            {"data_key": "searchlink", "data_value": "consumables:accessories_search"},
            {"data_key": "add", "data_value": "consumables:new-accessories"},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get("data_key") in resp.context)
                self.assertTrue(
                    resp.context[each.get("data_key")] == each.get("data_value")
                )

    def test_context_data_in_detail(self):
        context_data = [
            {"data_key": "add", "data_value": "consumables:new-accessories"},
            {"data_key": "update", "data_value": "consumables:accessories-update"},
            {"data_key": "delete", "data_value": "consumables:accessories-delete"},
        ]
        Accessories.objects.create(name="Christian-detail")
        model = Accessories.objects.get(
            name="Christian-detail",
        )
        resp = self.client.get(
            reverse("consumables:accessories-detail", kwargs={"pk": model.pk})
        )
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get("data_key") in resp.context)
            self.assertTrue(
                resp.context[each.get("data_key")] == each.get("data_value")
            )

    def test_pagination_is_ten(self):
        links = ["consumables:accessories_list", "consumables:accessories_search"]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(len(resp.context["accessories_list"]) == 20)

    def test_lists_all_accessories(self):
        links = ["consumables:accessories_list", "consumables:accessories_search"]
        for link in links:
            resp = self.client.get(reverse(link) + "?page=8")
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(len(resp.context["accessories_list"]) == 9)


class AccessoriesCategoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(
            User.objects.get_or_create(
                username="user", is_superuser=True, is_staff=True
            )[0]
        )

    @classmethod
    def setUpTestData(cls):
        number_of_accessories = 149
        AccCat.objects.create(name="some_category", slug="some_category")
        for accessories_num in range(number_of_accessories):
            Accessories.objects.create(
                name="Christian %s" % accessories_num,
                categories=AccCat.objects.get(slug="some_category"),
            )
        assert Accessories.objects.count() == 149
        assert AccCat.objects.count() == 1

    def test_context_data_in_category(self):
        context_data = [
            {"data_key": "title", "data_value": "Комплектующие"},
            {"data_key": "searchlink", "data_value": "consumables:accessories_search"},
            {"data_key": "add", "data_value": "consumables:new-accessories"},
        ]
        resp = self.client.get(
            reverse(
                "consumables:category_accessories",
                kwargs={"category_slug": AccCat.objects.get(slug="some_category")},
            )
        )
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get("data_key") in resp.context)
            self.assertTrue(
                resp.context[each.get("data_key")] == each.get("data_value")
            )

    def test_pagination_is_ten(self):
        resp = self.client.get(
            reverse(
                "consumables:category_accessories",
                kwargs={"category_slug": AccCat.objects.get(slug="some_category")},
            )
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("is_paginated" in resp.context)
        self.assertTrue(resp.context["is_paginated"] is True)
        self.assertTrue(len(resp.context["accessories_list"]) == 20)

    def test_lists_all_categories(self):
        resp = self.client.get(
            reverse(
                "consumables:category_accessories",
                kwargs={"category_slug": AccCat.objects.get(slug="some_category")},
            )
            + "?page=8"
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("is_paginated" in resp.context)
        self.assertTrue(resp.context["is_paginated"] is True)
        self.assertTrue(len(resp.context["accessories_list"]) == 9)
