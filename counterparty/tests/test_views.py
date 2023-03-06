from django.test import TestCase
from ..models import Manufacturer
from django.urls import reverse
import warnings


class manufacturerViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_of_manufacturer = 149
        for manufacturer_num in range(number_of_manufacturer):
            Manufacturer.objects.create(name='Christian %s' % manufacturer_num,)

    def test_view_url_exists_at_desired_location(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get('/counterparty/manufacturer/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('counterparty:manufacturer_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('counterparty:manufacturer_list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'counterparty/manufacturer_list.html')

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('counterparty:manufacturer_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['manufacturer_list']) == 10)

    def test_lists_all_manufacturer(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('counterparty:manufacturer_list')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['manufacturer_list']) == 9)