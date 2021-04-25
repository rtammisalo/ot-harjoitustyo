import time
from tkinter import ttk, constants, StringVar


class TimerFrame:
    def __init__(self, root, use_timer, time_limit):
        self._root = root
        self._time_limit = time_limit / 1000
        self.frame = ttk.Frame(master=root, borderwidth=2, relief="ridge")
        self._start_time = time.perf_counter()
        self._use_timer = use_timer

        self._elapsed_time_var = StringVar(self.frame)
        elapsed_time_label = ttk.Label(
            self.frame, textvariable=self._elapsed_time_var)

        self._time_left_var = StringVar(self.frame)
        time_left_label = ttk.Label(
            self.frame, textvariable=self._time_left_var)

        elapsed_time_label.grid(
            row=0, column=0, sticky=constants.W, pady=5, padx=5)

        if self._use_timer == 1:
            time_left_label.grid(
                row=0, column=1, sticky=constants.W, pady=5, padx=5)

        self.frame.grid_columnconfigure(0, weight=1, minsize=150)
        self.frame.grid_columnconfigure(1, weight=1, minsize=150)

        self.update()

    def get_elapsed_time(self):
        elapsed_time = time.perf_counter() - self._start_time

        if self._use_timer == 1:
            return elapsed_time if elapsed_time < self._time_limit else self._time_limit

        return elapsed_time

    def get_time_left(self):
        time_left = self._time_limit - self.get_elapsed_time()
        return time_left if time_left >= 0 else 0.0

    def is_under_time_limit(self):
        if self._use_timer == 0 or self.get_time_left() > 0:
            return True

        return False

    def update(self):
        self._elapsed_time_var.set(
            f"Elapsed time: {self.get_elapsed_time():.2f}")
        self._time_left_var.set(f"Time left: {self.get_time_left():.2f}")

    def reset_timer(self):
        self._start_time = time.perf_counter()
