from entities.setting_value import SettingValue


class Settings:
    MULTIPLY_OPERAND1_MIN = "multiply_operand1_min"
    MULTIPLY_OPERAND2_MIN = "multiply_operand2_min"
    MULTIPLY_OPERAND1_MAX = "multiply_operand1_max"
    MULTIPLY_OPERAND2_MAX = "multiply_operand2_max"
    MULTIPLY_TIMELIMIT = "multiply_timelimit"
    MULTIPLY_TIMER = "multiply_timer"
    DIVIDE_OPERAND1_MIN = "divide_operand1_min"
    DIVIDE_OPERAND2_MIN = "divide_operand2_min"
    DIVIDE_OPERAND1_MAX = "divide_operand1_max"
    DIVIDE_OPERAND2_MAX = "divide_operand2_max"
    DIVIDE_TIMER = "divide_timer"
    DIVIDE_TIMELIMIT = "divide_timelimit"
    ADD_OPERAND1_MIN = "add_operand1_min"
    ADD_OPERAND2_MIN = "add_operand2_min"
    ADD_OPERAND1_MAX = "add_operand1_max"
    ADD_OPERAND2_MAX = "add_operand2_max"
    ADD_TIMER = "add_timer"
    ADD_TIMELIMIT = "add_timelimit"
    SUB_OPERAND1_MIN = "sub_operand1_min"
    SUB_OPERAND2_MIN = "sub_operand2_min"
    SUB_OPERAND1_MAX = "sub_operand1_max"
    SUB_OPERAND2_MAX = "sub_operand2_max"
    SUB_TIMER = "sub_timer"
    SUB_TIMELIMIT = "sub_timelimit"

    def __init__(self):
        # These are the hard-coded default values that are used when even the default file
        # cannot be found.
        self._settings = {self.MULTIPLY_OPERAND1_MIN: SettingValue(2, self._sanitize_operand),
                          self.MULTIPLY_OPERAND2_MIN: SettingValue(2, self._sanitize_operand),
                          self.MULTIPLY_OPERAND1_MAX: SettingValue(9, self._sanitize_operand),
                          self.MULTIPLY_OPERAND2_MAX: SettingValue(9, self._sanitize_operand),
                          self.MULTIPLY_TIMELIMIT: SettingValue(10000, self._sanitize_timelimit),
                          self.MULTIPLY_TIMER: SettingValue(1, self._sanitize_timer),
                          self.DIVIDE_OPERAND1_MIN: SettingValue(2, self._sanitize_operand),
                          self.DIVIDE_OPERAND2_MIN: SettingValue(2, self._sanitize_operand),
                          self.DIVIDE_OPERAND1_MAX: SettingValue(9, self._sanitize_operand),
                          self.DIVIDE_OPERAND2_MAX: SettingValue(9, self._sanitize_operand),
                          self.DIVIDE_TIMELIMIT: SettingValue(10000, self._sanitize_timelimit),
                          self.DIVIDE_TIMER: SettingValue(1, self._sanitize_timer),
                          self.ADD_OPERAND1_MIN: SettingValue(2, self._sanitize_operand),
                          self.ADD_OPERAND2_MIN: SettingValue(2, self._sanitize_operand),
                          self.ADD_OPERAND1_MAX: SettingValue(500, self._sanitize_operand),
                          self.ADD_OPERAND2_MAX: SettingValue(500, self._sanitize_operand),
                          self.ADD_TIMELIMIT: SettingValue(10000, self._sanitize_timelimit),
                          self.ADD_TIMER: SettingValue(1, self._sanitize_timer),
                          self.SUB_OPERAND1_MIN: SettingValue(2, self._sanitize_operand),
                          self.SUB_OPERAND2_MIN: SettingValue(2, self._sanitize_operand),
                          self.SUB_OPERAND1_MAX: SettingValue(500, self._sanitize_operand),
                          self.SUB_OPERAND2_MAX: SettingValue(500, self._sanitize_operand),
                          self.SUB_TIMELIMIT: SettingValue(10000, self._sanitize_timelimit),
                          self.SUB_TIMER: SettingValue(1, self._sanitize_timer), }

    def get_settings_as_dict(self):
        return {key: setting.value for key, setting in self._settings.items()}

    def get_setting(self, setting):
        if setting not in self._settings:
            return None

        return self._settings[setting].value

    def set_setting(self, setting, value):
        if setting in self._settings:
            self._settings[setting].value = value

    def parse_and_set_setting(self, setting, value_str):
        if setting in self._settings:
            self._settings[setting].parse_and_set_value(value_str)

    def __str__(self):
        return self._settings.__str__()

    def set_settings_from_dict(self, new_settings):
        if not new_settings:
            return

        for setting, value in new_settings.items():
            self.parse_and_set_setting(setting, value)

    def _sanitize_operand(self, operand):
        return operand if (2 <= operand <= 1000) else 10

    def _sanitize_timelimit(self, timelimit):
        return timelimit if (100 <= timelimit <= 100000) else 10000

    def _sanitize_timer(self, timer):
        return timer if (0 <= timer <= 1) else 0

    def __eq__(self, other):
        if self._settings == other._settings:
            return True

        return False
