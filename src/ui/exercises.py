from tkinter import ttk
from ui.base import BaseView
from ui import constants as ui_constants


class ExercisesView(BaseView):
    def __init__(self, window, main_service, logout_handler, exercise_handlers):
        super().__init__(window, main_service)
        self._logout_handler = logout_handler
        self._exercise_handlers = exercise_handlers
        self._init_frame()

    def _init_frame(self):
        self._frame = ttk.Frame(master=self._root)
        frame_header_label = ttk.Label(
            master=self._frame,
            text=f"Choose exercise for {self._main_service.show_current_user().username}")

        exercises_frame = self._create_exercises_frame()

        logout_button = ttk.Button(
            master=self._frame, text="Logout", command=self._logout_handler)

        frame_header_label.grid(pady=10, padx=5)
        exercises_frame.grid(pady=10, padx=5)
        logout_button.grid(pady=10, padx=5)

    def _create_exercises_frame(self):
        exercises_frame = ttk.Frame(
            master=self._frame, borderwidth=2, relief="ridge")

        multiplication_button = ttk.Button(
            master=exercises_frame, text="Multiplication",
            command=self._exercise_handlers[ui_constants.MULTIPLICATION])
        addition_button = ttk.Button(master=exercises_frame, text="Addition")
        substraction_button = ttk.Button(
            master=exercises_frame, text="Substraction")
        division_button = ttk.Button(master=exercises_frame, text="Division")

        multiplication_button.grid(column=0, pady=5, padx=5)
        division_button.grid(row=0, column=1, pady=5, padx=5)
        addition_button.grid(column=0, pady=5, padx=5)
        substraction_button.grid(row=1, column=1, pady=5, padx=5)

        return exercises_frame
