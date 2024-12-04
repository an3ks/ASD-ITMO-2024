import unittest
from lab1.taks6.src.six import bubble_sort


class TestFirst(unittest.TestCase):

    def test_bubble_sort0(self):
        arr = [234, 325, 5, 1, -6, 0]
        list_length = len(arr)
        result = bubble_sort(list_length, arr)
        self.assertEqual(result, [-6, 0, 1, 5, 234, 325])

    def test_bubble_sort1(self):
        arr = [-1, -5, 5, 5, 3, -3]
        list_length = len(arr)
        result = bubble_sort(list_length, arr)
        self.assertEqual(result, [-5, -3, -1, 3, 5, 5])
