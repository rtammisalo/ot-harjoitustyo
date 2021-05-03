class User:
    """A small container class for Users.
    """

    def __init__(self, username, password, id_number, settings):
        """Initializes the user.

        Args:
            username (str): User's name.
            password (str): User's password.
            id_number (int): User's id number.
            settings (Settings): User's settings.
        """
        self.__username = username
        self.__password = password
        self.__id_number = id_number
        self.__settings = settings

    @property
    def username(self):
        """Returns User's username as a string."""
        return self.__username

    @property
    def password(self):
        """Returns User's password as a string."""
        return self.__password

    @property
    def id_number(self):
        """Returns User's id number."""
        return self.__id_number

    @property
    def settings(self):
        """Returns User's settings as a Settings-object."""
        return self.__settings
