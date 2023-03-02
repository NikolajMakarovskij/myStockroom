from django.test import TestCase
from ..models import Ups, Cassette
from django.urls import reverse

class upsViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_ups = 149
        for ups_num in range(number_of_ups):
            Ups.objects.create(name='Christian %s' % ups_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/ups/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('ups:ups_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('ups:ups_list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'ups/ups_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('ups:ups_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['ups_list']) == 10)

    def test_lists_all_ups(self):
        resp = self.client.get(reverse('ups:ups_list')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['ups_list']) == 9)

class cassetteViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_cassette = 149
        for cassette_num in range(number_of_cassette):
            Cassette.objects.create(name='Christian %s' % cassette_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/ups/cassette/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('ups:cassette_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('ups:cassette_list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'ups/cassette_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('ups:cassette_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['cassette_list']) == 10)

    def test_lists_all_cassette(self):
        resp = self.client.get(reverse('ups:cassette_list')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['cassette_list']) == 9)

