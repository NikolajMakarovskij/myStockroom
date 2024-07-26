from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from consumables.models import Consumables
from stockroom.models.consumables import History, StockCat, Stockroom


# Consumables
class StockroomViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user', is_superuser=True, is_staff=True)[0])

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
            self.assertTrue(len(resp.context['stockroom_list']) == 20)

    def test_lists_all_stockroom(self):
        links = ['stockroom:stock_list', 'stockroom:stock_search']
        for link in links:
            resp = self.client.get(reverse(link) + '?page=8')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['stockroom_list']) == 9)


class StockroomCategoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user', is_superuser=True, is_staff=True)[0])

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
        self.assertTrue(len(resp.context['stockroom_list']) == 20)

    def test_lists_all_stockroom_consumables(self):
        resp = self.client.get(reverse('stockroom:category', kwargs={
            "category_slug": StockCat.objects.get(slug="some_category")}) + '?page=8')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['stockroom_list']) == 9)


class HistoryStockViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user', is_superuser=True, is_staff=True)[0])

    @classmethod
    def setUpTestData(cls):
        number_in_history = 149
        Consumables.objects.create(name='check_consumable')
        for history_num in range(number_in_history):
            History.objects.create(
                stock_model='Christian %s' % history_num,
                stock_model_id=Consumables.objects.filter(name='check_consumable').get().id
            )
        assert History.objects.count() == 149

    def test_context_data_in_history_list(self):
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

    def test_context_data_in_consumption_list(self):
        links = ['stockroom:history_consumption_list', 'stockroom:history_consumption_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'Расход расходников по годам'},
            {'data_key': 'searchlink', 'data_value': 'stockroom:history_consumption_search'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten_in_history(self):
        links = ['stockroom:history_list', 'stockroom:history_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['history_list']) == 20)

    def test_pagination_is_ten_in_consumption(self):
        links = ['stockroom:history_consumption_list', 'stockroom:history_consumption_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)

    def test_lists_all_stockroom(self):
        links = ['stockroom:history_list', 'stockroom:history_search']
        for link in links:
            resp = self.client.get(reverse(link) + '?page=8')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['history_list']) == 9)


class HistoryCategoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user', is_superuser=True, is_staff=True)[0])

    @classmethod
    def setUpTestData(cls):
        number_in_stock = 149
        StockCat.objects.create(name="some_category", slug="some_category")
        Consumables.objects.create(name='check_consumable')
        for stocks_num in range(number_in_stock):
            History.objects.create(
                stock_model='Christian %s' % stocks_num,
                categories=StockCat.objects.get(slug="some_category"),
                stock_model_id=Consumables.objects.filter(name='check_consumable').get().id
                )
        assert History.objects.count() == 149
        assert StockCat.objects.count() == 1

    def test_context_data_in_history_category(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'История расходников'},
            {'data_key': 'searchlink', 'data_value': 'stockroom:history_search'},
        ]
        resp = self.client.get(
            reverse('stockroom:history_category',
                    kwargs={"category_slug": StockCat.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_context_data_in_consumption_category(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'Расход расходников по годам'},
            {'data_key': 'searchlink', 'data_value': 'stockroom:history_consumption_search'},
        ]
        resp = self.client.get(
            reverse('stockroom:history_consumption_category',
                    kwargs={"category_slug": StockCat.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten_in_history(self):
        resp = self.client.get(
            reverse('stockroom:history_category',
                    kwargs={"category_slug": StockCat.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['history_list']) == 20)

    def test_pagination_is_ten_in_consumption(self):
        resp = self.client.get(
            reverse('stockroom:history_consumption_category',
                    kwargs={"category_slug": StockCat.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)

    def test_lists_all_stockroom_history_consumables(self):
        resp = self.client.get(reverse('stockroom:history_category', kwargs={
            "category_slug": StockCat.objects.get(slug="some_category")}) + '?page=8')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['history_list']) == 9)
