import functools
from tkinter import StringVar, ttk, constants
from entities.settings import Settings


class KeypadFrame:
    """A keypad frame used for inputting answers without a keyboard.

    By default the keypad starts out hidden. Users can show it by clicking a button.

    Attributes:
        keypad_hidden: An attribute for deciding whether to show or hide the keypad.
    """

    def __init__(self, root, main_service, answer_entry, answer_handler):
        self._root = root
        self._main_service = main_service
        self.frame = None
        self._answer_entry = answer_entry
        self.frame = ttk.Frame(
            master=self._root, borderwidth=2, relief="ridge")
        self._hide_keypad_var = StringVar(master=self.frame)
        hide_keypad_button = ttk.Button(
            master=self.frame, textvariable=self._hide_keypad_var,
            command=self._flip_keypad_state)

        self._init_keypad(answer_handler)

        hide_keypad_button.grid(sticky=constants.EW)

        self._show_keypad()

        self.frame.grid_columnconfigure(0, weight=1, minsize=333)

    def _init_keypad(self, answer_handler):
        self.keypad = ttk.Frame(master=self.frame)

        for row in range(0, 3):
            for column in range(0, 3):
                button_number = 7 - (row * 3) + column
                # Partial freezes arguments in place. Used like a normal function call.
                input_function = functools.partial(
                    self._input_handler, str(button_number))
                button = ttk.Button(master=self.keypad,
                                    text=str(button_number),
                                    command=input_function)
                button.grid(row=row, column=column, sticky=constants.EW)

        zero_button = ttk.Button(
            master=self.keypad, text="0", command=lambda: self._input_handler("0"))
        dot_button = ttk.Button(
            master=self.keypad, text=".", command=lambda: self._input_handler("."))
        del_button = ttk.Button(
            master=self.keypad, text="<", command=self._remove_last_input)
        ce_button = ttk.Button(
            master=self.keypad, text="CE", command=self._clear_answer_entry)
        enter_button = ttk.Button(
            master=self.keypad, text="Enter", command=answer_handler)

        zero_button.grid(row=3, column=0, columnspan=2, sticky=constants.EW)
        dot_button.grid(row=3, column=2, sticky=constants.EW)
        del_button.grid(row=0, column=3, sticky=constants.EW)
        ce_button.grid(row=1, column=3, sticky=constants.EW)
        enter_button.grid(row=2, column=3, rowspan=2, sticky=constants.NSEW)

        self.keypad.grid_columnconfigure(0, weight=1, minsize=30)
        self.keypad.grid_columnconfigure(1, weight=1, minsize=30)
        self.keypad.grid_columnconfigure(2, weight=1, minsize=30)
        self.keypad.grid_columnconfigure(3, weight=1, minsize=50)

    def _input_handler(self, new_input):
        self._answer_entry.insert(constants.END, new_input)
        self._answer_entry.focus()

    def _remove_last_input(self):
        characters = len(self._answer_entry.get())
        if characters > 0:
            self._answer_entry.delete(characters - 1)
        self._answer_entry.focus()

    def _get_keypad_status(self):
        return self._main_service.show_current_user().settings.get_setting(Settings.HIDE_KEYPAD)

    def _set_keypad_status(self, new_state):
        self._main_service.show_current_user().settings.set_setting(
            Settings.HIDE_KEYPAD, new_state)
        self._main_service.save_settings()

    def _flip_keypad_state(self):
        keypad_hidden = self._get_keypad_status()

        if keypad_hidden == 1:
            self._set_keypad_status(0)
        else:
            self._set_keypad_status(1)

        self._show_keypad()

    def _show_keypad(self):
        keypad_hidden = self._get_keypad_status()

        if keypad_hidden == 1:
            self._hide_keypad_var.set("Show Keypad")
            self.keypad.grid_remove()
        else:
            self._hide_keypad_var.set("Hide Keypad")
            self.keypad.grid(sticky=constants.EW)

    def _clear_answer_entry(self):
        self._answer_entry.delete(0, constants.END)
        self._answer_entry.focus()
