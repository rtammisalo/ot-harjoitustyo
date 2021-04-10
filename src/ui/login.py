from tkinter import ttk, constants
from ui.base import BaseView


class LoginView(BaseView):
    def __init__(self, window, handle_new_user):
        super().__init__(window)
        self._handle_new_user = handle_new_user
        self._init_frame()

    def _init_frame(self):
        self._frame = ttk.Frame(master=self._root)

        login_header_label = ttk.Label(
            master=self._frame, text="Login as existing user")
        username_entry_label = ttk.Label(
            master=self._frame, text="Enter username:")
        password_entry_label = ttk.Label(
            master=self._frame, text="Enter password:")

        username_entry = ttk.Entry(master=self._frame)
        password_entry = ttk.Entry(master=self._frame)

        login_button = ttk.Button(master=self._frame, text="Login")
        create_new_user_button = ttk.Button(
            master=self._frame,
            text="Create new user",
            command=self._handle_new_user
        )

        login_header_label.grid(sticky=constants.N, pady=(5, 15))
        username_entry_label.grid(sticky=constants.W, padx=10)
        username_entry.grid(pady=(0, 10), padx=10)
        password_entry_label.grid(sticky=constants.W, padx=10)
        password_entry.grid(pady=(0, 20), padx=10)

        login_button.grid(sticky=constants.EW, pady=5, padx=5)
        create_new_user_button.grid(sticky=constants.EW, pady=5, padx=5)

        self._frame.grid_columnconfigure(0, weight=1, minsize=200)
