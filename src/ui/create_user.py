from tkinter import ttk, constants
from ui.base import BaseView


class CreateUserView(BaseView):
    def __init__(self, window, handle_quit):
        super().__init__(window)
        self._handle_quit = handle_quit
        self._init_frame()

    def _init_frame(self):
        self._frame = ttk.Frame(master=self._root)
        button = ttk.Button(master=self._frame,
                            text="Create User", command=self._handle_quit)
        button.grid()
