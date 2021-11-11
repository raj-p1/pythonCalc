"""Multiplication file"""
from calc.calculation import Calculation
class Multiplication(Calculation):
    # pylint: disable=too-few-public-methods
    """This is the multiplication calc being inherits the value A, B from the calculation class"""
    def getresult(self):
        #Use self to reference the data contained in the instance of the object.is encapsulation
        """define method"""
        return self.value_a * self.value_b
