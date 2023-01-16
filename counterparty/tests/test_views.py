from django.test import TestCase
from ..models import manufacturer
from django.urls import reverse


class manufacturerViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_manufacturer = 149
        for manufacturer_num in range(number_of_manufacturer):
            manufacturer.objects.create(name='Christian %s' % manufacturer_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/counterparty/manufacturer/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('counterparty:manufacturer'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('counterparty:manufacturer'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'counterparty/manufacturer_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('counterparty:manufacturer'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['manufacturer_list']) == 10)

    def test_lists_all_manufacturer(self):
        resp = self.client.get(reverse('counterparty:manufacturer')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['manufacturer_list']) == 9)

