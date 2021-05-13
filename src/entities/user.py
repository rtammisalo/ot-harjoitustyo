class User:
    """A small container class for Users.
    """

    def __init__(self, username, password_hash, id_number, settings):
        """Initializes the user.

        Args:
            username (str): User's name.
            password_hash: User's password hash.
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

    @property
    def password_hash(self):
        """Return User's password hash."""
        return self.__password_hash

    @property
    def id_number(self):
        """Returns User's id number."""
        return self.__id_number

    @property
    def settings(self):
        """Returns User's settings as a Settings-object."""
        return self.__settings
