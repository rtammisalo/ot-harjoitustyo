import sqlite3
from config import Config


class Database:
    """Tiny class meant to handle database connections to the sqlite3 database.
    """

    def __init__(self):
        """Inits the database connection.

        Call init_database() to (re)create the database before use, if needed.
        """
        self.connection = sqlite3.connect(Config.DB_FILEPATH)
        # Use the convenient row factory results
        self.connection.row_factory = sqlite3.Row

    def _drop_tables(self):
        """Drops all tables used by the program.
        """
        cursor = self.connection.cursor()

        cursor.execute("drop table if exists Users;")

        self.connection.commit()

    def _create_tables(self):
        """Creates the tables needed by the program.
        """
        cursor = self.connection.cursor()

        cursor.execute(
            "create table if not exists Users "
            "(id integer primary key, username text unique, password text);")

        self.connection.commit()

    def init_database(self):
        """Drops all tables and creates them.
        """
        self._drop_tables()
        self._create_tables()

    def is_db_connection_ok(self):
        """Checks if the connection to the database is working.

        Returns:
            boolean: True if the connection is ok. False otherwise.
        """
        try:
            self._create_tables()
            return True
        except sqlite3.DatabaseError:
            return False
