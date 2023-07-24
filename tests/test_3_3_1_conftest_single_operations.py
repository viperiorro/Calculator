import pytest

from calculator import Calculator

def test_add(calc):
    actual_result = calc.add(10).result
    expected_result = 10

    assert actual_result == expected_result


def test_sub(calc):
    actual_result = calc.sub(5).result
    expected_result = -5

    assert actual_result == expected_result