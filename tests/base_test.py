from unittest import TestCase
from script import Script


class TestScript(TestCase):
    """Test script.py"""

    def setUp(self):
        self.user_data = {}

    def test_get(self):
        """Test _get()"""
        self.assertEqual(Script()._get('key'), None)

    def test_set(self):
        """Test _set()"""
        self.assertEqual(Script()._set('key', 'value'), None)

    def test_unset(self):
        """Test _unset()"""
        self.assertEqual(Script()._unset('key'), None)

    def test_numequalto(self):
        """Test _numequalto()"""
        self.assertEqual(Script()._numequalto('value'), None)
