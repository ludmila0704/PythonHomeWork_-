import unittest
from hwt2 import psevdo_gen


class TestCaseError(unittest.TestCase):
    def test_type_error(self):
        self.assertRaises(TypeError, psevdo_gen, 'r', 'text_psevdo.txt')

    def test_value_error(self):
        self.assertRaises(ValueError, psevdo_gen, -6, 'text_psevdo.txt')


if __name__ == '__main__':
    unittest.main(verbosity=2)
