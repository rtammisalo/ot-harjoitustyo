from tkinter import constants, ttk, StringVar
from entities.setting_value import OperandSettingValue, TimelimitSettingValue


class SettingEntryFrame():
    """A base entry frame for handling singular setting entries in SettingsFrame.
    """

    def __init__(self, root, setting_name):
        self._root = root
        self.frame = ttk.Frame(master=self._root)
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

    def _check_entry_constraints(self, entry_string, min_value, max_value):
        try:
            entry_value = int(entry_string)

            if not min_value <= entry_value <= max_value:
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
        min_value = OperandSettingValue.MIN_VALUE
        max_value = OperandSettingValue.MAX_VALUE
        self._check_entry_constraints(entry_string, min_value, max_value)


class TimelimitEntryFrame(SettingEntryFrame):
    """ An entry frame for Timelimit-type settings.

        Used in the settings frames of the setting-view.
    """

    def _edit_callback(self, *args):
        entry_string = self._entry_var.get()
        min_value = TimelimitSettingValue.MIN_VALUE
        max_value = TimelimitSettingValue.MAX_VALUE
        self._check_entry_constraints(entry_string, min_value, max_value)
