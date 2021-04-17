import sqlite3
from config import Config


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(Config.DB_FILEPATH)
        # Use the convenient row factory results
        self.connection.row_factory = sqlite3.Row

    def _drop_tables(self):
        cursor = self.connection.cursor()

        cursor.execute("drop table if exists Users;")

        self.connection.commit()

    def _create_tables(self):
        cursor = self.connection.cursor()

        cursor.execute(
            "create table Users (id integer primary key, username text unique, password text);")

        self.connection.commit()

    def init_database(self):
        self._drop_tables()
        self._create_tables()
