import unittest
import time
from FirstSemester.lab4.utils.utils import time_memory_tracking1
from FirstSemester.lab4 import is_valid_parentheses


class TestIsValidParentheses(unittest.TestCase):
    TIME_LIMIT_SECONDS = 2
    MEMORY_LIMIT_MB = 256

    def test_should_validate1(self):
        """Базовый случай: корректная скобочная последовательность"""
        # given
        data = ["(())"]
        expected_result = ["YES"]

        # when
        start_time = time.perf_counter()
        result = [is_valid_parentheses(seq) for seq in data]
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_validate2(self):
        """Смешанная последовательность с правильным порядком"""
        # given
        data = ["([])"]
        expected_result = ["YES"]

        # when
        start_time = time.perf_counter()
        result = [is_valid_parentheses(seq) for seq in data]
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_validate3(self):
        """Некорректная последовательность"""
        # given
        data = ["([)]"]
        expected_result = ["NO"]

        # when
        start_time = time.perf_counter()
        result = [is_valid_parentheses(seq) for seq in data]
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_validate4(self):
        """Случай с пустой последовательностью"""
        # given
        data = [""]
        expected_result = ["YES"]

        # when
        start_time = time.perf_counter()
        result = [is_valid_parentheses(seq) for seq in data]
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_validate5(self):
        """Случай с большими данными для проверки производительности"""
        # given
        data = ["(" * 50000 + ")" * 50000]
        expected_result = ["YES"]

        # when
        start_time = time.perf_counter()
        result = [is_valid_parentheses(seq) for seq in data]
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_validate6(self):
        """Случай с незакрытыми скобками"""
        # given
        data = ["(()"]
        expected_result = ["NO"]

        # when
        start_time = time.perf_counter()
        result = [is_valid_parentheses(seq) for seq in data]
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == "__main__":
    unittest.main()