from django.test import TestCase
from ..models import References
from django.urls import reverse
import warnings



class referencesViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_of_references = 149
        for references_num in range(number_of_references):
            References.objects.create(name='Christian %s' % references_num,)

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        links = ['catalog:references_list', 'catalog:references_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['references_list']) == 10)

    def test_lists_all_references(self):
        warnings.filterwarnings(action="ignore")
        links = ['catalog:references_list', 'catalog:references_search']
        for link in links:
            resp = self.client.get(reverse(link)+'?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['references_list']) == 9)
