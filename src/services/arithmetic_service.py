import random as rand
from entities.operations import MultiplicationOperation, DivisionOperation
from entities.operations import AdditionOperation, SubstractionOperation


class ArithmeticService:
    """A small service-type class for handling arithmetic operations.

    The class is used to create new random questions based on the current user's settings
    and check for correct answers.
    """

    def _get_operand(self, min_op, max_op):
        """Returns a random integer between min_op and max_op ranges (inclusive).

        Args:
            min_op (int): Minimum operand size.
            max_op (int): Maximum operand size.

        Returns:
            int: A random integer between [min_op, max_op].
                Returns max_op, if min_op is greater than max_op.
        """
        if min_op > max_op:
            min_op = max_op

        return rand.randint(min_op, max_op)

    def get_multiplication_question(self, settings):
        """Generates a new multiplication question according to settings.

        Args:
            settings (Settings): User settings.

        Returns:
            MultiplicationOperation: A new multiplication operation.
        """
        op1 = self._get_operand(settings.get_setting(settings.MULTIPLY_OPERAND1_MIN),
                                settings.get_setting(settings.MULTIPLY_OPERAND1_MAX))
        op2 = self._get_operand(settings.get_setting(settings.MULTIPLY_OPERAND2_MIN),
                                settings.get_setting(settings.MULTIPLY_OPERAND2_MAX))
        return MultiplicationOperation(op1, op2)

    def get_division_question(self, settings):
        """Generates a new division question according to settings.

        Args:
            settings (Settings): User settings.

        Returns:
            DivisionOperation: A new division operation.
        """
        op1 = self._get_operand(settings.get_setting(settings.DIVIDE_OPERAND1_MIN),
                                settings.get_setting(settings.DIVIDE_OPERAND1_MAX))
        op2 = self._get_operand(settings.get_setting(settings.DIVIDE_OPERAND2_MIN),
                                settings.get_setting(settings.DIVIDE_OPERAND2_MAX))
        return DivisionOperation(op1, op2)

    def get_addition_question(self, settings):
        """Generates a new addition question according to settings.

        Args:
            settings (Settings): User settings.

        Returns:
            DivisionOperation: A new addition operation.
        """
        op1 = self._get_operand(settings.get_setting(settings.ADD_OPERAND1_MIN),
                                settings.get_setting(settings.ADD_OPERAND1_MAX))
        op2 = self._get_operand(settings.get_setting(settings.ADD_OPERAND2_MIN),
                                settings.get_setting(settings.ADD_OPERAND2_MAX))
        return AdditionOperation(op1, op2)

    def get_substraction_question(self, settings):
        """Generates a new substraction question according to settings.

        Args:
            settings (Settings): User settings.

        Returns:
            DivisionOperation: A new substraction operation.
        """
        op1 = self._get_operand(settings.get_setting(settings.SUB_OPERAND1_MIN),
                                settings.get_setting(settings.SUB_OPERAND1_MAX))
        op2 = self._get_operand(settings.get_setting(settings.SUB_OPERAND2_MIN),
                                settings.get_setting(settings.SUB_OPERAND2_MAX))
        return SubstractionOperation(op1, op2)

    def get_random_question(self, settings):
        """Generates a random-type question according to settings.

        Args:
            settings (Settings): User settings.

        Returns:
            A random type operation.
        """
        question_list = self._get_random_question_list(settings)
        return rand.choice(question_list)

    def _get_random_question_list(self, settings):
        """Returns a list of new questions. One question per type allowed in the settings.

        Args:
            settings (Settings): User settings.

        Returns:
            list: A list of new questions to select randomly from. If no question types allowed
                in the settings, returns a multiplication operation in the list.
        """
        questions = []

        if settings.get_setting(settings.RANDOM_USE_MULTIPLY) == 1:
            questions.append(self.get_multiplication_question(settings))

        if settings.get_setting(settings.RANDOM_USE_DIVIDE) == 1:
            questions.append(self.get_division_question(settings))

        if settings.get_setting(settings.RANDOM_USE_ADD) == 1:
            questions.append(self.get_addition_question(settings))

        if settings.get_setting(settings.RANDOM_USE_SUB) == 1:
            questions.append(self.get_substraction_question(settings))

        if len(questions) == 0:
            questions.append(self.get_multiplication_question(settings))

        return questions

    def check_answer(self, operation, user_answer):
        """Checks if the user answer is correct.

        Args:
            operation (Operation): The question being checked against.
            user_answer (str): User's answer as a string.

        Returns:
            boolean: Returns True if the answer is correct, False otherwise.
        """
        try:
            return operation.parse_and_check_answer(user_answer)
        except ValueError:
            pass

        return False
