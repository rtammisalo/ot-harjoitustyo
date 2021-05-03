from entities.setting_value import SettingValue


class Settings:
    """A class for storing in-use user settings. Contains ways to access and safely change settings.
    """
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
    RANDOM_USE_MULTIPLY = "random_use_multiply"
    RANDOM_USE_DIVIDE = "random_use_divide"
    RANDOM_USE_ADD = "random_use_add"
    RANDOM_USE_SUB = "random_use_sub"
    RANDOM_TIMER = "random_timer"
    RANDOM_TIMELIMIT = "random_timelimit"

    def __init__(self):
        """Initializes the Settings object to default values. Safe to use as is.
        """
        # These are the hard-coded default values that are used when even the default file
        # cannot be found.
        self._settings = {self.MULTIPLY_OPERAND1_MIN: SettingValue(2, self._sanitize_operand),
                          self.MULTIPLY_OPERAND2_MIN: SettingValue(2, self._sanitize_operand),
                          self.MULTIPLY_OPERAND1_MAX: SettingValue(9, self._sanitize_operand),
                          self.MULTIPLY_OPERAND2_MAX: SettingValue(9, self._sanitize_operand),
                          self.MULTIPLY_TIMELIMIT: SettingValue(10000, self._sanitize_timelimit),
                          self.MULTIPLY_TIMER: SettingValue(1, self._sanitize_boolean),
                          self.DIVIDE_OPERAND1_MIN: SettingValue(2, self._sanitize_operand),
                          self.DIVIDE_OPERAND2_MIN: SettingValue(2, self._sanitize_operand),
                          self.DIVIDE_OPERAND1_MAX: SettingValue(9, self._sanitize_operand),
                          self.DIVIDE_OPERAND2_MAX: SettingValue(9, self._sanitize_operand),
                          self.DIVIDE_TIMELIMIT: SettingValue(10000, self._sanitize_timelimit),
                          self.DIVIDE_TIMER: SettingValue(1, self._sanitize_boolean),
                          self.ADD_OPERAND1_MIN: SettingValue(2, self._sanitize_operand),
                          self.ADD_OPERAND2_MIN: SettingValue(2, self._sanitize_operand),
                          self.ADD_OPERAND1_MAX: SettingValue(500, self._sanitize_operand),
                          self.ADD_OPERAND2_MAX: SettingValue(500, self._sanitize_operand),
                          self.ADD_TIMELIMIT: SettingValue(10000, self._sanitize_timelimit),
                          self.ADD_TIMER: SettingValue(1, self._sanitize_boolean),
                          self.SUB_OPERAND1_MIN: SettingValue(2, self._sanitize_operand),
                          self.SUB_OPERAND2_MIN: SettingValue(2, self._sanitize_operand),
                          self.SUB_OPERAND1_MAX: SettingValue(500, self._sanitize_operand),
                          self.SUB_OPERAND2_MAX: SettingValue(500, self._sanitize_operand),
                          self.SUB_TIMELIMIT: SettingValue(10000, self._sanitize_timelimit),
                          self.SUB_TIMER: SettingValue(1, self._sanitize_boolean),
                          self.RANDOM_USE_MULTIPLY: SettingValue(1, self._sanitize_boolean),
                          self.RANDOM_USE_DIVIDE: SettingValue(1, self._sanitize_boolean),
                          self.RANDOM_USE_ADD: SettingValue(1, self._sanitize_boolean),
                          self.RANDOM_USE_SUB: SettingValue(1, self._sanitize_boolean),
                          self.RANDOM_TIMELIMIT: SettingValue(10000, self._sanitize_timelimit),
                          self.RANDOM_TIMER: SettingValue(1, self._sanitize_boolean), }

    def get_settings_as_dict(self):
        """Returns settings as dict.

        Returns:
            dict: Settings as (setting name, setting value) pairs.
        """
        return {key: setting.value for key, setting in self._settings.items()}

    def get_setting(self, setting):
        """Returns the value of a setting, if it exists.

        Args:
            setting (str): Setting-name as a string.

        Returns:
            int: Value of the setting.
            None: No setting with the name.
        """
        if setting not in self._settings:
            return None

        return self._settings[setting].value

    def set_setting(self, setting, value):
        """Tries to set a setting to the given value.

        Args:
            setting (str): Setting-name as a string.
            value: Value of the setting.
        """
        if setting in self._settings:
            self._settings[setting].value = value

    def parse_and_set_setting(self, setting, value_str):
        """Tries to parse the value string for a setting value and set it.

        Args:
            setting (str): Setting-name as a string.
            value_str: The new value of the setting.
        """
        if setting in self._settings:
            self._settings[setting].parse_and_set_value(value_str)

    def __str__(self):
        return self._settings.__str__()

    def set_settings_from_dict(self, new_settings):
        """Tries to set all the (setting, new value) pairs.

        Args:
            new_settings (dict): A dict with setting-name string pairs as keys
                and new values as value.
        """
        if not new_settings:
            return

        for setting, value in new_settings.items():
            self.parse_and_set_setting(setting, value)

    def _sanitize_operand(self, operand):
        """Returns a sanitized operand between 2-1000. Defaults to 10
        """
        return operand if (2 <= operand <= 1000) else 10

    def _sanitize_timelimit(self, timelimit):
        """Returns a sanitized timelimit between 100-100000. Defaults to 10000.
        """
        return timelimit if (100 <= timelimit <= 100000) else 10000

    def _sanitize_boolean(self, timer):
        """Returns a sanitized 'boolean'-value (actually just an int) with value 0 or 1.

        Defaults to 0.
        """
        return timer if (0 <= timer <= 1) else 0

    def __eq__(self, other):
        if self._settings == other._settings:
            return True

        return False
