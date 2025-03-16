import unittest
from random import randint
import time
from FirstSemester.lab3.task1.src.ex1 import quick_sort_upgrade
from lab3.utils.utils import time_memory_tracking1


class TestQuickSort(unittest.TestCase):
    TIME_LIMIT_SECONDS = 2
    MEMORY_LIMIT_MB = 256
    def test_should_quick_sort1(self):
        """Большой массив одинаковых чисел, кроме одного"""
        # given
        start_time = time.perf_counter()
        arr = [2] + [1] * 10 ** 5
        # when
        result = quick_sort_upgrade(arr)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEqual(result, sorted(arr))
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


    def test_should_quick_sort2(self):
        """Большой массив рандомных чисел"""
        # given
        start_time = time.perf_counter()
        arr = [randint(0, 10 ** 9) for i in range(10 ** 5)]
        # when
        result = quick_sort_upgrade(arr)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEqual(result, sorted(arr))
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


    def test_should_quick_sort3(self):
        """Массив из одного элемента"""
        # given
        start_time = time.perf_counter()
        arr = [1]
        # when
        result = quick_sort_upgrade(arr)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEqual(result, [1])
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


    def test_should_quick_sort4(self):
        """Пустой массив"""
        # given
        start_time = time.perf_counter()
        arr = []
        # when
        result = quick_sort_upgrade(arr)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEqual(result, [])
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == '__main__':
    unittest.main()
