"""Testing the Calculator"""
import pprint
from calculator.main import Calculator



def test_calculator_add():
    """Testing the Add function of the calculator"""
    assert Calculator.clear_history()
    assert Calculator.add_number(0, 1) == 1
    assert Calculator.add_number(9, 10) == 19
    assert Calculator.history_count() == 2
    assert Calculator.get_last_history_calculation_result() == 19
    pprint.pprint(Calculator.history)


def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(7, 5) == 2

def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_number(10, 3) == 30

def test_calculator_divide():
    """ tests division of two numbers"""
    assert Calculator.divide_number(6, 3) == 2
