import sqlite3
from entities.user import User
from config import Config
from repositories.settings_repository import SettingsRepository


class UserRepository:
    def __init__(self, database,
                 settings_repository=SettingsRepository(Config.USER_DEFAULT_CSV_FILEPATH,
                                                        Config.USER_CSV_PATH)):
        self._database = database
        self._settings_repository = settings_repository

    def get_user(self, username):
        cursor = self._database.connection.cursor()

        # Use (username, ) to signify that we are passing a tuple.
        cursor.execute("select * from Users where username = ?", (username, ))

        return self._get_user(cursor.fetchone())

    def create_user(self, username, password):
        cursor = self._database.connection.cursor()

        try:
            cursor.execute("insert into Users (username, password) values (?, ?)",
                           (username, password))

            self._database.connection.commit()

            return self.get_user(username)
        except sqlite3.IntegrityError:
            return None

    def _get_user(self, row_result):
        if not row_result:
            return None

        user_settings = self._settings_repository.get_settings_by_username(
            row_result["username"])
        return User(row_result["username"], row_result["password"], row_result["id"], user_settings)
