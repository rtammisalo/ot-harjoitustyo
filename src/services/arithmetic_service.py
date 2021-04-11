import random as rand
from entities.multiplication_operation import MultiplicationOperation


class ArithmeticService:
    def __init__(self):
        self._max_digits = 1

    def _get_operand(self):
        if self._max_digits <= 0:
            return 0

        return rand.randrange(2, self._max_digits * 10)

    def get_multiplication_question(self):
        op1 = self._get_operand()
        op2 = self._get_operand()
        return MultiplicationOperation(op1, op2)

    def check_answer(self, operation, user_answer):
        try:
            answer = int(user_answer)
            if operation.result() == answer:
                return True
        except ValueError:
            pass

        return False
