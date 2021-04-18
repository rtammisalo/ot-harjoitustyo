import copy

class Settings:
    MULTIPLY_OPERAND1_DIGITS = "multiply_operand1_digits"
    MULTIPLY_OPERAND2_DIGITS = "multiply_operand2_digits"
    MULTIPLY_TIMER = "multiply_timer"
    DIVIDE_OPERAND1_DIGITS = "divide_operand1_digits"
    DIVIDE_OPERAND2_DIGITS = "divide_operand2_digits"
    DIVIDE_TIMER = "divide_timer"
    ADD_OPERAND1_DIGITS = "add_operand1_digits"
    ADD_OPERAND2_DIGITS = "add_operand2_digits"
    ADD_TIMER = "add_timer"
    SUBSTRACT_OPERAND1_DIGITS = "substract_operand1_digits"
    SUBSTRACT_OPERAND2_DIGITS = "substract_operand2_digits"
    SUBSTRACT_TIMER = "substract_timer"

    def __init__(self):
        self._settings = {self.MULTIPLY_OPERAND1_DIGITS: 1,
                          self.MULTIPLY_OPERAND2_DIGITS: 1,
                          self.MULTIPLY_TIMER: 10000}

    def get_settings_as_dict(self):
        return copy.deepcopy(self._settings)

    def get_setting(self, setting):
        if setting not in self._settings:
            return None

        return self._settings[setting]

    def set_setting(self, setting, value):
        self._settings[setting] = value

    def __str__(self):
        return self._settings.__str__()
