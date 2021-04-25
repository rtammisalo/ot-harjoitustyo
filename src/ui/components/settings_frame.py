from tkinter import ttk, constants, IntVar


class SettingsFrame:
    OP1MIN = 0
    OP2MIN = 1
    OP1MAX = 2
    OP2MAX = 3
    TIMER = 4
    TIMELIMIT = 5

    def __init__(self, root, header):
        self._keys = {}
        self.frame = ttk.Frame(master=root, borderwidth=2, relief="ridge")

        header_label = ttk.Label(master=self.frame, text=header)
        self._operand1_min_entry = ttk.Entry(self.frame, width=10)
        self._operand2_min_entry = ttk.Entry(self.frame, width=10)
        self._operand1_max_entry = ttk.Entry(self.frame, width=10)
        self._operand2_max_entry = ttk.Entry(self.frame, width=10)
        self._timer_var = IntVar(self.frame)
        timer_radio_on = ttk.Radiobutton(
            master=self.frame, text="Timer on", variable=self._timer_var, value=1)
        timer_radio_off = ttk.Radiobutton(
            master=self.frame, text="Timer off", variable=self._timer_var, value=0)
        self._timer_var.set(0)
        self._timer_entry = ttk.Entry(self.frame, width=10)

        header_label.grid(columnspan=2, sticky=constants.N, pady=5, padx=5)
        self._set_label_entry_group(
            "Operand 1 Minimum:", self._operand1_min_entry, row=1)
        self._set_label_entry_group(
            "Operand 2 Minimum:", self._operand2_min_entry, row=2)
        self._set_label_entry_group(
            "Operand 1 Maximum:", self._operand1_max_entry, row=3)
        self._set_label_entry_group(
            "Operand 2 Maximum:", self._operand2_max_entry, row=4)

        timer_radio_on.grid(row=5, sticky=constants.W, pady=5, padx=5)
        timer_radio_off.grid(row=6, sticky=constants.W, pady=5, padx=5)
        self._set_label_entry_group("Timelimit:", self._timer_entry, row=7)

        self.frame.columnconfigure(0, minsize=100)
        self.frame.columnconfigure(1, minsize=100)

    def _set_label_entry_group(self, label_text, entry, row):
        label = ttk.Label(self.frame, text=label_text)
        label.grid(row=row, column=0, sticky=constants.W, pady=(0, 5), padx=5)
        entry.grid(row=row, column=1, sticky=constants.W, pady=(0, 5), padx=5)

    def set_entry_values(self, settings):
        self._operand1_min_entry.insert(
            0, settings.get_setting(self._keys[self.OP1MIN]))
        self._operand2_min_entry.insert(
            0, settings.get_setting(self._keys[self.OP2MIN]))
        self._operand1_max_entry.insert(
            0, settings.get_setting(self._keys[self.OP1MAX]))
        self._operand2_max_entry.insert(
            0, settings.get_setting(self._keys[self.OP2MAX]))
        self._timer_var.set(settings.get_setting(self._keys[self.TIMER]))
        self._timer_entry.insert(
            0, settings.get_setting(self._keys[self.TIMELIMIT]))

    def set_new_settings(self, settings):
        new_settings = {self._keys[self.OP1MIN]: self._operand1_min_entry.get(),
                        self._keys[self.OP2MIN]: self._operand2_min_entry.get(),
                        self._keys[self.OP1MAX]: self._operand1_max_entry.get(),
                        self._keys[self.OP2MAX]: self._operand2_max_entry.get(),
                        self._keys[self.TIMER]: self._timer_var.get(),
                        self._keys[self.TIMELIMIT]: self._timer_entry.get()}

        for setting, value_str in new_settings.items():
            try:
                settings.parse_and_set_setting(setting, value_str)
            except ValueError:
                pass
