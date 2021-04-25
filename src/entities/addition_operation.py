from entities.binary_operation import BinaryOperation


class AdditionOperation(BinaryOperation):
    def result(self):
        return self._operand1 + self._operand2

    def __str__(self):
        return f"{self._operand1} + {self._operand2}"
