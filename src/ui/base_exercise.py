from tkinter import ttk, constants
from ui.base import BaseView
from ui.components.exercise_frame import ExerciseFrame
from ui.components.exercise_results_frame import ExerciseResultsFrame
from ui.components.keypad_frame import KeypadFrame
from ui.components.timer_frame import TimerFrame


class BaseExerciseView(BaseView):
    def __init__(self, window, main_service, show_exercises, generate_new_question):
        super().__init__(window, main_service)
        self._show_exercises = show_exercises
        self._generate_new_question = generate_new_question
        self._question = None
        self._timer_frame = None
        self._exercise_frame = None
        self._results_frame = None
        self._frame = None

    def _init_question(self):
        self._question = self._generate_new_question(
            self._main_service.show_current_user().settings)
        self._exercise_frame.set_exercise_question(self._question)
        self._timer_frame.reset_timer()

    def _answer_handler(self):
        if self._main_service.arithmetic.check_answer(
                self._question, self._exercise_frame.get_user_answer()):
            self._results_frame.set_answer_result("Correct")
        else:
            self._results_frame.set_answer_result(
                "Wrong", correct_answer=self._question.result())

        self._results_frame.set_answer_timer(
            self._timer_frame.get_elapsed_time())
        self._init_question()
        self._exercise_frame.clear_answer_entry()

    def _init_frame(self, header, use_timer, time_limit):
        self._frame = ttk.Frame(master=self._root)
        frame_header_label = ttk.Label(
            master=self._frame, text=header)

        self._timer_frame = TimerFrame(self._frame, use_timer, time_limit)
        self._exercise_frame = ExerciseFrame(self._frame, self._answer_handler)
        self._init_question()
        self._results_frame = ExerciseResultsFrame(self._frame)

        keypad_frame = KeypadFrame(
            self._frame, self._exercise_frame.answer_entry, self._answer_handler)

        answer_button = ttk.Button(
            master=self._frame, text="Answer", command=self._answer_handler)
        back_button = ttk.Button(
            master=self._frame, text="Back", command=self._show_exercises)

        frame_header_label.grid(sticky=constants.N, pady=10, padx=5)
        self._exercise_frame.frame.grid(sticky=constants.EW, pady=5, padx=5)
        self._timer_frame.frame.grid(sticky=constants.EW, pady=5, padx=5)
        self._results_frame.frame.grid(sticky=constants.EW, pady=5, padx=5)
        keypad_frame.frame.grid(sticky=constants.EW, pady=5, padx=5)
        answer_button.grid(sticky=constants.EW, pady=5, padx=5)
        back_button.grid(sticky=constants.EW, pady=(1, 5), padx=5)

        self._exercise_frame.set_focus_on_answer()
        self._update()

    def _update(self):
        self._timer_frame.update()
        self._frame.after(97, self._update)

        if self._timer_frame.is_under_time_limit():
            return

        self._answer_handler()
