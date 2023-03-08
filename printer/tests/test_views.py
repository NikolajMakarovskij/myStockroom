from django.test import TestCase
from ..models import Printer, Categories
from django.urls import reverse
import warnings

class printerViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_printer = 149
        warnings.filterwarnings(action="ignore")
        for printer_num in range(number_of_printer):
            Printer.objects.create(name='Christian %s' % printer_num,)

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('printer:printer_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['printer_list']) == 10)

    def test_lists_all_printer(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('printer:printer_list')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['printer_list']) == 9)

class printerSearchViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_printer = 149
        warnings.filterwarnings(action="ignore")
        for printer_num in range(number_of_printer):
            Printer.objects.create(name='Christian %s' % printer_num,)

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('printer:printer_search'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['printer_list']) == 10)

    def test_lists_all_printer(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('printer:printer_search')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['printer_list']) == 9)


class printerCategoryViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_printer = 149
        warnings.filterwarnings(action="ignore")
        Categories.objects.create(name="some_category", slug="some_category")
        for printer_num in range(number_of_printer):
            Printer.objects.create(name='Christian %s' % printer_num, categories=Categories.objects.get(slug="some_category"))

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('printer:category', kwargs={"category_slug": Categories.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['printer_list']) == 10)

    def test_lists_all_printer(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('printer:category', kwargs={"category_slug": Categories.objects.get(slug="some_category")})+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['printer_list']) == 9)