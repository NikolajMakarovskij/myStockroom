from django.test import TestCase
from ..models import *
from django.urls import reverse
import warnings

class workstationViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_workstation = 149
        for workstation_num in range(number_of_workstation):
            Workstation.objects.create(name='Christian %s' % workstation_num,)
        assert Workstation.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['workstation:workstation_list', 'workstation:workstation_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'Рабочие станции'},
            {'data_key': 'searchlink', 'data_value': 'workstation:workstation_search'},
            {'data_key': 'add', 'data_value': 'workstation:new-workstation'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_context_data_in_detail(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'Рабочая станция'},
            {'data_key': 'add', 'data_value': 'workstation:new-workstation'},
            {'data_key': 'update', 'data_value': 'workstation:workstation-update'},
            {'data_key': 'delete', 'data_value': 'workstation:workstation-delete'},
        ]
        Workstation.objects.create(name='Christian_detail',)
        model = Workstation.objects.get(name='Christian_detail',)
        resp = self.client.get(reverse('workstation:workstation-detail', kwargs={"pk": model.pk}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        links = ['workstation:workstation_list', 'workstation:workstation_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['workstation_list']) == 10)

    def test_lists_all_workstation(self):
        links = ['workstation:workstation_list', 'workstation:workstation_search']
        for link in links:
            resp = self.client.get(reverse(link)+'?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['workstation_list']) == 9)

class workstationsCategoryViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_consumables = 149
        Categories.objects.create(name="some_category", slug="some_category")
        for consumables_num in range(number_of_consumables):
            Workstation.objects.create(name='Christian %s' % consumables_num, categories=Categories.objects.get(slug="some_category"))
        assert Workstation.objects.count() == 149
        assert Categories.objects.count() == 1

    def test_context_data_in_category(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'Рабочие станции'},
            {'data_key': 'searchlink', 'data_value': 'workstation:workstation_search'},
            {'data_key': 'add', 'data_value': 'workstation:new-workstation'},
        ]
        resp = self.client.get(reverse('workstation:category', kwargs={"category_slug": Categories.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('workstation:category', kwargs={"category_slug": Categories.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['workstation_list']) == 10)

    def test_lists_all_categories(self):
        resp = self.client.get(reverse('workstation:category', kwargs={"category_slug": Categories.objects.get(slug="some_category")})+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['workstation_list']) == 9)

class monitorViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_monitor = 149
        for monitor_num in range(number_of_monitor):
            Monitor.objects.create(name='Christian %s' % monitor_num,)
        assert Monitor.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['workstation:monitor_list', 'workstation:monitor_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'Мониторы'},
            {'data_key': 'searchlink', 'data_value': 'workstation:monitor_search'},
            {'data_key': 'add', 'data_value': 'workstation:new-monitor'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_context_data_in_detail(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'Монитор'},
            {'data_key': 'add', 'data_value': 'workstation:new-monitor'},
            {'data_key': 'update', 'data_value': 'workstation:monitor-update'},
            {'data_key': 'delete', 'data_value': 'workstation:monitor-delete'},
        ]
        Monitor.objects.create(name='Christian_detail',)
        model = Monitor.objects.get(name='Christian_detail',)
        resp = self.client.get(reverse('workstation:monitor-detail', kwargs={"pk": model.pk}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        links = ['workstation:monitor_list', 'workstation:monitor_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['monitor_list']) == 10)

    def test_lists_all_monitor(self):
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
        number_of_monitor = 149
        for monitor_num in range(number_of_monitor):
            KeyBoard.objects.create(name='Christian %s' % monitor_num,)
        assert KeyBoard.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['workstation:keyBoard_list', 'workstation:keyBoard_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'Клавиатуры'},
            {'data_key': 'searchlink', 'data_value': 'workstation:keyBoard_search'},
            {'data_key': 'add', 'data_value': 'workstation:new-keyBoard'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_context_data_in_detail(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'Клавиатура'},
            {'data_key': 'add', 'data_value': 'workstation:new-keyBoard'},
            {'data_key': 'update', 'data_value': 'workstation:keyBoard-update'},
            {'data_key': 'delete', 'data_value': 'workstation:keyBoard-delete'},
        ]
        KeyBoard.objects.create(name='Christian_detail',)
        model = KeyBoard.objects.get(name='Christian_detail',)
        resp = self.client.get(reverse('workstation:keyBoard-detail', kwargs={"pk": model.pk}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        links = ['workstation:keyBoard_list', 'workstation:keyBoard_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['keyboard_list']) == 10)

    def test_lists_all_keyBoards(self):
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
        number_of_monitor = 149
        for monitor_num in range(number_of_monitor):
            Mouse.objects.create(name='Christian %s' % monitor_num,)
        assert Mouse.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['workstation:mouse_list', 'workstation:mouse_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'Мыши'},
            {'data_key': 'searchlink', 'data_value': 'workstation:mouse_search'},
            {'data_key': 'add', 'data_value': 'workstation:new-mouse'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_context_data_in_detail(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'Мышь'},
            {'data_key': 'add', 'data_value': 'workstation:new-mouse'},
            {'data_key': 'update', 'data_value': 'workstation:mouse-update'},
            {'data_key': 'delete', 'data_value': 'workstation:mouse-delete'},
        ]
        Mouse.objects.create(name='Christian_detail',)
        model = Mouse.objects.get(name='Christian_detail',)
        resp = self.client.get(reverse('workstation:mouse-detail', kwargs={"pk": model.pk}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))


    def test_pagination_is_ten(self):
        links = ['workstation:mouse_list', 'workstation:mouse_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['mouse_list']) == 10)

    def test_lists_all_mouses(self):
        links = ['workstation:mouse_list', 'workstation:mouse_search']
        for link in links:
            resp = self.client.get(reverse(link)+'?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['mouse_list']) == 9)