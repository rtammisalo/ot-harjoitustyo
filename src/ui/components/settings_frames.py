from tkinter import ttk, constants, IntVar
from ui.components.settings_frame import SettingsFrame


class AdditionSettingsFrame(SettingsFrame):
    """A frame containing all settings related to addition exercises.
    """

    def __init__(self, root, settings):
        super().__init__(root, "Addition Settings")
        self._init_default_frame()
        self._keys = {self.OP1MIN: settings.ADD_OPERAND1_MIN,
                      self.OP2MIN: settings.ADD_OPERAND2_MIN,
                      self.OP1MAX: settings.ADD_OPERAND1_MAX,
                      self.OP2MAX: settings.ADD_OPERAND2_MAX,
                      self.TIMER: settings.ADD_TIMER,
                      self.TIMELIMIT: settings.ADD_TIMELIMIT}
        self.set_entry_values(settings)


class DivisionSettingsFrame(SettingsFrame):
    """A frame containing all settings related to division exercises.
    """

    def __init__(self, root, settings):
        super().__init__(root, "Division Settings")
        self._init_default_frame()
        self._keys = {self.OP1MIN: settings.DIVIDE_OPERAND1_MIN,
                      self.OP2MIN: settings.DIVIDE_OPERAND2_MIN,
                      self.OP1MAX: settings.DIVIDE_OPERAND1_MAX,
                      self.OP2MAX: settings.DIVIDE_OPERAND2_MAX,
                      self.TIMER: settings.DIVIDE_TIMER,
                      self.TIMELIMIT: settings.DIVIDE_TIMELIMIT}
        self.set_entry_values(settings)


class MultiplicationSettingsFrame(SettingsFrame):
    """A frame containing all settings related to Multiplication exercises.
    """

    def __init__(self, root, settings):
        super().__init__(root, "Multiplication Settings")
        self._init_default_frame()
        self._keys = {self.OP1MIN: settings.MULTIPLY_OPERAND1_MIN,
                      self.OP2MIN: settings.MULTIPLY_OPERAND2_MIN,
                      self.OP1MAX: settings.MULTIPLY_OPERAND1_MAX,
                      self.OP2MAX: settings.MULTIPLY_OPERAND2_MAX,
                      self.TIMER: settings.MULTIPLY_TIMER,
                      self.TIMELIMIT: settings.MULTIPLY_TIMELIMIT}
        self.set_entry_values(settings)


class SubstractionSettingsFrame(SettingsFrame):
    """A frame containing all settings related to substraction exercises.
    """

    def __init__(self, root, settings):
        super().__init__(root, "Substraction Settings")
        self._init_default_frame()
        self._keys = {self.OP1MIN: settings.SUB_OPERAND1_MIN,
                      self.OP2MIN: settings.SUB_OPERAND2_MIN,
                      self.OP1MAX: settings.SUB_OPERAND1_MAX,
                      self.OP2MAX: settings.SUB_OPERAND2_MAX,
                      self.TIMER: settings.SUB_TIMER,
                      self.TIMELIMIT: settings.SUB_TIMELIMIT}
        self.set_entry_values(settings)


class RandomExerciseSettingsFrame(SettingsFrame):
    """A frame containing all settings related to random exercises.
    """

    def __init__(self, root, settings):
        super().__init__(root, "Random Exercise Settings")
        self._use_multiply_var = IntVar(self.frame)
        self._use_divide_var = IntVar(self.frame)
        self._use_add_var = IntVar(self.frame)
        self._use_sub_var = IntVar(self.frame)
        self._init_frame()
        self.set_entry_values(settings)

    def _init_frame(self):
        self._init_radio_button("Multiplication", self._use_multiply_var, 1)
        self._init_radio_button("Division", self._use_divide_var, 3)
        self._init_radio_button("Addition", self._use_add_var, 5)
        self._init_radio_button("Substraction", self._use_sub_var, 7)
        self._init_timer_fields(9)

    def _init_radio_button(self, label_text, button_var, row):
        label = ttk.Label(master=self.frame, text=f"{label_text}:")
        radio_on = ttk.Radiobutton(
            master=self.frame, text="On", variable=button_var, value=1)
        radio_off = ttk.Radiobutton(
            master=self.frame, text="Off", variable=button_var, value=0)

        button_var.set(0)

        label.grid(row=row, sticky=constants.W, pady=5, padx=5)
        radio_on.grid(row=row + 1, column=0,
                      sticky=constants.W, pady=5, padx=5)
        radio_off.grid(row=row + 1, column=1,
                       sticky=constants.W, pady=5, padx=5)

    def set_entry_values(self, settings):
        """Sets entry values to settings-values.

        Args:
            settings (Settings): Settings-object of the user.
        """
        self._use_multiply_var.set(
            settings.get_setting(settings.RANDOM_USE_MULTIPLY))
        self._use_divide_var.set(
            settings.get_setting(settings.RANDOM_USE_DIVIDE))
        self._use_add_var.set(settings.get_setting(settings.RANDOM_USE_ADD))
        self._use_sub_var.set(settings.get_setting(settings.RANDOM_USE_SUB))
        self._timer_var.set(settings.get_setting(settings.RANDOM_TIMER))
        self._timer_entry.insert(
            0, settings.get_setting(settings.RANDOM_TIMELIMIT))

    def set_new_settings(self, settings):
        """Tries to set the entry field contents as settings in the Settings-object.

        Args:
            settings (Settings): Settings-object of the user.
        """
        new_settings = {settings.RANDOM_USE_MULTIPLY: self._use_multiply_var.get(),
                        settings.RANDOM_USE_DIVIDE: self._use_divide_var.get(),
                        settings.RANDOM_USE_ADD: self._use_add_var.get(),
                        settings.RANDOM_USE_SUB: self._use_sub_var.get(),
                        settings.RANDOM_TIMER: self._timer_var.get(),
                        settings.RANDOM_TIMELIMIT: self._timer_entry.get()}

        self._set_settings_dict(settings, new_settings)
