import unittest
import time
from lab2.task2.src.ex2 import merge_sort
from lab2.utils.utils import time_memory_tracking


class TestMergeSort(unittest.TestCase):
    def test_should_merge_sort1(self):
        """Тест с обычным массивом """
        # given
        start_time = time.perf_counter()
        arr = [3, 1, 4, 1, 5]
        index_log = []
        expected_sorted = sorted(arr)
        # when
        merge_sort(arr, index_log)
        # then
        self.assertEqual(arr, expected_sorted)
        self.assertTrue(len(index_log) > 0)
        time_memory_tracking(start_time)

    def test_should_merge_sort2(self):
        """Отсортированный массив"""
        # given
        start_time = time.perf_counter()
        arr = [1, 2, 3, 4, 5]
        index_log = []
        # when
        merge_sort(arr, index_log)
        # then
        self.assertEqual(arr, [1, 2, 3, 4, 5])
        self.assertTrue(len(index_log) > 0)
        time_memory_tracking(start_time)

    def test_should_merge_sort3(self):
        """Массив в обратном порядке"""
        # given
        start_time = time.perf_counter()
        arr = [5, 4, 3, 2, 1]
        index_log = []
        expected_sorted = [1, 2, 3, 4, 5]
        # when
        merge_sort(arr, index_log)
        # then
        self.assertEqual(arr, expected_sorted)
        self.assertTrue(len(index_log) > 0)
        time_memory_tracking(start_time)

    def test_should_merge_sort4(self):
        """Случайный большой массив"""
        # given
        start_time = time.perf_counter()
        import random
        arr = random.sample(range(-10 ** 9, 10 ** 9), 10 ** 5)
        index_log = []
        # when
        merge_sort(arr, index_log)
        # then
        self.assertEqual(arr, sorted(arr))
        self.assertTrue(len(index_log) > 0)
        time_memory_tracking(start_time)

    def test_should_merge_sort5(self):
        """Массив, длинной 1"""
        # given
        start_time = time.perf_counter()
        arr = [42]
        index_log = []
        # when
        merge_sort(arr, index_log)
        # then
        self.assertEqual(arr, [42])
        self.assertEqual(index_log, [])
        time_memory_tracking(start_time)

    def test_should_merge_sort6(self):
        """Пустой массив"""
        # given
        start_time = time.perf_counter()
        arr = []
        index_log = []
        # when
        merge_sort(arr, index_log)
        # then
        self.assertEqual(arr, [])
        self.assertEqual(index_log, [])
        time_memory_tracking(start_time)


if __name__ == '__main__':
    unittest.main()
