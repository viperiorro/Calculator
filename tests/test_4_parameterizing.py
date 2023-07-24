import pytest

from calculator import Calculator


@pytest.mark.parametrize('a, b, expected_result', [
    (5, 5, 10),
    (10, 10, 20),
    (10, -5, 5),
    (-10, -5, -5),
    (0, 0, 0),
    (0, 5, 5),
    (0, -5, -5)
])
def test_add(calc, a, b, expected_result):
    actual_result = calc.add(a).add(b).result

    assert actual_result == expected_result