from django.test import TestCase
from catalog.models.models import *
from django.urls import reverse





class manufacturerViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_manufacturer = 149
        for manufacturer_num in range(number_of_manufacturer):
            manufacturer.objects.create(name='Christian %s' % manufacturer_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/manufacturer/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('manufacturer'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('manufacturer'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/manufacturer_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('manufacturer'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['manufacturer_list']) == 10)

    def test_lists_all_manufacturer(self):
        resp = self.client.get(reverse('manufacturer')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['manufacturer_list']) == 9)




class upsViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_ups = 149
        for ups_num in range(number_of_ups):
            ups.objects.create(name='Christian %s' % ups_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/ups/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('ups'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('ups'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/ups/ups_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('ups'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['ups_list']) == 10)

    def test_lists_all_ups(self):
        resp = self.client.get(reverse('ups')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['ups_list']) == 9)

class cassetteViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_cassette = 149
        for cassette_num in range(number_of_cassette):
            cassette.objects.create(name='Christian %s' % cassette_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/cassette/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('cassette'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('cassette'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/ups/cassette_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('cassette'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['cassette_list']) == 10)

    def test_lists_all_cassette(self):
        resp = self.client.get(reverse('cassette')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['cassette_list']) == 9)

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

class printerViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_printer = 149
        for printer_num in range(number_of_printer):
            printer.objects.create(name='Christian %s' % printer_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/printer/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('printer'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('printer'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/printer/printer_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('printer'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['printer_list']) == 10)

    def test_lists_all_printer(self):
        resp = self.client.get(reverse('printer')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['printer_list']) == 9)

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

class signatureViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_signature = 149
        for signature_num in range(number_of_signature):
            signature.objects.create(name='Christian %s' % signature_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/signature/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('signature'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('signature'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/signature/signature_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('signature'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['signature_list']) == 10)

    def test_lists_all_signature(self):
        resp = self.client.get(reverse('signature')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['signature_list']) == 9)

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