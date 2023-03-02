from django.test import TestCase
from ..models import *
from django.urls import reverse

class signatureViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_signature = 149
        for signature_num in range(number_of_signature):
            Signature.objects.create(name='Christian %s' % signature_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/signature/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('signature:signature_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('signature:signature_list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'signature/signature_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('signature:signature_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['signature_list']) == 10)

    def test_lists_all_signature(self):
        resp = self.client.get(reverse('signature:signature_list')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['signature_list']) == 9)
