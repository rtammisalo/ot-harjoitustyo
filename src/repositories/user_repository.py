import sqlite3
from passlib.hash import pbkdf2_sha256
from entities.user import User
from config import Config
from repositories.settings_repository import SettingsRepository
from services.main_service import CriticalDatabaseError


class UserRepository:
    """A Repository pattern class for encapsulating database access regarging users.

    Also contains a reference a Settings repository, since each user also has settings.
    """

    def __init__(self, database,
                 settings_repository=SettingsRepository(Config.USER_DEFAULT_CSV_FILEPATH,
                                                        Config.USER_CSV_PATH)):
        """Initializes the repository to use the given Database connection.

        Args:
            database (Database): Used to get the connection to the database.
            settings_repository (SettingsRepository, optional):
                Settings repository for handling user settings.
                Defaults to SettingsRepository(Config.USER_DEFAULT_CSV_FILEPATH,
                                               Config.USER_CSV_PATH).
        """
        self._database = database
        self._settings_repository = settings_repository

    def get_user(self, username):
        """Returns a User if it exists.

        Args:
            username (str): User's name.

        Raises:
            CriticalDatabaseError: DB access failed badly.

        Returns:
            User: A fully formed User-object, with settings loaded from file.
        """
        try:
            cursor = self._database.connection.cursor()

            # Use (username, ) to signify that we are passing a tuple.
            cursor.execute(
                "select * from Users where username = ?", (username, ))

            return self._get_user_from_row(cursor.fetchone())
        except sqlite3.DatabaseError as error:
            raise CriticalDatabaseError(
                "ERROR: Critical failure while reading from database.") from error

    def create_user(self, username, password):
        """Tries to create a user with the given name and password.

        Args:
            username (str): Username of the new user.
            password (str): Password of the new user.

        Raises:
            CriticalDatabaseError: DB access failed badly.

        Returns:
            User: Returns a fully formed User-object with settings.
            None: Returns None if the username is already in use.
        """
        password_hash = self._create_password_hash(password)

        try:
            cursor = self._database.connection.cursor()
            cursor.execute("insert into Users (username, password) values (?, ?)",
                           (username, password_hash))

            self._database.connection.commit()

            return self.get_user(username)
        except sqlite3.IntegrityError:
            return None
        except sqlite3.DatabaseError as error:
            raise CriticalDatabaseError(
                "ERROR: Critical failure while writing to database.") from error

    def _get_user_from_row(self, row_result):
        """Returns a fully formed User object from the row result of a DB search.
        """
        if not row_result:
            return None

        user_settings = self._settings_repository.get_settings_by_username(
            row_result["username"])
        return User(row_result["username"], row_result["password"],
                    user_settings, self._verify_password_hash)

    def save_settings(self, user):
        """Access method for saving the user settings using the settings repository.

        Args:
            user (User): Owner of the settings.
        """
        if not user:
            return

        self._settings_repository.save_user_settings(user)

    def _create_password_hash(self, password):
        """Returns a password hash for storing.
        """
        return pbkdf2_sha256.hash(password)

    def _verify_password_hash(self, password_hash, password):
        """Verifies that the given password is the same as the password of the user.

        Args:
            password_hash: Hash string of the password to be verified against.
            password (str): Password string given by user.

        Returns:
            boolean: Returns True if the password is correct, False otherwise.
        """
        try:
            return pbkdf2_sha256.verify(password, password_hash)
        except (TypeError, ValueError):
            return False
