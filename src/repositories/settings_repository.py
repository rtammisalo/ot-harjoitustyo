import os
import csv
from entities.settings import Settings


class SettingsRepository:
    """ A repository pattern class for encapsulating user settings file management.
    """

    def __init__(self, default_filepath, users_path):
        """Initializes the repository to use the given default settings file and user
        settings directory.

        Args:
            default_filepath (str): Path to the default settings file.
            users_path (str): Path to the settings folder for users.
        """
        self._default_filepath = default_filepath
        self._users_path = users_path

    def _parse_settings(self, reader):
        """Parses a settings file using the given reader.

        Args:
            reader (csv.reader): A csv reader.

        Returns:
            Settings: Parsed settings or a newly created Settings-object.
        """
        settings = Settings()

        for line in reader:
            if len(line) != 2:
                continue
            try:
                setting = line[0]
                settings.parse_and_set_setting(setting, line[1])
            except ValueError:
                continue

        return settings

    def _read_settings_file(self, settings_filepath):
        """Tries to open and read the settings file named by settings_filepath.

        Args:
            settings_filepath (str): Filepath to the settings file.

        Returns:
            Settings: A Settings-object containing the file settings or a default one.
        """
        user_settings = Settings()

        with open(settings_filepath) as settings_file:
            reader = csv.reader(settings_file, delimiter=",")
            user_settings = self._parse_settings(reader)

        return user_settings

    def _create_user_settings_directory(self):
        """Creates the users-folder if it does not exist.
        """
        if not os.path.exists(self._users_path):
            os.makedirs(self._users_path)

    def _write_settings(self, settings_filepath, settings):
        """Tries to write the settings to the file named by settings_filepath.

        Args:
            settings_filepath (str): Filepath of the settings file.
            settings (Settings): Settings to be written to disk.
        """
        try:
            self._create_user_settings_directory()

            with open(settings_filepath, mode="w") as settings_file:
                writer = csv.writer(settings_file, delimiter=",")
                for setting, value in settings.get_settings_as_dict().items():
                    writer.writerow([setting, str(value)])
        except OSError:
            print(f"Failed to write user settings: {settings_filepath}")

    def _get_user_settings_filepath(self, username):
        """Returns a full path string to settings file.
        """
        return os.path.join(self._users_path, f"{username}.csv")

    def get_settings_by_username(self, username):
        """Reads and returns user settings for username.

        Creates default Settings if there is no settings file.

        Args:
            username (str): Username string

        Returns:
            Settings: Returns a Settings-object parsed from the file, or a default one.
        """
        filepath = self._get_user_settings_filepath(username)

        try:
            return self._read_settings_file(filepath)
        except FileNotFoundError:
            settings = self._get_default_settings()
            self._write_settings(filepath, settings)
            return settings

    def _get_default_settings(self):
        """Returns default user settings as defined by the default settings file.

        If the default settings file does not exist, the method creates a new one from
        the default values set in a new Settings-object.

        Returns:
            Settings: a default Settings-object.
        """
        settings = Settings()

        try:
            settings = self._read_settings_file(self._default_filepath)
        except FileNotFoundError:
            self._write_settings(self._default_filepath, settings)

        return settings

    def save_user_settings(self, user):
        """Saves user settings to the user's file.

        Args:
            user (User): User.
        """
        settings_filepath = self._get_user_settings_filepath(user.username)
        self._write_settings(settings_filepath, user.settings)
