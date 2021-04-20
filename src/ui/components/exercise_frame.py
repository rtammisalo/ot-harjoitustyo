from tkinter import ttk, constants, StringVar


class ExerciseFrame:
    def __init__(self, root, answer_handler):
        self._root = root
        self.frame = None
        self._exercise_question_var = None
        self._answer_entry = None
        self._init_exercise_frame(answer_handler)

    def _init_exercise_frame(self, answer_handler):
        self.frame = ttk.Frame(
            master=self._root, borderwidth=2, relief="ridge")
        question_title_label = ttk.Label(
            master=self.frame, text="Question:")
        self._exercise_question_var = StringVar(self.frame)
        question_label = ttk.Label(
            master=self.frame, textvariable=self._exercise_question_var)
        answer_label = ttk.Label(master=self.frame, text="Answer:")
        self._answer_entry = ttk.Entry(master=self.frame)
        self._answer_entry.bind(
            "<Return>", lambda event: answer_handler())
        question_title_label.grid(sticky=constants.W, pady=(10, 0), padx=5)
        question_label.grid(pady=5, padx=5)
        answer_label.grid(sticky=constants.W, pady=(5, 0), padx=5)
        self._answer_entry.grid(sticky=constants.EW, pady=5, padx=5)
        self.frame.grid_columnconfigure(0, weight=1, minsize=300)

    def set_exercise_question(self, question):
        self._exercise_question_var.set(question)

    def set_focus_on_answer(self):
        self._answer_entry.focus()

    def get_user_answer(self):
        return self._answer_entry.get()

    def clear_answer_field(self):
        self._answer_entry.delete(0, constants.END)
        self.set_focus_on_answer()
