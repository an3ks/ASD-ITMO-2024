import unittest
import time
from lab7.utils.utils import time_memory_tracking1
from lab7.task4.src.ex4 import process_lcs


class TestLCS(unittest.TestCase):
    TIME_LIMIT_SECONDS = 2
    MEMORY_LIMIT_MB = 256

    def test_should_find_lcs1(self):
        """Базовый случай: пересекающиеся последовательности"""
        # given
        n, seq1 = 3, [2, 7, 5]
        m, seq2 = 2, [2, 5]
        expected_result = 2

        # when
        start_time = time.perf_counter()
        result = process_lcs(n, seq1, m, seq2)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_find_lcs2(self):
        """Нет пересекающихся элементов"""
        # given
        n, seq1 = 4, [1, 2, 3, 4]
        m, seq2 = 3, [5, 6, 7]
        expected_result = 0

        # when
        start_time = time.perf_counter()
        result = process_lcs(n, seq1, m, seq2)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_find_lcs3(self):
        """Полное совпадение последовательностей"""
        # given
        n, seq1 = 5, [1, 2, 3, 4, 5]
        m, seq2 = 5, [1, 2, 3, 4, 5]
        expected_result = 5

        # when
        start_time = time.perf_counter()
        result = process_lcs(n, seq1, m, seq2)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_find_lcs4(self):
        """Стресс-тест с длинными последовательностями"""
        # given
        n = m = 100
        seq1 = list(range(1, 101))
        seq2 = list(range(50, 150))
        expected_result = 51

        # when
        start_time = time.perf_counter()
        result = process_lcs(n, seq1, m, seq2)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_find_lcs5(self):
        """Одна из последовательностей пустая"""
        # given
        n, seq1 = 0, []
        m, seq2 = 5, [1, 2, 3, 4, 5]
        expected_result = 0

        # when
        start_time = time.perf_counter()
        result = process_lcs(n, seq1, m, seq2)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == "__main__":
    unittest.main()