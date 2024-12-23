import unittest
import time
from lab7.utils.utils import time_memory_tracking1
from lab7.task6.src.ex6 import process_lis


class TestProcessLIS(unittest.TestCase):
    TIME_LIMIT_SECONDS = 2
    MEMORY_LIMIT_MB = 256

    def test_should_process_lis_case1(self):
        """Базовый случай"""
        # given
        n = 6
        sequence = [3, 29, 5, 5, 28, 6]
        expected_length = 3
        expected_lis = [3, 5, 28]

        # when
        start_time = time.perf_counter()
        lis_length, lis = process_lis(n, sequence)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(lis_length, expected_length)
        self.assertEqual(lis, expected_lis)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_process_lis_case2(self):
        """Упорядоченная последовательность"""
        # given
        n = 5
        sequence = [1, 2, 3, 4, 5]
        expected_length = 5
        expected_lis = [1, 2, 3, 4, 5]

        # when
        start_time = time.perf_counter()
        lis_length, lis = process_lis(n, sequence)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(lis_length, expected_length)
        self.assertEqual(lis, expected_lis)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_process_lis_case3(self):
        """Обратная последовательность"""
        # given
        n = 5
        sequence = [5, 4, 3, 2, 1]
        expected_length = 1
        expected_lis = [5]

        # when
        start_time = time.perf_counter()
        lis_length, lis = process_lis(n, sequence)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(lis_length, expected_length)
        self.assertIn(lis[0], sequence)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == "__main__":
    unittest.main()
