from passlib.hash import pbkdf2_sha256


class User:
    """A small container class for Users.
    """

    def __init__(self, username, password_hash, id_number, settings):
        """Initializes the user.

        Args:
            username (str): User's name.
            password (str): User's password.
            id_number (int): User's id number.
            settings (Settings): User's settings.
        """
        self.__username = username
        self.__password_hash = password_hash
        self.__id_number = id_number
        self.__settings = settings

    @property
    def username(self):
        """Returns User's username as a string."""
        return self.__username

    def verify_password(self, password):
        """Verifies if the given password is the password of the user.

        Args:
            password (str): Password string given by user.

        Returns:
            boolean: Returns True if the password is correct, False otherwise.
        """
        try:
            return pbkdf2_sha256.verify(password, self.__password_hash)
        except (TypeError, ValueError):
            return False

    @property
    def id_number(self):
        """Returns User's id number."""
        return self.__id_number

    @property
    def settings(self):
        """Returns User's settings as a Settings-object."""
        return self.__settings

    @staticmethod
    def create_password_hash(password):
        """Returns a password hash for storing.
        """
        return pbkdf2_sha256.hash(password)
