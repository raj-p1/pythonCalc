"""This file tests Addition of numbers"""
from calc.calculations.addition import Addition

def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    numbers_data = (5.0,10.0)
    addition = Addition(numbers_data)
    #Assert statement
    assert addition.getresult() == 15.0
