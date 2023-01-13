from django.test import TestCase
from ..models import *
from django.urls import reverse



class accumulatorViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_accumulator = 149
        for accumulator_num in range(number_of_accumulator):
            accumulator.objects.create(name='Christian %s' % accumulator_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/accumulator/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('accumulator'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('accumulator'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/ups/accumulator_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('accumulator'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['accumulator_list']) == 10)

    def test_lists_all_accumulator(self):
        resp = self.client.get(reverse('accumulator')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['accumulator_list']) == 9)

class cartridgeViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_cartridge = 149
        for cartridge_num in range(number_of_cartridge):
            cartridge.objects.create(name='Christian %s' % cartridge_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/cartridge/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('cartridge'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('cartridge'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/printer/cartridge_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('cartridge'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['cartridge_list']) == 10)

    def test_lists_all_cartridge(self):
        resp = self.client.get(reverse('cartridge')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['cartridge_list']) == 9)

class fotovalViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_fotoval = 149
        for fotoval_num in range(number_of_fotoval):
            fotoval.objects.create(name='Christian %s' % fotoval_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/fotoval/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('fotoval'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('fotoval'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/printer/fotoval_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('fotoval'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['fotoval_list']) == 10)

    def test_lists_all_fotoval(self):
        resp = self.client.get(reverse('fotoval')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['fotoval_list']) == 9)
    
class tonerViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_toner = 149
        for toner_num in range(number_of_toner):
            toner.objects.create(name='Christian %s' % toner_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/toner/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('toner'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('toner'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/printer/toner_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('toner'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['toner_list']) == 10)

    def test_lists_all_toner(self):
        resp = self.client.get(reverse('toner')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['toner_list']) == 9)

class storageViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_storage = 149
        for storage_num in range(number_of_storage):
            storage.objects.create(name='Christian %s' % storage_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/storage/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('storage'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('storage'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/storage_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('storage'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['storage_list']) == 10)

    def test_lists_all_storage(self):
        resp = self.client.get(reverse('storage')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['storage_list']) == 9)
