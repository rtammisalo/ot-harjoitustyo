import decimal


class BinaryOperation:
    """A base binary operation class inherited by the actual operation classes.
    """
    def __init__(self, operand1, operand2):
        """Sets the operands.
        """
        self._operand1 = decimal.Decimal(operand1)
        self._operand2 = decimal.Decimal(operand2)

    def result(self):
        pass

    def parse_and_check_answer(self, answer):
        """Parses and checks the given answer.

        Args:
            answer (str): Answer string given by the user.

        Raises:
            ValueError: Answer is not in a correct format.

        Returns:
            boolean: True if the answer is correct. False otherwise.
        """
        try:
            answer = decimal.Decimal(answer.replace(",", "."))
            if round(self.result(), 3) == answer:
                return True
        except decimal.InvalidOperation as error:
            raise ValueError("Cannot parse answer") from error
        except decimal.DivisionByZero:
            pass

        return False
