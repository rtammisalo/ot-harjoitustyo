class BaseView:
    """A small base view class used as a base for all the different views of the program.

    A view as a concept encapsulates all the UI-logic related to the "view" the user sees, e.g.
    LoginView, the window seen when logging in, or AdditionView, when the user is looking at
    addition exercises.
    """

    def __init__(self, window, main_service):
        self._root = window
        self._main_service = main_service
        self._frame = None

    def pack_frame(self):
        """Packs the frame to be shown to the user.
        """
        if self._frame:
            self._frame.pack()

    def destroy_frame(self):
        """Destroys all components related to this frame (and view).
        """
        if self._frame:
            self._frame.destroy()
