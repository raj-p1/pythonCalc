"""This file tests Addition of numbers"""
from pprint import pprint

from calc.calculations.addition import Addition
from calc.CSVReader import CSVReader


def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    # Arrange
    numbers_data = CSVReader("calc/CsvFiles/Addition.csv").data
    # Act
    for row in numbers_data:
        addition = Addition(row["Value 1"], row["Value 2"])
        assert addition.getresult() == int(row["Result"])
