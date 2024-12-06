import unittest
import time
from lab2.task4.src.ex4 import binary_search
from lab2.utils.utils import time_memory_tracking


class TestBinarySearch(unittest.TestCase):
    def test_should_binary_search1(self):
        """Простой тест"""
        # given
        start_time = time.perf_counter()
        arr = [1, 3, 5, 7, 9]
        # when
        index = binary_search(arr, 5)
        # then
        self.assertEqual(index, 2)  # Элемент 5 находится на индексе 2
        time_memory_tracking(start_time)

    def test_should_binary_search2(self):
        """Начальный элемент верный"""
        # given
        start_time = time.perf_counter()
        arr = [1, 3, 5, 7, 9]
        # when
        index = binary_search(arr, 1)
        # then
        self.assertEqual(index, 0)
        time_memory_tracking(start_time)

    def test_should_binary_search3(self):
        """Крайний элемент верный"""
        # given
        start_time = time.perf_counter()
        arr = [1, 3, 5, 7, 9]
        # when
        index = binary_search(arr, 9)
        # then
        self.assertEqual(index, 4)
        time_memory_tracking(start_time)

    def test_should_binary_search4(self):
        """Массив с 1 элементом"""
        # given
        start_time = time.perf_counter()
        arr = [10]
        # when
        index = binary_search(arr, 10)
        # then
        self.assertEqual(index, 0)
        time_memory_tracking(start_time)

    def test_should_binary_search5(self):
        """Массив с 1 элементом и без искомого элемента"""
        # given
        start_time = time.perf_counter()
        arr = [10]
        # when
        index = binary_search(arr, 5)
        # then
        self.assertEqual(index, -1)
        time_memory_tracking(start_time)

    def test_should_binary_search6(self):
        """Большой массив"""
        # given
        start_time = time.perf_counter()
        arr = list(range(1, 1000001))  # Массив от 1 до 1,000,000
        # when
        index = binary_search(arr, 500000)
        # then
        self.assertEqual(index, 499999)  # Элемент 500000 должен быть на индексе 499999
        time_memory_tracking(start_time)

    def test_should_binary_search7(self):
        """Тест с поиском отсутствующего элемента"""
        # given
        start_time = time.perf_counter()
        arr = list(range(1, 1000001))
        # when
        index = binary_search(arr, 1000001)
        # then
        self.assertEqual(index, -1)
        time_memory_tracking(start_time)


if __name__ == '__main__':
    unittest.main()
