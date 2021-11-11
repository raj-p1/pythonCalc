"""This is our calculation base class / Abstract Class"""
class Calculation:
    # pylint: disable=too-few-public-methods
    #contstructor and it is the first function called when an object of the class is instantiated
    """calc main file"""
    def __init__(self,value_a, value_b):
        #self references the instantiated object of the class
        #Instance properties being shared with the child classes (addition, subtraction, etc...)
        self.value_a = value_a
        self.value_b = value_b
