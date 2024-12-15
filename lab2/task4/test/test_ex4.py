import unittest
import time
from lab2.task4.src.ex4 import binary_search
from lab2.utils.utils import time_memory_tracking1


class TestBinarySearch(unittest.TestCase):
    TIME_LIMIT_SECONDS = 2
    MEMORY_LIMIT_MB = 256
    def test_should_binary_search1(self):
        """Простой тест"""
        # given
        start_time = time.perf_counter()
        arr = [1, 3, 5, 7, 9]
        # when
        index = binary_search(arr, 5)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEqual(index, 2)  # Элемент 5 находится на индексе 2
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_binary_search2(self):
        """Начальный элемент верный"""
        # given
        start_time = time.perf_counter()
        arr = [1, 3, 5, 7, 9]
        # when
        index = binary_search(arr, 1)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEqual(index, 0)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_binary_search3(self):
        """Крайний элемент верный"""
        # given
        start_time = time.perf_counter()
        arr = [1, 3, 5, 7, 9]
        # when
        index = binary_search(arr, 9)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEqual(index, 4)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_binary_search4(self):
        """Массив с 1 элементом"""
        # given
        start_time = time.perf_counter()
        arr = [10]
        # when
        index = binary_search(arr, 10)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEqual(index, 0)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_binary_search5(self):
        """Массив с 1 элементом и без искомого элемента"""
        # given
        start_time = time.perf_counter()
        arr = [10]
        # when
        index = binary_search(arr, 5)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEqual(index, -1)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_binary_search6(self):
        """Большой массив"""
        # given
        start_time = time.perf_counter()
        arr = list(range(1, 1000001))  # Массив от 1 до 1,000,000
        # when
        index = binary_search(arr, 500000)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEqual(index, 499999)  # Элемент 500000 должен быть на индексе 499999
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_should_binary_search7(self):
        """Тест с поиском отсутствующего элемента"""
        # given
        start_time = time.perf_counter()
        arr = list(range(1, 1000001))
        # when
        index = binary_search(arr, 1000001)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)
        # then
        self.assertEqual(index, -1)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} превышает лимит {self.TIME_LIMIT_SECONDS} секунд")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Использование памяти {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")


if __name__ == '__main__':
    unittest.main()
