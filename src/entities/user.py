class User:
    """A small container class for Users.
    """

    def __init__(self, username, password_hash, settings):
        """Initializes the user.

        Args:
            username (str): User's name.
            password_hash: User's password hash.
            settings (Settings): User's settings.
        """
        self.__username = username
        self.__password_hash = password_hash
        self.__settings = settings

    @property
    def username(self):
        """Returns User's username as a string."""
        return self.__username

    @property
    def password_hash(self):
        """Return User's password hash."""
        return self.__password_hash

    @property
    def settings(self):
        """Returns User's settings as a Settings-object."""
        return self.__settings
