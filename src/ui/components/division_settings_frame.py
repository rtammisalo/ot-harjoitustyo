from ui.components.settings_frame import SettingsFrame


class DivisionSettingsFrame(SettingsFrame):

    def __init__(self, root, settings):
        super().__init__(root, "Division Settings")
        self._keys = {self.OP1MIN: settings.DIVIDE_OPERAND1_MIN,
                      self.OP2MIN: settings.DIVIDE_OPERAND2_MIN,
                      self.OP1MAX: settings.DIVIDE_OPERAND1_MAX,
                      self.OP2MAX: settings.DIVIDE_OPERAND2_MAX,
                      self.TIMER: settings.DIVIDE_TIMER,
                      self.TIMELIMIT: settings.DIVIDE_TIMELIMIT}
        self.set_entry_values(settings)
