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
        self._settings_repository = SettingsRepository(Config.USER_DEFAULT_CSV_FILEPATH,
                                                       Config.USER_CSV_PATH)
        self._test_settings = self._settings_repository.get_settings_by_username(
            self.TEST_USER_NAME)
        self._test_settings.set_setting(
            Settings.MULTIPLY_TIMELIMIT, self._test_settings.get_setting(Settings.MULTIPLY_TIMELIMIT) + 1)
        self._default_settings = self._create_default_settings()

        self._write_settings(self.TEST_USER_NAME, self._test_settings)

    def _remove_file(self, file):
        if os.path.exists(file):
            os.remove(file)

    def _get_filepath(self, username):
        test_users_path = Config.USER_CSV_PATH
        return os.path.join(test_users_path, f"{username}.csv")

    def _remove_files(self):
        self._remove_file(self._get_filepath(self.TEST_USER_NAME))
        self._remove_file(self._get_filepath(self.TEST_NEW_USER_NAME))
        self._remove_file(Config.USER_DEFAULT_CSV_FILEPATH)
        self._remove_file(self._new_test_default_path)

    def test_created_settings_can_be_found(self):
        settings = self._settings_repository.get_settings_by_username(
            self.TEST_USER_NAME)
        self.assertEqual(self._test_settings, settings)

    def test_created_faulty_settings_are_not_loaded(self):
        with open(self._get_filepath(self.TEST_USER_NAME), mode="a") as settings_file:
            settings_file.write(f"{Settings.ADD_TIMELIMIT},5555,123")
            settings_file.write("false_setting_name,123")

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
        return User(username, "abc", settings)

    def _create_default_settings(self):
        changed_default_setting = Settings.SUB_TIMELIMIT
        changed_default_value = 12345

        with open(Config.USER_DEFAULT_CSV_FILEPATH, mode="a") as settings_file:
            settings_file.write(
                f"{changed_default_setting},{changed_default_value}")

        settings = Settings()
        settings.set_setting(changed_default_setting, changed_default_value)

        return settings
