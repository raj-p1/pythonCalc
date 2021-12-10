"""Calculation file"""
class Calculation:
    # pylint: disable=too-few-public-methods
    """calc main file"""
    def __init__(self,values: tuple):
        """ constructor method"""
        self.values = Calculation.convert_args_to_tuple_float(values)

    @classmethod
    def create(cls, values: tuple):
        """ Factory method for creating values for each calculation  """
        return cls(values)

    @staticmethod
    def convert_args_to_tuple_float(values):
        """ standardize values to list of floats"""
        list_data_float = []
        for item in values:
            list_data_float.append(float(item))
        return list_data_float
