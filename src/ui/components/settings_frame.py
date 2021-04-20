from tkinter import ttk, constants, IntVar


class SettingsFrame:
    def __init__(self, root, header):
        self._root = root
        self.frame = ttk.Frame(master=root, borderwidth=2, relief="ridge")

        header_label = ttk.Label(master=self.frame, text=header)
        self._operand1_min_entry = ttk.Entry(self.frame)
        self._operand2_min_entry = ttk.Entry(self.frame)
        self._operand1_max_entry = ttk.Entry(self.frame)
        self._operand2_max_entry = ttk.Entry(self.frame)
        self._timer_var = IntVar(self.frame)
        timer_radio_on = ttk.Radiobutton(
            master=self.frame, text="Timer on", variable=self._timer_var, value=1)
        timer_radio_off = ttk.Radiobutton(
            master=self.frame, text="Timer off", variable=self._timer_var, value=0)
        self._timer_var.set(0)
        self._timer_entry = ttk.Entry(self.frame)

        header_label.grid(columnspan=2, sticky=constants.N, pady=5, padx=5)
        self._set_label_entry_group(
            "Operand 1 Minimum:", self._operand1_min_entry, row=1)
        self._set_label_entry_group(
            "Operand 2 Minimum:", self._operand2_min_entry, row=2)
        self._set_label_entry_group(
            "Operand 1 Maximum:", self._operand1_max_entry, row=3)
        self._set_label_entry_group(
            "Operand 2 Maximum:", self._operand2_max_entry, row=4)

        timer_radio_on.grid(sticky=constants.W, pady=5, padx=5)
        timer_radio_off.grid(sticky=constants.W, pady=5, padx=5)
        self._set_label_entry_group("Timelimit:", self._timer_entry, row=8)

        self.frame.grid_columnconfigure(0, weight=1, minsize=150)
        self.frame.grid_columnconfigure(1, weight=1, minsize=150)

    def _set_label_entry_group(self, label_text, entry, row):
        label = ttk.Label(self.frame, text=label_text)
        label.grid(row=row, column=0, sticky=constants.EW, pady=(0, 5), padx=5)
        entry.grid(row=row, column=1, sticky=constants.EW, pady=(0, 5), padx=5)
