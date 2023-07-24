# In this example, we are using the "calculator_object" fixture
# to create a Calculator object 1 time for all tests in this module.
# and the "calc" fixture to clear the result after each test.
import pytest

from calculator import Calculator


@pytest.fixture(scope="module")  # 1 time before all tests in this module
def calculator_object():
    return Calculator()


@pytest.fixture  # before each test ("function" scope is the default)
def calc(calculator_object):  # fixture can use other fixtures
    yield calculator_object  # yield is like return, but it keeps the object alive
    calculator_object.clear()  # clear the result after each test
