class BaseView:
    def __init__(self, window):
        self._root = window
        self._frame = None

    def pack_frame(self):
        if self._frame:
            self._frame.pack()

    def destroy_frame(self):
        if self._frame:
            self._frame.destroy()
