import random as rand
from entities.multiplication_operation import MultiplicationOperation
from entities.division_operation import DivisionOperation
from entities.addition_operation import AdditionOperation
from entities.substraction_operation import SubstractionOperation
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

    def check_answer(self, operation, user_answer):
        try:
            return operation.parse_and_check_answer(user_answer)
        except ValueError:
            pass

        return False
