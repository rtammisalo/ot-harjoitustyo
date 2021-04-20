import re
from services.arithmetic_service import ArithmeticService


class InvalidPasswordException(Exception):
    pass


class InvalidUserException(Exception):
    pass


class MainService:
    def __init__(self, user_repository):
        self._logged_user = None
        self._user_repository = user_repository
        self.arithmetic = ArithmeticService()

    def login(self, username, password):
        username = username.lower()

        user = self._user_repository.get_user(username)

        if not user:
            raise InvalidUserException("No such user")

        if user.password != password:
            raise InvalidPasswordException("Invalid password")

        self._logged_user = user

    def logout(self):
        if self._logged_user:
            self._logged_user = None

    def _sanitize_username(self, username):
        if not username or len(username) < 3:
            raise InvalidUserException("Username too short")

        if not re.match("^[0-9a-zA-Z]*$", username):
            raise InvalidUserException("Username contains illegal characters")

        return username.lower()

    def create(self, username, password):
        username = self._sanitize_username(username)

        if not password or len(password) < 3:
            raise InvalidPasswordException("Password is too short")

        user = self._user_repository.create_user(username, password)

        if not user:
            raise InvalidUserException("Username is already in use")

        self._logged_user = user

    def save_settings(self):
        self._user_repository.save_settings(self._logged_user)

    def show_current_user(self):
        return self._logged_user
