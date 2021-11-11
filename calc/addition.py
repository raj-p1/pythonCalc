"""This is the addition calc that inherits the value A and value B from the calculation class"""
from calc.calculation import Calculation

#This is how you extend the Addition class with the Calculation
class Addition(Calculation):
    # pylint: disable=too-few-public-methods
    """The addition class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""
    def getresult(self):
        """define method"""
        #Use self to reference the data contained in the instance of the object.is encapsulation
        return self.value_a + self.value_b
