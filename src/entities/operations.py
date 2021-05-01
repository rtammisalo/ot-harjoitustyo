from entities.binary_operation import BinaryOperation


class AdditionOperation(BinaryOperation):
    def result(self):
        return self._operand1 + self._operand2

    def __str__(self):
        return f"{self._operand1} + {self._operand2}"


class DivisionOperation(BinaryOperation):
    def result(self):
        return self._operand1 / self._operand2

    def __str__(self):
        return f"{self._operand1} / {self._operand2}"


class MultiplicationOperation(BinaryOperation):
    def result(self):
        return self._operand1 * self._operand2

    def __str__(self):
        return f"{self._operand1} * {self._operand2}"


class SubstractionOperation(BinaryOperation):
    def result(self):
        return self._operand1 - self._operand2

    def __str__(self):
        return f"{self._operand1} - {self._operand2}"
