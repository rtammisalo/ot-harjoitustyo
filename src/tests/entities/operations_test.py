import unittest
from entities.operations import AdditionOperation, SubstractionOperation, \
    MultiplicationOperation, DivisionOperation


class TestAdditionOperation(unittest.TestCase):
    def setUp(self):
        self._default_addition = AdditionOperation(1, 2)

    def test_addition_result_correct(self):
        self.assertEqual(self._default_addition.result(), 3)

    def test_addition_as_string_correct(self):
        self.assertEqual(str(self._default_addition), "1 + 2")

    def test_correct_answer_parse_returns_true(self):
        self.assertTrue(self._default_addition.parse_and_check_answer("3"))

    def test_incorrect_answer_parse_returns_false(self):
        self.assertFalse(self._default_addition.parse_and_check_answer("2"))

    def test_non_integer_answer_parse_raises_exception(self):
        with self.assertRaises(ValueError):
            self._default_addition.parse_and_check_answer("abc")


class TestSubstractionOperation(unittest.TestCase):
    def setUp(self):
        self._default_substraction = SubstractionOperation(3, 2)
        self._negative_substraction = SubstractionOperation(2, 3)

    def test_substraction_result_correct(self):
        self.assertEqual(self._default_substraction.result(), 1)

    def test_negative_substraction_result_correct(self):
        self.assertEqual(self._negative_substraction.result(), -1)

    def test_substraction_as_string_correct(self):
        self.assertEqual(str(self._default_substraction), "3 - 2")

    def test_correct_answer_to_negative_result_returns_true(self):
        self.assertTrue(
            self._negative_substraction.parse_and_check_answer("-1"))


class TestMultiplicationOperation(unittest.TestCase):
    def setUp(self):
        self._default_multiplication = MultiplicationOperation(3, 2)

    def test_multiplication_result_correct(self):
        self.assertEqual(self._default_multiplication.result(), 6)

    def test_multiplication_as_string_correct(self):
        self.assertEqual(str(self._default_multiplication), "3 * 2")


class TestDivisionOperation(unittest.TestCase):
    def setUp(self):
        self._default_division = DivisionOperation(1, 2)

    def test_division_result_correct(self):
        self.assertEqual(self._default_division.result(), 0.5)

    def test_division_as_string_correct(self):
        self.assertEqual(str(self._default_division), "1 / 2")

    def test_parse_accepts_rounding_to_3_decimals(self):
        division = DivisionOperation(2, 3)
        self.assertTrue(division.parse_and_check_answer("0.667"))
