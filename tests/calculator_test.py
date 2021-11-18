"""Testing the Calculator"""
import pytest
from calc.main import Calculator
from calc.history.calculations import Calculations
@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()
#You have to add the fixture function as a parameter to the test that you want to use it with
def test_calculator_add_static(clear_history_fixture):
    """Testing the addition method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_numbers(5.0,10.0) == 15.0

def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtraction method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.subtract_numbers(10.0,5.0) == -5.0

def test_calculator_multiply_static(clear_history_fixture):
    """Testing the multiplication method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.multiply_numbers(5.0,10.0) == 50.0

def test_calculator_divide_static(clear_history_fixture):
    """Testing the division method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.divide_numbers(10.0, 5.0) == 0.5
