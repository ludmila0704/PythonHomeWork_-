import pytest
from hwt3 import is_real_date


def test_date1():
    assert is_real_date('01.01.2015') == True


def test_date2():
    assert is_real_date('33.07.2015') == False


def test_date3():
    assert is_real_date('15.13.2000') == False


def test_date4():
    assert is_real_date('30.02.2020') == False


def test_date5():
    assert is_real_date('29.02.2004') == True


def test_date6():
    assert is_real_date('29.02.2000') == True


if __name__ == "__main__":
    pytest.main(['-vv'])
