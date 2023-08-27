from django.test import TestCase, Client
from django.contrib.auth.models import User
from device.models import Device
from stockroom.models.devices import StockDev, HistoryDev, CategoryDev
from django.urls import reverse


# Devices
class StockDevViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user', is_superuser=True, is_staff=True)[0])

    @classmethod
    def setUpTestData(cls):
        number_in_stock = 149
        for stocks_num in range(number_in_stock):
            cons = Device.objects.create(name='Christian %s' % stocks_num)
            StockDev.objects.create(stock_model=cons)
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
            self.assertTrue(len(resp.context['stockdev_list']) == 20)

    def test_lists_all_stockroom(self):
        links = ['stockroom:stock_dev_list', 'stockroom:stock_dev_search']
        for link in links:
            resp = self.client.get(reverse(link) + '?page=8')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['stockdev_list']) == 9)


class StockroomDevCategoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user', is_superuser=True, is_staff=True)[0])

    @classmethod
    def setUpTestData(cls):
        number_in_stock = 149
        CategoryDev.objects.create(name="some_category", slug="some_category")
        for stocks_num in range(number_in_stock):
            cons = Device.objects.create(name='Christian %s' % stocks_num)
            StockDev.objects.create(stock_model=cons, categories=CategoryDev.objects.get(slug="some_category"))
        assert StockDev.objects.count() == 149
        assert CategoryDev.objects.count() == 1

    def test_context_data_in_category(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'Склад устройств'},
            {'data_key': 'searchlink', 'data_value': 'stockroom:stock_dev_search'},
        ]
        resp = self.client.get(
            reverse('stockroom:devices_category',
                    kwargs={"category_slug": CategoryDev.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        resp = self.client.get(
            reverse('stockroom:devices_category',
                    kwargs={"category_slug": CategoryDev.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['stockdev_list']) == 20)

    def test_lists_all_stockroom_consumables(self):
        resp = self.client.get(reverse('stockroom:devices_category', kwargs={
            "category_slug": CategoryDev.objects.get(slug="some_category")}) + '?page=8')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['stockdev_list']) == 9)


class HistoryDevStockViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user', is_superuser=True, is_staff=True)[0])

    @classmethod
    def setUpTestData(cls):
        number_in_history = 149
        for history_num in range(number_in_history):
            HistoryDev.objects.create(stock_model='Christian %s' % history_num, )
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
            self.assertTrue(len(resp.context['historydev_list']) == 20)

    def test_lists_all_stockroom(self):
        links = ['stockroom:history_dev_list', 'stockroom:history_dev_search']
        for link in links:
            resp = self.client.get(reverse(link) + '?page=8')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['historydev_list']) == 9)


class HistoryDevCategoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user', is_superuser=True, is_staff=True)[0])

    @classmethod
    def setUpTestData(cls):
        number_in_stock = 149
        CategoryDev.objects.create(name="some_category", slug="some_category")
        for stocks_num in range(number_in_stock):
            HistoryDev.objects.create(stock_model='Christian %s' % stocks_num,
                                      categories=CategoryDev.objects.get(slug="some_category"))
        assert HistoryDev.objects.count() == 149
        assert CategoryDev.objects.count() == 1

    def test_context_data_in_category(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'История устройств'},
            {'data_key': 'searchlink', 'data_value': 'stockroom:history_dev_search'},
        ]
        resp = self.client.get(
            reverse('stockroom:history_dev_category',
                    kwargs={"category_slug": CategoryDev.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        resp = self.client.get(
            reverse('stockroom:history_dev_category',
                    kwargs={"category_slug": CategoryDev.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['historydev_list']) == 20)

    def test_lists_all_stockroom_history_acc_consumables(self):
        resp = self.client.get(reverse('stockroom:history_dev_category', kwargs={
            "category_slug": CategoryDev.objects.get(slug="some_category")}) + '?page=8')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['historydev_list']) == 9)