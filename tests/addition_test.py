"""This file tests Addition of numbers"""
from pprint import pprint
import os
from calc.calculations.addition import Addition
from calc.CSVReader import CSVReader
import pandas as pd

file_path = os.path.dirname(os.path.realpath(__file__))
def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    # Arrange
    #numbers_data = CSVReader("CsvFiles/Addition.csv").data
    filename = 'CsvFiles/Addition.csv'
    path = os.path.join(file_path, filename)
    d_frame = pd.read_csv(path)
    # Act
    for i, row in d_frame.iterrows():
        values = (row.Value1, row.Value2)
        #addition = Addition(row["Value 1"], row["Value 2"])
        #assert addition.getresult() == int(row["Result"])
        add = Addition.create(values)
        add_result = d_frame["Result"][i]
        #result = int(row["Result"])
        assert add.getresult() == add_result
