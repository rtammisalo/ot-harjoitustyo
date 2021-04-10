from tkinter import Tk, ttk, constants
from ui.login import LoginView
from ui.create_user import CreateUserView
from ui.base import BaseView


class UI:
    def __init__(self, window, main_service):
        self._root = window
        self._view = BaseView(window)
        self._main_service = main_service

    def _show_new_view(self, new_view):
        self._view.destroy_frame()
        self._view = new_view
        self._view.pack_frame()

    def _show_create_user_view(self):
        self._show_new_view(CreateUserView(self._root, self._main_service, self._show_login_view, lambda : print("ja taas")))

    def _show_login_view(self):
        self._show_new_view(LoginView(self._root, self._main_service, self._show_create_user_view, lambda : print("Im in")))

    def start(self):
        self._show_login_view()
