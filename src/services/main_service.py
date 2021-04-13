from repositories.user_repository import UserRepository
from services.arithmetic_service import ArithmeticService


class InvalidPasswordException(Exception):
    pass


class InvalidUserException(Exception):
    pass


class MainService:
    def __init__(self):
        self._logged_user = None
        # Hardcode this in for now, since we don't have a db.
        self._user_repository = UserRepository()
        self.arithmetic = ArithmeticService()

    def login(self, username, password):
        user = self._user_repository.get_user(username)

        if not user:
            raise InvalidUserException("No such user")

        if user.password != password:
            raise InvalidPasswordException("Invalid password")

        self._logged_user = user

    def logout(self):
        if self._logged_user:
            self._logged_user = None

    def create(self, username, password):
        if not username or len(username) < 3:
            raise InvalidUserException("Username too short")

        if not password or len(password) < 3:
            raise InvalidPasswordException("Password is too short")

        user = self._user_repository.create_user(username, password)

        if not user:
            raise InvalidUserException("Username is already in use")

        self._logged_user = user

    def show_current_user(self):
        return self._logged_user