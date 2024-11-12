import unittest
from random import randint
from ..src.ex1 import quick_sort_upgrade


class TestQuickSort(unittest.TestCase):

    def test_quick_sort1(self):
        """Большой массив одинаковых чисел, кроме одного"""
        arr = [2] + [1] * 10 ** 5
        self.assertEqual(quick_sort_upgrade(arr), sorted(arr))

    def test_quick_sort2(self):
        """Большой массив рандомных чисел"""
        arr = [randint(0, 10 ** 9) for i in range(10 ** 5)]
        self.assertEqual(quick_sort_upgrade(arr), sorted(arr))

    def test_quick_sort3(self):
        """Массив из одного элемента"""
        arr = [1]
        self.assertEqual(quick_sort_upgrade(arr), [1])


    def test_quick_sort4(self):
        """Пустой массив"""
        arr = []
        self.assertEqual(quick_sort_upgrade(arr), [])


if __name__ == '__main__':
    unittest.main()
