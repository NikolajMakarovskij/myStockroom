from django.test import TestCase
from software.models import Software, Os
from django.urls import reverse
import warnings

class softwareViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_of_software = 149
        for software_num in range(number_of_software):
            Software.objects.create(name='Christian %s' % software_num,)

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        links = ['software:software_list', 'software:software_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['software_list']) == 10)

    def test_lists_all_software(self):
        warnings.filterwarnings(action="ignore")
        links = ['software:software_list', 'software:software_search']
        for link in links:
            resp = self.client.get(reverse(link)+'?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['software_list']) == 9)

class OSViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_of_OS = 149
        for OS_num in range(number_of_OS):
            Os.objects.create(name='Christian %s' % OS_num,)

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        links = ['software:OS_list', 'software:OS_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['os_list']) == 10)

    def test_lists_all_OS(self):
        warnings.filterwarnings(action="ignore")
        links = ['software:OS_list', 'software:OS_search']
        for link in links:
            resp = self.client.get(reverse(link)+'?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['os_list']) == 9)