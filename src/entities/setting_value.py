class SettingValue:
    """A tiny wrapper class for setting values used by Settings.

    Has the ability to parse and sanitize values.
    """

    def __init__(self, value, sanitize):
        """Initializes the SettingValue to a starting value and sanitizer-function.

        Args:
            value: Starting value.
            sanitize (function): The sanitizer function should take a value and return
                value that is within acceptable range or some other parameter.
        """
        self._value = sanitize(value)
        self._sanitize = sanitize
        self._parse = int

    @property
    def value(self):
        """Returns the value of the SettingValue.
        """
        return self._value

    @value.setter
    def value(self, new_value):
        """Sanitizes and sets the value.
        """
        self._value = self._sanitize(new_value)

    def parse_and_set_value(self, new_value_str):
        """Parses and sanitizes the new value string.
        """
        self.value = self._parse(new_value_str)

    def __eq__(self, other):
        if self._value == other._value:
            return True

        return False
