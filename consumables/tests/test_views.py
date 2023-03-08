from django.test import TestCase
from ..models import *
from django.urls import reverse
import warnings


class consumablesViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_of_consumables = 149
        for consumables_num in range(number_of_consumables):
            Consumables.objects.create(name='Christian %s' % consumables_num,)

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('consumables:consumables_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['consumables_list']) == 10)

    def test_lists_all_consumables(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('consumables:consumables_list')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['consumables_list']) == 9)


class consumablesSearchViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_of_consumables = 149
        for consumables_num in range(number_of_consumables):
            Consumables.objects.create(name='Christian %s' % consumables_num,)

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('consumables:consumables_search'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['consumables_list']) == 10)

    def test_lists_all_consumables(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('consumables:consumables_search')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['consumables_list']) == 9)

class consumablesCategoryViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_of_consumables = 149
        Categories.objects.create(name="some_category", slug="some_category")
        for consumables_num in range(number_of_consumables):
            Consumables.objects.create(name='Christian %s' % consumables_num, categories=Categories.objects.get(slug="some_category"))

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('consumables:category', kwargs={"category_slug": Categories.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['consumables_list']) == 10)

    def test_lists_all_consumables(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('consumables:category', kwargs={"category_slug": Categories.objects.get(slug="some_category")})+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['consumables_list']) == 9)