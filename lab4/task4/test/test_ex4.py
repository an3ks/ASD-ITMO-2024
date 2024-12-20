import unittest
import time
from lab4.utils.utils import time_memory_tracking1
from lab4.task4.src.ex4 import is_valid_brackets


class TestBracketsValidator(unittest.TestCase):
    TIME_LIMIT_SECONDS = 5
    MEMORY_LIMIT_MB = 512

    def test_should_validate1(self):
        """Базовый случай: корректная последовательность скобок"""
        # given
        data = ["{[()]}"]
        expected_result = ["Success"]

        # when
        start_time = time.perf_counter()
        result = [is_valid_brackets(sequence) for sequence in data]
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_validate2(self):
        """Случай с ошибочной закрывающей скобкой"""
        # given
        data = ["{[()]}}"]
        expected_result = [7]

        # when
        start_time = time.perf_counter()
        result = [is_valid_brackets(sequence) for sequence in data]
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_validate3(self):
        """Случай с лишней открывающей скобкой"""
        # given
        data = ["([{}]"]
        expected_result = [1]

        # when
        start_time = time.perf_counter()
        result = [is_valid_brackets(sequence) for sequence in data]
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_validate4(self):
        """Случай с большим объемом данных"""
        # given
        data = ["{" * 100000 + "}" * 100000]
        expected_result = ["Success"]

        # when
        start_time = time.perf_counter()
        result = [is_valid_brackets(sequence) for sequence in data]
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == "__main__":
    unittest.main()
