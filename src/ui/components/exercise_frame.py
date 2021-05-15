from tkinter import ttk, constants, StringVar


class ExerciseFrame:
    """Frame-container class for displaying an exercise question to the user in ExerciseView.

    The frame contains a label for the question and an answer entry field.
    Has methods needed to set/get and clear answer entry.
    """

    def __init__(self, root, answer_handler):
        self._root = root
        self.frame = None
        self._exercise_question_var = None
        self.answer_entry = None
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
        self.answer_entry = ttk.Entry(master=self.frame)
        self.answer_entry.bind(
            "<Return>", lambda event: answer_handler())
        question_title_label.grid(sticky=constants.W, pady=(10, 0), padx=5)
        question_label.grid(pady=5, padx=5)
        answer_label.grid(sticky=constants.W, pady=(5, 0), padx=5)
        self.answer_entry.grid(sticky=constants.EW, pady=5, padx=5)
        self.frame.grid_columnconfigure(0, weight=1, minsize=300)

    def set_exercise_question(self, question):
        """Sets a new exercise question.

        Args:
            question (Operation): A new question, such as DivisionOperation.
        """
        self._exercise_question_var.set(question)

    def set_focus_on_answer(self):
        """Sets the focus on the answer entry.
        """
        self.answer_entry.focus()

    def get_user_answer(self):
        """Returns the user answer.

        Returns:
            str: Answer from the user.
        """
        return self.answer_entry.get()

    def clear_answer_entry(self):
        """Clears the answer entry and resets focus to it.
        """
        self.answer_entry.delete(0, constants.END)
        self.set_focus_on_answer()
