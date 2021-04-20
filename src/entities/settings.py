import copy


class Settings:
    MULTIPLY_OPERAND1_MIN = "multiply_operand1_min"
    MULTIPLY_OPERAND2_MIN = "multiply_operand2_min"
    MULTIPLY_OPERAND1_MAX = "multiply_operand1_max"
    MULTIPLY_OPERAND2_MAX = "multiply_operand2_max"
    MULTIPLY_TIMELIMIT = "multiply_timelimit"
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
        self._sanitize = {
            self.MULTIPLY_OPERAND1_MIN: self._sanitize_operand,
            self.MULTIPLY_OPERAND2_MIN: self._sanitize_operand,
            self.MULTIPLY_OPERAND1_MAX: self._sanitize_operand,
            self.MULTIPLY_OPERAND2_MAX: self._sanitize_operand,
            self.MULTIPLY_TIMELIMIT: self._sanitize_timelimit,
            self.MULTIPLY_TIMER: self._sanitize_timer
        }
        self._settings = {self.MULTIPLY_OPERAND1_MIN: 2,
                          self.MULTIPLY_OPERAND2_MIN: 2,
                          self.MULTIPLY_OPERAND1_MAX: 9,
                          self.MULTIPLY_OPERAND2_MAX: 9,
                          self.MULTIPLY_TIMELIMIT: 10000,
                          self.MULTIPLY_TIMER: 1}

    def get_settings_as_dict(self):
        return copy.deepcopy(self._settings)

    def get_setting(self, setting):
        if setting not in self._settings:
            return None

        return self._settings[setting]

    def set_setting(self, setting, value):
        self._settings[setting] = self._sanitize[setting](value)

    def __str__(self):
        return self._settings.__str__()

    def set_settings_from_dict(self, new_settings):
        if not new_settings:
            return

        for setting, value in new_settings.items():
            self.set_setting(setting, value)

    def _sanitize_operand(self, operand):
        return operand if (2 <= operand <= 1000) else 10

    def _sanitize_timelimit(self, timelimit):
        return timelimit if (100 <= timelimit <= 100000) else 10000

    def _sanitize_timer(self, timer):
        return timer if (0 <= timer <= 1) else 0
