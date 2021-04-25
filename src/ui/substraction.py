from ui.base_exercise import BaseExerciseView
from entities.settings import Settings


class SubstractionView(BaseExerciseView):
    def __init__(self, window, main_service, show_exercises):
        super().__init__(window, main_service, show_exercises,
                         main_service.arithmetic.get_substraction_question)
        user = main_service.show_current_user()
        use_timer = user.settings.get_setting(Settings.SUB_TIMER)
        time_limit = user.settings.get_setting(Settings.SUB_TIMELIMIT)
        self._init_frame("Substraction", use_timer, time_limit)
