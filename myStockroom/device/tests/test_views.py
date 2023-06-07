from django.test import TestCase
from ..models import Device, Device_cat
from django.urls import reverse
import warnings

class deviceViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_device = 149
        for device_num in range(number_of_device):
            Device.objects.create(name='Christian %s' % device_num,)
        assert Device.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['device:device_list', 'device:device_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'Устройства'},
            {'data_key': 'searchlink', 'data_value': 'device:device_search'},
            {'data_key': 'add', 'data_value': 'device:new-device'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_context_data_in_detail(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'Устройство'},
            {'data_key': 'add', 'data_value': 'device:new-device'},
            {'data_key': 'update', 'data_value': 'device:device-update'},
            {'data_key': 'delete', 'data_value': 'device:device-delete'},
        ]
        Device.objects.create(name='Christian_detail',)
        model = Device.objects.get(name='Christian_detail',)
        resp = self.client.get(reverse('device:device-detail', kwargs={"pk": model.pk}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        links = ['device:device_list', 'device:device_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['device_list']) == 10)

    def test_lists_all_device(self):
        links = ['device:device_list', 'device:device_search']
        for link in links:
            resp = self.client.get(reverse(link)+'?page=15')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue( len(resp.context['device_list']) == 9)

class deviceCategoryViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_device = 149
        Device_cat.objects.create(name="some_category", slug="some_category")
        for device_num in range(number_of_device):
            Device.objects.create(name='Christian %s' % device_num, categories=Device_cat.objects.get(slug="some_category"))
        assert Device.objects.count() == 149
        assert Device_cat.objects.count() == 1

    def test_context_data_in_category(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'Устройства'},
            {'data_key': 'searchlink', 'data_value': 'device:device_search'},
            {'data_key': 'add', 'data_value': 'device:new-device'},
        ]
        resp = self.client.get(reverse('device:category', kwargs={"category_slug": Device_cat.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)
            self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('device:category', kwargs={"category_slug": Device_cat.objects.get(slug="some_category")}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['device_list']) == 10)

    def test_lists_all_device(self):
        resp = self.client.get(reverse('device:category', kwargs={"category_slug": Device_cat.objects.get(slug="some_category")})+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['device_list']) == 9)