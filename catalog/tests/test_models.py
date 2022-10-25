"""
from django.test import TestCase

from catalog.models import *

class WorkstationModelTest(TestCase):

    @classmethod
    def test_get_absolute_url(self):
        author=workstation.objects.get()
        #This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(),'/catalog/workstation/')
"""