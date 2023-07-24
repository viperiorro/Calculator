import pytest

from calculator import Calculator


def test_multiple_add(calc):
    actual_result = calc.add(5).add(5).add(5).result
    expected_result = 15

    assert actual_result == expected_result


def test_multiple_sub(calc):
    actual_result = calc.sub(5).sub(5).sub(5).result
    expected_result = -15

    assert actual_result == expected_result