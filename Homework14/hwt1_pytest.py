import pytest
from hwt1 import Person


@pytest.fixture
def person():
    pers1 = Person('Ivanov', 'Ivan', 'Ivanovich', 35)
    return pers1


def test_before_change(person):
    assert person.get_age() == 35


def test_after_change(person):
    person.birthday()
    assert person.get_age() == 36


def test_full_name(person):
    assert person.full_name() == 'Ivanov Ivan Ivanovich'


if __name__ == "__main__":
    pytest.main(['-vv'])
