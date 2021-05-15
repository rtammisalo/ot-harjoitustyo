import unittest
from entities.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self._no_hash_user = User("name", "password", None)
        self._hash_user = User("name", "password", None,
                               self._fake_hash_verify)
        self._verifier_called = False

    def test_correct_password_verifies_when_not_hashing(self):
        self.assertTrue(self._no_hash_user.verify_password("password"))

    def test_incorrect_password_does_not_verify_when_not_hashing(self):
        self.assertFalse(self._no_hash_user.verify_password("wrong_password"))

    def test_correct_password_verifies(self):
        self.assertTrue(self._hash_user.verify_password("password"))

    def test_incorrect_password_does_not_verify(self):
        self.assertFalse(self._hash_user.verify_password("wrong_password"))

    def test_hash_verifier_is_called_when_verifying_password(self):
        self._hash_user.verify_password("password")
        self.assertTrue(self._verifier_called)

    def _fake_hash_verify(self, password_hash, password):
        self._verifier_called = True

        if password_hash == password:
            return True

        return False
