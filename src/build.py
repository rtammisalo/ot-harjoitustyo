from database import Database

# Removes all tables from the database and recreates them.
if __name__ == "__main__":
    database = Database()
    database.init_database()
