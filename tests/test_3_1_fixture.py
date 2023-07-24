import pytest

from calculator import Calculator


# In this example, we are using the fixture
# to create a Calculator object before each test.

@pytest.fixture  # before each test ("function" scope is the default)
def calc():
    return Calculator()


def test_add(calc):
    actual_result = calc.add(10).result
    expected_result = 10

    assert actual_result == expected_result


def test_sub(calc):
    actual_result = calc.sub(5).result
    expected_result = -5

    assert actual_result == expected_result