from tkinter import ttk, constants, StringVar
from ui.base import BaseView
from services.main_service import InvalidPasswordException, InvalidUserException

class LoginView(BaseView):
    def __init__(self, window, main_service, show_create_new_user, show_exercises):
        super().__init__(window)
        self._show_create_new_user = show_create_new_user
        self._show_exercises = show_exercises
        self._main_service = main_service
        self._init_frame()

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            self._main_service.login(username, password)
            self._show_exercises()
        except InvalidUserException as error:
            self._show_error_message(error)
        except InvalidPasswordException as error:
            self._show_error_message(error)

    def _show_error_message(self, message):
        self._error_message.set(message)
        self._error_label.grid(sticky=constants.N, pady=5)

    def _hide_error_message(self):
        self._error_label.grid_remove()

    def _init_frame(self):
        self._frame = ttk.Frame(master=self._root)

        login_header_label = ttk.Label(
            master=self._frame, text="Login as existing user")
        username_entry_label = ttk.Label(
            master=self._frame, text="Enter username:")
        password_entry_label = ttk.Label(
            master=self._frame, text="Enter password:")

        self._username_entry = ttk.Entry(master=self._frame)
        self._password_entry = ttk.Entry(master=self._frame)

        login_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._login_handler)

        create_new_user_button = ttk.Button(
            master=self._frame,
            text="Create new user",
            command=self._show_create_new_user)

        self._error_message = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error_message)

        login_header_label.grid(sticky=constants.N, pady=(5, 15))
        username_entry_label.grid(sticky=constants.W, padx=10)
        self._username_entry.grid(pady=(0, 10), padx=10)
        password_entry_label.grid(sticky=constants.W, padx=10)
        self._password_entry.grid(pady=(0, 20), padx=10)

        login_button.grid(sticky=constants.EW, pady=5, padx=5)
        create_new_user_button.grid(sticky=constants.EW, pady=5, padx=5)

        self._frame.grid_columnconfigure(0, weight=1, minsize=200)
