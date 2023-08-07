import pytest
from hwt2 import psevdo_gen


def test_type_error():
    with pytest.raises(TypeError):
        psevdo_gen('r', 'text_psevdo.txt')


def test_value_error():
    with pytest.raises(ValueError):
        psevdo_gen(-6, 'text_psevdo.txt')


if __name__ == "__main__":
    pytest.main(['-vv'])
