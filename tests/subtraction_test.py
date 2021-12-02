"""This file tests Subtraction of numbers"""
from calc.calculations.subtraction import Subtraction
from calc.CSVReader import CSVReader


def test_calculation_subtraction():
    """testing that our calculator has a static method for subtraction"""
    # Arrange
    numbers_data = CSVReader("calc/CsvFiles/Addition.csv").data
    for row in numbers_data:
        subtraction = Subtraction(row["Value 1"], row["Value 2"])
        assert subtraction.getresult() == int(row["Result"])
