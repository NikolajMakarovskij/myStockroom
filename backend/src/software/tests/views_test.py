from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from software.models import Os, Software


class SoftwareViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(
            User.objects.get_or_create(
                username="user", is_superuser=True, is_staff=True
            )[0]
        )

    @classmethod
    def setUpTestData(cls):
        number_of_software = 149
        for software_num in range(number_of_software):
            Software.objects.create(
                name="Christian %s" % software_num,
            )
        assert Software.objects.count() == 149

    def test_context_data_in_list(self):
        links = ["software:software_list", "software:software_search"]
        context_data = [
            {"data_key": "title", "data_value": "Список ПО"},
            {"data_key": "searchlink", "data_value": "software:software_search"},
            {"data_key": "add", "data_value": "software:new-software"},
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
            {"data_key": "title", "data_value": "Программное обеспечение"},
            {"data_key": "add", "data_value": "software:new-software"},
            {"data_key": "update", "data_value": "software:software-update"},
            {"data_key": "delete", "data_value": "software:software-delete"},
        ]
        Software.objects.create(name="Christian_detail")
        model = Software.objects.get(name="Christian_detail")
        resp = self.client.get(
            reverse("software:software-detail", kwargs={"pk": model.pk})
        )
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get("data_key") in resp.context)
            self.assertTrue(
                resp.context[each.get("data_key")] == each.get("data_value")  # type: ignore[index]
            )

    def test_pagination_is_ten(self):
        links = ["software:software_list", "software:software_search"]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(len(resp.context["software_list"]) == 20)

    def test_lists_all_software(self):
        links = ["software:software_list", "software:software_search"]
        for link in links:
            resp = self.client.get(reverse(link) + "?page=8")
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(len(resp.context["software_list"]) == 9)


class OSViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(
            User.objects.get_or_create(
                username="user", is_superuser=True, is_staff=True
            )[0]
        )

    @classmethod
    def setUpTestData(cls):
        number_of_os = 149
        for OS_num in range(number_of_os):
            Os.objects.create(
                name="Christian %s" % OS_num,
            )
        assert Os.objects.count() == 149

    def test_context_data_in_list(self):
        links = ["software:OS_list", "software:OS_search"]
        context_data = [
            {"data_key": "title", "data_value": "Список ОС"},
            {"data_key": "searchlink", "data_value": "software:OS_search"},
            {"data_key": "add", "data_value": "software:new-OS"},
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
            {"data_key": "title", "data_value": "Операционная система"},
            {"data_key": "add", "data_value": "software:new-OS"},
            {"data_key": "update", "data_value": "software:OS-update"},
            {"data_key": "delete", "data_value": "software:OS-delete"},
        ]
        Os.objects.create(name="Christian_detail")
        model = Os.objects.get(name="Christian_detail")
        resp = self.client.get(reverse("software:OS-detail", kwargs={"pk": model.pk}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get("data_key") in resp.context)
            self.assertTrue(
                resp.context[each.get("data_key")] == each.get("data_value")  # type: ignore[index]
            )

    def test_pagination_is_ten(self):
        links = ["software:OS_list", "software:OS_search"]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(len(resp.context["os_list"]) == 20)

    def test_lists_all_OS(self):
        links = ["software:OS_list", "software:OS_search"]
        for link in links:
            resp = self.client.get(reverse(link) + "?page=8")
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(len(resp.context["os_list"]) == 9)
