import os
import unittest
from database import Database
from repositories.user_repository import UserRepository
from services.main_service import MainService, InvalidUserException, InvalidPasswordException
from tests.repositories.fake_user_repository import FakeUserRepository
from config import Config


class TestMainService(unittest.TestCase):
    TEST_USER_NAME = "testuser"
    TEST_USER_PASSWORD = "test_password"

    def setUp(self):
        self._fake_user_repository = FakeUserRepository()
        self._fake_service = MainService(self._fake_user_repository)
        self._fake_service.create(TestMainService.TEST_USER_NAME,
                                  TestMainService.TEST_USER_PASSWORD)
        self._fake_service.logout()
        self._remove_files()

    def _remove_file(self, file):
        if os.path.exists(file):
            os.remove(file)

    def _remove_files(self):
        test_users_path = Config.USER_CSV_PATH
        self._remove_file(os.path.join(
            test_users_path, f"{TestMainService.TEST_USER_NAME}.csv"))
        self._remove_file(os.path.join(test_users_path, "newuser.csv"))

    def test_cannot_log_in_with_nonexistant_user(self):
        with self.assertRaises(InvalidUserException):
            self._fake_service.login("nosuchuser", "password")

    def test_can_log_in_with_correct_password(self):
        try:
            self._fake_service.login(TestMainService.TEST_USER_NAME,
                                     TestMainService.TEST_USER_PASSWORD)
        except:
            self.assertTrue(False)

        user = self._fake_service.show_current_user()
        self.assertIsNotNone(user)
        self.assertEqual(TestMainService.TEST_USER_NAME, user.username)

    def test_cannot_log_in_with_incorrect_password(self):
        with self.assertRaises(InvalidPasswordException):
            self._fake_service.login(
                TestMainService.TEST_USER_NAME, "wrong_password")

    def test_can_create_new_user(self):
        try:
            self._fake_service.create("newuser", "password")
        except:
            self.assertTrue(False)

        created_user = self._fake_service.show_current_user()
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.username, "newuser")

    def test_cannot_create_user_with_small_name(self):
        with self.assertRaises(InvalidUserException):
            self._fake_service.create("a", "password")

    def test_cannot_create_user_with_spaces_in_password(self):
        with self.assertRaises(InvalidPasswordException):
            self._fake_service.create("newuser", "p a ss")

    def test_cannot_create_user_with_small_password(self):
        with self.assertRaises(InvalidPasswordException):
            self._fake_service.create("newuser", "a")

    def test_cannot_create_same_user_again(self):
        with self.assertRaises(InvalidUserException):
            self._fake_service.create(
                TestMainService.TEST_USER_NAME, "password")

    def test_logout_does_nothing_if_no_user(self):
        try:
            self._fake_service.logout()
        except:
            self.assertTrue(False)

        self.assertIsNone(self._fake_service.show_current_user())

    def test_cannot_create_user_with_nonascii_username(self):
        with self.assertRaises(InvalidUserException):
            self._fake_service.create("123 a1", "password")

    def test_saving_user_settings_calls_user_repository(self):
        self.assertEqual(0, self._fake_user_repository.settings_saved())
        self._fake_service.login(TestMainService.TEST_USER_NAME,
                                 TestMainService.TEST_USER_PASSWORD)
        self._fake_service.save_settings()
        self.assertEqual(1, self._fake_user_repository.settings_saved())

    def test_logging_in_as_user_loads_previous_settings_from_file(self):
        database = Database()
        database.init_database()
        main_service = MainService(UserRepository(database))
        main_service.create(TestMainService.TEST_USER_NAME,
                            TestMainService.TEST_USER_PASSWORD)
        user = main_service.show_current_user()
        self.assertNotEqual(user.settings.get_setting(
            user.settings.ADD_TIMELIMIT), 5555)
        user.settings.set_setting(user.settings.ADD_TIMELIMIT, 5555)
        main_service.save_settings()
        main_service.logout()

        main_service.login(
            TestMainService.TEST_USER_NAME, TestMainService.TEST_USER_PASSWORD)
        user = main_service.show_current_user()
        self.assertEqual(user.settings.get_setting(
            user.settings.ADD_TIMELIMIT), 5555)
