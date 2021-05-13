import unittest
from database import Database
from repositories.user_repository import UserRepository
from tests.repositories.fake_settings_repository import FakeSettingsRepository


class TestUserRepository(unittest.TestCase):
    TEST_USER_NAME = "testuser"
    TEST_USER_PASSWORD = "test_password"

    def setUp(self):
        database = Database()
        database.init_database()
        self._fake_settings_repository = FakeSettingsRepository()
        self._user_repository = UserRepository(
            database, self._fake_settings_repository)
        self._user_repository.create_user(
            TestUserRepository.TEST_USER_NAME, TestUserRepository.TEST_USER_PASSWORD)

    def test_cannot_create_existing_user(self):
        user = self._user_repository.create_user(
            TestUserRepository.TEST_USER_NAME, TestUserRepository.TEST_USER_PASSWORD)
        self.assertIsNone(user)

    def test_can_create_new_user(self):
        user = self._user_repository.create_user("newuser", "newpassword")
        self.assertIsNotNone(user)
        self.assertEqual("newuser", user.username)
        self.assertTrue(self._user_repository.verify_password(user, "newpassword"))

    def test_can_find_existing_user(self):
        user = self._user_repository.get_user(
            TestUserRepository.TEST_USER_NAME)
        self.assertIsNotNone(user)
        self.assertEqual(TestUserRepository.TEST_USER_NAME, user.username)
        self.assertTrue(self._user_repository.verify_password(user,
                                                       TestUserRepository.TEST_USER_PASSWORD))

    def test_cannot_find_nonexisting_user(self):
        user = self._user_repository.get_user("nosuchuser")
        self.assertIsNone(user)

    def test_user_gets_assigned_correct_settings(self):
        user = self._user_repository.get_user(
            TestUserRepository.TEST_USER_NAME)
        user_settings = self._fake_settings_repository.get_settings_by_username(
            TestUserRepository.TEST_USER_NAME)
        self.assertEqual(id(user.settings), id(user_settings))

    def test_saving_non_existing_user_settings_does_nothing(self):
        self._user_repository.save_settings(None)
        self.assertEqual(
            0, self._fake_settings_repository.user_settings_saved())

    def test_saving_user_settings_calls_settings_repository(self):
        user = self._user_repository.get_user(
            TestUserRepository.TEST_USER_NAME)
        self.assertEqual(
            0, self._fake_settings_repository.settings_saved_by_username(user.username))
        self._user_repository.save_settings(user)
        self.assertEqual(
            1, self._fake_settings_repository.settings_saved_by_username(user.username))
