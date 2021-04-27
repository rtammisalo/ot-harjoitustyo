import decimal


class BinaryOperation:
    def __init__(self, operand1, operand2):
        self._operand1 = decimal.Decimal(operand1)
        self._operand2 = decimal.Decimal(operand2)

    def result(self):
        pass

    def parse_and_check_answer(self, answer):
        try:
            answer = decimal.Decimal(answer.replace(",", "."))
            if round(self.result(), 3) == answer:
                return True
        except decimal.InvalidOperation as error:
            raise ValueError("Cannot parse answer") from error
        except decimal.DivisionByZero:
            pass

        return False
