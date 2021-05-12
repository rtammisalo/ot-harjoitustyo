from entities.user import User

class FakeUserRepository:
    def __init__(self):
        self._users = {}
        self._settings_saved = 0

    def get_user(self, username):
        return self._users.get(username, None)

    def create_user(self, username, password):
        if username in self._users:
            return None

        new_user = User(username, User.create_password_hash(password), len(self._users), None)
        self._users[username] = new_user
        return new_user

    def save_settings(self, user):
        self._settings_saved += 1

    def settings_saved(self):
        return self._settings_saved