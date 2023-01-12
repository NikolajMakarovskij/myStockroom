from django.test import TestCase
from employee.models import employee, post, departament
from django.urls import reverse


class EmployeeListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_employees = 149
        for employee_num in range(number_of_employees):
            employee.objects.create(name='Christian %s' % employee_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/employee/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('employee'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('employee'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/employee/employee_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('employee'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['employee_list']) == 10)

    def test_lists_all_employee(self):
        resp = self.client.get(reverse('employee')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['employee_list']) == 9)

class postViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_post = 149
        for post_num in range(number_of_post):
            post.objects.create(name='Christian %s' % post_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/post/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('post'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('post'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/employee/post_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('post'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['post_list']) == 10)

    def test_lists_all_signature(self):
        resp = self.client.get(reverse('post')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['post_list']) == 9)

class departamentViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_departament = 149
        for departament_num in range(number_of_departament):
            departament.objects.create(name='Christian %s' % departament_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/departament/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('departament'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('departament'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/employee/departament_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('departament'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['departament_list']) == 10)

    def test_lists_all_signature(self):
        resp = self.client.get(reverse('departament')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['departament_list']) == 9)

class softwareViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_software = 149
        for software_num in range(number_of_software):
            software.objects.create(name='Christian %s' % software_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/software/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('software'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('software'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'catalog/software/software_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('software'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['software_list']) == 10)

    def test_lists_all_software(self):
        resp = self.client.get(reverse('software')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['software_list']) == 9)

class manufacturerViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_manufacturer = 149
        for manufacturer_num in range(number_of_manufacturer):
            manufacturer.objects.create(name='Christian %s' % manufacturer_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/manufacturer/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('manufacturer'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('manufacturer'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/manufacturer_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('manufacturer'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['manufacturer_list']) == 10)

    def test_lists_all_manufacturer(self):
        resp = self.client.get(reverse('manufacturer')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['manufacturer_list']) == 9)

class OSViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_OS = 149
        for OS_num in range(number_of_OS):
            os.objects.create(name='Christian %s' % OS_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/OS/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('OS'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('OS'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/software/OS_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('OS'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['os_list']) == 10)

    def test_lists_all_OS(self):
        resp = self.client.get(reverse('OS')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['os_list']) == 9)

class workstationViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_workstation = 149
        for workstation_num in range(number_of_workstation):
            workstation.objects.create(name='Christian %s' % workstation_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/workstation/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('workstation'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('workstation'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/workstation/workstation_list.html')

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

class upsViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_ups = 149
        for ups_num in range(number_of_ups):
            ups.objects.create(name='Christian %s' % ups_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/ups/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('ups'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('ups'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/ups/ups_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('ups'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['ups_list']) == 10)

    def test_lists_all_ups(self):
        resp = self.client.get(reverse('ups')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['ups_list']) == 9)

class cassetteViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_cassette = 149
        for cassette_num in range(number_of_cassette):
            cassette.objects.create(name='Christian %s' % cassette_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/cassette/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('cassette'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('cassette'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/ups/cassette_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('cassette'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['cassette_list']) == 10)

    def test_lists_all_cassette(self):
        resp = self.client.get(reverse('cassette')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['cassette_list']) == 9)

class accumulatorViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_accumulator = 149
        for accumulator_num in range(number_of_accumulator):
            accumulator.objects.create(name='Christian %s' % accumulator_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/accumulator/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('accumulator'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('accumulator'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/ups/accumulator_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('accumulator'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['accumulator_list']) == 10)

    def test_lists_all_accumulator(self):
        resp = self.client.get(reverse('accumulator')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['accumulator_list']) == 9)

class printerViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_printer = 149
        for printer_num in range(number_of_printer):
            printer.objects.create(name='Christian %s' % printer_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/printer/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('printer'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('printer'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/printer/printer_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('printer'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['printer_list']) == 10)

    def test_lists_all_printer(self):
        resp = self.client.get(reverse('printer')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['printer_list']) == 9)

class cartridgeViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_cartridge = 149
        for cartridge_num in range(number_of_cartridge):
            cartridge.objects.create(name='Christian %s' % cartridge_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/cartridge/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('cartridge'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('cartridge'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/printer/cartridge_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('cartridge'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['cartridge_list']) == 10)

    def test_lists_all_cartridge(self):
        resp = self.client.get(reverse('cartridge')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['cartridge_list']) == 9)

class fotovalViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_fotoval = 149
        for fotoval_num in range(number_of_fotoval):
            fotoval.objects.create(name='Christian %s' % fotoval_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/fotoval/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('fotoval'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('fotoval'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/printer/fotoval_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('fotoval'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['fotoval_list']) == 10)

    def test_lists_all_fotoval(self):
        resp = self.client.get(reverse('fotoval')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['fotoval_list']) == 9)
    
class tonerViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_toner = 149
        for toner_num in range(number_of_toner):
            toner.objects.create(name='Christian %s' % toner_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/toner/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('toner'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('toner'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/printer/toner_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('toner'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['toner_list']) == 10)

    def test_lists_all_toner(self):
        resp = self.client.get(reverse('toner')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['toner_list']) == 9)

class signatureViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_signature = 149
        for signature_num in range(number_of_signature):
            signature.objects.create(name='Christian %s' % signature_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/signature/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('signature'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('signature'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/signature/signature_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('signature'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['signature_list']) == 10)

    def test_lists_all_signature(self):
        resp = self.client.get(reverse('signature')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['signature_list']) == 9)

class storageViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_storage = 149
        for storage_num in range(number_of_storage):
            storage.objects.create(name='Christian %s' % storage_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/storage/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('storage'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('storage'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/storage_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('storage'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['storage_list']) == 10)

    def test_lists_all_storage(self):
        resp = self.client.get(reverse('storage')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['storage_list']) == 9)