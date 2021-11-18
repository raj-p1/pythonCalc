"""Division file"""
from calc.calculations.calculation import Calculation
class Division(Calculation):
    # pylint: disable=too-few-public-methods
    """This is the division calc being inherits the value A,value B from the calculation class"""
    def getresult(self):
        #Use self to reference the data contained in the instance of the object.is encapsulation
        """define method"""
        total_division = 1.0
        for value in self.values:
            total_division =  value / total_division
        return total_division
