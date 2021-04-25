from ui.base_exercise import BaseExerciseView
from entities.settings import Settings

class MultiplicationView(BaseExerciseView):
    def __init__(self, window, main_service, show_exercises):
        super().__init__(window, main_service, show_exercises,
                         main_service.arithmetic.get_multiplication_question)
        user = main_service.show_current_user()
        use_timer = user.settings.get_setting(Settings.MULTIPLY_TIMER)
        time_limit = user.settings.get_setting(Settings.MULTIPLY_TIMELIMIT)
        self._init_frame("Multiplication", use_timer, time_limit)
