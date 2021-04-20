from tkinter import ttk, constants
from ui.base import BaseView
from ui.components.multiplication_settings_frame import MultiplicationSettingsFrame


class SettingsView(BaseView):
    def __init__(self, window, main_service, show_exercises):
        super().__init__(window, main_service)
        self._show_exercises = show_exercises
        self._init_frame()

    def _save_settings(self):
        user = self._main_service.show_current_user()

        self._multiplication_settings_frame.set_new_settings(user.settings)

        self._main_service.save_settings()
        self._show_exercises()

    def _init_frame(self):
        self._frame = ttk.Frame(master=self._root)
        frame_header_label = ttk.Label(
            master=self._frame,
            text="Settings")

        settings = self._main_service.show_current_user().settings
        self._multiplication_settings_frame = MultiplicationSettingsFrame(
            self._frame, settings)

        accept_button = ttk.Button(
            master=self._frame, text="Accept", command=self._save_settings)
        back_button = ttk.Button(
            master=self._frame, text="Back", command=self._show_exercises)

        frame_header_label.grid(pady=10, padx=5)
        self._multiplication_settings_frame.frame.grid(pady=5, padx=5)
        accept_button.grid(sticky=constants.EW, pady=5, padx=5)
        back_button.grid(sticky=constants.EW, pady=5, padx=5)
