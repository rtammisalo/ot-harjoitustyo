class User:
    def __init__(self, username, password, id):
        self.__username = username
        self.__password = password
        self.__id = id

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def id(self):
        return self.__id
