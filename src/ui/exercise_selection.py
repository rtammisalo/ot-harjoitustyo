from tkinter import ttk, constants
from ui.base import BaseView
from ui import constants as ui_constants


class ExerciseSelectionView(BaseView):
    def __init__(self, window, main_service, logout_handler, exercise_handlers, settings_handler):
        super().__init__(window, main_service)
        self._logout_handler = logout_handler
        self._exercise_handlers = exercise_handlers
        self._settings_handler = settings_handler
        self._init_frame()

    def _init_frame(self):
        self._frame = ttk.Frame(master=self._root)
        frame_header_label = ttk.Label(
            master=self._frame,
            text=f"Choose exercise for {self._main_service.show_current_user().username}")

        exercises_frame = self._create_exercises_frame()

        settings_button = ttk.Button(
            master=self._frame, text="Settings", command=self._settings_handler)
        logout_button = ttk.Button(
            master=self._frame, text="Logout", command=self._logout_handler)

        frame_header_label.grid(pady=10, padx=5)
        exercises_frame.grid(pady=10, padx=5)
        settings_button.grid(pady=10, padx=5)
        logout_button.grid(pady=10, padx=5)

        self._frame.focus()
        self._frame.bind(
            "1", lambda event: self._exercise_handlers[ui_constants.MULTIPLICATION]())
        self._frame.bind(
            "2", lambda event: self._exercise_handlers[ui_constants.DIVISION]())
        self._frame.bind(
            "3", lambda event: self._exercise_handlers[ui_constants.ADDITION]())
        self._frame.bind(
            "4", lambda event: self._exercise_handlers[ui_constants.SUBSTRACTION]())
        self._frame.bind(
            "5", lambda event: self._exercise_handlers[ui_constants.RANDOM]())

    def _create_exercises_frame(self):
        exercises_frame = ttk.Frame(
            master=self._frame, borderwidth=2, relief="ridge")

        style = ttk.Style()
        style.configure("Left.TButton", anchor=constants.W)

        multiplication_button = ttk.Button(
            master=exercises_frame, text="(1) Multiplication", style="Left.TButton",
            command=self._exercise_handlers[ui_constants.MULTIPLICATION])
        division_button = ttk.Button(
            master=exercises_frame, text="(2) Division", style="Left.TButton",
            command=self._exercise_handlers[ui_constants.DIVISION])
        addition_button = ttk.Button(
            master=exercises_frame, text="(3) Addition", style="Left.TButton",
            command=self._exercise_handlers[ui_constants.ADDITION])
        substraction_button = ttk.Button(
            master=exercises_frame, text="(4) Substraction", style="Left.TButton",
            command=self._exercise_handlers[ui_constants.SUBSTRACTION])
        random_button = ttk.Button(
            master=exercises_frame, text="(5) Random Exercises",
            command=self._exercise_handlers[ui_constants.RANDOM])

        multiplication_button.grid(
            row=0, column=0, sticky=constants.EW, pady=2, padx=2)
        division_button.grid(
            row=0, column=1, sticky=constants.EW, pady=2, padx=2)
        addition_button.grid(
            row=1, column=0, sticky=constants.EW, pady=2, padx=2)
        substraction_button.grid(
            row=1, column=1, sticky=constants.EW, pady=2, padx=2)
        random_button.grid(row=2, columnspan=2,
                           sticky=constants.EW, pady=5, padx=2)

        return exercises_frame
