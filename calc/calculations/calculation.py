"""Calculation file"""
class Calculation:
    # pylint: disable=too-few-public-methods
    """calc main file"""
    def __init__(self,numbers: tuple):
        """ constructor method"""
        self.values = Calculation.list_data(numbers)
    @staticmethod
    def list_data(numbers):
        """ standardize values to list of floats"""
        list_data = []
        for item in numbers:
            list_data.append(float(item))
        return list_data
