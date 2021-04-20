from entities.settings import Settings

class FakeSettingsRepository:
    def __init__(self):
        self._settings = {}

    def get_settings_by_username(self, username):
        if username not in self._settings:
            self._settings[username] = (Settings(), 0)

        return self._settings[username]

    def settings_saved_by_username(self, username):
        settings, times_saved = self._settings[username]
        return times_saved

    def save_user_settings(self, user):
        settings, times_saved = self._settings[user.username]
        self._settings[user.username] = (settings, times_saved + 1)

    def user_settings_saved(self):
        saved = 0

        for settings, times_saved in self._settings.values():
            saved += times_saved

        return saved