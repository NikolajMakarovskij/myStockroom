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

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        links = ['workstation:workstation_list', 'workstation:workstation_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['workstation_list']) == 10)

    def test_lists_all_workstation(self):
        warnings.filterwarnings(action="ignore")
        links = ['workstation:workstation_list', 'workstation:workstation_search']
        for link in links:
            resp = self.client.get(reverse(link)+'?page=15')
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

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        links = ['workstation:monitor_list', 'workstation:monitor_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['monitor_list']) == 10)

    def test_lists_all_monitor(self):
        warnings.filterwarnings(action="ignore")
        links = ['workstation:monitor_list', 'workstation:monitor_search']
        for link in links:
            resp = self.client.get(reverse(link)+'?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['monitor_list']) == 9)

class keyBoardViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_of_monitor = 149
        for monitor_num in range(number_of_monitor):
            KeyBoard.objects.create(name='Christian %s' % monitor_num,)

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        links = ['workstation:keyBoard_list', 'workstation:keyBoard_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['keyboard_list']) == 10)

    def test_lists_all_keyBoards(self):
        warnings.filterwarnings(action="ignore")
        links = ['workstation:keyBoard_list', 'workstation:keyBoard_search']
        for link in links:
            resp = self.client.get(reverse(link)+'?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['keyboard_list']) == 9)

class mouseViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_of_monitor = 149
        for monitor_num in range(number_of_monitor):
            Mouse.objects.create(name='Christian %s' % monitor_num,)

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        links = ['workstation:mouse_list', 'workstation:mouse_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['mouse_list']) == 10)

    def test_lists_all_mouses(self):
        warnings.filterwarnings(action="ignore")
        links = ['workstation:mouse_list', 'workstation:mouse_search']
        for link in links:
            resp = self.client.get(reverse(link)+'?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['mouse_list']) == 9)