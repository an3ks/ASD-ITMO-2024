import unittest
from lab1.task4.src.four import linear_search


class TestFirst(unittest.TestCase):

    def test_linear_search0(self):
        arr = [234, 325, 5, 1, -6, 0]
        v = 5
        result = linear_search(v, arr)
        self.assertEqual(result, 2)

    def test_linear_search1(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        v = 7
        result = linear_search(v, arr)
        self.assertEqual(result, 6)

    def test_linear_search(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 7, 7, 10, 11, 12, 13, 14, 15, 16]
        v = 7
        result = linear_search(v, arr)
        self.assertEqual(result, ([6, 7, 8], 3))
