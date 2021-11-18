"""This file tests Subtraction of numbers"""
from calc.calculations.subtraction import Subtraction

def test_calculation_subtraction():
    """testing that our calculator has a static method for subtraction"""
    #Arrange
    numbers_data = (10.0,5.0)
    subtraction = Subtraction(numbers_data)
    #Assert statement
    assert subtraction.getresult() == -5.0
