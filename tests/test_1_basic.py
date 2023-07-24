from calculator import Calculator

# 1st approach: test functions
def test_add():
    calc = Calculator()

    actual_result = calc.add(10).result
    expected_result = 10

    assert actual_result == expected_result

def test_multiple_add():
    calc = Calculator()

    actual_result = calc.add(10).add(5).add(2).result
    expected_result = 17

    assert actual_result == expected_result


# 2nd approach: test class
class TestCalculator:
    def test_add(self):
        calc = Calculator()

        actual_result = calc.add(10).result
        expected_result = 10

        assert actual_result == expected_result

    def test_multiple_add(self):
        calc = Calculator()

        actual_result = calc.add(10).add(5).add(2).result
        expected_result = 27

        assert actual_result == expected_result


def test_basic():
    actual_result = 1
    expected_result = 1

    assert actual_result == expected_result