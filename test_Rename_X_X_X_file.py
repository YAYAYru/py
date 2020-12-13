from unittest import TestCase

from Rename_X_X_X_file import is_prime


class Test(TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(5))

    def test_is_not_prime(self):
        self.assertFalse(is_prime(6))
