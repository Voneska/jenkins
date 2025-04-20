import pytest
from main import bitnumb_to_decimal


def test_bitnumb_to_decimal_positive_number():
    assert bitnumb_to_decimal('0111010110') == 470


def test_bitnumb_to_decimal_negative_number():
    assert bitnumb_to_decimal('100110') == -26


def test_bitnumb_to_decimal_some_numbers():
    assert bitnumb_to_decimal('1111111111110001') == -16 # add error (1111111111110000)
    assert bitnumb_to_decimal('1000000000000001') == -32767
    assert bitnumb_to_decimal('0011001100110100 ') == 13108
    assert bitnumb_to_decimal('0101010101010101 ') == 21845


def test_bitnumb_to_decimal_not_binary():
    with pytest.raises(Exception, match='The value must be binary') as e:
        bitnumb_to_decimal('01lsf')
    print(e)


def test_bitnumb_to_decimal_wrong_len():
    with pytest.raises(Exception,
                       match='The value must be signed: min length = 2') as e:
        bitnumb_to_decimal('0')
    print(e)
