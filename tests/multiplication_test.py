"""This file tests Multiplication of numbers"""
from calc.calculations.multiplication import Multiplication

def test_calculation_multiplication():
    """testing that our calculator has a static method for multiplication"""
    #Arrange
    numbers_data = (5.0,10.0)
    multiplication = Multiplication(numbers_data)
    #Assert statement
    assert multiplication.getresult() == 50
