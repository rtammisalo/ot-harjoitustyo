from entities.user import User


class UserRepository:
    def __init__(self):
        self._users = {"aaa":"aaa"}

    def get_user(self, username):
        return User(username, self._users[username]) if username in self._users else None

    def create_user(self, username, password):
        if username not in self._users:
            self._users[username] = password
            return self._new_user(username, password)

        return None

    def _new_user(self, username, password):
        return User(username, password)
