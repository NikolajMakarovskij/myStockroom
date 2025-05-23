from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from ..models import Signature
from core.utils import DataMixin


class SignatureViewTest(TestCase, DataMixin):
    number_of_signature = 149

    def setUp(self):
        self.client = Client()
        self.client.force_login(
            User.objects.get_or_create(
                username="user", is_superuser=True, is_staff=True
            )[0]
        )

    @classmethod
    def setUpTestData(cls):
        for signature_num in range(cls.number_of_signature):
            Signature.objects.create(
                name="Christian %s" % signature_num,
            )
        assert Signature.objects.count() == 149

    def test_context_data_in_list(self):
        links = ["signature:signature_list", "signature:signature_search"]
        context_data = [
            {"data_key": "title", "data_value": "ЭЦП"},
            {"data_key": "searchlink", "data_value": "signature:signature_search"},
            {"data_key": "add", "data_value": "signature:new-signature"},
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
            {"data_key": "title", "data_value": "ЭЦП"},
            {"data_key": "add", "data_value": "signature:new-signature"},
            {"data_key": "update", "data_value": "signature:signature-update"},
            {"data_key": "delete", "data_value": "signature:signature-delete"},
        ]
        Signature.objects.create(
            name="Christian_detail",
        )
        model = Signature.objects.get(
            name="Christian_detail",
        )
        resp = self.client.get(
            reverse("signature:signature-detail", kwargs={"pk": model.pk})
        )
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get("data_key") in resp.context)
            self.assertTrue(
                resp.context[each.get("data_key")] == each.get("data_value")  # type: ignore[index]
            )

    def test_pagination_is_paginate(self):
        links = ["signature:signature_list", "signature:signature_search"]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(len(resp.context["signature_list"]) == self.paginate)

    def test_lists_all_signature(self):
        links = ["signature:signature_list", "signature:signature_search"]
        for link in links:
            resp = self.client.get(
                reverse(link) + f"?page={self.number_of_signature // self.paginate + 1}"
            )
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(
                len(resp.context["signature_list"])
                == self.number_of_signature
                - (self.number_of_signature // self.paginate) * self.paginate
            )
