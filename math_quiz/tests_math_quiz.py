import unittest
from math_quiz import generate_random_integer, random_operation_selector, math_operation


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        """
        Test if random numbers generated are within the specified range.
        """
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operation_selector(self):
        """
        Test the random_operation_selector function to ensure it returns a valid math operation.
        """
        valid_operations_set = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random values
            operation = random_operation_selector()
            self.assertTrue(operation in valid_operations_set)

    def test_math_operation(self):
        """
        Test the math_operation function with some test cases.
        """
        test_cases = [
                (1, 9, '+', '1 + 9', 10),(7,2,'-','7 - 2',5),(4,7,'*','4 * 7',28)
            ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = math_operation(num1, num2, operator)
                
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()