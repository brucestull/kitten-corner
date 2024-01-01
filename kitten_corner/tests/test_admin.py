from django.test import TestCase

from kitten_corner.models import Kitten
from kitten_corner.admin import KittenAdmin


class KittenAdminTestCase(TestCase):
    """Test the KittenAdmin class."""

    def test_search_fields(self):
        self.assertEqual(KittenAdmin.search_fields, ("name", "age"))

    def test_list_display(self):
        self.assertEqual(KittenAdmin.list_display, ("name", "age"))

    def test_ordering(self):
        self.assertEqual(KittenAdmin.ordering, ("name",))
