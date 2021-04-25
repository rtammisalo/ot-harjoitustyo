from ui.components.settings_frame import SettingsFrame


class MultiplicationSettingsFrame(SettingsFrame):
    def __init__(self, root, settings):
        super().__init__(root, "Multiplication Settings")
        self._keys = {self.OP1MIN: settings.MULTIPLY_OPERAND1_MIN,
                      self.OP2MIN: settings.MULTIPLY_OPERAND2_MIN,
                      self.OP1MAX: settings.MULTIPLY_OPERAND1_MAX,
                      self.OP2MAX: settings.MULTIPLY_OPERAND2_MAX,
                      self.TIMER: settings.MULTIPLY_TIMER,
                      self.TIMELIMIT: settings.MULTIPLY_TIMELIMIT}
        self.set_entry_values(settings)
