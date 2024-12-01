import unittest
import time
from lab4.utils.utils import time_memory_tracking
from lab4.task3.src.ex3 import is_valid_parentheses


class TestIsValidParentheses(unittest.TestCase):

    def test_should_validate1(self):
        """Базовый случай: корректная скобочная последовательность"""
        # given
        data = ["(())"]
        expected_result = ["YES"]

        # when
        result = [is_valid_parentheses(seq) for seq in data]

        # then
        self.assertEqual(result, expected_result)

    def test_should_validate2(self):
        """Смешанная последовательность с правильным порядком"""
        # given
        data = ["([])"]
        expected_result = ["YES"]

        # when
        result = [is_valid_parentheses(seq) for seq in data]

        # then
        self.assertEqual(result, expected_result)

    def test_should_validate3(self):
        """Некорректная последовательность"""
        # given
        data = ["([)]"]
        expected_result = ["NO"]

        # when
        result = [is_valid_parentheses(seq) for seq in data]

        # then
        self.assertEqual(result, expected_result)

    def test_should_validate4(self):
        """Случай с пустой последовательностью"""
        # given
        data = [""]
        expected_result = ["YES"]

        # when
        result = [is_valid_parentheses(seq) for seq in data]

        # then
        self.assertEqual(result, expected_result)

    def test_should_validate5(self):
        """Случай с большими данными для проверки производительности"""
        # given
        data = ["(" * 50000 + ")" * 50000]
        expected_result = ["YES"]
        start_time = time.perf_counter()

        # when
        result = [is_valid_parentheses(seq) for seq in data]

        # then
        self.assertEqual(result, expected_result)
        time_memory_tracking(start_time)

    def test_should_validate6(self):
        """Случай с незакрытыми скобками"""
        # given
        data = ["(()"]
        expected_result = ["NO"]

        # when
        result = [is_valid_parentheses(seq) for seq in data]

        # then
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()