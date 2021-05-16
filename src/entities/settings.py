from entities.setting_value import OperandSettingValue, TimelimitSettingValue,\
    BooleanSettingValue


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
    HIDE_KEYPAD = "hide_keypad"

    def __init__(self):
        """Initializes the Settings object to default values. Safe to use as is.
        """
        # These are the hard-coded default values that are used when even the default file
        # cannot be found.
        self._settings = {self.MULTIPLY_OPERAND1_MIN: OperandSettingValue(2),
                          self.MULTIPLY_OPERAND2_MIN: OperandSettingValue(2),
                          self.MULTIPLY_OPERAND1_MAX: OperandSettingValue(9),
                          self.MULTIPLY_OPERAND2_MAX: OperandSettingValue(9),
                          self.MULTIPLY_TIMELIMIT: TimelimitSettingValue(10000),
                          self.MULTIPLY_TIMER: BooleanSettingValue(1),
                          self.DIVIDE_OPERAND1_MIN: OperandSettingValue(2),
                          self.DIVIDE_OPERAND2_MIN: OperandSettingValue(2),
                          self.DIVIDE_OPERAND1_MAX: OperandSettingValue(9),
                          self.DIVIDE_OPERAND2_MAX: OperandSettingValue(9),
                          self.DIVIDE_TIMELIMIT: TimelimitSettingValue(20000),
                          self.DIVIDE_TIMER: BooleanSettingValue(1),
                          self.ADD_OPERAND1_MIN: OperandSettingValue(2),
                          self.ADD_OPERAND2_MIN: OperandSettingValue(2),
                          self.ADD_OPERAND1_MAX: OperandSettingValue(500),
                          self.ADD_OPERAND2_MAX: OperandSettingValue(500),
                          self.ADD_TIMELIMIT: TimelimitSettingValue(15000),
                          self.ADD_TIMER: BooleanSettingValue(1),
                          self.SUB_OPERAND1_MIN: OperandSettingValue(2),
                          self.SUB_OPERAND2_MIN: OperandSettingValue(2),
                          self.SUB_OPERAND1_MAX: OperandSettingValue(500),
                          self.SUB_OPERAND2_MAX: OperandSettingValue(500),
                          self.SUB_TIMELIMIT: TimelimitSettingValue(15000),
                          self.SUB_TIMER: BooleanSettingValue(1),
                          self.RANDOM_USE_MULTIPLY: BooleanSettingValue(1),
                          self.RANDOM_USE_DIVIDE: BooleanSettingValue(1),
                          self.RANDOM_USE_ADD: BooleanSettingValue(1),
                          self.RANDOM_USE_SUB: BooleanSettingValue(1),
                          self.RANDOM_TIMELIMIT: TimelimitSettingValue(20000),
                          self.RANDOM_TIMER: BooleanSettingValue(1),
                          self.HIDE_KEYPAD: BooleanSettingValue(1) }

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

        Raises:
            ValueError: The value could not be parsed.
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

        Raises:
            ValueError: One of the values could not be parsed.
        """
        if not new_settings:
            return

        for setting, value in new_settings.items():
            self.parse_and_set_setting(setting, value)

    def __eq__(self, other):
        if self._settings == other._settings:
            return True

        return False
