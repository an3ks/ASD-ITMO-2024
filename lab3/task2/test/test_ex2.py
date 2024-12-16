import unittest
import time
from lab3.task2.src.ex2 import anti_quick_sort
from lab3.utils.utils import time_memory_tracking1


class TestAntiQuickSortFunction(unittest.TestCase):
    TIME_LIMIT_SECONDS = 2
    MEMORY_LIMIT_MB = 256

    def test_should_generate_anti_quick_sort4(self):
        """Тест с минимальным значением n = 1"""

        # given
        n = 1
        expected_result = [1]

        # when
        start_time = time.perf_counter()
        result = anti_quick_sort(n)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_generate_anti_quick_sort5(self):
        """Проверка на корректность для большого n"""

        # given
        n = 1000

        # when
        start_time = time.perf_counter()
        result = anti_quick_sort(n)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(len(result), n)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == "__main__":
    unittest.main()
