"""Calculation history Class"""
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
    def get_first_calculation():
        """gets first calculation from the history"""
        return Calculations.history[-1]
    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]
    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return Calculations.history.append(calculation)
