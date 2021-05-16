from tkinter import ttk, constants, IntVar
from ui.components.setting_entry_frame import OperandEntryFrame, TimelimitEntryFrame


class SettingsFrame:
    """A base frame for organizing the different settings by group in one frame.

    Not to be used as is. Inherited by classes in settings_frames.py, such as AdditionSettingsFrame.
    """
    OP1MIN = 0
    OP2MIN = 1
    OP1MAX = 2
    OP2MAX = 3
    TIMER = 4
    TIMELIMIT = 5

    def __init__(self, root, header):
        """Inits the frame.

        Args:
            root: Frame of the settings view.
            header (str): Name of this settings frame.
        """
        self._keys = {}
        self.frame = ttk.Frame(master=root, borderwidth=2, relief="ridge")
        self._operand1_min_entry = None
        self._operand2_min_entry = None
        self._operand1_max_entry = None
        self._operand2_max_entry = None
        self._timer_var = None
        self._timelimit_entry = None

        header_label = ttk.Label(master=self.frame, text=header)
        header_label.grid(columnspan=2, sticky=constants.N, pady=5, padx=5)
        self.frame.columnconfigure(0, minsize=100)

    def _init_default_frame(self):
        self._operand1_min_entry = OperandEntryFrame(
            self.frame, "Operand 1 Minimum")
        self._operand2_min_entry = OperandEntryFrame(
            self.frame, "Operand 2 Minimum")
        self._operand1_max_entry = OperandEntryFrame(
            self.frame, "Operand 1 Maximum")
        self._operand2_max_entry = OperandEntryFrame(
            self.frame, "Operand 2 Maximum")

        self._init_timer_fields(5)

        self._operand1_min_entry.frame.grid(row=1, sticky=constants.W)
        self._operand2_min_entry.frame.grid(row=2, sticky=constants.W)
        self._operand1_max_entry.frame.grid(row=3, sticky=constants.W)
        self._operand2_max_entry.frame.grid(row=4, sticky=constants.W)

    def _init_timer_fields(self, row):
        self._timer_var = IntVar(self.frame)
        timer_radio_on = ttk.Radiobutton(
            master=self.frame, text="Timer on", variable=self._timer_var, value=1)
        timer_radio_off = ttk.Radiobutton(
            master=self.frame, text="Timer off", variable=self._timer_var, value=0)
        self._timer_var.set(0)
        self._timelimit_entry = TimelimitEntryFrame(self.frame, "Timelimit")

        self._timelimit_entry.frame.grid(row=row, sticky=constants.W)
        timer_radio_on.grid(row=row + 1, sticky=constants.W, pady=5, padx=5)
        timer_radio_off.grid(row=row + 2, sticky=constants.W, pady=5, padx=5)

    def set_entry_values(self, settings):
        """Sets the entry values to show the current settings related to this frame.

        Args:
            settings (Settings): Settings-object of the user.
        """
        self._operand1_min_entry.set_entry(
            settings.get_setting(self._keys[self.OP1MIN]))
        self._operand2_min_entry.set_entry(
            settings.get_setting(self._keys[self.OP2MIN]))
        self._operand1_max_entry.set_entry(
            settings.get_setting(self._keys[self.OP1MAX]))
        self._operand2_max_entry.set_entry(
            settings.get_setting(self._keys[self.OP2MAX]))
        self._timer_var.set(settings.get_setting(self._keys[self.TIMER]))
        self._timelimit_entry.set_entry(
            settings.get_setting(self._keys[self.TIMELIMIT]))

    def set_new_settings(self, settings):
        """Tries to to set the contents of the entry fields as new settings values.

        Args:
            settings (Settings): Settings-object of the user.
        """
        new_settings = {self._keys[self.OP1MIN]: self._operand1_min_entry.get_entry(),
                        self._keys[self.OP2MIN]: self._operand2_min_entry.get_entry(),
                        self._keys[self.OP1MAX]: self._operand1_max_entry.get_entry(),
                        self._keys[self.OP2MAX]: self._operand2_max_entry.get_entry(),
                        self._keys[self.TIMER]: self._timer_var.get(),
                        self._keys[self.TIMELIMIT]: self._timelimit_entry.get_entry()}

        self._set_settings_dict(settings, new_settings)

    def _set_settings_dict(self, settings, new_settings):
        for setting, value_str in new_settings.items():
            try:
                settings.parse_and_set_setting(setting, value_str)
            except ValueError:
                pass
