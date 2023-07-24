import pytest

from calculator import Calculator

# For grouping tests, we can use markers.
# @pytest.mark.<markername>

# Tests for addition
@pytest.mark.addition_suite
def test_addition():
    calc = Calculator()

    actual_result = calc.add(10).result
    expected_result = 10

    assert actual_result == expected_result


@pytest.mark.addition_suite
@pytest.mark.multiple_suite
def test_multiple_addition():
    calc = Calculator()

    actual_result = calc.add(10).add(5).add(2).result
    expected_result = 17

    assert actual_result == expected_result


# Tests for subtraction
@pytest.mark.subtraction_suite
def test_subtraction():
    calc = Calculator()

    actual_result = calc.sub(5).result
    expected_result = -5

    assert actual_result == expected_result


@pytest.mark.subtraction_suite
@pytest.mark.multiple_suite
def test_multiple_subtraction():
    calc = Calculator()

    actual_result = calc.sub(5).sub(2).sub(1).result
    expected_result = -8

    assert actual_result == expected_result
