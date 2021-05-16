from tkinter import ttk, constants, StringVar


class ExerciseResultsFrame:
    """Frame-container class for displaying the results of the last answer in ExerciseView.

    The results include correctness, possibly correct answer and time used.
    Has methods needed to set the result and the timer.
    """

    def __init__(self, root):
        """Inits the exercise results component frame.
        """
        self._root = root
        self.frame = None
        self._answer_result_var = None
        self._answer_timer_var = None
        self._correct_answer_var = None
        self._correct_answer_label = None
        self._init_results_frame()

    def _init_results_frame(self):
        self.frame = ttk.Frame(
            master=self._root, borderwidth=2, relief="ridge")
        self._answer_result_var = StringVar(self.frame)

        answer_result_label = ttk.Label(
            master=self.frame, textvariable=self._answer_result_var)
        self._answer_timer_var = StringVar(self.frame)
        self.set_answer_timer("")
        answer_timer_label = ttk.Label(
            master=self.frame, textvariable=self._answer_timer_var)

        self._correct_answer_var = StringVar(self.frame)
        self._correct_answer_label = ttk.Label(
            master=self.frame, textvariable=self._correct_answer_var)
        self._set_answer_text_red()
        self._answer_result_var.set("Result:")

        answer_result_label.grid(
            row=0, column=0, sticky=constants.W, pady=5, padx=5)
        answer_timer_label.grid(
            row=0, column=1, sticky=constants.W, pady=5, padx=5)
        self._correct_answer_label.grid(
            sticky=constants.W, columnspan=2, pady=2, padx=5)

        self.frame.grid_columnconfigure(0, weight=1, minsize=150)
        self.frame.grid_columnconfigure(1, weight=1, minsize=150)

    def set_answer_result(self, result_correct, correct_answer=None):
        """Sets the answer result label to show the results of the last answer.

        Args:
            result_correct (boolean): If the answer was correct or not.
            correct_answer (optional): The correct answer.
        """
        if result_correct:
            self._answer_result_var.set("Result: Correct")
            self._correct_answer_var.set("")
        elif correct_answer:
            self._answer_result_var.set("Result: Wrong")
            self._correct_answer_var.set(
                f"Correct answer: {correct_answer:.3f}")

    def _set_answer_text_red(self):
        style = ttk.Style()
        style.configure("Red.TLabel", foreground="red")
        self._correct_answer_label.configure(style="Red.TLabel")

    def set_answer_timer(self, timer):
        """Sets the timer result for the last answer.
        """
        if timer == "":
            self._answer_timer_var.set("Time: ")
        else:
            self._answer_timer_var.set(f"Time: {timer:.2f}")
