from ui.base_exercise import BaseExerciseView


class MultiplicationView(BaseExerciseView):
    def __init__(self, window, main_service, show_exercises):
        super().__init__(window, main_service, show_exercises,
                         main_service.arithmetic.get_multiplication_question)
        self._init_frame("Multiplication")
