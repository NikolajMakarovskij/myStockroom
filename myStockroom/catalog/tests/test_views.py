from django.test import TestCase
from django.urls import reverse
from ..models import References


class ReferencesViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_references = 149
        for references_num in range(number_of_references):
            References.objects.create(name='Christian %s' % references_num, )
        assert References.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['catalog:references_list', 'catalog:references_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'Справочники'},
            {'data_key': 'searchlink', 'data_value': 'catalog:references_search'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        links = ['catalog:references_list', 'catalog:references_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['references_list']) == 10)

    def test_lists_all_references(self):
        links = ['catalog:references_list', 'catalog:references_search']
        for link in links:
            resp = self.client.get(reverse(link) + '?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['references_list']) == 9)
