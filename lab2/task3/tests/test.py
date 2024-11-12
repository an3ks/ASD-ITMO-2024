import unittest
from lab2.task3.src.third import merge_sort


class TestInversionCount(unittest.TestCase):
    def test_should_merge_sort_small_array(self):
        """Тест с обычным массивом"""
        # given
        arr = [3, 1, 4, 1, 5]
        expected_inversions = 3
        # when
        inversions = merge_sort(arr.copy())
        # then
        self.assertEqual(inversions, expected_inversions)

    def test_should_merge_sort_already_sorted(self):
        """Отсортированный массив"""
        # given
        arr = [1, 2, 3, 4, 5]
        # when
        inversions = merge_sort(arr.copy())
        # then
        self.assertEqual(inversions, 0)

    def test_should_merge_sort_reverse_sorted(self):
        """Массив в обратном порядке"""
        # given
        arr = [5, 4, 3, 2, 1]
        expected_inversions = 10
        # when
        inversions = merge_sort(arr.copy())
        # then
        self.assertEqual(inversions, expected_inversions)

    def test_should_merge_sort_large_random_array(self):
        """Случайный большой массив"""
        # given
        import random
        arr = random.sample(range(-10 ** 5, 10 ** 5), 10 ** 3)
        # when
        expected_inversions = sum(1 for i in range(len(arr)) for j in range(i + 1, len(arr)) if arr[i] > arr[j])
        inversions = merge_sort(arr.copy())
        # then
        self.assertEqual(inversions, expected_inversions)

    def test_should_merge_sort_single_element(self):
        """Массив, длинной 1"""
        # given
        arr = [42]
        # when
        inversions = merge_sort(arr.copy())
        # then
        self.assertEqual(inversions, 0)

    def test_should_merge_sort_empty_array(self):
        """Пустой массив"""
        # given
        arr = []
        # when
        inversions = merge_sort(arr.copy())
        # then
        self.assertEqual(inversions, 0)


if __name__ == '__main__':
    unittest.main()
