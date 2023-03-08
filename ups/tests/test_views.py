from django.test import TestCase
from ..models import Ups, Cassette
from django.urls import reverse
import warnings


class upsViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_of_ups = 149
        for ups_num in range(number_of_ups):
            Ups.objects.create(name='Christian %s' % ups_num,)

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        links = ['ups:ups_list', 'ups:ups_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['ups_list']) == 10)

    def test_lists_all_ups(self):
        warnings.filterwarnings(action="ignore")
        links = ['ups:ups_list', 'ups:ups_search']
        for link in links:
            resp = self.client.get(reverse(link)+'?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['ups_list']) == 9)

class cassetteViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_of_cassette = 149
        for cassette_num in range(number_of_cassette):
            Cassette.objects.create(name='Christian %s' % cassette_num,)

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        links = ['ups:cassette_list', 'ups:cassette_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['cassette_list']) == 10)

    def test_lists_all_cassette(self):
        warnings.filterwarnings(action="ignore")
        links = ['ups:cassette_list', 'ups:cassette_search']
        for link in links:
            resp = self.client.get(reverse(link)+'?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['cassette_list']) == 9)



