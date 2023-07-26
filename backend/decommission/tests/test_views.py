from django.test import TestCase, Client
from django.contrib.auth.models import User
from device.models import Device
from decommission.models import Decommission, CategoryDec, Disposal, CategoryDis
from django.urls import reverse


# Decommission
class DecommissionViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user')[0])

    @classmethod
    def setUpTestData(cls):
        number_in_stock = 149
        for stocks_num in range(number_in_stock):
            dev = Device.objects.create(name='Christian %s' % stocks_num)
            Decommission.objects.create(stock_model=dev)
        assert Decommission.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['decommission:decom_list', 'decommission:decom_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'Списание устройств'},
            {'data_key': 'searchlink', 'data_value': 'decommission:decom_search'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        links = ['decommission:decom_list', 'decommission:decom_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['decommission_list']) == 10)

    def test_lists_all_decommission(self):
        links = ['decommission:decom_list', 'decommission:decom_search']
        for link in links:
            resp = self.client.get(reverse(link) + '?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['decommission_list']) == 9)


class DecommissionCategoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user')[0])

    @classmethod
    def setUpTestData(cls):
        number_in_stock = 149
        CategoryDec.objects.create(name="some_category", slug="some_category")
        for stocks_num in range(number_in_stock):
            dev = Device.objects.create(name='Christian %s' % stocks_num)
            Decommission.objects.create(stock_model=dev, categories=CategoryDec.objects.get(slug="some_category"))
        assert Decommission.objects.count() == 149
        assert CategoryDec.objects.count() == 1

    def test_context_data_in_category(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'Списание устройств'},
            {'data_key': 'searchlink', 'data_value': 'decommission:decom_search'},
        ]
        resp = self.client.get(
            reverse('decommission:decom_category',
                    kwargs={"category_slug": CategoryDec.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        resp = self.client.get(
            reverse('decommission:decom_category',
                    kwargs={"category_slug": CategoryDec.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['decommission_list']) == 10)

    def test_lists_all_stockroom_consumables(self):
        resp = self.client.get(reverse('decommission:decom_category', kwargs={
            "category_slug": CategoryDec.objects.get(slug="some_category")}) + '?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['decommission_list']) == 9)


# Disposal
class DisposalViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user')[0])

    @classmethod
    def setUpTestData(cls):
        number_in_stock = 149
        for stocks_num in range(number_in_stock):
            dev = Device.objects.create(name='Christian %s' % stocks_num)
            Disposal.objects.create(stock_model=dev)
        assert Disposal.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['decommission:disp_list', 'decommission:disp_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'Утилизация устройств'},
            {'data_key': 'searchlink', 'data_value': 'decommission:disp_search'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        links = ['decommission:disp_list', 'decommission:disp_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['disposal_list']) == 10)

    def test_lists_all_disposal(self):
        links = ['decommission:disp_list', 'decommission:disp_search']
        for link in links:
            resp = self.client.get(reverse(link) + '?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['disposal_list']) == 9)


class DisposalCategoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user')[0])

    @classmethod
    def setUpTestData(cls):
        number_in_stock = 149
        CategoryDis.objects.create(name="some_category", slug="some_category")
        for stocks_num in range(number_in_stock):
            dev = Device.objects.create(name='Christian %s' % stocks_num)
            Disposal.objects.create(stock_model=dev, categories=CategoryDis.objects.get(slug="some_category"))
        assert Disposal.objects.count() == 149
        assert CategoryDis.objects.count() == 1

    def test_context_data_in_category(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'Утилизация устройств'},
            {'data_key': 'searchlink', 'data_value': 'decommission:disp_search'},
        ]
        resp = self.client.get(
            reverse('decommission:disp_category',
                    kwargs={"category_slug": CategoryDis.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        resp = self.client.get(
            reverse('decommission:disp_category',
                    kwargs={"category_slug": CategoryDis.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['disposal_list']) == 10)

    def test_lists_all_disposal_categories(self):
        resp = self.client.get(reverse('decommission:disp_category', kwargs={
            "category_slug": CategoryDis.objects.get(slug="some_category")}) + '?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['disposal_list']) == 9)
