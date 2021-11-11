"""Testing the Calculator"""
import pprint
from calculator.main import Calculator
def test_calculator_add():
    """Test code for addition of two numbers"""
    assert Calculator.clear_history()
    assert Calculator.add_number(0, 1) == 1
    assert Calculator.add_number(9, 10) == 19
    assert Calculator.history_count() == 2
    assert Calculator.get_last_history_calculation_result() == 19
    pprint.pprint(Calculator.history)

def test_calculator_subtract():
    """Test code for subtraction of two numbers"""
    assert Calculator.clear_history()
    assert Calculator.subtract_number(7, 5) == 2
    assert Calculator.subtract_number(17, 10) == 7
    assert Calculator.history_count() == 2
    assert Calculator.get_last_history_calculation_result() == 7

def test_calculator_multiply():
    """ Test code for multiplication of two numbers"""
    assert Calculator.clear_history()
    assert Calculator.multiply_number(10, 3) == 30
    assert Calculator.history_count() == 1
    assert Calculator.get_last_history_calculation_result() == 30

def test_calculator_divide():
    """ Test code for division of two numbers"""
    assert Calculator.clear_history()
    assert Calculator.divide_number(6, 3) == 2
    assert Calculator.history_count() == 1
    assert Calculator.get_last_history_calculation_result() == 2

def test_get_history():
    """Test code for the history of calculation"""
    assert Calculator.add_number(0, 1) == 1
    assert Calculator.subtract_number(7, 5) == 2
    assert Calculator.divide_number(6, 3) == 2
    assert Calculator.get_history()

def test_get_last_calculation():
    """Test code to get the last calculation"""
    assert Calculator.add_number(0, 1) == 1
    assert Calculator.subtract_number(7, 5) == 2
    assert Calculator.divide_number(6, 3) == 2
    calculation = Calculator.history[-1].getresult()
    assert calculation == 2

def test_add_calculation_to_history_():
    """Test code to check the addition of history"""
    assert Calculator.clear_history()
    previous_count = Calculator.history_count()
    assert Calculator.add_number(5, 7) == 12
    updated_count = Calculator.history_count()
    assert updated_count == previous_count + 1

def test_get_first_calculation():
    """Test code to view 1st calculation in history"""
    assert Calculator.get_first_history_calculation() == Calculator.history[0]


def test_get_last_calculation_object():
    """Test code for verifying last calculation in the history"""
    assert Calculator.get_last_history_calculation() == Calculator.history[-1]
