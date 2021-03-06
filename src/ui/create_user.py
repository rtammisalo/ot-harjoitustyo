from tkinter import ttk, constants, StringVar
from ui.base import BaseView
from ui import constants as ui_constants


class CreateUserView(BaseView):
    """The implementation for the view seen when the user tries to create a new user account.
    """

    def __init__(self, window, main_service, login_handlers):
        """Inits the user creation view.

        Args:
            window: Main UI.
            main_service (MainService): The MainService of the program.
            login_handlers (dict of login handling functions): Used to change views for the user.
        """
        super().__init__(window, main_service)
        self._show_login = login_handlers[ui_constants.LOGIN_VIEW]
        self._login_handler = login_handlers[ui_constants.LOGIN_HANDLER]
        self._init_frame()

    def _create_user_handler(self):
        if self._password_entry.get() == self._password_second_entry.get():
            self._login_handler(self._username_entry.get(), self._password_entry.get(),
                                self._main_service.create,
                                self._show_error_message)
        else:
            self._show_error_message(
                "Passwords mismatch")

    def _show_error_message(self, message):
        self._error_message.set(message)
        self._error_label.grid(sticky=constants.N, pady=5, padx=5)

    def _hide_error_message(self):
        self._error_label.grid_remove()

    def _init_frame(self):
        self._frame = ttk.Frame(master=self._root)
        frame_header_label = ttk.Label(
            master=self._frame, text="Create new user")

        username_entry_label = ttk.Label(
            master=self._frame, text="Enter new username:")
        password_entry_label = ttk.Label(
            master=self._frame, text="Enter new password:")
        password_second_entry_label = ttk.Label(
            master=self._frame, text="Re-enter password:")

        self._username_entry = ttk.Entry(master=self._frame)
        self._username_entry.bind(
            "<Return>", lambda event: self._create_user_handler())
        self._password_entry = ttk.Entry(master=self._frame, show="*")
        self._password_entry.bind(
            "<Return>", lambda event: self._create_user_handler())
        self._password_second_entry = ttk.Entry(master=self._frame, show="*")
        self._password_second_entry.bind(
            "<Return>", lambda event: self._create_user_handler())

        self._error_message = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error_message, borderwidth=2, relief="solid")
        self._error_label.config(foreground="red")

        create_button = ttk.Button(master=self._frame,
                                   text="Create User", command=self._create_user_handler)

        back_button = ttk.Button(
            master=self._frame, text="Back", command=self._show_login)

        frame_header_label.grid(sticky=constants.N, pady=(5, 15))
        username_entry_label.grid(sticky=constants.W, padx=5)
        self._username_entry.grid(sticky=constants.W, pady=(0, 10), padx=10)
        password_entry_label.grid(sticky=constants.W, padx=5)
        self._password_entry.grid(sticky=constants.W, pady=(0, 20), padx=10)
        password_second_entry_label.grid(sticky=constants.W, padx=5)
        self._password_second_entry.grid(
            sticky=constants.W, pady=(0, 20), padx=10)
        create_button.grid(sticky=constants.EW, pady=5, padx=5)
        back_button.grid(sticky=constants.EW, pady=5, padx=5)
        self._frame.grid_columnconfigure(0, weight=1, minsize=200)

        self._username_entry.focus()
