from django.test import TestCase
from workstation.models import *
from django.urls import reverse

class workstationViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_workstation = 149
        for workstation_num in range(number_of_workstation):
            workstation.objects.create(name='Christian %s' % workstation_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('workstation/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('workstation'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('workstation'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'workstation/workstation_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('workstation'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['workstation_list']) == 10)

    def test_lists_all_workstation(self):
        resp = self.client.get(reverse('workstation')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['workstation_list']) == 9)

class monitorViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_monitor = 149
        for monitor_num in range(number_of_monitor):
            monitor.objects.create(name='Christian %s' % monitor_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/monitor/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('monitor'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('monitor'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/workstation/monitor_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('monitor'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['monitor_list']) == 10)

    def test_lists_all_workstation(self):
        resp = self.client.get(reverse('monitor')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['monitor_list']) == 9)

class motherboardViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_motherboard = 149
        for motherboard_num in range(number_of_motherboard):
            motherboard.objects.create(name='Christian %s' % motherboard_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/motherboard/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('motherboard'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('motherboard'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/workstation/motherboard_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('motherboard'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['motherboard_list']) == 10)

    def test_lists_all_workstation(self):
        resp = self.client.get(reverse('motherboard')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['motherboard_list']) == 9)

class cpuViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_cpu = 149
        for cpu_num in range(number_of_cpu):
            cpu.objects.create(name='Christian %s' % cpu_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/cpu/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('cpu'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('cpu'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/workstation/cpu_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('cpu'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['cpu_list']) == 10)

    def test_lists_all_cpu(self):
        resp = self.client.get(reverse('cpu')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['cpu_list']) == 9)

class gpuViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_gpu = 149
        for gpu_num in range(number_of_gpu):
            gpu.objects.create(name='Christian %s' % gpu_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/gpu/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('gpu'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('gpu'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/workstation/gpu_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('gpu'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['gpu_list']) == 10)

    def test_lists_all_gpu(self):
        resp = self.client.get(reverse('gpu')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['gpu_list']) == 9)
    
class ramViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_ram = 149
        for ram_num in range(number_of_ram):
            ram.objects.create(name='Christian %s' % ram_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/ram/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('ram'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('ram'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/workstation/ram_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('ram'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['ram_list']) == 10)

    def test_lists_all_ram(self):
        resp = self.client.get(reverse('ram')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['ram_list']) == 9)

class ssdViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_ssd = 149
        for ssd_num in range(number_of_ssd):
            ssd.objects.create(name='Christian %s' % ssd_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/ssd/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('ssd'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('ssd'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/workstation/ssd_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('ssd'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['ssd_list']) == 10)

    def test_lists_all_ssd(self):
        resp = self.client.get(reverse('ssd')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['ssd_list']) == 9)

class hddViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_hdd = 149
        for hdd_num in range(number_of_hdd):
            hdd.objects.create(name='Christian %s' % hdd_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/hdd/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('hdd'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('hdd'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/workstation/hdd_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('hdd'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['hdd_list']) == 10)

    def test_lists_all_hdd(self):
        resp = self.client.get(reverse('hdd')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['hdd_list']) == 9)

class dcpowerViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_dcpower = 149
        for dcpower_num in range(number_of_dcpower):
            dcpower.objects.create(name='Christian %s' % dcpower_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/dcpower/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('dcpower'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('dcpower'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/workstation/dcpower_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('dcpower'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['dcpower_list']) == 10)

    def test_lists_all_dcpower(self):
        resp = self.client.get(reverse('dcpower')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['dcpower_list']) == 9)

class keyBoardViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_keyBoard = 149
        for keyBoard_num in range(number_of_keyBoard):
            keyBoard.objects.create(name='Christian %s' % keyBoard_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/keyBoard/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('keyBoard'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('keyBoard'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/workstation/keyBoard_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('keyBoard'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['keyboard_list']) == 10)

    def test_lists_all_keyBoard(self):
        resp = self.client.get(reverse('keyBoard')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['keyboard_list']) == 9)

class mouseViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_mouse = 149
        for mouse_num in range(number_of_mouse):
            mouse.objects.create(name='Christian %s' % mouse_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/mouse/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('mouse'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('mouse'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/workstation/mouse_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('mouse'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['mouse_list']) == 10)

    def test_lists_all_mouse(self):
        resp = self.client.get(reverse('mouse')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['mouse_list']) == 9)
