import unittest
from entities.setting_value import OperandSettingValue, TimelimitSettingValue, \
    BooleanSettingValue


def parse_set_value(setting_value, value):
    """Parses and tries to set value. Returns True if successful.
    """
    setting_value.parse_and_set_value(str(value))
    return setting_value.value == int(value)


def set_value(setting_value, value):
    """Tries to set value. Return True if successful.
    """
    setting_value.value = value
    return setting_value.value == value


class TestOperandSettingValue(unittest.TestCase):
    def setUp(self):
        self._operand = OperandSettingValue(OperandSettingValue.MIN_VALUE + 2)

    def test_operand_does_not_parse_and_set_outside_acceptable_range(self):
        self.assertFalse(parse_set_value(
            self._operand, OperandSettingValue.MIN_VALUE - 1))

    def test_operand_does_not_set_outside_acceptable_range(self):
        self.assertFalse(
            set_value(self._operand, OperandSettingValue.MIN_VALUE - 1))

    def test_operand_parses_and_sets_within_acceptable_range(self):
        self.assertTrue(parse_set_value(
            self._operand, OperandSettingValue.MIN_VALUE + 1))

    def test_operand_sets_within_acceptable_range(self):
        self.assertTrue(
            set_value(self._operand, OperandSettingValue.MIN_VALUE + 1))


class TestTimelimitSettingValue(unittest.TestCase):
    def setUp(self):
        self._timelimit = TimelimitSettingValue(
            TimelimitSettingValue.MIN_VALUE + 2)

    def test_timelimit_does_not_parse_and_set_outside_acceptable_range(self):
        self.assertFalse(parse_set_value(
            self._timelimit, TimelimitSettingValue.MIN_VALUE - 1))

    def test_timelimit_does_not_set_outside_acceptable_range(self):
        self.assertFalse(
            set_value(self._timelimit, TimelimitSettingValue.MIN_VALUE - 1))

    def test_timelimit_parses_and_sets_within_acceptable_range(self):
        self.assertTrue(parse_set_value(self._timelimit,
                        TimelimitSettingValue.MIN_VALUE + 1))

    def test_timelimit_sets_within_acceptable_range(self):
        self.assertTrue(set_value(self._timelimit,
                        TimelimitSettingValue.MIN_VALUE + 1))


class TestBooleanSettingValue(unittest.TestCase):
    def setUp(self):
        self._boolean = BooleanSettingValue(1)

    def test_boolean_does_not_parse_and_set_outside_acceptable_range(self):
        self.assertFalse(parse_set_value(self._boolean, 3))

    def test_boolean_does_not_set_outside_acceptable_range(self):
        self.assertFalse(set_value(self._boolean, 3))

    def test_boolean_parses_and_sets_within_acceptable_range(self):
        self.assertTrue(parse_set_value(self._boolean, 0))

    def test_boolean_sets_within_acceptable_range(self):
        self.assertTrue(set_value(self._boolean, 0))
