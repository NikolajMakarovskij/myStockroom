from django.test import TestCase
from ..models import *
from django.urls import reverse
import warnings


class stockroomViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_in_stock = 149
        for stocks_num in range(number_in_stock):
            cons = Consumables.objects.create(name='Christian %s' % stocks_num,)
            Stockroom.objects.create(consumables = cons)
        assert Consumables.objects.count() == 149

    def test_context_data_in_list(self):
        warnings.filterwarnings(action="ignore")
        links = ['stockroom:stock_list', 'stockroom:stock_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'Склад'},
            {'data_key': 'searchlink', 'data_value': 'stockroom:stock_search'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        links = ['stockroom:stock_list', 'stockroom:stock_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['stockroom_list']) == 10)

    def test_lists_all_stockroom(self):
        warnings.filterwarnings(action="ignore")
        links = ['stockroom:stock_list', 'stockroom:stock_search']
        for link in links:
            resp = self.client.get(reverse(link)+'?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['stockroom_list']) == 9)
