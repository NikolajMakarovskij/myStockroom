from django.test import TestCase
from ..models import *
from django.urls import reverse


class accumulatorViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_accumulator = 149
        for accumulator_num in range(number_of_accumulator):
            Accumulator.objects.create(name='Christian %s' % accumulator_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/consumables/accumulator/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('consumables:accumulator_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('consumables:accumulator_list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'consumables/accumulator_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('consumables:accumulator_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['accumulator_list']) == 10)

    def test_lists_all_accumulator(self):
        resp = self.client.get(reverse('consumables:accumulator_list')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['accumulator_list']) == 9)

class cartridgeViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_cartridge = 149
        for cartridge_num in range(number_of_cartridge):
            Cartridge.objects.create(name='Christian %s' % cartridge_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/consumables/cartridge/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('consumables:cartridge_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('consumables:cartridge_list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'consumables/cartridge_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('consumables:cartridge_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['cartridge_list']) == 10)

    def test_lists_all_cartridge(self):
        resp = self.client.get(reverse('consumables:cartridge_list')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['cartridge_list']) == 9)

class fotovalViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_fotoval = 149
        for fotoval_num in range(number_of_fotoval):
            Fotoval.objects.create(name='Christian %s' % fotoval_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/consumables/fotoval/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('consumables:fotoval_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('consumables:fotoval_list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'consumables/fotoval_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('consumables:fotoval_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['fotoval_list']) == 10)

    def test_lists_all_fotoval(self):
        resp = self.client.get(reverse('consumables:fotoval_list')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['fotoval_list']) == 9)
    
class tonerViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_toner = 149
        for toner_num in range(number_of_toner):
            Toner.objects.create(name='Christian %s' % toner_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/consumables/toner/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('consumables:toner_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('consumables:toner_list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'consumables/toner_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('consumables:toner_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['toner_list']) == 10)

    def test_lists_all_toner(self):
        resp = self.client.get(reverse('consumables:toner_list')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['toner_list']) == 9)

class storageViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_storage = 149
        for storage_num in range(number_of_storage):
            Storage.objects.create(name='Christian %s' % storage_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/consumables/storage/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('consumables:storage_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('consumables:storage_list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'consumables/storage_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('consumables:storage_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['storage_list']) == 10)

    def test_lists_all_storage(self):
        resp = self.client.get(reverse('consumables:storage_list')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['storage_list']) == 9)
