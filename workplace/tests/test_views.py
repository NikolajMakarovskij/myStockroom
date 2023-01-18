from django.test import TestCase
from workplace.models import Room, Workplace
from django.urls import reverse

class RoomListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_rooms = 149
        for room_num in range(number_of_rooms):
            Room.objects.create(name='Christian %s' % room_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/workplace/room/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('workplace:room'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('workplace:room'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'workplace/room_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('workplace:room'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['room_list']) == 10)

    def test_lists_all_room(self):
        resp = self.client.get(reverse('workplace:room')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['room_list']) == 9)

class WorkplaceListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_workplaces = 149
        for Workplace_num in range(number_of_workplaces):
            Workplace.objects.create(name='Christian %s' % Workplace_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/workplace/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('workplace:workplace'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('workplace:workplace'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'workplace/workplace_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('workplace:workplace'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['workplace_list']) == 10)

    def test_lists_all_workplaces(self):
        resp = self.client.get(reverse('workplace:workplace')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['workplace_list']) == 9)