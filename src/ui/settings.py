from tkinter import ttk, constants, Canvas
from ui.base import BaseView
from ui.components.multiplication_settings_frame import MultiplicationSettingsFrame
from ui.components.division_settings_frame import DivisionSettingsFrame
from ui.components.addition_settings_frame import AdditionSettingsFrame
from ui.components.substraction_settings_frame import SubstractionSettingsFrame

class SettingsView(BaseView):
    def __init__(self, window, main_service, show_exercises):
        super().__init__(window, main_service)
        self._show_exercises = show_exercises
        self._init_frame()

    def _save_settings(self):
        user = self._main_service.show_current_user()

        for settings_frame in self._settings_frames:
            settings_frame.set_new_settings(user.settings)

        self._main_service.save_settings()
        self._show_exercises()

    def _init_frame(self):
        self._frame = ttk.Frame(master=self._root)
        frame_header_label = ttk.Label(
            master=self._frame,
            text="Settings")

        canvas = Canvas(self._frame, height=260, width=270)
        scroller = ttk.Scrollbar(
            self._frame, orient=constants.VERTICAL, command=canvas.yview)
        canvas.configure(yscrollcommand=scroller.set)
        canvas.bind("<Configure>", lambda event: canvas.configure(
            scrollregion=canvas.bbox("all")))

        settings = self._main_service.show_current_user().settings
        settings_frame = ttk.Frame(master=canvas)
        self._settings_frames = [MultiplicationSettingsFrame(settings_frame, settings),
                                 DivisionSettingsFrame(settings_frame, settings),
                                 AdditionSettingsFrame(settings_frame, settings),
                                 SubstractionSettingsFrame(settings_frame, settings)]

        accept_button = ttk.Button(
            master=self._frame, text="Accept", command=self._save_settings)
        back_button = ttk.Button(
            master=self._frame, text="Back", command=self._show_exercises)

        frame_header_label.grid(pady=10, padx=5)

        for frame in self._settings_frames:
            frame.frame.grid(sticky=constants.W, pady=5, padx=5)

        canvas.create_window(
            (0, 0), window=settings_frame, anchor=constants.NW)
        canvas.grid(row=0, column=0, sticky=constants.W, pady=5, padx=5)
        scroller.grid(row=0, column=1,
                      sticky=constants.NS, pady=5, padx=2)
        accept_button.grid(row=1, column=0, columnspan=2,
                           sticky=constants.EW, pady=5, padx=5)
        back_button.grid(row=2, column=0, columnspan=2,
                         sticky=constants.EW, pady=5, padx=5)
