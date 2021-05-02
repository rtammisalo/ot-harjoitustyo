import random as rand
from entities.operations import MultiplicationOperation, DivisionOperation
from entities.operations import AdditionOperation, SubstractionOperation


class ArithmeticService:
    def _get_operand(self, min_op, max_op):
        if min_op > max_op:
            min_op = max_op

        return rand.randint(min_op, max_op)

    def get_multiplication_question(self, settings):
        op1 = self._get_operand(settings.get_setting(settings.MULTIPLY_OPERAND1_MIN),
                                settings.get_setting(settings.MULTIPLY_OPERAND1_MAX))
        op2 = self._get_operand(settings.get_setting(settings.MULTIPLY_OPERAND2_MIN),
                                settings.get_setting(settings.MULTIPLY_OPERAND2_MAX))
        return MultiplicationOperation(op1, op2)

    def get_division_question(self, settings):
        op1 = self._get_operand(settings.get_setting(settings.DIVIDE_OPERAND1_MIN),
                                settings.get_setting(settings.DIVIDE_OPERAND1_MAX))
        op2 = self._get_operand(settings.get_setting(settings.DIVIDE_OPERAND2_MIN),
                                settings.get_setting(settings.DIVIDE_OPERAND2_MAX))
        return DivisionOperation(op1, op2)

    def get_addition_question(self, settings):
        op1 = self._get_operand(settings.get_setting(settings.ADD_OPERAND1_MIN),
                                settings.get_setting(settings.ADD_OPERAND1_MAX))
        op2 = self._get_operand(settings.get_setting(settings.ADD_OPERAND2_MIN),
                                settings.get_setting(settings.ADD_OPERAND2_MAX))
        return AdditionOperation(op1, op2)

    def get_substraction_question(self, settings):
        op1 = self._get_operand(settings.get_setting(settings.SUB_OPERAND1_MIN),
                                settings.get_setting(settings.SUB_OPERAND1_MAX))
        op2 = self._get_operand(settings.get_setting(settings.SUB_OPERAND2_MIN),
                                settings.get_setting(settings.SUB_OPERAND2_MAX))
        return SubstractionOperation(op1, op2)

    def get_random_question(self, settings):
        question_list = self._get_random_question_list(settings)
        return rand.choice(question_list)

    def _get_random_question_list(self, settings):
        questions = []

        if settings.get_setting(settings.RANDOM_USE_MULTIPLY) == 1:
            questions.append(self.get_multiplication_question(settings))

        if settings.get_setting(settings.RANDOM_USE_DIVIDE) == 1:
            questions.append(self.get_division_question(settings))

        if settings.get_setting(settings.RANDOM_USE_ADD) == 1:
            questions.append(self.get_addition_question(settings))

        if settings.get_setting(settings.RANDOM_USE_SUB) == 1:
            questions.append(self.get_substraction_question(settings))

        if len(questions) == 0:
            questions.append(self.get_multiplication_question(settings))

        return questions

    def check_answer(self, operation, user_answer):
        try:
            return operation.parse_and_check_answer(user_answer)
        except ValueError:
            pass

        return False
