from tkinter import ttk, constants, Canvas
from ui.base import BaseView
from ui.components.settings_frames import MultiplicationSettingsFrame, DivisionSettingsFrame, \
    AdditionSettingsFrame, SubstractionSettingsFrame, RandomExerciseSettingsFrame


class SettingsView(BaseView):
    """A view for looking at and changing settings.

    Saves settings through MainService. Uses all the different SettingsFrames as components.
    """

    def __init__(self, window, main_service, show_exercises):
        """Inits the settings view.

        Args:
            window: Main UI.
            main_service (MainService): MainService of the program.
            show_exercises (function): Used to change view back to showing the exercise
                selection list.
        """
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

        canvas = Canvas(self._frame, height=2000, width=270)
        scroller = ttk.Scrollbar(
            self._frame, orient=constants.VERTICAL, command=canvas.yview)
        canvas.configure(yscrollcommand=scroller.set)
        canvas.bind("<Configure>", lambda event: canvas.configure(
            scrollregion=canvas.bbox("all")))

        settings = self._main_service.show_current_user().settings
        settings_frame = ttk.Frame(master=canvas)
        self._settings_frames = [MultiplicationSettingsFrame(settings_frame, settings),
                                 DivisionSettingsFrame(
                                     settings_frame, settings),
                                 AdditionSettingsFrame(
                                     settings_frame, settings),
                                 SubstractionSettingsFrame(
                                     settings_frame, settings),
                                 RandomExerciseSettingsFrame(
                                     settings_frame, settings)]

        accept_button = ttk.Button(
            master=self._frame, text="Accept", command=self._save_settings)
        back_button = ttk.Button(
            master=self._frame, text="Back", command=self._show_exercises)

        for frame in self._settings_frames:
            frame.frame.grid(sticky=constants.EW, pady=5, padx=5)

        canvas.create_window(
            (0, 0), window=settings_frame, anchor=constants.NW)
        canvas.grid(row=0, column=0, sticky=constants.NS, pady=5, padx=5)
        scroller.grid(row=0, column=1,
                      sticky=constants.NS, pady=5, padx=2)
        accept_button.grid(row=1, column=0, columnspan=2,
                           sticky=constants.EW, pady=5, padx=5)
        back_button.grid(row=2, column=0, columnspan=2,
                         sticky=constants.EW, pady=5, padx=5)

        self._frame.rowconfigure(0, weight=1)
