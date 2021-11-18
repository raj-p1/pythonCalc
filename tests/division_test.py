"""This file tests Division of numbers"""
from calc.calculations.division import Division

def test_calculation_division():
    """testing that our calculator has a static method for division"""
    #Arrange
    numbers_data = (10.0,5.0)
    division = Division(numbers_data)
    #Assert statement
    assert division.getresult() == 0.5
