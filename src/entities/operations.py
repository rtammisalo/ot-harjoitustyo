from entities.binary_operation import BinaryOperation


class AdditionOperation(BinaryOperation):
    """Addition operation, a + b. Can be printed.
    """
    def result(self):
        """Returns the result of the addition as a Decimal.
        """
        return self._operand1 + self._operand2

    def __str__(self):
        return f"{self._operand1} + {self._operand2}"


class DivisionOperation(BinaryOperation):
    """Division operation, a / b. Can be printed.
    """
    def result(self):
        """Returns the result of the division as a Decimal.
        """
        return self._operand1 / self._operand2

    def __str__(self):
        return f"{self._operand1} / {self._operand2}"


class MultiplicationOperation(BinaryOperation):
    """Multiplication operation, a * b. Can be printed.
    """
    def result(self):
        """Returns the result of the multiplication as a Decimal.
        """
        return self._operand1 * self._operand2

    def __str__(self):
        return f"{self._operand1} * {self._operand2}"


class SubstractionOperation(BinaryOperation):
    """Substraction operation, a - b. Can be printed.
    """
    def result(self):
        """Return the result of the substraction as a Decimal.
        """
        return self._operand1 - self._operand2

    def __str__(self):
        return f"{self._operand1} - {self._operand2}"
