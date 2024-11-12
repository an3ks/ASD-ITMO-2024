import unittest
from lab2.task2.src.second import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_small_array(self):
        """Тест с обычным массивом """
        # given
        arr = [3, 1, 4, 1, 5]
        index_log = []
        expected_sorted = sorted(arr)
        # when
        merge_sort(arr, index_log)
        # then
        self.assertEqual(arr, expected_sorted)
        self.assertTrue(len(index_log) > 0)

    def test_already_sorted(self):
        """Отсортированный массив"""
        # given
        arr = [1, 2, 3, 4, 5]
        index_log = []
        # when
        merge_sort(arr, index_log)
        # then
        self.assertEqual(arr, [1, 2, 3, 4, 5])
        self.assertTrue(len(index_log) > 0)

    def test_reverse_sorted(self):
        """Массив в обратном порядке"""
        # given
        arr = [5, 4, 3, 2, 1]
        index_log = []
        expected_sorted = [1, 2, 3, 4, 5]
        # when
        merge_sort(arr, index_log)
        # then
        self.assertEqual(arr, expected_sorted)
        self.assertTrue(len(index_log) > 0)

    def test_large_random_array(self):
        """Случайный большой массив"""
        # given
        import random
        arr = random.sample(range(-10 ** 9, 10 ** 9), 10 ** 5)
        index_log = []
        # when
        merge_sort(arr, index_log)
        # then
        self.assertEqual(arr, sorted(arr))
        self.assertTrue(len(index_log) > 0)

    def test_single_element(self):
        """Массив, длинной 1"""
        # given
        arr = [42]
        index_log = []
        # when
        merge_sort(arr, index_log)
        # then
        self.assertEqual(arr, [42])
        self.assertEqual(index_log, [])

    def test_empty_array(self):
        """Пустой массив"""
        # given
        arr = []
        index_log = []
        # when
        merge_sort(arr, index_log)
        # then
        self.assertEqual(arr, [])
        self.assertEqual(index_log, [])


if __name__ == '__main__':
    unittest.main()
