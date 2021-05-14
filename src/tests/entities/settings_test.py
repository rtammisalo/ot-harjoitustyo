import unittest
from entities.setting_value import OperandSettingValue, TimelimitSettingValue
from entities.settings import Settings


class TestSettings(unittest.TestCase):
    OPERANDS = [Settings.MULTIPLY_OPERAND1_MIN,
                Settings.MULTIPLY_OPERAND1_MAX,
                Settings.MULTIPLY_OPERAND2_MIN,
                Settings.MULTIPLY_OPERAND2_MAX,
                Settings.DIVIDE_OPERAND1_MIN,
                Settings.DIVIDE_OPERAND1_MAX,
                Settings.DIVIDE_OPERAND2_MIN,
                Settings.DIVIDE_OPERAND2_MAX,
                Settings.ADD_OPERAND1_MIN,
                Settings.ADD_OPERAND1_MAX,
                Settings.ADD_OPERAND2_MIN,
                Settings.ADD_OPERAND2_MAX,
                Settings.SUB_OPERAND1_MIN,
                Settings.SUB_OPERAND1_MAX,
                Settings.SUB_OPERAND2_MIN,
                Settings.SUB_OPERAND2_MAX]
    TIMELIMITS = [Settings.MULTIPLY_TIMELIMIT,
                  Settings.DIVIDE_TIMELIMIT,
                  Settings.ADD_TIMELIMIT,
                  Settings.SUB_TIMELIMIT,
                  Settings.RANDOM_TIMELIMIT]
    BOOLEANS = [Settings.MULTIPLY_TIMER,
                Settings.DIVIDE_TIMER,
                Settings.ADD_TIMER,
                Settings.SUB_TIMER,
                Settings.RANDOM_TIMER,
                Settings.RANDOM_USE_MULTIPLY,
                Settings.RANDOM_USE_DIVIDE,
                Settings.RANDOM_USE_ADD,
                Settings.RANDOM_USE_SUB]

    def setUp(self):
        self._settings = Settings()

    def test_operands_are_not_set_to_bad_values(self):
        bad_values = {}
        for operand_name in self.OPERANDS:
            bad_values[operand_name] = "-1"

        self._settings.set_settings_from_dict(bad_values)

        for operand_name in self.OPERANDS:
            self.assertNotEqual(self._settings.get_setting(operand_name), -1)

    def test_operands_are_set_to_correct_values(self):
        good_values = {}
        for operand_name in self.OPERANDS:
            good_values[operand_name] = str(OperandSettingValue.MIN_VALUE)

        self._settings.set_settings_from_dict(good_values)

        for operand_name in self.OPERANDS:
            self.assertEqual(self._settings.get_setting(
                operand_name), OperandSettingValue.MIN_VALUE)

    def test_timelimits_are_not_set_to_bad_values(self):
        bad_values = {}
        for timelimit_name in self.TIMELIMITS:
            bad_values[timelimit_name] = "-1"

        self._settings.set_settings_from_dict(bad_values)

        for timelimit_name in self.TIMELIMITS:
            self.assertNotEqual(self._settings.get_setting(timelimit_name), -1)

    def test_timelimits_are_set_to_correct_values(self):
        good_values = {}
        for timelimit_name in self.TIMELIMITS:
            good_values[timelimit_name] = str(TimelimitSettingValue.MIN_VALUE)

        self._settings.set_settings_from_dict(good_values)

        for timelimit_name in self.TIMELIMITS:
            self.assertEqual(self._settings.get_setting(
                timelimit_name), TimelimitSettingValue.MIN_VALUE)

    def test_booleans_are_not_set_to_bad_values(self):
        bad_values = {}
        for boolean_name in self.BOOLEANS:
            bad_values[boolean_name] = "-1"

        self._settings.set_settings_from_dict(bad_values)

        for boolean_name in self.BOOLEANS:
            self.assertNotEqual(self._settings.get_setting(boolean_name), -1)

    def test_booleans_are_set_to_correct_values(self):
        good_values = {}
        for boolean_name in self.BOOLEANS:
            good_values[boolean_name] = "0"

        self._settings.set_settings_from_dict(good_values)

        for boolean_name in self.BOOLEANS:
            self.assertEqual(self._settings.get_setting(boolean_name), 0)

    def test_setting_non_existent_setting_name_changes_nothing(self):
        new_settings = Settings()
        new_settings.set_setting("no_such_name", 123)
        new_settings.parse_and_set_setting("no_such_name", "123")
        self.assertEqual(new_settings, self._settings)

    def test_accessing_non_existent_setting_returns_none(self):
        self.assertIsNone(self._settings.get_setting("no_such_name"))
