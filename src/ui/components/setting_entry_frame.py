from tkinter import constants, ttk, StringVar
from entities.setting_value import OperandSettingValue, TimelimitSettingValue


class SettingEntryFrame():
    """A base entry frame for handling singular setting entries in SettingsFrame.
    """

    def __init__(self, root, setting_name):
        """Inits the SettingEntryFrame.

        Args:
            root: The SettingsFrame this entry belongs to.
            setting_name (str): Name of the setting.
        """
        self.frame = ttk.Frame(master=root)
        header_label = ttk.Label(master=self.frame, text=f"{setting_name}:")
        self._entry_var = StringVar(master=self.frame)
        self._entry_var.trace_add(mode="write", callback=self._edit_callback)
        entry = ttk.Entry(
            master=self.frame, textvariable=self._entry_var, width=10)
        self._error_var = StringVar(master=self.frame)
        self._error_label = ttk.Label(
            master=self.frame, textvariable=self._error_var)

        header_label.grid(row=0, column=0, sticky=constants.W,
                          pady=(0, 5), padx=5)
        entry.grid(row=0, column=1, sticky=constants.W,
                   pady=(0, 5), padx=5)

        self.frame.columnconfigure(0, minsize=170)
        self.frame.columnconfigure(1, minsize=70)

    def _edit_callback(self, *args):
        pass

    def _check_entry_constraints(self, entry_string, parser, sanitizer, min_value, max_value):
        try:
            entry_value = parser(entry_string)
            if entry_value != sanitizer(entry_value):
                self._show_error(
                    f"Value is not between {min_value}, {max_value}")
            else:
                self._hide_error()
        except ValueError:
            self._show_error("Value is not an integer")

    def _show_error(self, error_message):
        self._error_var.set(error_message)
        self._error_label.grid(row=1, columnspan=2, sticky=constants.W,
                               pady=(0, 5), padx=5)

    def _hide_error(self):
        self._error_var.set("")
        self._error_label.grid_remove()

    def get_entry(self):
        """Returns the value of this entry as a string.
        """
        return self._entry_var.get()

    def set_entry(self, value):
        """Sets the value of this entry.
        """
        self._entry_var.set(value)


class OperandEntryFrame(SettingEntryFrame):
    """ An entry frame for Operand-type settings.

        Used in the settings frames of the setting-view.
    """

    def _edit_callback(self, *args):
        entry_string = self._entry_var.get()
        self._check_entry_constraints(entry_string,
                                      OperandSettingValue.parse,
                                      OperandSettingValue.sanitize,
                                      OperandSettingValue.MIN_VALUE,
                                      OperandSettingValue.MAX_VALUE)


class TimelimitEntryFrame(SettingEntryFrame):
    """ An entry frame for Timelimit-type settings.

        Used in the settings frames of the setting-view.
    """

    def _edit_callback(self, *args):
        entry_string = self._entry_var.get()
        self._check_entry_constraints(entry_string,
                                      TimelimitSettingValue.parse,
                                      TimelimitSettingValue.sanitize,
                                      TimelimitSettingValue.MIN_VALUE,
                                      TimelimitSettingValue.MAX_VALUE)
