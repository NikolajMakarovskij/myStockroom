from django.test import TestCase
from ..models import Signature
from django.urls import reverse


class SignatureViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_signature = 149
        for signature_num in range(number_of_signature):
            Signature.objects.create(name='Christian %s' % signature_num, )
        assert Signature.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['signature:signature_list', 'signature:signature_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'ЭЦП'},
            {'data_key': 'searchlink', 'data_value': 'signature:signature_search'},
            {'data_key': 'add', 'data_value': 'signature:new-signature'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_context_data_in_detail(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'ЭЦП'},
            {'data_key': 'add', 'data_value': 'signature:new-signature'},
            {'data_key': 'update', 'data_value': 'signature:signature-update'},
            {'data_key': 'delete', 'data_value': 'signature:signature-delete'},
        ]
        Signature.objects.create(name='Christian_detail', )
        model = Signature.objects.get(name='Christian_detail', )
        resp = self.client.get(reverse('signature:signature-detail', kwargs={"pk": model.pk}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        links = ['signature:signature_list', 'signature:signature_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['signature_list']) == 10)

    def test_lists_all_signature(self):
        links = ['signature:signature_list', 'signature:signature_search']
        for link in links:
            resp = self.client.get(reverse(link) + '?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['signature_list']) == 9)
