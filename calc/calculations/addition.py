"""Addition file"""
from calc.calculations.calculation import Calculation
class Addition(Calculation):
    # pylint: disable=too-few-public-methods
    """This is the addition calc that inherits the value A and value B from the calculation class"""
    def getresult(self):
        """define method"""
        #Use self to reference the data contained in the instance of the object.is encapsulation
        total_addition = 0.0
        for value in self.values:
            total_addition = value + total_addition
        return total_addition
