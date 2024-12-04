import unittest
from lab1.task3.src.third import reversed_insertion_sort


class TestTask3(unittest.TestCase):

    def test_reverse_insertion_sort0(self):
        arr = [4, 1, 24, 512, 5, 3]
        list_length = len(arr)
        result = reversed_insertion_sort(list_length, arr)
        self.assertEquals(result, [512, 24, 5, 4, 3, 1])

    def test_reverse_insertion_sort1(self):
        arr = [-5, -10, -12034, -431, -4]
        list_length = len(arr)
        result = reversed_insertion_sort(list_length, arr)
        self.assertEquals(result, [-4, -5, -10, -431, -12034])
