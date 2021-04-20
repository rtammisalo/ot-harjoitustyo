import random as rand
from entities.multiplication_operation import MultiplicationOperation


class ArithmeticService:

    def _get_operand(self, min_op, max_op):
        if min_op > max_op:
            max_op = min_op

        return rand.randint(min_op, max_op)

    def get_multiplication_question(self, settings):
        op1 = self._get_operand(settings.get_setting(settings.MULTIPLY_OPERAND1_MIN),
                                settings.get_setting(settings.MULTIPLY_OPERAND1_MAX))
        op2 = self._get_operand(settings.get_setting(settings.MULTIPLY_OPERAND2_MIN),
                                settings.get_setting(settings.MULTIPLY_OPERAND2_MAX))
        return MultiplicationOperation(op1, op2)

    def check_answer(self, operation, user_answer):
        try:
            answer = int(user_answer)
            if operation.result() == answer:
                return True
        except ValueError:
            pass

        return False
