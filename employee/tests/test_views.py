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
        resp = self.client.get('/employee/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('employee:employee'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('employee:employee'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'employee/employee_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('employee:employee'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['employee_list']) == 10)

    def test_lists_all_employee(self):
        resp = self.client.get(reverse('employee:employee')+'?page=15')
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
        resp = self.client.get('/employee/post/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('employee:post'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('employee:post'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'employee/post_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('employee:post'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['post_list']) == 10)

    def test_lists_all_signature(self):
        resp = self.client.get(reverse('employee:post')+'?page=15')
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
        resp = self.client.get('/employee/departament/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('employee:departament'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('employee:departament'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'employee/departament_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('employee:departament'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['departament_list']) == 10)

    def test_lists_all_signature(self):
        resp = self.client.get(reverse('employee:departament')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['departament_list']) == 9)

