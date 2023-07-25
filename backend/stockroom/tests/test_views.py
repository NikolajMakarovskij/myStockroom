from django.test import TestCase, Client
from django.contrib.auth.models import User
from consumables.models import Consumables, Accessories, AccCat, Categories
from device.models import Device, DeviceCat
from ..models import Stockroom, History, StockAcc, HistoryAcc, StockDev, HistoryDev, StockCat, CategoryAcc, CategoryDev
from django.urls import reverse


# Consumables
class StockroomViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user')[0])

    @classmethod
    def setUpTestData(cls):
        number_in_stock = 149
        for stocks_num in range(number_in_stock):
            cons = Consumables.objects.create(name='Christian %s' % stocks_num)
            Stockroom.objects.create(stock_model=cons)
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


class StockroomCategoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user')[0])

    @classmethod
    def setUpTestData(cls):
        number_in_stock = 149
        StockCat.objects.create(name="some_category", slug="some_category")
        for stocks_num in range(number_in_stock):
            cons = Consumables.objects.create(name='Christian %s' % stocks_num)
            Stockroom.objects.create(stock_model=cons, categories=StockCat.objects.get(slug="some_category"))
        assert Stockroom.objects.count() == 149
        assert StockCat.objects.count() == 1

    def test_context_data_in_category(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'Склад расходников'},
            {'data_key': 'searchlink', 'data_value': 'stockroom:stock_search'},
        ]
        resp = self.client.get(
            reverse('stockroom:category', kwargs={"category_slug": StockCat.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        resp = self.client.get(
            reverse('stockroom:category', kwargs={"category_slug": StockCat.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['stockroom_list']) == 10)

    def test_lists_all_stockroom_consumables(self):
        resp = self.client.get(reverse('stockroom:category', kwargs={
            "category_slug": StockCat.objects.get(slug="some_category")}) + '?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['stockroom_list']) == 9)


class HistoryStockViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user')[0])

    @classmethod
    def setUpTestData(cls):
        number_in_history = 149
        for history_num in range(number_in_history):
            History.objects.create(stock_model='Christian %s' % history_num, )
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


class HistoryCategoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user')[0])

    @classmethod
    def setUpTestData(cls):
        number_in_stock = 149
        StockCat.objects.create(name="some_category", slug="some_category")
        for stocks_num in range(number_in_stock):
            History.objects.create(stock_model='Christian %s' % stocks_num,
                                   categories=StockCat.objects.get(slug="some_category"))
        assert History.objects.count() == 149
        assert StockCat.objects.count() == 1

    def test_context_data_in_category(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'История расходников'},
            {'data_key': 'searchlink', 'data_value': 'stockroom:history_search'},
        ]
        resp = self.client.get(
            reverse('stockroom:history_category', kwargs={"category_slug": StockCat.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        resp = self.client.get(
            reverse('stockroom:history_category', kwargs={"category_slug": StockCat.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['history_list']) == 10)

    def test_lists_all_stockroom_history_consumables(self):
        resp = self.client.get(reverse('stockroom:history_category', kwargs={
            "category_slug": StockCat.objects.get(slug="some_category")}) + '?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['history_list']) == 9)


# Accessories
class StockAccViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user')[0])

    @classmethod
    def setUpTestData(cls):
        number_in_stock = 149
        for stocks_num in range(number_in_stock):
            cons = Accessories.objects.create(name='Christian %s' % stocks_num)
            StockAcc.objects.create(stock_model=cons)
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


class StockroomAccCategoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user')[0])

    @classmethod
    def setUpTestData(cls):
        number_in_stock = 149
        CategoryAcc.objects.create(name="some_category", slug="some_category")
        for stocks_num in range(number_in_stock):
            cons = Accessories.objects.create(name='Christian %s' % stocks_num)
            StockAcc.objects.create(stock_model=cons, categories=CategoryAcc.objects.get(slug="some_category"))
        assert StockAcc.objects.count() == 149
        assert CategoryAcc.objects.count() == 1

    def test_context_data_in_category(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'Склад комплектующих'},
            {'data_key': 'searchlink', 'data_value': 'stockroom:stock_acc_search'},
        ]
        resp = self.client.get(
            reverse('stockroom:accessories_category',
                    kwargs={"category_slug": CategoryAcc.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        resp = self.client.get(
            reverse('stockroom:accessories_category',
                    kwargs={"category_slug": CategoryAcc.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['stockacc_list']) == 10)

    def test_lists_all_stockroom_consumables(self):
        resp = self.client.get(reverse('stockroom:accessories_category', kwargs={
            "category_slug": CategoryAcc.objects.get(slug="some_category")}) + '?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['stockacc_list']) == 9)


class HistoryAccStockViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user')[0])

    @classmethod
    def setUpTestData(cls):
        number_in_history = 149
        for history_num in range(number_in_history):
            HistoryAcc.objects.create(stock_model='Christian %s' % history_num, )
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


class HistoryAccCategoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user')[0])

    @classmethod
    def setUpTestData(cls):
        number_in_stock = 149
        CategoryAcc.objects.create(name="some_category", slug="some_category")
        for stocks_num in range(number_in_stock):
            HistoryAcc.objects.create(stock_model='Christian %s' % stocks_num,
                                      categories=CategoryAcc.objects.get(slug="some_category"))
        assert HistoryAcc.objects.count() == 149
        assert CategoryAcc.objects.count() == 1

    def test_context_data_in_category(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'История комплектующих'},
            {'data_key': 'searchlink', 'data_value': 'stockroom:history_acc_search'},
        ]
        resp = self.client.get(
            reverse('stockroom:history_acc_category',
                    kwargs={"category_slug": CategoryAcc.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        resp = self.client.get(
            reverse('stockroom:history_acc_category',
                    kwargs={"category_slug": CategoryAcc.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['historyacc_list']) == 10)

    def test_lists_all_stockroom_history_acc_consumables(self):
        resp = self.client.get(reverse('stockroom:history_acc_category', kwargs={
            "category_slug": CategoryAcc.objects.get(slug="some_category")}) + '?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['historyacc_list']) == 9)


# Devices
class StockDevViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user')[0])

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
            self.assertTrue(len(resp.context['stockdev_list']) == 10)

    def test_lists_all_stockroom(self):
        links = ['stockroom:stock_dev_list', 'stockroom:stock_dev_search']
        for link in links:
            resp = self.client.get(reverse(link) + '?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['stockdev_list']) == 9)


class StockroomDevCategoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user')[0])

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
            reverse('stockroom:devices_category', kwargs={"category_slug": CategoryDev.objects.get(slug="some_category")}))
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
        self.assertTrue(len(resp.context['stockdev_list']) == 10)

    def test_lists_all_stockroom_consumables(self):
        resp = self.client.get(reverse('stockroom:devices_category', kwargs={
            "category_slug": CategoryDev.objects.get(slug="some_category")}) + '?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['stockdev_list']) == 9)


class HistoryDevStockViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user')[0])

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
            self.assertTrue(len(resp.context['historydev_list']) == 10)

    def test_lists_all_stockroom(self):
        links = ['stockroom:history_dev_list', 'stockroom:history_dev_search']
        for link in links:
            resp = self.client.get(reverse(link) + '?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['historydev_list']) == 9)


class HistoryDevCategoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user')[0])

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
        self.assertTrue(len(resp.context['historydev_list']) == 10)

    def test_lists_all_stockroom_history_acc_consumables(self):
        resp = self.client.get(reverse('stockroom:history_dev_category', kwargs={
            "category_slug": CategoryDev.objects.get(slug="some_category")}) + '?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['historydev_list']) == 9)