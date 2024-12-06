import unittest
import time
from lab1.task1.src.ex1 import insertion_sort
from lab1.utils.utils import time_memory_tracking


class TestFirst(unittest.TestCase):

    def test_should_insertion_sort0(self):
        # given
        start_time = time.perf_counter()
        arr = [234, 325, 5, 1, -6, 0]
        list_length = len(arr)
        # when
        result = insertion_sort(list_length, arr)
        # then
        self.assertEqual(result, [-6, 0, 1, 5, 234, 325])
        time_memory_tracking(start_time)

    def test_should_insertion_sort1(self):
        # given
        start_time = time.perf_counter()
        arr = [-1, -5, 5, 5, 3, -3]
        list_length = len(arr)
        # when
        result = insertion_sort(list_length, arr)
        # then
        self.assertEqual(result, [-5, -3, -1, 3, 5, 5])
        time_memory_tracking(start_time)


if __name__ == "__main__":
    unittest.main()
