from entities.user import User
import sqlite3


class UserRepository:
    def __init__(self, database):
        self._database = database

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

        return User(row_result["username"], row_result["password"], row_result["id"])
