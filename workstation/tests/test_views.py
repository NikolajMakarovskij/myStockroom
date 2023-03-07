from django.test import TestCase
from ..models import *
from django.urls import reverse
import warnings

class workstationViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_of_workstation = 149
        for workstation_num in range(number_of_workstation):
            Workstation.objects.create(name='Christian %s' % workstation_num,)

    def test_view_url_exists_at_desired_location(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get('/workstation/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('workstation:workstation_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('workstation:workstation_list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'workstation/workstation_list.html')

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('workstation:workstation_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['workstation_list']) == 10)

    def test_lists_all_workstation(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('workstation:workstation_list')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['workstation_list']) == 9)

class monitorViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_of_monitor = 149
        for monitor_num in range(number_of_monitor):
            Monitor.objects.create(name='Christian %s' % monitor_num,)

    def test_view_url_exists_at_desired_location(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get('/workstation/monitor/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('workstation:monitor'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('workstation:monitor'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'workstation/monitor_list.html')

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('workstation:monitor'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['monitor_list']) == 10)

    def test_lists_all_workstation(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('workstation:monitor')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['monitor_list']) == 9)

