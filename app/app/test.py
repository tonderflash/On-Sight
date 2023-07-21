"""
Sample test file
"""
from django.test import SimpleTestCase

from . import calc


class CalcTest(SimpleTestCase):
    def test_add(self):
        res = calc.add(2, 3)

        self.assertEqual(res, 5)

    def test_subtract(self):
        """test subtract function"""
        res = calc.subtract(5, 3)

        self.assertEqual(res, 2)
