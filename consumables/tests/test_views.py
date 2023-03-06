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

    def test_view_url_exists_at_desired_location(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get('/consumables/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('consumables:consumables_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('consumables:consumables_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'consumables/consumables_list.html')

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