from django.test import TestCase
from catalog.models.models import *
from django.urls import reverse

class RoomListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_rooms = 149
        for room_num in range(number_of_rooms):
            Room.objects.create(name='Christian %s' % room_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/room/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('room'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('room'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/workplace/room_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('room'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['room_list']) == 10)

    def test_lists_all_room(self):
        resp = self.client.get(reverse('room')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['room_list']) == 9)

class WorkplaceListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_workplaces = 149
        for Workplace_num in range(number_of_workplaces):
            Workplace.objects.create(name='Christian %s' % Workplace_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/workplace/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('workplace'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('workplace'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/workplace/workplace_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('workplace'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['workplace_list']) == 10)

    def test_lists_all_workplaces(self):
        resp = self.client.get(reverse('workplace')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['workplace_list']) == 9)

class EmployeeListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_employees = 149
        for employee_num in range(number_of_employees):
            Employee.objects.create(name='Christian %s' % employee_num,)

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

        self.assertTemplateUsed(resp, 'catalog/workstation_list.html')

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

        self.assertTemplateUsed(resp, 'catalog/printer_list.html')

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

class digitalSignatureViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_digitalSignature = 149
        for digitalSignature_num in range(number_of_digitalSignature):
            digitalSignature.objects.create(name='Christian %s' % digitalSignature_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/digital_signature/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('digital-signature'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('digital-signature'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/digitalsignature_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('digital-signature'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['digitalsignature_list']) == 10)

    def test_lists_all_signature(self):
        resp = self.client.get(reverse('digital-signature')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['digitalsignature_list']) == 9)

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

        self.assertTemplateUsed(resp, 'catalog/software_list.html')

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