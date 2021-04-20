from ui.components.settings_frame import SettingsFrame


class MultiplicationSettingsFrame(SettingsFrame):
    def __init__(self, root, settings):
        super().__init__(root, "Multiplication Settings")
        self.set_values(settings)

    def set_values(self, settings):
        self._operand1_min_entry.insert(
            0, settings.get_setting(settings.MULTIPLY_OPERAND1_MIN))
        self._operand2_min_entry.insert(
            0, settings.get_setting(settings.MULTIPLY_OPERAND2_MIN))
        self._operand1_max_entry.insert(
            0, settings.get_setting(settings.MULTIPLY_OPERAND1_MAX))
        self._operand2_max_entry.insert(
            0, settings.get_setting(settings.MULTIPLY_OPERAND2_MAX))
        self._timer_var.set(settings.get_setting(settings.MULTIPLY_TIMER))
        self._timer_entry.insert(
            0, settings.get_setting(settings.MULTIPLY_TIMELIMIT))

    def get_values_in_dict(self, settings):
        try:
            new_settings = {settings.MULTIPLY_OPERAND1_MIN: int(self._operand1_min_entry.get()),
                            settings.MULTIPLY_OPERAND2_MIN: int(self._operand2_min_entry.get()),
                            settings.MULTIPLY_OPERAND1_MAX: int(self._operand1_max_entry.get()),
                            settings.MULTIPLY_OPERAND2_MAX: int(self._operand2_max_entry.get()),
                            settings.MULTIPLY_TIMER: int(self._timer_var.get()),
                            settings.MULTIPLY_TIMELIMIT: int(self._timer_entry.get())}
        except ValueError:
            return None

        return new_settings

    def set_new_settings(self, settings):
        settings.set_settings_from_dict(self.get_values_in_dict(settings))
