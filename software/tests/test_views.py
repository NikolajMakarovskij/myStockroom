from django.test import TestCase
from software.models import software, os
from django.urls import reverse

class softwareViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_software = 149
        for software_num in range(number_of_software):
            software.objects.create(name='Christian %s' % software_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/software/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('software:software'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('software:software'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'software/software_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('software:software'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['software_list']) == 10)

    def test_lists_all_software(self):
        resp = self.client.get(reverse('software:software')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['software_list']) == 9)

class OSViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_OS = 149
        for OS_num in range(number_of_OS):
            os.objects.create(name='Christian %s' % OS_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/software/OS/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('software:OS'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('software:OS'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'software/OS_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('software:OS'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['os_list']) == 10)

    def test_lists_all_OS(self):
        resp = self.client.get(reverse('software:OS')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['os_list']) == 9)