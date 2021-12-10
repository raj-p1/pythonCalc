""" This is the increment function"""
#first import the addition namespace
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division
from calc.history.calculations import Calculations

class Calculator:
    """ This is the Calculator class"""
    #this is the calculator static property
    def add_numbers(tuple_values: tuple):
        """ adds a list of numbers"""
        Calculations.add_addition_calculation(tuple_values)
        return True

    @staticmethod
    def subtract_numbers(tuple_values: tuple):
        """ subtract a list of numbers from result"""
        Calculations.add_subtraction_calculation(tuple_values)
        return True

    @staticmethod
    def multiply_numbers(tuple_values: tuple):
        """ multiplies a number with the result"""
        Calculations.add_multiplication_calculation(tuple_values)
        return True

    @staticmethod
    def divide_numbers(tuple_values: tuple):
        """ Divides a number from the result"""
        Calculations.add_division_calculation(tuple_values)
        return True

    @staticmethod
    def get_last_result_value():
        """ This is the gets the result of the calculation"""
        return Calculations.get_last_calculation_result_value()
