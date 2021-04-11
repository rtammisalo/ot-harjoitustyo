from ui.base import BaseView
from tkinter import ttk, constants, StringVar


class MultiplicationView(BaseView):
    def __init__(self, window, main_service, show_exercises):
        super().__init__(window, main_service)
        self._show_exercises = show_exercises
        self._init_frame()

    def _create_exercise_frame(self):
        self._exercise_frame = ttk.Frame(
            master=self._frame, borderwidth=2, relief="ridge")

        question_title_label = ttk.Label(
            master=self._exercise_frame, text="Question:")
        self._exercise_question = StringVar(self._exercise_frame)
        self._exercise_question.set("Huuhaa")
        self._question_label = ttk.Label(
            master=self._exercise_frame, textvariable=self._exercise_question)
        answer_label = ttk.Label(master=self._exercise_frame, text="Answer:")
        self._answer_entry = ttk.Entry(master=self._exercise_frame)

        question_title_label.grid(sticky=constants.W, pady=(10,0), padx=5)
        self._question_label.grid(pady=5, padx=5)
        answer_label.grid(sticky=constants.W, pady=(5,0), padx=5)
        self._answer_entry.grid(sticky=constants.EW, pady=5, padx=5)

    def _init_frame(self):
        self._frame = ttk.Frame(master=self._root)
        frame_header_label = ttk.Label(
            master=self._frame, text="Multiplication")
        self._create_exercise_frame()
        answer_button = ttk.Button(master=self._frame, text="Answer")
        back_button = ttk.Button(master=self._frame, text="Back")
        settings_button = ttk.Button(master=self._frame, text="Settings")

        frame_header_label.grid(sticky=constants.N, pady=10, padx=5)
        self._exercise_frame.grid(sticky=constants.EW, pady=5, padx=5)
        answer_button.grid(sticky=constants.EW, pady=5, padx=5)
        settings_button.grid(sticky=constants.EW, pady=(5,1), padx=5)
        back_button.grid(sticky=constants.EW, pady=(1,5), padx=5)