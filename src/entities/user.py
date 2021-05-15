class User:
    """A small class for Users. Has a method for verifying passwords.
    """

    def __init__(self, username, password_hash, settings,
                 verify_password_hash=None):
        """Initializes the user.

        Args:
            username (str): User's name.
            password_hash: User's password hash.
            settings (Settings): User's settings.
            verify_password (function, optional): Function used to verify password hash to password.
                Defaults to an equals-check (no hashing).
                Function arguments are in order (hash, password).
        """

        self.__username = username
        self.__password_hash = password_hash
        self.__settings = settings
        self.__verify_password_hash = verify_password_hash

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

    def verify_password(self, password):
        """Verifies that the given password matches the hashed password of the user.

        This function uses the password hash verifier given at initialization of the User-object.
        If no hash verifier was given, the function does an equals-check on the password/hash.

        Args:
            password (str): Password given by the user.
        """
        if self.__verify_password_hash:
            return self.__verify_password_hash(self.__password_hash, password)

        return self.__password_hash == password
