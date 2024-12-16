import unittest
import time
from lab5.utils.utils import write_output, read_input_lines, time_memory_tracking1
from lab5.task1.src.ex1 import is_heap


class TestIsHeapFunction(unittest.TestCase):
    TIME_LIMIT_SECONDS = 2
    MEMORY_LIMIT_MB = 256

    def test_should_be_heap1(self):
        """Базовый случай: массив является кучей"""
        # given
        n = 5
        data = [1, 3, 2, 5, 4]
        expected_result = "YES"

        # when
        start_time = time.perf_counter()
        result = is_heap(data, n)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_not_be_heap(self):
        """Массив не является кучей"""
        # given
        n = 5
        data = [1, 0, 1, 2, 0]
        expected_result = "NO"

        # when
        start_time = time.perf_counter()
        result = is_heap(data, n)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_empty_heap(self):
        """Пустой массив или массив с одним элементом"""
        # given
        n = 1
        data = [42]
        expected_result = "YES"

        # when
        start_time = time.perf_counter()
        result = is_heap(data, n)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_large_heap(self):
        """Большие данные для проверки производительности"""
        # given
        n = 100000
        data = [i for i in range(1, n + 1)]
        expected_result = "YES"

        # when
        start_time = time.perf_counter()
        result = is_heap(data, n)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_large_not_heap(self):
        """Большой массив, который не является кучей"""
        # given
        n = 100000
        data = [i for i in range(1, n + 1)]
        data[1] = 0
        expected_result = "NO"

        # when
        start_time = time.perf_counter()
        result = is_heap(data, n)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == "__main__":
    unittest.main()