import unittest
import time
from lab3.task3.src.ex3 import pugalo_sort
from lab3.utils.utils import time_memory_tracking1


class TestPugaloSortFunction(unittest.TestCase):
    TIME_LIMIT_SECONDS = 2
    MEMORY_LIMIT_MB = 256

    def test_pugalo_sort_basic(self):
        """Базовый тест: возможно отсортировать"""

        # given
        n, k = 5, 3
        sizes = [1, 5, 3, 4, 1]
        expected_result = "ДА"

        # when
        start_time = time.perf_counter()
        result = pugalo_sort(n, k, sizes)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_pugalo_sort_single_bucket(self):
        """Тест: одна корзина"""

        # given
        n, k = 5, 1
        sizes = [5, 4, 3, 2, 1]
        expected_result = "ДА"

        # when
        start_time = time.perf_counter()
        result = pugalo_sort(n, k, sizes)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == "__main__":
    unittest.main()
