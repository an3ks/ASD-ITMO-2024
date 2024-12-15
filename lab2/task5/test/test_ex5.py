import unittest
import time
from lab2.task5.src.ex5 import majority_element
from lab2.utils.utils import time_memory_tracking1


class TestMajorityElement(unittest.TestCase):
    TIME_LIMIT_SECONDS = 2
    MEMORY_LIMIT_MB = 256
    def test_should_majority_element1(self):
        """Обычный тест"""
        # given
        start_time = time.perf_counter()
        arr = [1, 2, 3, 3, 3, 3, 3]
        # when
        result = majority_element(arr, 0, len(arr) - 1)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEqual(result, 3)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_majority_element2(self):
        """Тест без представителей большинства"""
        # given
        start_time = time.perf_counter()
        arr = [1, 2, 3, 4, 5, 6, 7]
        # when
        result = majority_element(arr, 0, len(arr) - 1)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEqual(result, 0)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_majority_element3(self):
        """Тест с массивом из 1-го элемента"""
        # given
        start_time = time.perf_counter()
        arr = [10]
        # when
        result = majority_element(arr, 0, len(arr) - 1)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEqual(result, 10)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_majority_element4(self):
        """Массив с одинаковыми элементами"""
        # given
        start_time = time.perf_counter()
        arr = [5, 5, 5, 5, 5]
        # when
        result = majority_element(arr, 0, len(arr) - 1)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEqual(result, 5)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_majority_element5(self):
        """Большой массив"""
        # given
        start_time = time.perf_counter()
        arr = [4] * 100000 + [1, 2, 3, 5, 6]
        # when
        result = majority_element(arr, 0, len(arr) - 1)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEqual(result, 4)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == '__main__':
    unittest.main()
