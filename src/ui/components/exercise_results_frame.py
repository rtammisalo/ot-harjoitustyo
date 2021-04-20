from tkinter import ttk, constants, StringVar


class ExerciseResultsFrame:
    def __init__(self, root):
        self._root = root
        self.frame = None
        self._answer_result_var = None
        self._answer_timer_var = None
        self._init_results_frame()

    def _init_results_frame(self):
        self.frame = ttk.Frame(
            master=self._root, borderwidth=2, relief="ridge")
        self._answer_result_var = StringVar(self.frame)
        self.set_answer_result("")
        answer_result_label = ttk.Label(
            master=self.frame, textvariable=self._answer_result_var)
        self._answer_timer_var = StringVar(self.frame)
        self.set_answer_timer("")
        answer_timer_label = ttk.Label(
            master=self.frame, textvariable=self._answer_timer_var)

        answer_result_label.grid(
            row=0, column=0, sticky=constants.W, pady=5, padx=5)
        answer_timer_label.grid(
            row=0, column=1, sticky=constants.W, pady=5, padx=5)
        self.frame.grid_columnconfigure(0, weight=1, minsize=150)
        self.frame.grid_columnconfigure(1, weight=1, minsize=150)

    def set_answer_result(self, result):
        self._answer_result_var.set(f"Result: {result}")

    def set_answer_timer(self, timer):
        if timer == "":
            self._answer_timer_var.set("Time: ")
        else:
            self._answer_timer_var.set(f"Time: {timer:.2f}")