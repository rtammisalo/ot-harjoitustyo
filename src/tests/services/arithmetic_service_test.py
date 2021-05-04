import unittest
from services.arithmetic_service import ArithmeticService
from entities.settings import Settings
from entities.operations import DivisionOperation, MultiplicationOperation


class TestArithmeticService(unittest.TestCase):

    def setUp(self):
        self._arithmetic = ArithmeticService()
        self._settings = Settings()

    def test_operations_with_greater_operand_minimum_defaults_to_max(self):
        settings = Settings()
        settings.set_setting(settings.MULTIPLY_OPERAND1_MIN, 100)
        settings.set_setting(settings.MULTIPLY_OPERAND1_MAX, 9)
        settings.set_setting(settings.MULTIPLY_OPERAND2_MIN, 9)
        settings.set_setting(settings.MULTIPLY_OPERAND2_MAX, 9)
        self.assertEqual(100, settings.get_setting(
            settings.MULTIPLY_OPERAND1_MIN))
        self.assertEqual(9, settings.get_setting(
            settings.MULTIPLY_OPERAND1_MAX))

        operation = self._arithmetic.get_multiplication_question(settings)
        self.assertEqual("9 * 9", operation.__str__())

    def test_division_by_zero_does_not_crash(self):
        bad_division = DivisionOperation(1, 0)
        try:
            self._arithmetic.check_answer(bad_division, "0")
        except:
            self.assertFalse(True)

    def test_checking_correct_answer_for_division_returns_true(self):
        operation = self._arithmetic.get_division_question(self._settings)
        self._check_correct_answer(operation)

    def test_checking_correct_answer_for_multiplication_returns_true(self):
        operation = self._arithmetic.get_multiplication_question(
            self._settings)
        self._check_correct_answer(operation)

    def test_checking_correct_answer_for_addition_returns_true(self):
        operation = self._arithmetic.get_addition_question(
            self._settings)
        self._check_correct_answer(operation)

    def test_checking_correct_answer_for_substraction_returns_true(self):
        operation = self._arithmetic.get_substraction_question(
            self._settings)
        self._check_correct_answer(operation)

    def _check_correct_answer(self, operation):
        answer = str(round(operation.result(), 3))
        self.assertTrue(self._arithmetic.check_answer(
            operation, answer))

    def test_checking_false_answer_for_division_returns_false(self):
        operation = self._arithmetic.get_division_question(self._settings)
        self.assertFalse(self._arithmetic.check_answer(
            operation, str(operation.result()+1)))

    def test_checking_false_answer_for_multiplication_returns_false(self):
        operation = self._arithmetic.get_multiplication_question(
            self._settings)
        self.assertFalse(self._arithmetic.check_answer(
            operation, str(operation.result()+1)))

    def test_checking_false_answer_for_addition_returns_false(self):
        operation = self._arithmetic.get_addition_question(self._settings)
        self.assertFalse(self._arithmetic.check_answer(
            operation, str(operation.result()+1)))

    def test_checking_false_answer_for_substraction_returns_false(self):
        operation = self._arithmetic.get_substraction_question(self._settings)
        self.assertFalse(self._arithmetic.check_answer(
            operation, str(operation.result()+1)))

    def test_checking_bad_input_returns_false(self):
        operation = self._arithmetic.get_substraction_question(self._settings)
        self.assertFalse(self._arithmetic.check_answer(operation, "abc"))

    def test_generated_random_question_is_within_setting_parameters(self):
        settings = Settings()
        settings.set_settings_from_dict({settings.RANDOM_USE_ADD: 1,
                                         settings.RANDOM_USE_DIVIDE: 0,
                                         settings.RANDOM_USE_MULTIPLY: 0,
                                         settings.RANDOM_USE_SUB: 0})
        operation = self._arithmetic.get_random_question(settings)
        parts = operation.__str__().split(" + ")
        op1_min = settings.get_setting(settings.ADD_OPERAND1_MIN)
        op1_max = settings.get_setting(settings.ADD_OPERAND1_MAX)
        op2_min = settings.get_setting(settings.ADD_OPERAND2_MIN)
        op2_max = settings.get_setting(settings.ADD_OPERAND2_MAX)
        self.assertTrue(op1_min <= int(parts[0]) <= op1_max)
        self.assertTrue(op2_min <= int(parts[1]) <= op2_max)

    def test_generated_random_question_is_multiplication_when_none_selected(self):
        settings = Settings()
        settings.set_settings_from_dict({settings.RANDOM_USE_ADD: 0,
                                         settings.RANDOM_USE_DIVIDE: 0,
                                         settings.RANDOM_USE_MULTIPLY: 0,
                                         settings.RANDOM_USE_SUB: 0})
        operation = self._arithmetic.get_random_question(settings)
        self.assertTrue(isinstance(operation, MultiplicationOperation))
