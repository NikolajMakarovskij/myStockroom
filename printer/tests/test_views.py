from django.test import TestCase
from ..models import Printer
from django.urls import reverse

class printerViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_printer = 149
        for printer_num in range(number_of_printer):
            Printer.objects.create(name='Christian %s' % printer_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/printer/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('printer:printer_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('printer:printer_list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'printer/printer_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('printer:printer_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['printer_list']) == 10)

    def test_lists_all_printer(self):
        resp = self.client.get(reverse('printer:printer_list')+'?page=15')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['printer_list']) == 9)