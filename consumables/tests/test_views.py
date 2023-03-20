from django.test import TestCase
from ..models import *
from django.urls import reverse
import warnings


class consumablesViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_consumables = 149
        Categories.objects.create(name="some_category", slug="some_category")
        for consumables_num in range(number_of_consumables):
            Consumables.objects.create(name='Christian %s' % consumables_num, categories=Categories.objects.get(slug="some_category"))
        assert Consumables.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['consumables:consumables_list', 'consumables:consumables_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'Расходники'},
            {'data_key': 'searchlink', 'data_value': 'consumables:consumables_search'},
            {'data_key': 'add', 'data_value': 'consumables:new-consumables'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_context_data_in_detail(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'Расходник'},
            {'data_key': 'add', 'data_value': 'consumables:new-consumables'},
            {'data_key': 'update', 'data_value': 'consumables:consumables-update'},
            {'data_key': 'delete', 'data_value': 'consumables:consumables-delete'},
        ]
        Consumables.objects.create(name='Christian_detail',)
        model = Consumables.objects.get(name='Christian_detail',)
        resp = self.client.get(reverse('consumables:consumables-detail', kwargs={"pk": model.pk}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        links = ['consumables:consumables_list', 'consumables:consumables_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['consumables_list']) == 10)

    def test_lists_all_consumables(self):
        links = ['consumables:consumables_list', 'consumables:consumables_search']
        for link in links:
            resp = self.client.get(reverse(link)+'?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['consumables_list']) == 9)

class consumablesCategoryViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_consumables = 149
        Categories.objects.create(name="some_category", slug="some_category")
        for consumables_num in range(number_of_consumables):
            Consumables.objects.create(name='Christian %s' % consumables_num, categories=Categories.objects.get(slug="some_category"))
        assert Consumables.objects.count() == 149
        assert Categories.objects.count() == 1

    def test_context_data_in_category(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'Расходники'},
            {'data_key': 'searchlink', 'data_value': 'consumables:consumables_search'},
            {'data_key': 'add', 'data_value': 'consumables:new-consumables'},
        ]
        resp = self.client.get(reverse('consumables:category', kwargs={"category_slug": Categories.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('consumables:category', kwargs={"category_slug": Categories.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['consumables_list']) == 10)

    def test_lists_all_categories(self):
        resp = self.client.get(reverse('consumables:category', kwargs={"category_slug": Categories.objects.get(slug="some_category")})+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['consumables_list']) == 9)