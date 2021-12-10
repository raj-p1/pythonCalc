"""Calculation history Class"""
from calc.calculations.addition  import Addition
from calc.calculations.division  import Division
from calc.calculations.subtraction  import Subtraction
from calc.calculations.multiplication import Multiplication
class Calculations:
    """Calculation history Class Method"""
    history = []
    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """clears history"""
        Calculations.history.clear()
        return True
    @staticmethod
    def count_history():
        """counts the length"""
        return len(Calculations.history)
    @staticmethod
    def get_last_calculation():
        """gets last calculation from the history"""
        return Calculations.history[-1]
    @staticmethod
    def get_last_calculation_result_value():
        """get last calculation"""
        calculation = Calculations.get_last_calculation()
        return calculation.get_result()
    @staticmethod
    def get_first_calculation():
        """gets first calculation from the history"""
        return Calculations.history[0]
    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]
    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return Calculations.history.append(calculation)
    @staticmethod
    def add_addition_calculation(values):
        """create an addition and add object to history using factory method create"""
        Calculations.add_calculation(Addition.create(values))
        return True
    @staticmethod
    def add_subtraction_calculation(values):
        """create a subtraction object to history using factory method create"""
        Calculations.add_calculation(Subtraction.create(values))
        return True
    @staticmethod
    def add_multiplication_calculation(values):
        """Add a multiplication object to history using factory method create"""
        Calculations.add_calculation(Multiplication.create(values))
        return True
    @staticmethod
    def add_division_calculation(values):
        """Add a division object to history using factory method create"""
        Calculations.add_calculation(Division.create(values))
        return True
