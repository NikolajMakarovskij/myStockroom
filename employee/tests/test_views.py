from django.test import TestCase
from employee.models import Employee, Post, Departament
from django.urls import reverse
import warnings


class EmployeeListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_of_employees = 149
        for employee_num in range(number_of_employees):
            Employee.objects.create(name='Christian %s' % employee_num,)

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('employee:employee_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['employee_list']) == 10)

    def test_lists_all_employee(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('employee:employee_list')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['employee_list']) == 9)

class EmployeeSearchListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_of_employees = 149
        for employee_num in range(number_of_employees):
            Employee.objects.create(name='Christian %s' % employee_num,)

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('employee:employee_search'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['employee_list']) == 10)

    def test_lists_all_employee(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('employee:employee_search')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['employee_list']) == 9)

class postViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_of_post = 149
        for post_num in range(number_of_post):
            Post.objects.create(name='Christian %s' % post_num,)

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('employee:post_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['post_list']) == 10)

    def test_lists_all_signature(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('employee:post_list')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['post_list']) == 9)

class postSearchViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_of_post = 149
        for post_num in range(number_of_post):
            Post.objects.create(name='Christian %s' % post_num,)

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('employee:post_search'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['post_list']) == 10)

    def test_lists_all_signature(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('employee:post_search')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['post_list']) == 9)

class departamentViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_of_departament = 149
        for departament_num in range(number_of_departament):
            Departament.objects.create(name='Christian %s' % departament_num,)

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('employee:departament_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['departament_list']) == 10)

    def test_lists_all_signature(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('employee:departament_list')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['departament_list']) == 9)

class departamentSearchViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        warnings.filterwarnings(action="ignore")
        number_of_departament = 149
        for departament_num in range(number_of_departament):
            Departament.objects.create(name='Christian %s' % departament_num,)

    def test_pagination_is_ten(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('employee:departament_search'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['departament_list']) == 10)

    def test_lists_all_signature(self):
        warnings.filterwarnings(action="ignore")
        resp = self.client.get(reverse('employee:departament_search')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['departament_list']) == 9)