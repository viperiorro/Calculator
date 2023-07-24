import pytest

from calculator import Calculator


@pytest.mark.skip(reason='Division by zero is not implemented yet')
def test_divide_by_zero(calc):
    actual_result = calc.add(1).divide(0).result
    expected_result = 'inf'

    assert actual_result == expected_result


@pytest.mark.xfail(reason='String representation is not implemented yet')
def test_str(calc):
    actual_result = str(calc.add(5).sub(3))
    expected_result = 'Result is 2'

    assert actual_result == expected_result