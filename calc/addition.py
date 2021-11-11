"""Addition file"""
from calc.calculation import Calculation
class Addition(Calculation):
    # pylint: disable=too-few-public-methods
    """This is the addition calc that inherits the value A and value B from the calculation class"""
    def getresult(self):
        """define method"""
        #Use self to reference the data contained in the instance of the object.is encapsulation
        return self.value_a + self.value_b
