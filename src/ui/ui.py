from ui.login import LoginView
from ui.create_user import CreateUserView
from ui.exercise_selection import ExerciseSelectionView
from ui.exercises import MultiplicationView, DivisionView, AdditionView, SubstractionView
from ui.settings import SettingsView
from ui.base import BaseView
import ui.constants as ui_constants
from services.main_service import InvalidPasswordException, InvalidUserException


class UI:

    def __init__(self, window, main_service):
        self._root = window
        # Set to avoid checking for None.
        self._view = BaseView(window, main_service)
        self._main_service = main_service

        self._exercise_handlers = {
            ui_constants.MULTIPLICATION: self._show_multiplication_exercise,
            ui_constants.DIVISION: self._show_division_exercise,
            ui_constants.ADDITION: self._show_addition_exercise,
            ui_constants.SUBSTRACTION: self._show_substraction_exercise}
        self._login_handlers = {ui_constants.LOGIN_VIEW: self._show_login_view,
                                ui_constants.CREATE_USER_VIEW: self._show_create_user_view,
                                ui_constants.EXERCISES_VIEW: self._show_exercises_view,
                                ui_constants.LOGIN_HANDLER: self._login_handler}

    def _show_new_view(self, new_view):
        self._view.destroy_frame()
        self._view = new_view
        self._view.pack_frame()

    def _show_create_user_view(self):
        self._show_new_view(CreateUserView(
            self._root, self._main_service, self._login_handlers))

    def _show_login_view(self):
        self._show_new_view(
            LoginView(self._root, self._main_service, self._login_handlers))

    def _show_exercises_view(self):
        self._show_new_view(ExerciseSelectionView(
            self._root, self._main_service, self._logout_handler, self._exercise_handlers,
            self._show_settings_view))

    def _show_multiplication_exercise(self):
        self._show_new_view(MultiplicationView(
            self._root, self._main_service, self._show_exercises_view))

    def _show_division_exercise(self):
        self._show_new_view(DivisionView(
            self._root, self._main_service, self._show_exercises_view))

    def _show_addition_exercise(self):
        self._show_new_view(AdditionView(
            self._root, self._main_service, self._show_exercises_view))

    def _show_substraction_exercise(self):
        self._show_new_view(SubstractionView(
            self._root, self._main_service, self._show_exercises_view))

    def _show_settings_view(self):
        self._show_new_view(SettingsView(
            self._root, self._main_service, self._show_exercises_view))

    def _login_handler(self, username, password, login, error_handler):
        try:
            # By passing the login function, we can use the same method for both logging-in
            # or creating an account AND logging-in.
            login(username, password)
            self._show_exercises_view()
        except (InvalidUserException, InvalidPasswordException) as error:
            error_handler(error)

    def _logout_handler(self):
        self._main_service.logout()
        self._show_login_view()

    def start(self):
        self._show_login_view()
