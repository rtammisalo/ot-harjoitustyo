class SettingValue:
    """A tiny wrapper class for generic setting values used by Settings.

    Has the ability to parse and sanitize values.
    """

    def __init__(self, value):
        """Initializes the SettingValue to a starting value.

        Args:
            value: Starting value.
        """
        self._value = self.sanitize(value)

    @staticmethod
    def parse(value):
        """Parses the value. Raises ValueError if parsing fails.
        """
        return int(value)

    @classmethod
    def sanitize(cls, value):
        """Returns the value as is.
        """
        return value

    @property
    def value(self):
        """Returns the value of the SettingValue.
        """
        return self._value

    @value.setter
    def value(self, new_value):
        """Sanitizes and sets the value.
        """
        self._value = self.sanitize(new_value)

    def parse_and_set_value(self, new_value_str):
        """Parses and sanitizes the new value string.
        """
        self.value = self.parse(new_value_str)

    def __eq__(self, other):
        if self._value == other._value:
            return True

        return False

    @staticmethod
    def _get_value_inside_range(value, min_value, max_value, default_value):
        if min_value <= value <= max_value:
            return value
        return default_value


class OperandSettingValue(SettingValue):
    """A class for holding operand-type values.
    """
    MIN_VALUE = 2
    MAX_VALUE = 1000
    DEFAULT_VALUE = 10

    @classmethod
    def sanitize(cls, value):
        """Returns a sanitized operand value between 2-1000. Defaults to 10
        """
        return cls._get_value_inside_range(value, cls.MIN_VALUE,
                                              cls.MAX_VALUE, cls.DEFAULT_VALUE)


class TimelimitSettingValue(SettingValue):
    """A class for holding timelimit-type values.
    """
    MIN_VALUE = 100
    MAX_VALUE = 100000
    DEFAULT_VALUE = 10000

    @classmethod
    def sanitize(cls, value):
        """Returns a sanitized timelimit between 100-100000. Defaults to 10000.
        """
        return cls._get_value_inside_range(value, cls.MIN_VALUE,
                                              cls.MAX_VALUE, cls.DEFAULT_VALUE)


class BooleanSettingValue(SettingValue):
    """A class for holding all boolean-type values.
    """
    MIN_VALUE = 0
    MAX_VALUE = 1
    DEFAULT_VALUE = 0

    @classmethod
    def sanitize(cls, value):
        """Returns a sanitized 'boolean'-value (actually just an int) with value 0 or 1.

        Defaults to 0.
        """
        return cls._get_value_inside_range(value, cls.MIN_VALUE,
                                              cls.MAX_VALUE, cls.DEFAULT_VALUE)
