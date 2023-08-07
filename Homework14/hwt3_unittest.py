import unittest

from hwt3 import is_real_date


class TestCaseDate(unittest.TestCase):
    def test_date_1(self):
        self.assertTrue(is_real_date('01.01.2015'))

    def test_date_2(self):
        self.assertFalse(is_real_date('33.07.2015'))

    def test_date_3(self):
        self.assertFalse(is_real_date('15.13.2000'))

    def test_date_4(self):
        self.assertFalse(is_real_date('30.02.2020'))

    def test_date_5(self):
        self.assertTrue(is_real_date('29.02.2004'))

    def test_date_6(self):
        self.assertTrue(is_real_date('29.02.2000'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
