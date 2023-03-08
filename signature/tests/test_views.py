from django.test import TestCase
from ..models import *
from django.urls import reverse
import warnings

class signatureViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_of_signature = 149
        for signature_num in range(number_of_signature):
            Signature.objects.create(name='Christian %s' % signature_num,)

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('signature:signature_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['signature_list']) == 10)

    def test_lists_all_signature(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('signature:signature_list')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['signature_list']) == 9)

class signatureSearchViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_of_signature = 149
        for signature_num in range(number_of_signature):
            Signature.objects.create(name='Christian %s' % signature_num,)

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('signature:signature_search'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['signature_list']) == 10)

    def test_lists_all_signature(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('signature:signature_search')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['signature_list']) == 9)
