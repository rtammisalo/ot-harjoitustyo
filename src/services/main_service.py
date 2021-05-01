import re
from services.arithmetic_service import ArithmeticService
from repositories.user_repository import CriticalDatabaseError


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

        try:
            user = self._user_repository.get_user(username)
        except CriticalDatabaseError as error:
            raise error

        if not user:
            raise InvalidUserException("No such user")

        if user.password != password:
            raise InvalidPasswordException("Invalid password")

        self._logged_user = user

    def logout(self):
        if self._logged_user:
            self._logged_user = None

    def _sanitize_username(self, username):
        if not username or len(username) < 3 or len(username) > 12:
            raise InvalidUserException("Username too short")

        if not re.match("^[0-9a-zA-Z]*$", username):
            raise InvalidUserException("Username contains illegal characters")

        return username.lower()

    def create(self, username, password):
        username = self._sanitize_username(username)

        if not password or len(password) < 3 or len(password) > 20:
            raise InvalidPasswordException("Password is too short or too long")

        try:
            user = self._user_repository.create_user(username, password)
        except CriticalDatabaseError as error:
            raise error

        if not user:
            raise InvalidUserException("Username is already in use")

        self._logged_user = user

    def save_settings(self):
        self._user_repository.save_settings(self._logged_user)

    def show_current_user(self):
        return self._logged_user
