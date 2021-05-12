import re
from services.arithmetic_service import ArithmeticService


class InvalidPasswordException(Exception):
    pass


class InvalidUserException(Exception):
    pass


class CriticalDatabaseError(Exception):
    pass


class MainService:
    """Provides all necessary business logic functionality to the UI-layer.

    Attributes:
        arithmetic: Arithmetic service for generating new questions and checking
            answers from users.
    """

    def __init__(self, user_repository):
        """Initializes MainService to read/store from a user repository.

        Args:
            user_repository (UserRepository): A repository for user related information.
        """
        self._logged_user = None
        self._user_repository = user_repository
        self.arithmetic = ArithmeticService()

    def login(self, username, password):
        """Tries to set a stored user, with a matching password, as the logged-in user.

        Args:
            username (str): Username as a string. This is always treated as lower-case.
            password (str): Password as a string.

        Raises:
            CriticalDatabaseError: Encountered a problem while accessing DB.
            InvalidUserException: There was no such user in the user repository.
            InvalidPasswordException: The given password does not match the stored password.
        """

        username = username.lower()

        try:
            user = self._user_repository.get_user(username)
        except CriticalDatabaseError as error:
            raise error

        if not user:
            raise InvalidUserException("No such user")

        if not user.verify_password(password):
            raise InvalidPasswordException("Invalid password")

        self._logged_user = user

    def logout(self):
        """Logs out the current user from the system.
        """
        if self._logged_user:
            self._logged_user = None

    def _sanitize_username(self, username):
        """Checks if the given username fits accepted length and character constraints.

        Accepted usernames can only contain 3-12 characters with numbers
        and upper/lowercase letters.

        Args:
            username (str): Username-string from the user.

        Raises:
            InvalidUserException: The username is too long, short or contains
                illegal characters.

        Returns:
            str: Returns the username in lowercase.
        """
        if not username or len(username) < 3 or len(username) > 12:
            raise InvalidUserException("Username too short or too long")

        if not re.match("^[0-9a-zA-Z]*$", username):
            raise InvalidUserException("Username contains illegal characters")

        return username.lower()

    def _check_password_validity(self, password):
        """Checks whether the password fits accepted length and character constraints.

        Accepted passwords can only contain 3-20 characters with no empty spaces.

        Args:
            password (str): Password string from the user.

        Raises:
            InvalidPasswordException: Raised when the password is too long/short or
                contains illegal characters.
        """
        if not password or len(password) < 3 or len(password) > 20:
            raise InvalidPasswordException("Password is too short or too long")

        if re.match("\\s+", password):
            raise InvalidPasswordException(
                "Password containts empty spaces")

    def create(self, username, password):
        """Tries to create a new user, add it to the repository and set it as logged-in.

        The username is checked first with _sanitize_username(). It can also not already be
        in use. Given passwords are only accepted when they are 3-20 characters long.

        Args:
            username (str): A new username-string from the user.
            password (str): A string containing the password.

        Raises:
            InvalidPasswordException: The password size failed a constraint check.
            CriticalDatabaseError: Encountered a problem while accessing DB.
            InvalidUserException: The username was already in use.
        """
        username = self._sanitize_username(username)
        self._check_password_validity(password)

        try:
            user = self._user_repository.create_user(username, password)
        except CriticalDatabaseError as error:
            raise error

        if not user:
            raise InvalidUserException("Username is already in use")

        self._logged_user = user

    def save_settings(self):
        """Saves the user's settings to the repository.
        """
        self._user_repository.save_settings(self._logged_user)

    def show_current_user(self):
        """Returns the current user, or None.

        Returns:
            User: Currently logged-in user.
        """
        return self._logged_user
