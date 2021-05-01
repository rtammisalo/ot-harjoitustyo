import os
from config import Config
from database import Database

# Removes all tables from the database and recreates them.
if __name__ == "__main__":
    if os.path.exists(Config.DB_FILEPATH):
        os.remove(Config.DB_FILEPATH)

    database = Database()
    database.init_database()
