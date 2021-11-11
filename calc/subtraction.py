"""This is the subtraction calc that inherits the value A and value B from the calculation class"""
from calc.calculation import Calculation

#This is how you extend the Subtraction class with the Calculation
class Subtraction(Calculation):
    # pylint: disable=too-few-public-methods
    """The subtraction class has 1 method to get the result of the the calculation A,B come from
    the calculation parent class"""
    def getresult(self):
        #Use self to reference the data contained in the instance of the object.is encapsulation
        """define method"""
        return self.value_a - self.value_b
