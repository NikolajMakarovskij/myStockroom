from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from ..models import Manufacturer


class ManufacturerViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='user', is_superuser=True, is_staff=True)[0])

    @classmethod
    def setUpTestData(cls):
        number_of_manufacturer = 149
        for manufacturer_num in range(number_of_manufacturer):
            Manufacturer.objects.create(name='Christian %s' % manufacturer_num, )
        assert Manufacturer.objects.count() == 149

    def test_context_data_in_list(self):
        links = ['counterparty:manufacturer_list', 'counterparty:manufacturer_search']
        context_data = [
            {'data_key': 'title', 'data_value': 'Список производителей'},
            {'data_key': 'searchlink', 'data_value': 'counterparty:manufacturer_search'},
            {'data_key': 'add', 'data_value': 'counterparty:new-manufacturer'},
        ]
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            for each in context_data:
                self.assertTrue(each.get('data_key') in resp.context)
                self.assertTrue(resp.context[each.get('data_key')] == each.get('data_value'))

    def test_context_data_in_detail(self):
        context_data = [
            {'data_key': 'title', 'data_value': 'Производитель'},
            {'data_key': 'add', 'data_value': 'counterparty:new-manufacturer'},
            {'data_key': 'update', 'data_value': 'counterparty:manufacturer-update'},
            {'data_key': 'delete', 'data_value': 'counterparty:manufacturer-delete'},
        ]
        Manufacturer.objects.create(name='Christian_detail', )
        model = Manufacturer.objects.get(name='Christian_detail', )
        resp = self.client.get(reverse('counterparty:manufacturer-detail', kwargs={"pk": model.pk}))
        self.assertEqual(resp.status_code, 200)
        for each in context_data:
            self.assertTrue(each.get('data_key') in resp.context)

    def test_pagination_is_ten(self):
        links = ['counterparty:manufacturer_list', 'counterparty:manufacturer_search']
        for link in links:
            resp = self.client.get(reverse(link))
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['manufacturer_list']) == 20)

    def test_lists_all_manufacturer(self):
        links = ['counterparty:manufacturer_list', 'counterparty:manufacturer_search']
        for link in links:
            resp = self.client.get(reverse(link) + '?page=8')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] is True)
            self.assertTrue(len(resp.context['manufacturer_list']) == 9)
