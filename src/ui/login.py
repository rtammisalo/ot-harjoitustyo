from tkinter import ttk, constants, StringVar
from ui.base import BaseView
from ui import constants as ui_constants


class LoginView(BaseView):
    """A login view implementation.

    This is used to create the view that the user sees when loggin in.
    """

    def __init__(self, window, main_service, login_handlers):
        super().__init__(window, main_service)
        self._show_create_new_user = login_handlers[ui_constants.CREATE_USER_VIEW]
        self._login_handler = login_handlers[ui_constants.LOGIN_HANDLER]
        self._init_frame()

    def _login(self):
        self._login_handler(self._username_entry.get(),
                            self._password_entry.get(),
                            self._main_service.login,
                            self._show_error_message)

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
        self._username_entry.bind("<Return>", lambda event: self._login())
        self._password_entry = ttk.Entry(master=self._frame, show="*")
        self._password_entry.bind("<Return>", lambda event: self._login())

        login_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._login)

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

        self._username_entry.focus()
