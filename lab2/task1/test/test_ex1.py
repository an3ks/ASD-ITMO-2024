import unittest
import time
from lab2.task1.src.ex1 import merge_sort
from lab2.utils.utils import time_memory_tracking1


class TestMergeSort(unittest.TestCase):
    TIME_LIMIT_SECONDS = 2
    MEMORY_LIMIT_MB = 256

    def test_sorted_array(self):
        """Отсортированный массив"""
        #given
        start_time = time.perf_counter()
        arr = [1, 2, 3, 4, 5]

        # when
        merge_sort(arr)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(arr, [1, 2, 3, 4, 5])
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS,
                             f"Время выполнения {elapsed_time:.2f} с превышает лимит {self.TIME_LIMIT_SECONDS} с")
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB,
                             f"Память {memory_usage:.2f} MB превышает лимит {self.MEMORY_LIMIT_MB} MB")

    def test_reverse_sorted_array(self):
        """Массив в обратном порядке"""
        # given
        start_time = time.perf_counter()
        arr = [5, 4, 3, 2, 1]

        # when
        merge_sort(arr)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(arr, [1, 2, 3, 4, 5])
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS)
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB)

    def test_random_array(self):
        """Случайный массив"""
        # given
        start_time = time.perf_counter()
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

        # when
        expected = sorted(arr)
        merge_sort(arr)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(arr, expected)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS)
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB)

    def test_large_random_array(self):
        """Случайный большой массив"""
        # given
        import random
        start_time = time.perf_counter()
        arr = random.sample(range(-10 ** 9, 10 ** 9), 10 ** 5)

        # when
        expected = sorted(arr)
        merge_sort(arr)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(arr, expected)
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS)
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB)

    def test_single_element_array(self):
        """Массив из одного элемента"""
        # given
        start_time = time.perf_counter()
        arr = [42]

        # when
        merge_sort(arr)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(arr, [42])
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS)
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB)

    def test_empty_array(self):
        """Пустой массив"""
        # given
        start_time = time.perf_counter()
        arr = []

        # when
        merge_sort(arr)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(arr, [])
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS)
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB)

    def test_duplicate_elements_array(self):
        """Массив с повторяющимися элементами"""
        # given
        start_time = time.perf_counter()
        arr = [2, 2, 2, 2, 2]

        #when
        merge_sort(arr)
        elapsed_time, memory_usage = time_memory_tracking1(start_time)

        # then
        self.assertEqual(arr, [2, 2, 2, 2, 2])
        self.assertLessEqual(elapsed_time, self.TIME_LIMIT_SECONDS)
        self.assertLessEqual(memory_usage, self.MEMORY_LIMIT_MB)


if __name__ == '__main__':
    unittest.main()