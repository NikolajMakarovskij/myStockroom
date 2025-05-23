from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from workplace.models import Room, Workplace
from core.utils import DataMixin


class RoomListViewTest(TestCase, DataMixin):
    number_of_rooms = 149

    def setUp(self):
        self.client = Client()
        self.client.force_login(
            User.objects.get_or_create(
                username="user", is_superuser=True, is_staff=True
            )[0]
        )

    @classmethod
    def setUpTestData(cls):
        for room_num in range(cls.number_of_rooms):
            Room.objects.create(
                name="r %s" % room_num,
            )
        assert Room.objects.count() == 149

    def test_context_data_in_list(self):
        links = ["workplace:room_list", "workplace:room_search"]
        context_data = [
            {"data_key": "title", "data_value": "Кабинеты"},
            {"data_key": "searchlink", "data_value": "workplace:room_search"},
            {"data_key": "add", "data_value": "workplace:new-room"},
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
            {"data_key": "title", "data_value": "Кабинет"},
            {"data_key": "add", "data_value": "workplace:new-room"},
            {"data_key": "update", "data_value": "workplace:room-update"},
            {"data_key": "delete", "data_value": "workplace:room-delete"},
        ]
        Room.objects.create(
            name="room_detail",
        )
        model = Room.objects.get(
            name="room_detail",
        )
        resp = self.client.get(
            reverse("workplace:room-detail", kwargs={"pk": model.pk})
        )
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get("data_key") in resp.context)
            self.assertTrue(
                resp.context[each.get("data_key")] == each.get("data_value")  # type: ignore[index]
            )

    def test_pagination_is_paginate(self):
        links = ["workplace:room_list", "workplace:room_search"]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(len(resp.context["room_list"]) == self.paginate)

    def test_lists_all_room(self):
        links = ["workplace:room_list", "workplace:room_search"]
        for link in links:
            resp = self.client.get(
                reverse(link) + f"?page={self.number_of_rooms // self.paginate + 1}"
            )
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(
                len(resp.context["room_list"])
                == self.number_of_rooms
                - (self.number_of_rooms // self.paginate) * self.paginate
            )


class WorkplaceListViewTest(TestCase, DataMixin):
    number_of_workplaces = 149

    def setUp(self):
        self.client = Client()
        self.client.force_login(
            User.objects.get_or_create(
                username="user", is_superuser=True, is_staff=True
            )[0]
        )

    @classmethod
    def setUpTestData(cls):
        for Workplace_num in range(cls.number_of_workplaces):
            Workplace.objects.create(
                name="Christian %s" % Workplace_num,
            )
        assert Workplace.objects.count() == 149

    def test_context_data_in_list(self):
        links = ["workplace:workplace_list", "workplace:workplace_search"]
        context_data = [
            {"data_key": "title", "data_value": "Рабочие места"},
            {"data_key": "searchlink", "data_value": "workplace:workplace_search"},
            {"data_key": "add", "data_value": "workplace:new-workplace"},
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
            {"data_key": "title", "data_value": "Рабочее место"},
            {"data_key": "add", "data_value": "workplace:new-workplace"},
            {"data_key": "update", "data_value": "workplace:workplace-update"},
            {"data_key": "delete", "data_value": "workplace:workplace-delete"},
        ]
        Workplace.objects.create(
            name="room_detail",
        )
        model = Workplace.objects.get(
            name="room_detail",
        )
        resp = self.client.get(
            reverse("workplace:workplace-detail", kwargs={"pk": model.pk})
        )
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get("data_key") in resp.context)
            self.assertTrue(
                resp.context[each.get("data_key")] == each.get("data_value")  # type: ignore[index]
            )

    def test_pagination_is_paginate(self):
        links = ["workplace:workplace_list", "workplace:workplace_search"]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(len(resp.context["workplace_list"]) == self.paginate)

    def test_lists_all_workplaces(self):
        links = ["workplace:workplace_list", "workplace:workplace_search"]
        for link in links:
            resp = self.client.get(
                reverse(link)
                + f"?page={self.number_of_workplaces // self.paginate + 1}"
            )
            self.assertEqual(resp.status_code, 200)
            self.assertTrue("is_paginated" in resp.context)
            self.assertTrue(resp.context["is_paginated"] is True)
            self.assertTrue(
                len(resp.context["workplace_list"])
                == self.number_of_workplaces
                - (self.number_of_workplaces // self.paginate) * self.paginate
            )
