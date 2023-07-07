from django.test import TestCase
from consumables.models import Consumables, Accessories
from device.models import Device
from ..models import Stockroom, History, StockAcc, HistoryAcc, StockDev, HistoryDev
from django.urls import reverse


# Consumables
class StockroomViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_in_stock = 149
        for stocks_num in range(number_in_stock):
            cons = Consumables.objects.create(name='Christian %s' % stocks_num)
            Stockroom.objects.create(consumables=cons)
        assert Consumables.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['stockroom:stock_list', 'stockroom:stock_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'Склад расходников'},
            {'data_key': 'searchlink', 'data_value': 'stockroom:stock_search'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        links = ['stockroom:stock_list', 'stockroom:stock_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['stockroom_list']) == 10)

    def test_lists_all_stockroom(self):
        links = ['stockroom:stock_list', 'stockroom:stock_search']
        for link in links:
            resp = self.client.get(reverse(link) + '?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['stockroom_list']) == 9)


class HistoryStockViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_in_history = 149
        for history_num in range(number_in_history):
            History.objects.create(consumable='Christian %s' % history_num, )
        assert History.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['stockroom:history_list', 'stockroom:history_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'История расходников'},
            {'data_key': 'searchlink', 'data_value': 'stockroom:history_search'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        links = ['stockroom:history_list', 'stockroom:history_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['history_list']) == 10)

    def test_lists_all_stockroom(self):
        links = ['stockroom:history_list', 'stockroom:history_search']
        for link in links:
            resp = self.client.get(reverse(link) + '?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['history_list']) == 9)


# Accessories
class StockAccViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_in_stock = 149
        for stocks_num in range(number_in_stock):
            cons = Accessories.objects.create(name='Christian %s' % stocks_num)
            StockAcc.objects.create(accessories=cons)
        assert Accessories.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['stockroom:stock_acc_list', 'stockroom:stock_acc_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'Склад комплектующих'},
            {'data_key': 'searchlink', 'data_value': 'stockroom:stock_acc_search'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        links = ['stockroom:stock_acc_list', 'stockroom:stock_acc_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['stockacc_list']) == 10)

    def test_lists_all_stockroom(self):
        links = ['stockroom:stock_acc_list', 'stockroom:stock_acc_search']
        for link in links:
            resp = self.client.get(reverse(link) + '?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['stockacc_list']) == 9)


class HistoryAccStockViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_in_history = 149
        for history_num in range(number_in_history):
            HistoryAcc.objects.create(accessories='Christian %s' % history_num, )
        assert HistoryAcc.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['stockroom:history_acc_list', 'stockroom:history_acc_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'История комплектующих'},
            {'data_key': 'searchlink', 'data_value': 'stockroom:history_acc_search'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        links = ['stockroom:history_acc_list', 'stockroom:history_acc_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['historyacc_list']) == 10)

    def test_lists_all_stockroom(self):
        links = ['stockroom:history_acc_list', 'stockroom:history_acc_search']
        for link in links:
            resp = self.client.get(reverse(link) + '?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['historyacc_list']) == 9)


# Devices
class StockDevViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_in_stock = 149
        for stocks_num in range(number_in_stock):
            cons = Device.objects.create(name='Christian %s' % stocks_num)
            StockDev.objects.create(devices=cons)
        assert Device.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['stockroom:stock_dev_list', 'stockroom:stock_dev_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'Склад устройств'},
            {'data_key': 'searchlink', 'data_value': 'stockroom:stock_dev_search'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        links = ['stockroom:stock_dev_list', 'stockroom:stock_dev_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['stockdev_list']) == 10)

    def test_lists_all_stockroom(self):
        links = ['stockroom:stock_dev_list', 'stockroom:stock_dev_search']
        for link in links:
            resp = self.client.get(reverse(link) + '?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['stockdev_list']) == 9)


class HistoryDevStockViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_in_history = 149
        for history_num in range(number_in_history):
            HistoryDev.objects.create(devices='Christian %s' % history_num, )
        assert HistoryDev.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['stockroom:history_dev_list', 'stockroom:history_dev_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'История устройств'},
            {'data_key': 'searchlink', 'data_value': 'stockroom:history_dev_search'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        links = ['stockroom:history_dev_list', 'stockroom:history_dev_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['historydev_list']) == 10)

    def test_lists_all_stockroom(self):
        links = ['stockroom:history_dev_list', 'stockroom:history_dev_search']
        for link in links:
            resp = self.client.get(reverse(link) + '?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['historydev_list']) == 9)
