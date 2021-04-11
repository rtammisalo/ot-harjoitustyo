class BaseView:
    def __init__(self, window, main_service):
        self._root = window
        self._main_service = main_service
        self._frame = None

    def pack_frame(self):
        if self._frame:
            self._frame.pack()

    def destroy_frame(self):
        if self._frame:
            self._frame.destroy()
