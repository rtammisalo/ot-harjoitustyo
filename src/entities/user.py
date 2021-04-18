class User:
    def __init__(self, username, password, id_number, settings):
        self.__username = username
        self.__password = password
        self.__id_number = id_number
        self.__settings = settings

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def id_number(self):
        return self.__id_number

    @property
    def settings(self):
        return self.__settings
