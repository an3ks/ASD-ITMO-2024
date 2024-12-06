import unittest
import time
from lab2.task3.src.ex3 import merge_sort
from lab2.utils.utils import time_memory_tracking


class TestInversionCount(unittest.TestCase):
    def test_should_merge_sort1(self):
        """Тест с обычным массивом"""
        # given
        start_time = time.perf_counter()
        arr = [3, 1, 4, 1, 5]
        expected_inversions = 3
        # when
        inversions = merge_sort(arr.copy())
        # then
        self.assertEqual(inversions, expected_inversions)
        time_memory_tracking(start_time)

    def test_should_merge_sort2(self):
        """Отсортированный массив"""
        # given
        start_time = time.perf_counter()
        arr = [1, 2, 3, 4, 5]
        # when
        inversions = merge_sort(arr.copy())
        # then
        self.assertEqual(inversions, 0)
        time_memory_tracking(start_time)

    def test_should_merge_sort3(self):
        """Массив в обратном порядке"""
        # given
        start_time = time.perf_counter()
        arr = [5, 4, 3, 2, 1]
        expected_inversions = 10
        # when
        inversions = merge_sort(arr.copy())
        # then
        self.assertEqual(inversions, expected_inversions)
        time_memory_tracking(start_time)

    def test_should_merge_sort4(self):
        """Случайный большой массив"""
        # given
        start_time = time.perf_counter()
        import random
        arr = random.sample(range(-10 ** 5, 10 ** 5), 10 ** 3)
        expected_inversions = sum(1 for i in range(len(arr)) for j in range(i + 1, len(arr)) if arr[i] > arr[j])
        # when
        inversions = merge_sort(arr.copy())
        # then
        self.assertEqual(inversions, expected_inversions)
        time_memory_tracking(start_time)

    def test_should_merge_sort5(self):
        """Массив, длинной 1"""
        # given
        start_time = time.perf_counter()
        arr = [42]
        # when
        inversions = merge_sort(arr.copy())
        # then
        self.assertEqual(inversions, 0)
        time_memory_tracking(start_time)

    def test_should_merge_sort6(self):
        """Пустой массив"""
        # given
        start_time = time.perf_counter()
        arr = []
        # when
        inversions = merge_sort(arr.copy())
        # then
        self.assertEqual(inversions, 0)
        time_memory_tracking(start_time)


if __name__ == '__main__':
    unittest.main()
