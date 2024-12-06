import unittest
from lab2.task3.src.ex3 import merge_sort


class TestInversionCount(unittest.TestCase):
    def test_small_array(self):
        """Тест с обычным массивом"""
        arr = [3, 1, 4, 1, 5]
        expected_inversions = 3
        inversions = merge_sort(arr.copy())
        self.assertEqual(inversions, expected_inversions)

    def test_already_sorted(self):
        """Отсортированный массив"""
        arr = [1, 2, 3, 4, 5]
        inversions = merge_sort(arr.copy())
        self.assertEqual(inversions, 0)

    def test_reverse_sorted(self):
        """Массив в обратном порядке"""
        arr = [5, 4, 3, 2, 1]
        expected_inversions = 10
        inversions = merge_sort(arr.copy())
        self.assertEqual(inversions, expected_inversions)

    def test_large_random_array(self):
        """Случайный большой массив"""
        import random
        arr = random.sample(range(-10 ** 5, 10 ** 5), 10 ** 3)
        expected_inversions = sum(1 for i in range(len(arr)) for j in range(i + 1, len(arr)) if arr[i] > arr[j])
        inversions = merge_sort(arr.copy())
        self.assertEqual(inversions, expected_inversions)

    def test_single_element(self):
        """Массив, длинной 1"""
        arr = [42]
        inversions = merge_sort(arr.copy())
        self.assertEqual(inversions, 0)

    def test_empty_array(self):
        """Пустой массив"""
        arr = []
        inversions = merge_sort(arr.copy())
        self.assertEqual(inversions, 0)


if __name__ == '__main__':
    unittest.main()
