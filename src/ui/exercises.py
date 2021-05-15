from ui.base_exercise import BaseExerciseView
from entities.settings import Settings


class AdditionView(BaseExerciseView):
    """A view for practicing additions.
    """

    def __init__(self, window, main_service, show_exercises):
        super().__init__(window, main_service, show_exercises,
                         main_service.arithmetic.get_addition_question)
        user = main_service.show_current_user()
        use_timer = user.settings.get_setting(Settings.ADD_TIMER)
        time_limit = user.settings.get_setting(Settings.ADD_TIMELIMIT)
        self._init_frame("Addition", use_timer, time_limit)


class DivisionView(BaseExerciseView):
    """A view for practicing division.
    """

    def __init__(self, window, main_service, show_exercises):
        super().__init__(window, main_service, show_exercises,
                         main_service.arithmetic.get_division_question)
        user = main_service.show_current_user()
        use_timer = user.settings.get_setting(Settings.DIVIDE_TIMER)
        time_limit = user.settings.get_setting(Settings.DIVIDE_TIMELIMIT)
        self._init_frame("Division", use_timer, time_limit)


class MultiplicationView(BaseExerciseView):
    """A view for practicing multiplication.
    """

    def __init__(self, window, main_service, show_exercises):
        super().__init__(window, main_service, show_exercises,
                         main_service.arithmetic.get_multiplication_question)
        user = main_service.show_current_user()
        use_timer = user.settings.get_setting(Settings.MULTIPLY_TIMER)
        time_limit = user.settings.get_setting(Settings.MULTIPLY_TIMELIMIT)
        self._init_frame("Multiplication", use_timer, time_limit)


class SubstractionView(BaseExerciseView):
    """A view for practicing substraction.
    """

    def __init__(self, window, main_service, show_exercises):
        super().__init__(window, main_service, show_exercises,
                         main_service.arithmetic.get_substraction_question)
        user = main_service.show_current_user()
        use_timer = user.settings.get_setting(Settings.SUB_TIMER)
        time_limit = user.settings.get_setting(Settings.SUB_TIMELIMIT)
        self._init_frame("Substraction", use_timer, time_limit)


class RandomView(BaseExerciseView):
    """A view for practicing random exercises.
    """

    def __init__(self, window, main_service, show_exercises):
        super().__init__(window, main_service, show_exercises,
                         main_service.arithmetic.get_random_question)
        user = main_service.show_current_user()
        use_timer = user.settings.get_setting(Settings.RANDOM_TIMER)
        time_limit = user.settings.get_setting(Settings.RANDOM_TIMELIMIT)
        self._init_frame("Random Exercises", use_timer, time_limit)
