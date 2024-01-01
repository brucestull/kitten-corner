from django.test import TestCase

from kitten_corner.models import Kitten


class KittenModelTestCase(TestCase):
    """Test the Kitten model."""

    def test_name_verbose_name(self):
        name_verbose_name = Kitten._meta.get_field("name").verbose_name
        self.assertEqual(name_verbose_name, "name")

    def test_name_is_char_field(self):
        name_field = Kitten._meta.get_field("name")
        self.assertEqual(name_field.__class__.__name__, "CharField")

    def test_age_verbose_name(self):
        age_verbose_name = Kitten._meta.get_field("age").verbose_name
        self.assertEqual(age_verbose_name, "age")

    def test_age_is_integer_field(self):
        age_field = Kitten._meta.get_field("age")
        self.assertEqual(age_field.__class__.__name__, "IntegerField")

    def test_dunder_string_method(self):
        kitten = Kitten.objects.create(name="Test", age=1)
        self.assertEqual(str(kitten), "Test : 1")
