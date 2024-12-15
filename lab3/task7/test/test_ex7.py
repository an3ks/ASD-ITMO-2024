import unittest
import time
from lab3.task7.src.ex7 import digital_sorting
from lab3.utils.utils import time_memory_tracking1
class TestDigitalSortingFunction(unittest.TestCase):
    TIME_LIMIT_SECONDS = 2
    MEMORY_LIMIT_MB = 256

    def test_should_digital_sorting1(self):
        """Базовый тест"""
        n, m, k = 3, 3, 1
        matrix = [
            "bab",
            "bba",
            "baa"
        ]
        expected_result = [2, 3, 1]

        # when
        start_time = time.perf_counter()
        result = digital_sorting(n, m, k, matrix)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_digital_sorting2(self):
        """Тест с несколькими фазами сортировки"""
        n, m, k = 3, 3, 2
        matrix = [
            "bab",
            "bba",
            "baa"
        ]
        expected_result = [3, 2, 1]

        # when
        start_time = time.perf_counter()
        result = digital_sorting(n, m, k, matrix)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_digital_sorting3(self):
        n, m, k = 5, 5, 3
        matrix = [
            "edcba",
            "zyxwv",
            "kjihg",
            "utsrq",
            "ponml"
        ]
        expected_result = [5, 4, 3, 2, 1]

        # when
        start_time = time.perf_counter()
        result = digital_sorting(n, m, k, matrix)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_digital_sorting4(self):
        """Тест на пустую матрицу"""
        n, m, k = 0, 0, 0
        matrix = []
        expected_result = []

        # when
        start_time = time.perf_counter()
        result = digital_sorting(n, m, k, matrix)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == "__main__":
    unittest.main()