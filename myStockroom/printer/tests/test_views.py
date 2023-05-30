from django.test import TestCase
from ..models import Printer, Printer_cat
from django.urls import reverse
import warnings

class printerViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_printer = 149
        for printer_num in range(number_of_printer):
            Printer.objects.create(name='Christian %s' % printer_num,)
        assert Printer.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['printer:printer_list', 'printer:printer_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'Принтеры'},
            {'data_key': 'searchlink', 'data_value': 'printer:printer_search'},
            {'data_key': 'add', 'data_value': 'printer:new-printer'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_context_data_in_detail(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'Принтер'},
            {'data_key': 'add', 'data_value': 'printer:new-printer'},
            {'data_key': 'update', 'data_value': 'printer:printer-update'},
            {'data_key': 'delete', 'data_value': 'printer:printer-delete'},
        ]
        Printer.objects.create(name='Christian_detail',)
        model = Printer.objects.get(name='Christian_detail',)
        resp = self.client.get(reverse('printer:printer-detail', kwargs={"pk": model.pk}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        links = ['printer:printer_list', 'printer:printer_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['printer_list']) == 10)

    def test_lists_all_printer(self):
        links = ['printer:printer_list', 'printer:printer_search']
        for link in links:
            resp = self.client.get(reverse(link)+'?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['printer_list']) == 9)

class printerCategoryViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_printer = 149
        Printer_cat.objects.create(name="some_category", slug="some_category")
        for printer_num in range(number_of_printer):
            Printer.objects.create(name='Christian %s' % printer_num, categories=Printer_cat.objects.get(slug="some_category"))
        assert Printer.objects.count() == 149
        assert Printer_cat.objects.count() == 1

    def test_context_data_in_category(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'Принтеры'},
            {'data_key': 'searchlink', 'data_value': 'printer:printer_search'},
            {'data_key': 'add', 'data_value': 'printer:new-printer'},
        ]
        resp = self.client.get(reverse('printer:category', kwargs={"category_slug": Printer_cat.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('printer:category', kwargs={"category_slug": Printer_cat.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['printer_list']) == 10)

    def test_lists_all_printer(self):
        resp = self.client.get(reverse('printer:category', kwargs={"category_slug": Printer_cat.objects.get(slug="some_category")})+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['printer_list']) == 9)