class SettingValue:
    def __init__(self, value, sanitize):
        self._value = sanitize(value)
        self._sanitize = sanitize
        self._parse = int

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = self._sanitize(new_value)

    def parse_and_set_value(self, new_value_str):
        self.value = self._parse(new_value_str)

    def __eq__(self, other):
        if self._value == other._value:
            return True

        return False
