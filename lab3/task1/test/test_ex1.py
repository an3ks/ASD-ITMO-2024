import unittest
from random import randint
from lab3.task1.src.ex1 import quick_sort_upgrade


class TestQuickSort(unittest.TestCase):

    def test_should_quick_sort1(self):
        """Большой массив одинаковых чисел, кроме одного"""
        # given
        arr = [2] + [1] * 10 ** 5
        # then
        self.assertEqual(quick_sort_upgrade(arr), sorted(arr))

    def test_should_quick_sort2(self):
        """Большой массив рандомных чисел"""
        # given
        arr = [randint(0, 10 ** 9) for i in range(10 ** 5)]
        # then
        self.assertEqual(quick_sort_upgrade(arr), sorted(arr))

    def test_should_quick_sort3(self):
        """Массив из одного элемента"""
        # given
        arr = [1]
        self.assertEqual(quick_sort_upgrade(arr), [1])


    def test_should_quick_sort4(self):
        """Пустой массив"""
        # given
        arr = []
        # then
        self.assertEqual(quick_sort_upgrade(arr), [])


if __name__ == '__main__':
    unittest.main()
