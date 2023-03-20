from django.test import TestCase
from ..models import Ups, Cassette
from django.urls import reverse
import warnings


class upsViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_ups = 149
        for ups_num in range(number_of_ups):
            Ups.objects.create(name='Christian %s' % ups_num,)
        assert Ups.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['ups:ups_list', 'ups:ups_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'ИБП'},
            {'data_key': 'searchlink', 'data_value': 'ups:ups_search'},
            {'data_key': 'add', 'data_value': 'ups:new-ups'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_context_data_in_detail(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'ИБП'},
            {'data_key': 'add', 'data_value': 'ups:new-ups'},
            {'data_key': 'update', 'data_value': 'ups:ups-update'},
            {'data_key': 'delete', 'data_value': 'ups:ups-delete'},
        ]
        Ups.objects.create(name='Christian_detail',)
        model = Ups.objects.get(name='Christian_detail',)
        resp = self.client.get(reverse('ups:ups-detail', kwargs={"pk": model.pk}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        links = ['ups:ups_list', 'ups:ups_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['ups_list']) == 10)

    def test_lists_all_ups(self):
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
        number_of_cassette = 149
        for cassette_num in range(number_of_cassette):
            Cassette.objects.create(name='Christian %s' % cassette_num,)
        assert Cassette.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['ups:cassette_list', 'ups:cassette_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'Кассеты'},
            {'data_key': 'searchlink', 'data_value': 'ups:cassette_search'},
            {'data_key': 'add', 'data_value': 'ups:new-cassette'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_context_data_in_detail(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'Кассета'},
            {'data_key': 'add', 'data_value': 'ups:new-cassette'},
            {'data_key': 'update', 'data_value': 'ups:cassette-update'},
            {'data_key': 'delete', 'data_value': 'ups:cassette-delete'},
        ]
        Cassette.objects.create(name='Christian_detail',)
        model = Cassette.objects.get(name='Christian_detail',)
        resp = self.client.get(reverse('ups:cassette-detail', kwargs={"pk": model.pk}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        links = ['ups:cassette_list', 'ups:cassette_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['cassette_list']) == 10)

    def test_lists_all_cassette(self):
        links = ['ups:cassette_list', 'ups:cassette_search']
        for link in links:
            resp = self.client.get(reverse(link)+'?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['cassette_list']) == 9)



