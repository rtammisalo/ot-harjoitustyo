from ui.components.settings_frame import SettingsFrame


class SubstractionSettingsFrame(SettingsFrame):

    def __init__(self, root, settings):
        super().__init__(root, "Substraction Settings")
        self._keys = {self.OP1MIN: settings.SUB_OPERAND1_MIN,
                      self.OP2MIN: settings.SUB_OPERAND2_MIN,
                      self.OP1MAX: settings.SUB_OPERAND1_MAX,
                      self.OP2MAX: settings.SUB_OPERAND2_MAX,
                      self.TIMER: settings.SUB_TIMER,
                      self.TIMELIMIT: settings.SUB_TIMELIMIT}
        self.set_entry_values(settings)
