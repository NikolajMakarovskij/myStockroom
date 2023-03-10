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
        assert Software.objects.count() == 149

    def test_context_data_in_list(self):
        warnings.filterwarnings(action="ignore")
        links = ['software:software_list', 'software:software_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'Список ПО'},
            {'data_key': 'searchlink', 'data_value': 'software:software_search'},
            {'data_key': 'add', 'data_value': 'software:new-software'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_context_data_in_detail(self):
        warnings.filterwarnings(action="ignore")
        context_data = [
            {'data_key': 'title', 'data_value': 'Програмное обеспечение'},
            {'data_key': 'add', 'data_value': 'software:new-software'},
            {'data_key': 'update', 'data_value': 'software:software-update'},
            {'data_key': 'delete', 'data_value': 'software:software-delete'},
        ]
        Software.objects.create(name='Christian_detail')
        model = Software.objects.get(name='Christian_detail')
        resp = self.client.get(reverse('software:software-detail', kwargs={"pk": model.pk}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

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
        assert Os.objects.count() == 149

    def test_context_data_in_list(self):
        warnings.filterwarnings(action="ignore")
        links = ['software:OS_list', 'software:OS_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'Список ОС'},
            {'data_key': 'searchlink', 'data_value': 'software:OS_search'},
            {'data_key': 'add', 'data_value': 'software:new-OS'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_context_data_in_detail(self):
        warnings.filterwarnings(action="ignore")
        context_data = [
            {'data_key': 'title', 'data_value': 'Операционная система'},
            {'data_key': 'add', 'data_value': 'software:new-OS'},
            {'data_key': 'update', 'data_value': 'software:OS-update'},
            {'data_key': 'delete', 'data_value': 'software:OS-delete'},
        ]
        Os.objects.create(name='Christian_detail')
        model = Os.objects.get(name='Christian_detail')
        resp = self.client.get(reverse('software:OS-detail', kwargs={"pk": model.pk}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

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