import unittest
from hwt1 import Person


class TestCaseDate(unittest.TestCase):
    def setUp(self) -> None:
        self.pers1 = Person('Ivanov', 'Ivan', 'Ivanovich', 35)
        self.pers2 = Person('Petrov', 'Petr', 'Petrovich', 2)

    def test_before_change(self):
        self.assertEqual(self.pers1.get_age(), 35)

    def test_full_name(self):
        self.assertEqual(self.pers1.full_name(), 'Ivanov Ivan Ivanovich')

    def test_after_change(self):
        self.pers2.birthday()
        self.assertEqual(self.pers2.get_age(), 3)


if __name__ == '__main__':
    unittest.main(verbosity=2)
