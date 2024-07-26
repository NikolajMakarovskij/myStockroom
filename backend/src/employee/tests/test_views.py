from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from employee.models import Departament, Employee, Post


class EmployeeListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user', is_superuser=True, is_staff=True)[0])

    @classmethod
    def setUpTestData(cls):
        number_of_employees = 149
        for employee_num in range(number_of_employees):
            Employee.objects.create(name='Christian %s' % employee_num, )
        assert Employee.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['employee:employee_list', 'employee:employee_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'Список сотрудников'},
            {'data_key': 'searchlink', 'data_value': 'employee:employee_search'},
            {'data_key': 'add', 'data_value': 'employee:new-employee'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_context_data_in_detail(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'Сотрудник'},
            {'data_key': 'add', 'data_value': 'employee:new-employee'},
            {'data_key': 'update', 'data_value': 'employee:employee-update'},
            {'data_key': 'delete', 'data_value': 'employee:employee-delete'},
        ]
        Employee.objects.create(name='Christian_detail', )
        model = Employee.objects.get(name='Christian_detail', )
        resp = self.client.get(reverse('employee:employee-detail', kwargs={"pk": model.pk}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        links = ['employee:employee_list', 'employee:employee_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['employee_list']) == 20)

    def test_lists_all_employee(self):
        links = ['employee:employee_list', 'employee:employee_search']
        for link in links:
            resp = self.client.get(reverse(link) + '?page=8')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['employee_list']) == 9)


class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user', is_superuser=True, is_staff=True)[0])

    @classmethod
    def setUpTestData(cls):
        number_of_post = 149
        for post_num in range(number_of_post):
            Post.objects.create(name='Christian %s' % post_num, )
        assert Post.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['employee:post_list', 'employee:post_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'Список должностей'},
            {'data_key': 'searchlink', 'data_value': 'employee:post_search'},
            {'data_key': 'add', 'data_value': 'employee:new-post'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_context_data_in_detail(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'Должность'},
            {'data_key': 'add', 'data_value': 'employee:new-post'},
            {'data_key': 'update', 'data_value': 'employee:post-update'},
            {'data_key': 'delete', 'data_value': 'employee:post-delete'},
        ]
        Post.objects.create(name='Christian_detail', )
        model = Post.objects.get(name='Christian_detail', )
        resp = self.client.get(reverse('employee:post-detail', kwargs={"pk": model.pk}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        links = ['employee:post_list', 'employee:post_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['post_list']) == 20)

    def test_lists_all_signature(self):
        links = ['employee:post_list', 'employee:post_search']
        for link in links:
            resp = self.client.get(reverse(link) + '?page=8')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['post_list']) == 9)


class DepartamentViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user', is_superuser=True, is_staff=True)[0])

    @classmethod
    def setUpTestData(cls):
        number_of_departament = 149
        for departament_num in range(number_of_departament):
            Departament.objects.create(name='Christian %s' % departament_num, )
        assert Departament.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['employee:departament_list', 'employee:departament_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'Список отделов'},
            {'data_key': 'searchlink', 'data_value': 'employee:departament_search'},
            {'data_key': 'add', 'data_value': 'employee:new-departament'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_context_data_in_detail(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'Отдел'},
            {'data_key': 'add', 'data_value': 'employee:new-departament'},
            {'data_key': 'update', 'data_value': 'employee:departament-update'},
            {'data_key': 'delete', 'data_value': 'employee:departament-delete'},
        ]
        Departament.objects.create(name='Christian_detail', )
        model = Departament.objects.get(name='Christian_detail', )
        resp = self.client.get(reverse('employee:departament-detail', kwargs={"pk": model.pk}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        links = ['employee:departament_list', 'employee:departament_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['departament_list']) == 20)

    def test_lists_all_signature(self):
        links = ['employee:departament_list', 'employee:departament_search']
        for link in links:
            resp = self.client.get(reverse(link) + '?page=8')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['departament_list']) == 9)
