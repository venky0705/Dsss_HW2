import unittest
from math_quiz import returnRandom, operation_choice, result


class TestMathGame(unittest.TestCase):

    def test_returnRandom(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = returnRandom(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_operation_choice(self):
        # Test if operation_choice returns one of the valid operators
        self.assertTrue(operation_choice() == '+' or operation_choice() == '-' or operation_choice() == '*')

    def test_result(self):
        # Test all the three operators
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (1, 2, '-', '1 - 2', -1),
            (5, 5, '*', '5 * 5', 25),
        ]
        # looping over the input test cases for all three operators
        for number1, number2, operator, expected_problem, expected_answer in test_cases:
            if operator == '+':
                (self.assertEquals(result(number1, number2, operator)[1], number1 + number2) and self.assertEquals(
                    result(number1, number2, operator)[0], expected_answer))
            elif operator == '-':
                (self.assertEquals(result(number1, number2, operator)[1], number1 - number2) and self.assertEquals(
                    result(number1, number2, operator)[0], expected_answer))
            else:
                (self.assertEquals(result(number1, number2, operator)[1], number1 * number2) and self.assertEquals(
                    result(number1, number2, operator)[0], expected_answer))


if __name__ == "__main__":
    unittest.main()