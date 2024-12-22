import unittest
import time
from lab7.utils.utils import time_memory_tracking1
from lab7.task5.src.ex5 import process_lcs_3


class TestProcessLCS3(unittest.TestCase):
    TIME_LIMIT_SECONDS = 2
    MEMORY_LIMIT_MB = 128

    def test_should_process_lcs_3_case1(self):
        """Базовый случай: последовательности пересекаются"""
        # given
        n, seq1 = 3, [1, 2, 3]
        m, seq2 = 3, [2, 1, 3]
        l, seq3 = 3, [1, 3, 5]
        expected_result = 2

        # when
        start_time = time.perf_counter()
        result = process_lcs_3(n, seq1, m, seq2, l, seq3)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_process_lcs_3_case2(self):
        """Нет общих элементов"""
        # given
        n, seq1 = 4, [1, 2, 3, 4]
        m, seq2 = 4, [5, 6, 7, 8]
        l, seq3 = 4, [9, 10, 11, 12]
        expected_result = 0

        # when
        start_time = time.perf_counter()
        result = process_lcs_3(n, seq1, m, seq2, l, seq3)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_process_lcs_3_case3(self):
        """Полное совпадение последовательностей"""
        # given
        n, seq1 = 5, [1, 2, 3, 4, 5]
        m, seq2 = 5, [1, 2, 3, 4, 5]
        l, seq3 = 5, [1, 2, 3, 4, 5]
        expected_result = 5

        # when
        start_time = time.perf_counter()
        result = process_lcs_3(n, seq1, m, seq2, l, seq3)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_process_lcs_3_case4(self):
        """Стресс-тест с большими последовательностями"""
        # given
        n = m = l = 100
        seq1 = list(range(1, 101))
        seq2 = list(range(50, 150))
        seq3 = list(range(75, 175))
        expected_result = 26

        # when
        start_time = time.perf_counter()
        result = process_lcs_3(n, seq1, m, seq2, l, seq3)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == "__main__":
    unittest.main()