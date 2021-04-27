import os
import unittest
from repositories.settings_repository import SettingsRepository
from config import Config
from entities.user import User
from entities.settings import Settings


class TestSettingsRepository(unittest.TestCase):
    TEST_USER_NAME = "testuser"
    TEST_NEW_USER_NAME = "newuser"
    TEST_USER_PASSWORD = "test_password"

    def setUp(self):
        self._new_test_default_path = f"{Config.USER_DEFAULT_CSV_FILEPATH}.test"
        self._remove_files()
        self._default_settings = self._create_default_settings()
        self._settings_repository = SettingsRepository(Config.USER_DEFAULT_CSV_FILEPATH,
                                                       Config.USER_CSV_PATH)
        self._test_settings = self._settings_repository.get_settings_by_username(
            self.TEST_USER_NAME)
        self._test_settings.set_setting(
            Settings.MULTIPLY_TIMELIMIT, self._test_settings.get_setting(Settings.MULTIPLY_TIMELIMIT) + 1)

        self._write_settings(self.TEST_USER_NAME, self._test_settings)

    def _remove_file(self, file):
        if os.path.exists(file):
            os.remove(file)

    def _remove_files(self):
        test_users_path = Config.USER_CSV_PATH
        self._remove_file(os.path.join(
            test_users_path, f"{self.TEST_USER_NAME}.csv"))
        self._remove_file(os.path.join(
            test_users_path, f"{self.TEST_NEW_USER_NAME}.csv"))
        self._remove_file(self._new_test_default_path)

    def test_created_settings_can_be_found(self):
        settings = self._settings_repository.get_settings_by_username(
            self.TEST_USER_NAME)
        self.assertEqual(self._test_settings, settings)

    def test_created_settings_are_set_to_default_values_from_file(self):
        settings = self._settings_repository.get_settings_by_username(
            self.TEST_NEW_USER_NAME)
        self.assertEqual(self._default_settings, settings)

    def test_changing_settings_only_affects_one_file(self):
        settings = self._settings_repository.get_settings_by_username(
            self.TEST_NEW_USER_NAME)
        settings.set_setting(Settings.MULTIPLY_OPERAND1_MIN, 2112)
        self._write_settings(self.TEST_NEW_USER_NAME, settings)

        other_settings = self._settings_repository.get_settings_by_username(
            self.TEST_USER_NAME)

        self.assertNotEqual(other_settings, settings)

    def test_settings_repository_can_create_new_settings_without_default_file(self):
        self.assertFalse(os.path.exists(self._new_test_default_path))
        no_default_repository = SettingsRepository(self._new_test_default_path,
                                                   Config.USER_CSV_PATH)
        settings = no_default_repository.get_settings_by_username(
            self.TEST_NEW_USER_NAME)

        self.assertEqual(Settings(), settings)

    def test_settings_repository_creates_a_new_default_file(self):
        self.assertFalse(os.path.exists(self._new_test_default_path))
        no_default_repository = SettingsRepository(self._new_test_default_path,
                                                   Config.USER_CSV_PATH)
        settings = no_default_repository.get_settings_by_username(
            self.TEST_NEW_USER_NAME)
        self.assertTrue(os.path.exists(self._new_test_default_path))

    def _write_settings(self, username, settings):
        self._settings_repository.save_user_settings(
            self._create_user(username, settings))

    def _create_user(self, username, settings):
        return User(username, "abc", 1, settings)

    def _create_default_settings(self):
        settings = Settings()
        setting_values = {Settings.MULTIPLY_OPERAND1_MIN: 2,
                          Settings.MULTIPLY_OPERAND2_MIN: 2,
                          Settings.MULTIPLY_OPERAND1_MAX: 9,
                          Settings.MULTIPLY_OPERAND2_MAX: 9,
                          Settings.MULTIPLY_TIMELIMIT: 10000,
                          Settings.MULTIPLY_TIMER: 1,
                          Settings.DIVIDE_OPERAND1_MIN: 2,
                          Settings.DIVIDE_OPERAND2_MIN: 2,
                          Settings.DIVIDE_OPERAND1_MAX: 9,
                          Settings.DIVIDE_OPERAND2_MAX: 9,
                          Settings.DIVIDE_TIMELIMIT: 10000,
                          Settings.DIVIDE_TIMER: 1,
                          Settings.ADD_OPERAND1_MIN: 2,
                          Settings.ADD_OPERAND2_MIN: 2,
                          Settings.ADD_OPERAND1_MAX: 500,
                          Settings.ADD_OPERAND2_MAX: 500,
                          Settings.ADD_TIMELIMIT: 10000,
                          Settings.ADD_TIMER: 1,
                          Settings.SUB_OPERAND1_MIN: 2,
                          Settings.SUB_OPERAND2_MIN: 2,
                          Settings.SUB_OPERAND1_MAX: 500,
                          Settings.SUB_OPERAND2_MAX: 500,
                          Settings.SUB_TIMELIMIT: 10000,
                          Settings.SUB_TIMER: 1}
        settings.set_settings_from_dict(setting_values)
        return settings
