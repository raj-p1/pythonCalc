""" This is the increment function"""
#first import the addition namespace
from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
from calc.division import Division

class Calculator:
    """ This is the Calculator class"""
    #this is the calculator static property
    history = []

    @staticmethod
    def get_history():
        """gets history"""
        get_history = Calculator.history
        return get_history

    @staticmethod
    def get_first_history_calculation():
        """gets first calculation from history"""
        return Calculator.history[0]

    @staticmethod
    def get_last_history_calculation():
        """gets the result of last calculation from history"""
        return Calculator.history[-1]

    @staticmethod
    def get_last_history_calculation_result():
        """gets the result of last calculation from history"""
        return Calculator.history[-1].getresult()

    @staticmethod
    def clear_history():
        """clear history"""
        Calculator.history.clear()
        return True

    @staticmethod
    def history_count():
        """keeps history count"""
        return len(Calculator.history)

    @staticmethod
    def add_calculation_to_history(calculation):
        """as"""
        Calculator.history.append(calculation)
        return True

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        addition = Addition(value_a, value_b)
        Calculator.history.append(addition)
        return addition.getresult()

    @staticmethod
    #this is an example of a calling method
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        subtraction = Subtraction(value_a, value_b)
        Calculator.history.append(subtraction)
        return subtraction.getresult()

    @staticmethod
    def multiply_number(value_a, value_b):
        """ multiply two numbers and store the result"""
        multiplication = Multiplication(value_a, value_b)
        Calculator.history.append(multiplication)
        return multiplication.getresult()

    @staticmethod
    def divide_number(value_a, value_b):
        """ divide two numbers and store the result"""
        # this is a shorthand way to create the division object and added it the history in one line
        division = Division(value_a, value_b)
        Calculator.history.append(division)
        return division.getresult()
