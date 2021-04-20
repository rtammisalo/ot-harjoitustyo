import time
from tkinter import ttk, constants
from ui.base import BaseView
from ui.components.exercise_frame import ExerciseFrame
from ui.components.exercise_results_frame import ExerciseResultsFrame


class BaseExerciseView(BaseView):
    def __init__(self, window, main_service, show_exercises, generate_new_question):
        super().__init__(window, main_service)
        self._show_exercises = show_exercises
        self._generate_new_question = generate_new_question
        self._question = None
        self._start_time = 0
        self._exercise_frame = None
        self._results_frame = None
        self._frame = None

    def _init_question(self):
        self._question = self._generate_new_question(
            self._main_service.show_current_user().settings)
        self._exercise_frame.set_exercise_question(self._question)
        self._start_time = time.perf_counter()

    def _answer_handler(self):
        elapsed_time = time.perf_counter() - self._start_time

        if self._main_service.arithmetic.check_answer(
                self._question, self._exercise_frame.get_user_answer()):
            self._results_frame.set_answer_result("Correct")
        else:
            self._results_frame.set_answer_result(
                f"Wrong ({self._question.result()})")

        self._results_frame.set_answer_timer(elapsed_time)
        self._init_question()
        self._exercise_frame.clear_answer_field()

    def _init_frame(self, header):
        self._frame = ttk.Frame(master=self._root)
        frame_header_label = ttk.Label(
            master=self._frame, text=header)

        self._exercise_frame = ExerciseFrame(self._frame, self._answer_handler)
        self._init_question()
        self._results_frame = ExerciseResultsFrame(self._frame)

        answer_button = ttk.Button(
            master=self._frame, text="Answer", command=self._answer_handler)
        back_button = ttk.Button(
            master=self._frame, text="Back", command=self._show_exercises)

        frame_header_label.grid(sticky=constants.N, pady=10, padx=5)
        self._exercise_frame.frame.grid(sticky=constants.EW, pady=5, padx=5)
        self._results_frame.frame.grid(sticky=constants.EW, pady=5, padx=5)
        answer_button.grid(sticky=constants.EW, pady=5, padx=5)
        back_button.grid(sticky=constants.EW, pady=(1, 5), padx=5)

        self._exercise_frame.set_focus_on_answer()
