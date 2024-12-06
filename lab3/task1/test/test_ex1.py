import unittest
from random import randint
import time
from lab3.task1.src.ex1 import quick_sort_upgrade
from lab3.utils.utils import time_memory_tracking


class TestQuickSort(unittest.TestCase):

    def test_should_quick_sort1(self):
        """Большой массив одинаковых чисел, кроме одного"""
        # given
        start_time = time.perf_counter()
        arr = [2] + [1] * 10 ** 5
        # when
        result = quick_sort_upgrade(arr)
        # then
        self.assertEqual(result, sorted(arr))
        time_memory_tracking(start_time)

    def test_should_quick_sort2(self):
        """Большой массив рандомных чисел"""
        # given
        start_time = time.perf_counter()
        arr = [randint(0, 10 ** 9) for i in range(10 ** 5)]
        # when
        result = quick_sort_upgrade(arr)
        # then
        self.assertEqual(result, sorted(arr))
        time_memory_tracking(start_time)

    def test_should_quick_sort3(self):
        """Массив из одного элемента"""
        # given
        start_time = time.perf_counter()
        arr = [1]
        # when
        result = quick_sort_upgrade(arr)
        # then
        self.assertEqual(result, [1])
        time_memory_tracking(start_time)

    def test_should_quick_sort4(self):
        """Пустой массив"""
        # given
        start_time = time.perf_counter()
        arr = []
        # when
        result = quick_sort_upgrade(arr)
        # then
        self.assertEqual(result, [])
        time_memory_tracking(start_time)


if __name__ == '__main__':
    unittest.main()
