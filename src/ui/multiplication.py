import time
from tkinter import ttk, constants, StringVar
from ui.base import BaseView


class MultiplicationView(BaseView):
    def __init__(self, window, main_service, show_exercises):
        super().__init__(window, main_service)
        self._show_exercises = show_exercises
        self._question = None
        self._start_time = 0
        self._answer_entry = None
        self._answer_result_var = None
        self._answer_timer_var = None
        self._exercise_question_var = None
        self._init_frame()

    def _init_new_question(self):
        self._question = self._main_service.arithmetic.get_multiplication_question()
        self._exercise_question_var.set(self._question)
        self._start_time = time.perf_counter()

    def _init_exercise_frame(self):
        exercise_frame = ttk.Frame(
            master=self._frame, borderwidth=2, relief="ridge")

        question_title_label = ttk.Label(
            master=exercise_frame, text="Question:")
        self._exercise_question_var = StringVar(exercise_frame)
        self._init_new_question()
        question_label = ttk.Label(
            master=exercise_frame, textvariable=self._exercise_question_var)
        answer_label = ttk.Label(master=exercise_frame, text="Answer:")
        self._answer_entry = ttk.Entry(master=exercise_frame)
        self._answer_entry.bind(
            "<Return>", lambda event: self._answer_handler())
        question_title_label.grid(sticky=constants.W, pady=(10, 0), padx=5)
        question_label.grid(pady=5, padx=5)
        answer_label.grid(sticky=constants.W, pady=(5, 0), padx=5)
        self._answer_entry.grid(sticky=constants.EW, pady=5, padx=5)
        exercise_frame.grid_columnconfigure(0, weight=1, minsize=300)

        return exercise_frame

    def _init_results_frame(self):
        results_frame = ttk.Frame(
            master=self._frame, borderwidth=2, relief="ridge")

        self._answer_result_var = StringVar(results_frame)
        self._set_answer_result("")
        answer_result_label = ttk.Label(
            master=results_frame, textvariable=self._answer_result_var)
        self._answer_timer_var = StringVar(results_frame)
        self._set_answer_timer("")
        answer_timer_label = ttk.Label(
            master=results_frame, textvariable=self._answer_timer_var)

        answer_result_label.grid(
            row=0, column=0, sticky=constants.W, pady=5, padx=5)
        answer_timer_label.grid(
            row=0, column=1, sticky=constants.W, pady=5, padx=5)
        results_frame.grid_columnconfigure(0, weight=1, minsize=150)
        results_frame.grid_columnconfigure(1, weight=1, minsize=150)

        return results_frame

    def _set_answer_result(self, result):
        self._answer_result_var.set(f"Result: {result}")

    def _set_answer_timer(self, timer):
        if timer == "":
            self._answer_timer_var.set("Time: ")
        else:
            self._answer_timer_var.set(f"Time: {timer:.2f}")

    def _answer_handler(self):
        elapsed_time = time.perf_counter() - self._start_time

        if self._main_service.arithmetic.check_answer(
                self._question, self._answer_entry.get()):
            self._set_answer_result("Correct")
        else:
            self._set_answer_result(f"Wrong ({self._question.result()})")

        self._set_answer_timer(elapsed_time)
        self._init_new_question()
        self._answer_entry.delete(0, constants.END)
        self._answer_entry.focus()

    def _init_frame(self):
        self._frame = ttk.Frame(master=self._root)
        frame_header_label = ttk.Label(
            master=self._frame, text="Multiplication")

        exercise_frame = self._init_exercise_frame()
        results_frame = self._init_results_frame()
        answer_button = ttk.Button(
            master=self._frame, text="Answer", command=self._answer_handler)
        back_button = ttk.Button(master=self._frame, text="Back", command=self._show_exercises)
        settings_button = ttk.Button(master=self._frame, text="Settings")

        frame_header_label.grid(sticky=constants.N, pady=10, padx=5)
        exercise_frame.grid(sticky=constants.EW, pady=5, padx=5)
        results_frame.grid(sticky=constants.EW, pady=5, padx=5)
        answer_button.grid(sticky=constants.EW, pady=5, padx=5)
        settings_button.grid(sticky=constants.EW, pady=(5, 1), padx=5)
        back_button.grid(sticky=constants.EW, pady=(1, 5), padx=5)

        self._answer_entry.focus()
