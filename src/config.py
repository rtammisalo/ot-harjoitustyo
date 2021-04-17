import os
from dotenv import load_dotenv


class Config:
    DATA_DIRECTORY = "data"
    DB_FILENAME = "db.sqlite"
    DB_FILEPATH = ""

    @classmethod
    def init(cls):
        project_root_dir = os.path.join(os.path.dirname(__file__), "..")
        project_data_dir = os.path.join(project_root_dir, cls.DATA_DIRECTORY)

        try:
            load_dotenv(dotenv_path=os.path.join(project_root_dir, ".env"))

            cls.DB_FILENAME = Config.get_env("DB_FILENAME", cls.DB_FILENAME)
            cls.DB_FILEPATH = os.path.join(project_data_dir, cls.DB_FILENAME)
        except FileNotFoundError:
            pass

    @staticmethod
    def get_env(env_name, default_value):
        env_value = os.getenv(env_name)
        return env_value if env_value else default_value


Config.init()
