"""Subtraction file"""
from calc.calculations.calculation import Calculation
class Subtraction(Calculation):
    # pylint: disable=too-few-public-methods
    """This is the subtraction calc that inherits the value A,value B from the calculation class"""
    def getresult(self):
        #Use self to reference the data contained in the instance of the object.is encapsulation
        """define method"""
        total_subtraction = 0.0
        for value in self.values:
            total_subtraction = total_subtraction - value
        return total_subtraction
