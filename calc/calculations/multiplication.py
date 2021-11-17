"""Multiplication file"""
from calc.calculations.calculation import Calculation
class Multiplication(Calculation):
    # pylint: disable=too-few-public-methods
    """This is the multiplication calc being inherits the value A, B from the calculation class"""
    def getresult(self):
        #Use self to reference the data contained in the instance of the object.is encapsulation
        """define method"""
        initial_multiply = 1.0
        for value in self.values:
            initial_multiply = initial_multiply * value
        return initial_multiply
