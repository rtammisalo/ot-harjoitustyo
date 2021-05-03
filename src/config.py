import os
from dotenv import load_dotenv


class Config:
    """Config-class holds all needed paths needed by the program as class attributes.

    Values are initialized from the .env file.
    """
    DATA_DIRECTORY = "data"
    DB_FILENAME = "db.sqlite"
    DB_FILEPATH = ""
    USER_CSV_PATH = "users"
    USER_DEFAULT_CSV_FILENAME = "default_user.csv"
    USER_DEFAULT_CSV_FILEPATH = ""

    @classmethod
    def init(cls):
        """Initializes the paths to files and directories named in the .env
        """
        project_root_dir = os.path.join(os.path.dirname(__file__), "..")
        project_data_dir = os.path.join(project_root_dir, cls.DATA_DIRECTORY)

        try:
            load_dotenv(dotenv_path=os.path.join(project_root_dir, ".env"))
        except FileNotFoundError:
            pass

        cls.DB_FILENAME = Config.get_env("DB_FILENAME", cls.DB_FILENAME)
        cls.DB_FILEPATH = os.path.join(project_data_dir, cls.DB_FILENAME)

        cls.USER_CSV_PATH = Config.get_env(
            "USER_CSV_PATH", cls.USER_CSV_PATH)
        cls.USER_CSV_PATH = os.path.join(project_data_dir, cls.USER_CSV_PATH)

        cls.USER_DEFAULT_CSV_FILENAME = Config.get_env(
            "USER_DEFAULT_CSV_FILENAME", cls.USER_DEFAULT_CSV_FILENAME)
        cls.USER_DEFAULT_CSV_FILEPATH = os.path.join(
            project_data_dir, cls.USER_DEFAULT_CSV_FILENAME)

    @staticmethod
    def get_env(env_name, default_value):
        """Returns the value of a environmental variable or a default if it is undefined.
        """
        env_value = os.getenv(env_name)
        return env_value if env_value else default_value


Config.init()
