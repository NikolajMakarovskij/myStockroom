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


class manufacturerSearchViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_of_manufacturer = 149
        for manufacturer_num in range(number_of_manufacturer):
            Manufacturer.objects.create(name='Christian %s' % manufacturer_num,)

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('counterparty:manufacturer_search'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['manufacturer_list']) == 10)

    def test_lists_all_manufacturer(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('counterparty:manufacturer_search')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['manufacturer_list']) == 9)