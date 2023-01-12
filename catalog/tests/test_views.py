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