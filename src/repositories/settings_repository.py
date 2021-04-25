import os
import csv
from entities.settings import Settings


class SettingsRepository:
    def __init__(self, default_filepath, users_path):
        self._default_filepath = default_filepath
        self._users_path = users_path

    def _parse_settings(self, reader):
        settings = Settings()

        for line in reader:
            if len(line) != 2:
                continue
            try:
                setting = line[0]
                settings.parse_and_set_setting(setting, line[1])
            except ValueError:
                continue
            except KeyError:
                continue

        return settings

    def _read_settings_file(self, settings_filepath):
        user_settings = Settings()

        with open(settings_filepath) as settings_file:
            reader = csv.reader(settings_file, delimiter=",")
            user_settings = self._parse_settings(reader)

        return user_settings

    def _create_user_settings_directory(self):
        if not os.path.exists(self._users_path):
            os.makedirs(self._users_path)

    def _write_settings(self, settings_filepath, settings):
        try:
            self._create_user_settings_directory()

            with open(settings_filepath, mode="w") as settings_file:
                writer = csv.writer(settings_file, delimiter=",")
                for setting, value in settings.get_settings_as_dict().items():
                    writer.writerow([setting, str(value)])
        except OSError:
            print(f"Failed to write user settings: {settings_filepath}")

    def _get_user_settings_filepath(self, username):
        return os.path.join(self._users_path, f"{username}.csv")

    def get_settings_by_username(self, username):
        filepath = self._get_user_settings_filepath(username)
        settings = Settings()

        try:
            return self._read_settings_file(filepath)
        except FileNotFoundError:
            try:
                settings = self._read_settings_file(self._default_filepath)
            except FileNotFoundError:
                pass

        self._write_settings(filepath, settings)
        return settings

    def save_user_settings(self, user):
        settings_filepath = self._get_user_settings_filepath(user.username)
        self._write_settings(settings_filepath, user.settings)
