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

    def test_view_url_exists_at_desired_location(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get('/stockroom/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('stockroom:stock_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('stockroom:stock_list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'stock/stock_list.html')

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('stockroom:stock_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['stockroom_list']) == 10)

    def test_lists_all_stockroom(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('stockroom:stock_list')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['stockroom_list']) == 9)