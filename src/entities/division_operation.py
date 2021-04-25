from entities.binary_operation import BinaryOperation


class DivisionOperation(BinaryOperation):
    def result(self):
        print()
        return self._operand1 / self._operand2

    def __str__(self):
        return f"{self._operand1} / {self._operand2}"
