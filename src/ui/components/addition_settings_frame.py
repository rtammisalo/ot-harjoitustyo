from ui.components.settings_frame import SettingsFrame


class AdditionSettingsFrame(SettingsFrame):

    def __init__(self, root, settings):
        super().__init__(root, "Addition Settings")
        self._keys = {self.OP1MIN: settings.ADD_OPERAND1_MIN,
                      self.OP2MIN: settings.ADD_OPERAND2_MIN,
                      self.OP1MAX: settings.ADD_OPERAND1_MAX,
                      self.OP2MAX: settings.ADD_OPERAND2_MAX,
                      self.TIMER: settings.ADD_TIMER,
                      self.TIMELIMIT: settings.ADD_TIMELIMIT}
        self.set_entry_values(settings)
